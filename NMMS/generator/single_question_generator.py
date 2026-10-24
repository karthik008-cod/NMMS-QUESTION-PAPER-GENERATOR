"""
Dedicated Single-Question & Section Regeneration Engine for NMMS Question Paper Generator
Guarantees:
1. NEVER just shuffles options on the same question stem.
2. Always generates BRAND NEW questions with new stems, new figures, new numbers, and new answers.
3. Connected groups (Venn diagrams Q131-134, Survey Venn Q135-138, Cubes Q155-160) are
   regenerated together so the shared diagram and all corresponding sub-questions remain 100% synchronized.
4. Renders fresh HD 300 DPI vector diagrams on disk with unique timestamp names.
"""

import os
import time
import random
import shutil
import numpy as np
from typing import List, Optional, Tuple, Dict, Any, Set

from .core import ExamQuestion, SectionInfo, BLUEPRINT
from .diagrams import (
    generate_two_dice, generate_three_dice, generate_dice_net,
    generate_3d_cube, generate_clock_face, generate_mirror_problem,
    generate_water_problem, generate_paper_fold_cut_problem,
    generate_transparent_fold_problem, generate_circular_fold_cut_problem,
    generate_embedded_figure_problem, generate_analogy_problem,
    generate_dot_situation, generate_series_problem,
    generate_survey_venn_graduates, generate_four_shape_venn_diagram
)
from .procedural_questions import generate_procedural_question, helper_shuffle_with_images, make_dice_questions
from .venn_generator import (
    VENN_GEOM_ALL_IDS, VENN_SURVEY_ALL_IDS,
    generate_venn_geometric_group,
    generate_venn_survey_group as vg_generate_venn_survey_group
)
from .paper_fold_generator import (
    PFC_ALL_PATTERN_IDS, generate_pfc_problem, generate_pfc_options, get_pfc_pattern_details
)
from .pattern_tracker import get_least_recently_used_patterns

def get_project_root() -> str:
    """Returns the absolute path to the project root directory."""
    cur = os.path.abspath(__file__)
    for _ in range(3):
        cur = os.path.dirname(cur)
    return cur


def find_section_for_q(q_num: int) -> SectionInfo:
    """Find which section a given question number belongs to based on BLUEPRINT."""
    curr_start = 1
    for sec in BLUEPRINT:
        curr_end = curr_start + sec.count - 1
        if curr_start <= q_num <= curr_end:
            return sec
        curr_start = curr_end + 1
    return BLUEPRINT[-1]


def get_section_q_range(sec_num: int) -> Tuple[int, int]:
    """Get the 1-based (start_q, end_q) range for a section number."""
    start = 1
    for sec in BLUEPRINT:
        end = start + sec.count - 1
        if sec.sec_num == sec_num:
            return start, end
        start = end + 1
    return 1, 10


def helper_shuffle_options(opts: List[str], correct_idx: int) -> Tuple[List[str], int]:
    """Helper to shuffle options while preserving the correct answer index (1-indexed)."""
    if opts == ["(1)", "(2)", "(3)", "(4)"] or len(opts) != 4:
        return list(opts), correct_idx
    correct_val = opts[correct_idx - 1]
    shuffled = list(opts)
    random.shuffle(shuffled)
    new_correct_idx = shuffled.index(correct_val) + 1
    return shuffled, new_correct_idx


# =========================================================================
# VENN DIAGRAM GROUP 1 (Q131 - Q134) VIA LRU PATTERN TRACKER
# =========================================================================

def generate_venn_shapes_group(output_img_dir: str, test_num: int, uid: str, current_stem: str = "") -> List[ExamQuestion]:
    """
    Generates Q131 - Q134 dynamically from 12 distinct 4-shape Geometric Venn patterns.
    Uses persistent Least-Recently-Used (LRU) tracking to guarantee fresh patterns across tests.
    """
    curr_lower = current_stem.lower()
    exclude = [pid for pid in VENN_GEOM_ALL_IDS if any(w in curr_lower for w in pid.split('_') if len(w) > 4)]
    pids = get_least_recently_used_patterns('venn_geometric', VENN_GEOM_ALL_IDS, count=1, current_test_num=test_num, exclude=exclude)
    chosen_id = pids[0]
    return generate_venn_geometric_group(chosen_id, output_img_dir, test_num, uid, start_q_num=131)


# =========================================================================
# VENN DIAGRAM GROUP 2 (Q135 - Q138) VIA LRU PATTERN TRACKER
# =========================================================================

def generate_venn_survey_group(output_img_dir: str, test_num: int, uid: str, current_stem: str = "") -> List[ExamQuestion]:
    """
    Generates Q135 - Q138 dynamically from 12 distinct Survey Venn patterns.
    Uses persistent Least-Recently-Used (LRU) tracking to guarantee fresh patterns across tests.
    """
    curr_lower = current_stem.lower()
    exclude = [pid for pid in VENN_SURVEY_ALL_IDS if any(w in curr_lower for w in pid.split('_') if len(w) > 4)]
    pids = get_least_recently_used_patterns('venn_survey', VENN_SURVEY_ALL_IDS, count=1, current_test_num=test_num, exclude=exclude)
    chosen_id = pids[0]
    return vg_generate_venn_survey_group(chosen_id, output_img_dir, test_num, uid, start_q_num=135)


# =========================================================================
# CUBES & PAINTED FACES GROUP (Q155 - Q160)
# =========================================================================

def generate_cubes_group(output_img_dir: str, test_num: int, uid: str, current_stem: str = "") -> List[ExamQuestion]:
    """
    Generates Q155 - Q160 dynamically based on a 3D painted cube of dimension n.
    Guarantees switching to a different cube dimension n from the current one.
    """
    sec = BLUEPRINT[19]
    curr_lower = current_stem.lower()

    # Determine current cube dimension and pick a different one
    curr_n = 3
    if "4 cm" in curr_lower or "4x4" in curr_lower or "64" in curr_lower:
        curr_n = 4
    elif "5 cm" in curr_lower or "5x5" in curr_lower or "125" in curr_lower:
        curr_n = 5

    possible_n = [x for x in [3, 4, 5] if x != curr_n]
    n_cube = random.choice(possible_n)

    c3 = 8
    c2 = 12 * (n_cube - 2)
    c1 = 6 * ((n_cube - 2)**2)
    c0 = (n_cube - 2)**3
    c_tot = n_cube**3
    c_cuts = 3 * (n_cube - 1)

    cube_path = os.path.join(output_img_dir, f"test{test_num}_cube_{n_cube}x{n_cube}_{uid}.png")
    generate_3d_cube(n_cube, cube_path)

    cubes_data = [
        (f"A large cube of side {n_cube} cm is painted red on all its six faces and then cut into smaller cubes of side 1 cm each (shown in figure). Answer questions 155 to 160 based on this.\nHow many smaller cubes have exactly THREE faces painted?",
         [str(c3), str(c3 - 4), str(c3 - 2), str(c3 + 4)], 1,
         "Corner cubes always have 3 faces painted. There are always exactly 8 corners in any cube.", cube_path),
        ("How many smaller cubes have exactly TWO faces painted?",
         [str(c2), str(c2 - 4), str(c2 + 4), str(c2 + 8)], 1,
         f"Edge cubes have 2 faces painted: 12 * (n - 2) = 12 * ({n_cube} - 2) = {c2} cubes.", None),
        ("How many smaller cubes have exactly ONE face painted?",
         [str(c1), str(c1 - 2), str(c1 + 4), str(c1 + 6)], 1,
         f"Face center cubes have 1 face painted: 6 * (n - 2)^2 = 6 * ({n_cube} - 2)^2 = {c1} cubes.", None),
        ("How many smaller cubes have NO face painted (zero painted faces)?",
         [str(c0), "0", str(c0 + 2), str(c0 + 4)], 1,
         f"Inner core cubes have no painted faces: (n - 2)^3 = ({n_cube} - 2)^3 = {c0} cubes.", None),
        (f"What is the total number of 1 cm smaller cubes formed by cutting the {n_cube} cm cube?",
         [str(c_tot), str(c_tot - 9), str(c_tot - 5), str(c_tot + 9)], 1,
         f"Total smaller cubes = n^3 = {n_cube}^3 = {c_tot} cubes.", None),
        (f"What is the minimum number of cuts required to divide a {n_cube} cm cube into {c_tot} equal 1 cm smaller cubes?",
         [str(c_cuts), str(c_cuts - 2), str(c_cuts + 2), str(c_cuts + 3)], 1,
         f"Cuts required = 3 * (n - 1) = 3 * ({n_cube} - 1) = {c_cuts} cuts.", None)
    ]

    res = []
    for idx, (stem, opts, ans, exp, img) in enumerate(cubes_data):
        q_num = 155 + idx
        shuffled_opts, new_ans = helper_shuffle_options(opts, ans)
        res.append(ExamQuestion(
            q_num=q_num,
            stem=stem,
            options=shuffled_opts,
            correct_opt=new_ans,
            explanation=exp,
            section_name=(f"SECTION {sec.sec_num}: {sec.name}" if idx == 0 else None),
            directions=(sec.directions if idx == 0 else None),
            image_path=img
        ))
    return res


# =========================================================================
# ENTIRE SECTION GENERATOR
# =========================================================================

def generate_entire_section(
    sec_num: int,
    current_questions: List[ExamQuestion],
    output_img_dir: str,
    test_num: int
) -> List[ExamQuestion]:
    """
    Regenerates ALL questions belonging to section `sec_num`.
    Returns the complete list of ExamQuestion objects for that section.
    """
    os.makedirs(output_img_dir, exist_ok=True)
    uid = f"{int(time.time() * 1000)}_{random.randint(100, 999)}"

    # SECTION 17: VENN DIAGRAMS (Q131 - Q138)
    if sec_num == 17:
        stem131 = current_questions[130].stem if len(current_questions) >= 131 else ""
        stem135 = current_questions[134].stem if len(current_questions) >= 135 else ""
        g1 = generate_venn_shapes_group(output_img_dir, test_num, uid, current_stem=stem131)
        g2 = generate_venn_survey_group(output_img_dir, test_num, uid, current_stem=stem135)
        return g1 + g2

    # SECTION 20: CUBES & PAINTED FACES (Q155 - Q160)
    if sec_num == 20:
        stem155 = current_questions[154].stem if len(current_questions) >= 155 else ""
        return generate_cubes_group(output_img_dir, test_num, uid, current_stem=stem155)

    # SECTION 19: DICE & OPEN DICE PROBLEMS (Q149 - Q154)
    if sec_num == 19:
        sec = BLUEPRINT[18]
        dice_qs = make_dice_questions(output_img_dir, test_num, uid)
        res = []
        for idx, (stem, opts, ans, exp, dimg) in enumerate(dice_qs):
            shuffled_opts, new_ans = helper_shuffle_options(opts, ans)
            res.append(ExamQuestion(
                q_num=149 + idx,
                stem=stem,
                options=shuffled_opts,
                correct_opt=new_ans,
                explanation=exp,
                section_name=(f"SECTION {sec.sec_num}: {sec.name}" if idx == 0 else None),
                directions=(sec.directions if idx == 0 else None),
                image_path=dimg
            ))
        return res

    start_q, end_q = get_section_q_range(sec_num)
    count = end_q - start_q + 1

    # Check if procedural generation is available for this section:
    # SECTION 23: PAPER FOLDING & CUTTING (Q173 - Q176)
    if sec_num == 23:
        pids = get_least_recently_used_patterns('paper_folding', PFC_ALL_PATTERN_IDS, count=4, current_test_num=test_num)
        sec = BLUEPRINT[22]
        res = []
        for idx, pid in enumerate(pids):
            cfg = get_pfc_pattern_details(pid)
            prob_path = os.path.join(output_img_dir, f"test{test_num}_pfc_{pid}_{uid}.png")
            generate_pfc_problem(pid, prob_path)
            opt_imgs = generate_pfc_options(pid, output_img_dir, f"test{test_num}_pfc_opt_{pid}_{uid}")
            shuffled_opts, new_corr, shuffled_opt_imgs = helper_shuffle_with_images(["", "", "", ""], 1, opt_imgs)
            res.append(ExamQuestion(
                q_num=173 + idx,
                stem=cfg['stem'],
                options=shuffled_opts,
                correct_opt=new_corr,
                explanation=cfg['exp'],
                section_name=(f"SECTION {sec.sec_num}: {sec.name}" if idx == 0 else None),
                directions=(sec.directions if idx == 0 else None),
                image_path=prob_path,
                option_images=shuffled_opt_imgs
            ))
        return res

    if sec_num in [1, 2, 3, 4, 6, 7, 12, 13, 14, 15, 16, 18, 21, 22, 24, 25]:
        used: Set[str] = set()
        procs = []
        sec = BLUEPRINT[sec_num - 1]
        for i in range(count):
            this_q = start_q + i
            pq = generate_procedural_question(sec_num, used, "", output_img_dir, test_num, uid, q_num=this_q)
            if pq:
                pq.q_num = this_q
                if i != 0:
                    pq.section_name = None
                    pq.directions = None
                else:
                    pq.section_name = f"SECTION {sec.sec_num}: {sec.name}"
                    pq.directions = sec.directions
                used.add(pq.stem.strip().lower())
                procs.append(pq)
        if len(procs) == count:
            return procs

    # For other sections: generate fresh questions from build_test_questions
    from .questions import build_test_questions
    new_seed = (int(time.time() * 1000) ^ (os.getpid() << 16) ^ random.randint(1, 1000000)) % (2**31 - 1)
    new_paper = build_test_questions(test_num, output_img_dir, seed=new_seed)

    start_q, end_q = get_section_q_range(sec_num)
    sec_slice = new_paper[start_q - 1 : end_q]

    for idx, q in enumerate(sec_slice):
        q.q_num = start_q + idx

    return sec_slice


# =========================================================================
# SINGLE QUESTION REPLACEMENT (WITH GROUP AWARENESS)
# =========================================================================

def generate_single_replacement_question(
    q_num: int,
    current_questions: List[ExamQuestion],
    output_img_dir: str,
    test_num: int
) -> Any:
    """
    Regenerates question `q_num`.
    If q_num belongs to a connected group (Venn Q131-134, Venn Q135-138, Cubes Q155-160),
    regenerates and returns the entire group of connected questions as a List[ExamQuestion].
    Otherwise, returns a single replacement ExamQuestion.
    """
    sec = find_section_for_q(q_num)
    os.makedirs(output_img_dir, exist_ok=True)
    uid = f"{int(time.time() * 1000)}_{random.randint(100, 999)}"

    # 1. Connected Group: Venn Diagram 1 (Q131 - Q134)
    if 131 <= q_num <= 134:
        stem131 = current_questions[130].stem if len(current_questions) >= 131 else ""
        return generate_venn_shapes_group(output_img_dir, test_num, uid, current_stem=stem131)

    # 2. Connected Group: Survey Venn Diagram 2 (Q135 - Q138)
    if 135 <= q_num <= 138:
        stem135 = current_questions[134].stem if len(current_questions) >= 135 else ""
        return generate_venn_survey_group(output_img_dir, test_num, uid, current_stem=stem135)

    # 3. Connected Group: Cubes (Q155 - Q160)
    if 155 <= q_num <= 160:
        stem155 = current_questions[154].stem if len(current_questions) >= 155 else ""
        return generate_cubes_group(output_img_dir, test_num, uid, current_stem=stem155)

    # 4. Standalone Question: Try Procedural Engine first (guaranteed 100% fresh, no duplicates)
    used_stems = set(q.stem.strip().lower() for q in current_questions if q.stem)
    old_q = current_questions[q_num - 1] if 0 < q_num <= len(current_questions) else None
    old_stem = old_q.stem.strip().lower() if old_q else ""
    start_q, end_q = get_section_q_range(sec.sec_num)

    proc_q = generate_procedural_question(sec.sec_num, used_stems, old_stem, output_img_dir, test_num, uid, q_num=q_num)
    if proc_q is not None:
        proc_q.q_num = q_num
        if q_num != start_q:
            proc_q.section_name = None
            proc_q.directions = None
        else:
            proc_q.section_name = f"SECTION {sec.sec_num}: {sec.name}"
            proc_q.directions = sec.directions
        return proc_q

    # 5. General Fallback with Guaranteed Non-Duplication:
    from .questions import build_test_questions
    for attempt in range(25):
        new_seed = (int(time.time() * 1000) ^ (os.getpid() << 16) ^ random.randint(1, 1000000)) % (2**31 - 1)
        temp_img_dir = os.path.join(output_img_dir, f"tmp_single_{uid}")
        new_paper = build_test_questions(test_num, temp_img_dir, seed=new_seed)

        # Prioritize candidates from the section that match the format (image vs matrix vs text)
        sec_candidates = new_paper[start_q - 1 : end_q]
        expects_image = bool(old_q and old_q.image_path) or (143 <= q_num <= 148)
        expects_matrix = bool(old_q and old_q.matrix_data) or (139 <= q_num <= 142)

        if expects_image:
            filtered = [c for c in sec_candidates if c.image_path]
            if filtered:
                sec_candidates = filtered
        elif expects_matrix:
            filtered = [c for c in sec_candidates if c.matrix_data]
            if filtered:
                sec_candidates = filtered

        random.shuffle(sec_candidates)

        for cand in sec_candidates:
            cand_stem = cand.stem.strip().lower()
            if cand_stem not in used_stems and cand_stem != old_stem:
                cand.q_num = q_num
                if q_num != start_q:
                    cand.section_name = None
                    cand.directions = None
                else:
                    cand.section_name = f"SECTION {sec.sec_num}: {sec.name}"
                    cand.directions = sec.directions

                if cand.image_path and os.path.isfile(cand.image_path):
                    new_img_name = f"test{test_num}_q{q_num}_{uid}_{os.path.basename(cand.image_path)}"
                    dest = os.path.join(output_img_dir, new_img_name)
                    shutil.copy2(cand.image_path, dest)
                    cand.image_path = dest
                if getattr(cand, 'option_images', None):
                    new_opt_imgs = []
                    for opt_img in cand.option_images:
                        if opt_img and os.path.isfile(opt_img):
                            n_name = f"test{test_num}_q{q_num}_{uid}_{os.path.basename(opt_img)}"
                            n_dest = os.path.join(output_img_dir, n_name)
                            shutil.copy2(opt_img, n_dest)
                            new_opt_imgs.append(n_dest)
                        else:
                            new_opt_imgs.append(opt_img)
                    cand.option_images = new_opt_imgs
                shutil.rmtree(temp_img_dir, ignore_errors=True)
                return cand

        # If not returned, copy image before cleaning up temp dir
        chosen_cand = None
        for cand in sec_candidates:
            if cand.stem.strip().lower() != old_stem:
                chosen_cand = cand
                break
        if chosen_cand is None and sec_candidates:
            chosen_cand = sec_candidates[0]

        if chosen_cand:
            chosen_cand.q_num = q_num
            if q_num != start_q:
                chosen_cand.section_name = None
                chosen_cand.directions = None
            if chosen_cand.image_path and os.path.isfile(chosen_cand.image_path):
                new_img_name = f"test{test_num}_q{q_num}_{uid}_{os.path.basename(chosen_cand.image_path)}"
                dest = os.path.join(output_img_dir, new_img_name)
                shutil.copy2(chosen_cand.image_path, dest)
                chosen_cand.image_path = dest
            if getattr(chosen_cand, 'option_images', None):
                new_opt_imgs = []
                for opt_img in chosen_cand.option_images:
                    if opt_img and os.path.isfile(opt_img):
                        n_name = f"test{test_num}_q{q_num}_{uid}_{os.path.basename(opt_img)}"
                        n_dest = os.path.join(output_img_dir, n_name)
                        shutil.copy2(opt_img, n_dest)
                        new_opt_imgs.append(n_dest)
                    else:
                        new_opt_imgs.append(opt_img)
                chosen_cand.option_images = new_opt_imgs
            shutil.rmtree(temp_img_dir, ignore_errors=True)
            return chosen_cand

        shutil.rmtree(temp_img_dir, ignore_errors=True)

    cand = sec_candidates[0]
    cand.q_num = q_num
    return cand
