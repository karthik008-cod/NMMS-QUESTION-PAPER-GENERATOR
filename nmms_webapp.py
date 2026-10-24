#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
NMMS 180-Question Paper Generator – Flask Web Application
==========================================================
A web wrapper around the NMMS CLI paper generator.
Provides routes for generating, reviewing, regenerating individual
questions, and finalising the paper into downloadable PDFs.
"""

import os
import sys
import json
import time
import random
import shutil
import threading
from datetime import datetime
from dataclasses import asdict
from urllib.parse import quote

# ---------------------------------------------------------------------------
# Path bootstrap – make sure the NMMS package is importable
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from flask import (
    Flask, render_template, request, jsonify, send_from_directory, abort
)

from NMMS.generator import (
    build_test_questions,
    generate_single_replacement_question,
    generate_entire_section,
    build_question_paper_pdf,
    build_key_solutions_pdf,
    build_complete_master_pdf,
)
from NMMS.generator.core import BLUEPRINT, ExamQuestion

import pymupdf  # fitz – used for page-count verification after PDF build

# ---------------------------------------------------------------------------
# Flask application
# ---------------------------------------------------------------------------
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB upload limit

# ---------------------------------------------------------------------------
# Global paper state (single-user / single-paper-at-a-time)
# ---------------------------------------------------------------------------
paper_state = {
    'questions': [],
    'test_num': 0,
    'img_dir': '',
    'seed': 0,
    'paper_code': '',
}

state_lock = threading.Lock()

# ---------------------------------------------------------------------------
# Daily serial counter (file-based)
# ---------------------------------------------------------------------------
SERIAL_FILE = os.path.join(BASE_DIR, 'NMMS', 'output', '.serial_counter.json')


def _next_serial(test_num: int) -> int:
    """Return a daily serial number.  Resets each calendar day."""
    today = datetime.now().strftime('%Y%m%d')
    data = {}
    try:
        if os.path.isfile(SERIAL_FILE):
            with open(SERIAL_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
    except (json.JSONDecodeError, OSError):
        data = {}

    if data.get('date') != today:
        data = {'date': today, 'serial': 0}

    data['serial'] = data.get('serial', 0) + 1
    serial = data['serial']

    os.makedirs(os.path.dirname(SERIAL_FILE), exist_ok=True)
    with open(SERIAL_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f)

    return serial


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _make_seed() -> int:
    """Generate a dynamic seed from time, pid, and randomness."""
    return (int(time.time() * 1000) ^ (os.getpid() << 16) ^ random.randint(1, 1_000_000)) % (2**31 - 1)


def question_to_dict(q: ExamQuestion) -> dict:
    """Serialise an ExamQuestion to a JSON-friendly dict."""
    d = {
        'q_num': q.q_num,
        'stem': q.stem,
        'options': q.options,
        'correct_opt': q.correct_opt,
        'explanation': q.explanation,
        'section_name': q.section_name,
        'directions': q.directions,
        'matrix_data': q.matrix_data,
        'image_url': None,
        'option_image_urls': None,
    }
    if q.image_path:
        full_path = os.path.normpath(os.path.abspath(q.image_path))
        if os.path.isfile(full_path):
            safe_path = full_path.replace(os.sep, '/')
            d['image_url'] = f"/image?path={quote(safe_path, safe='/:')}"
    if getattr(q, 'option_images', None):
        opt_urls = []
        for p in q.option_images:
            if p:
                f_path = os.path.normpath(os.path.abspath(p))
                if os.path.isfile(f_path):
                    s_path = f_path.replace(os.sep, '/')
                    opt_urls.append(f"/image?path={quote(s_path, safe='/:')}")
                else:
                    opt_urls.append(None)
            else:
                opt_urls.append(None)
        d['option_image_urls'] = opt_urls
    return d


def _verify_pdf(path: str) -> int:
    """Open a PDF with pymupdf and return its page count (0 on failure)."""
    try:
        doc = pymupdf.open(path)
        count = doc.page_count
        doc.close()
        return count
    except Exception:
        return 0


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route('/')
def index():
    """Render the main page, passing the BLUEPRINT as JSON."""
    blueprint_data = []
    for sec in BLUEPRINT:
        blueprint_data.append({
            'sec_num': sec.sec_num,
            'name': sec.name,
            'directions': sec.directions,
            'q_range': sec.q_range,
            'count': sec.count,
        })
    return render_template('index.html', blueprint_json=json.dumps(blueprint_data, ensure_ascii=False))


@app.route('/generate', methods=['POST'])
def generate():
    """Generate all 180 questions for the requested test number."""
    data = request.get_json(force=True) or {}
    test_num = int(data.get('test_num', 1))

    output_img_dir = os.path.join(BASE_DIR, 'NMMS', 'output', f'webapp_test{test_num}_diagrams')
    os.makedirs(output_img_dir, exist_ok=True)

    run_seed = _make_seed()
    questions = build_test_questions(test_num, output_img_dir, seed=run_seed)

    custom_code = data.get('paper_code')
    if custom_code and str(custom_code).strip():
        paper_code = str(custom_code).strip()
    else:
        serial = _next_serial(test_num)
        paper_code = datetime.now().strftime('%Y%m%d') + f'{serial:03d}'

    with state_lock:
        paper_state['questions'] = questions
        paper_state['test_num'] = test_num
        paper_state['img_dir'] = output_img_dir
        paper_state['seed'] = run_seed
        paper_state['paper_code'] = paper_code

    return jsonify({
        'status': 'success',
        'test_num': test_num,
        'paper_code': paper_code,
        'total_questions': len(questions),
        'questions': [question_to_dict(q) for q in questions]
    })


@app.route('/current_paper', methods=['GET'])
def get_current_paper():
    """Retrieve the currently loaded paper in memory if any."""
    with state_lock:
        if not paper_state['questions']:
            return jsonify({'loaded': False, 'questions': []})
        return jsonify({
            'loaded': True,
            'test_num': paper_state['test_num'],
            'paper_code': paper_state['paper_code'],
            'total_questions': len(paper_state['questions']),
            'questions': [question_to_dict(q) for q in paper_state['questions']]
        })


@app.route('/update_question/<int:q_num>', methods=['POST'])
def update_question(q_num: int):
    """Update question stem, options, correct_opt, or explanation in memory."""
    data = request.get_json(force=True) or {}
    with state_lock:
        if not paper_state['questions']:
            return jsonify({'error': 'No paper generated yet'}), 400

        idx = q_num - 1
        if idx < 0 or idx >= len(paper_state['questions']):
            return jsonify({'error': f'Invalid question number: {q_num}'}), 400

        q = paper_state['questions'][idx]
        if 'stem' in data:
            q.stem = str(data['stem']).strip()
        if 'options' in data and isinstance(data['options'], list):
            q.options = [str(opt) for opt in data['options']]
        if 'correct_opt' in data:
            try:
                c_opt = int(data['correct_opt'])
                if 1 <= c_opt <= len(q.options):
                    q.correct_opt = c_opt
            except ValueError:
                pass
        if 'explanation' in data:
            q.explanation = str(data['explanation']).strip()

        return jsonify({
            'status': 'success',
            'question': question_to_dict(q)
        })


@app.route('/regenerate/<int:q_num>', methods=['POST'])
def regenerate(q_num: int):
    """
    Regenerate question `q_num`.
    If q_num belongs to a connected group (Venn Diagrams Q131-134, Survey Venn Q135-138, Cubes Q155-160),
    regenerates all questions in that group together so diagrams and questions remain 100% synchronized!
    """
    with state_lock:
        if not paper_state['questions']:
            return jsonify({'error': 'No paper generated yet'}), 400

        idx = q_num - 1
        if idx < 0 or idx >= len(paper_state['questions']):
            return jsonify({'error': f'Invalid question number: {q_num}'}), 400

        test_num = paper_state['test_num']
        main_img_dir = paper_state['img_dir']
        current_q_list = list(paper_state['questions'])

    try:
        result = generate_single_replacement_question(
            q_num=q_num,
            current_questions=current_q_list,
            output_img_dir=main_img_dir,
            test_num=test_num
        )

        with state_lock:
            if isinstance(result, list):
                # Connected group
                for rep_q in result:
                    paper_state['questions'][rep_q.q_num - 1] = rep_q
                return jsonify({
                    'status': 'success',
                    'is_group': True,
                    'questions': [question_to_dict(q) for q in result]
                })
            else:
                paper_state['questions'][idx] = result
                return jsonify({
                    'status': 'success',
                    'is_group': False,
                    'question': question_to_dict(result)
                })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Failed to regenerate question {q_num}: {str(e)}'}), 500


@app.route('/regenerate_section/<int:sec_num>', methods=['POST'])
def regenerate_section(sec_num: int):
    """
    Regenerate all questions belonging to section `sec_num`.
    Refreshes the shared diagrams, questions, options, and explanations.
    """
    with state_lock:
        if not paper_state['questions']:
            return jsonify({'error': 'No paper generated yet'}), 400
        test_num = paper_state['test_num']
        main_img_dir = paper_state['img_dir']
        current_q_list = list(paper_state['questions'])

    try:
        new_sec_qs = generate_entire_section(
            sec_num=sec_num,
            current_questions=current_q_list,
            output_img_dir=main_img_dir,
            test_num=test_num
        )

        with state_lock:
            for q in new_sec_qs:
                paper_state['questions'][q.q_num - 1] = q

        return jsonify({
            'status': 'success',
            'sec_num': sec_num,
            'questions': [question_to_dict(q) for q in new_sec_qs]
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Failed to regenerate section {sec_num}: {str(e)}'}), 500


@app.route('/finalize', methods=['POST'])
def finalize():
    """Build QP, Key, and Complete-Master PDFs from the current paper_state."""
    with state_lock:
        if not paper_state['questions']:
            return jsonify({'error': 'No paper generated yet'}), 400
        questions = list(paper_state['questions'])
        test_num = paper_state['test_num']
        paper_code = paper_state['paper_code']

    output_dir = os.path.join(BASE_DIR, 'NMMS', 'output')
    os.makedirs(output_dir, exist_ok=True)

    qp_filename = f'NMMS_Mental_Ability_Grand_Test_{test_num}_{paper_code}_180Q.pdf'
    key_filename = f'NMMS_Mental_Ability_Grand_Test_{test_num}_{paper_code}_Key_and_Solutions.pdf'
    comp_filename = f'NMMS_Mental_Ability_Grand_Test_{test_num}_{paper_code}_Complete.pdf'

    qp_path = os.path.join(output_dir, qp_filename)
    key_path = os.path.join(output_dir, key_filename)
    comp_path = os.path.join(output_dir, comp_filename)

    # Build the three PDFs
    build_question_paper_pdf(questions, qp_path, test_num=test_num, paper_code=paper_code)
    build_key_solutions_pdf(questions, key_path, test_num=test_num, paper_code=paper_code)
    build_complete_master_pdf(qp_path, key_path, comp_path)

    # Verify page counts
    qp_pages = _verify_pdf(qp_path)
    key_pages = _verify_pdf(key_path)
    comp_pages = _verify_pdf(comp_path)

    return jsonify({
        'status': 'success',
        'paper_code': paper_code,
        'test_num': test_num,
        'qp': {
            'filename': qp_filename,
            'url': f'/download/{qp_filename}',
            'pages': qp_pages,
        },
        'key': {
            'filename': key_filename,
            'url': f'/download/{key_filename}',
            'pages': key_pages,
        },
        'complete': {
            'filename': comp_filename,
            'url': f'/download/{comp_filename}',
            'pages': comp_pages,
        },
    })


@app.route('/download/<path:filename>')
def download(filename):
    """Serve generated PDFs from NMMS/output/."""
    output_dir = os.path.join(BASE_DIR, 'NMMS', 'output')
    # Security: case-insensitive normalisation for Windows
    safe_dir = os.path.normpath(os.path.abspath(output_dir)).lower()
    safe_path = os.path.normpath(os.path.abspath(os.path.join(output_dir, filename))).lower()
    if not safe_path.startswith(safe_dir):
        abort(403)
    return send_from_directory(output_dir, filename, as_attachment=True)


@app.route('/image')
def serve_image():
    """Serve a diagram image by absolute path (validated to be under project dir)."""
    raw_path = request.args.get('path', '')
    if not raw_path:
        abort(400)

    # Strip any cache-busting query fragments that might have been glued into the path
    clean_path = raw_path.split('?')[0].split('&')[0]

    # Normalise both paths with lowercase check for safe Windows path validation
    abs_project = os.path.normpath(os.path.abspath(BASE_DIR)).lower()
    abs_image = os.path.normpath(os.path.abspath(clean_path))

    if not abs_image.lower().startswith(abs_project):
        abort(403)

    if not os.path.isfile(abs_image):
        abort(404)

    directory = os.path.dirname(abs_image)
    basename = os.path.basename(abs_image)
    response = send_from_directory(directory, basename)
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
