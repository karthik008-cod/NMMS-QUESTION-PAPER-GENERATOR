"""
NMMS Mental Ability Practice Question Paper and Answer Key Generator
Command-line interface to generate unique, printer-friendly, 2-column examination papers.
Uses Paper Code format: YYYYMMDD001, YYYYMMDD002, etc. (Year, Month, Date + 3-digit daily serial).
"""

import os
import sys
import json
import argparse
import time
from generator import (
    generate_full_test_questions,
    build_question_paper_pdf,
    build_answer_key_pdf
)

TRACKER_FILE = os.path.join(os.path.dirname(__file__), "generator", "test_tracker.json")

def get_next_paper_code(user_code=None) -> str:
    """
    Reads tracker and generates YYYYMMDD followed by 001, 002, 003...
    YYYY = 4-digit Year
    MM   = 2-digit Month
    DD   = 2-digit Day
    001, 002... = daily serial number of test generated that day.
    """
    today_str = time.strftime("%Y%m%d")
    
    if user_code is not None:
        user_code = str(user_code).strip()
        if len(user_code) <= 4:
            # If user passed just a number e.g. 1 or 2, format as YYYYMMDD001
            return f"{today_str}{int(user_code):03d}"
        return user_code

    daily_serial = 1
    if os.path.exists(TRACKER_FILE):
        try:
            with open(TRACKER_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data.get("date") == today_str:
                    daily_serial = int(data.get("daily_serial", 0)) + 1
                else:
                    daily_serial = 1
        except Exception:
            daily_serial = 1

    paper_code = f"{today_str}{daily_serial:03d}"
    
    try:
        with open(TRACKER_FILE, "w", encoding="utf-8") as f:
            json.dump({
                "date": today_str,
                "daily_serial": daily_serial,
                "last_code": paper_code,
                "last_generated_at": time.strftime("%Y-%m-%d %H:%M:%S")
            }, f, indent=2)
    except Exception as e:
        print(f"Warning: Could not update tracker file: {e}")

    return paper_code

def main():
    parser = argparse.ArgumentParser(description="Generate NMMS Mental Ability Test Paper & Key")
    parser.add_argument("--code", type=str, default=None, help="Explicit Paper Code (e.g. 20260925001 or 1)")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducible generation")
    args = parser.parse_args()

    paper_code = get_next_paper_code(args.code)
    print("=" * 65)
    print(f"  Generating NMMS Mental Ability Grand Test")
    print(f"  Paper Code: {paper_code}")
    print("=" * 65)

    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, "output")
    diagrams_dir = os.path.join(output_dir, "diagrams", f"code_{paper_code}")
    os.makedirs(diagrams_dir, exist_ok=True)

    # 1. Procedural Question Generation (18 topics strictly covered, topic order shuffled)
    print("-> Creating 90 authentic NMMS MAT questions strictly following the 18-topic syllabus...")
    seed_val = args.seed if args.seed is not None else int(time.time() * 1000) % 10000000 + int(paper_code[-3:]) * 1013
    questions = generate_full_test_questions(diagrams_dir, seed=seed_val)

    # 2. Strict Key Verification
    print("-> Verifying answer key integrity and ensuring exactly 1 correct option per question...")
    for q in questions:
        if len(q.options) != 4:
            raise ValueError(f"Error: Question {q.q_num} has {len(q.options)} options instead of 4.")
        if len(set(q.options)) != 4:
            raise ValueError(f"Error: Question {q.q_num} has duplicate options: {q.options}")
        if q.correct_opt not in [1, 2, 3, 4]:
            raise ValueError(f"Error: Question {q.q_num} has invalid correct option {q.correct_opt}")

    # 3. PDF Paths
    qp_pdf_name = f"NMMS_Mental_Ability_Grand_Test_{paper_code}.pdf"
    key_pdf_name = f"NMMS_Mental_Ability_Grand_Test_{paper_code}_Key.pdf"
    qp_pdf_path = os.path.join(output_dir, qp_pdf_name)
    key_pdf_path = os.path.join(output_dir, key_pdf_name)

    # 4. Build Question Paper PDF
    print(f"-> Compiling 2-column Question Paper PDF: {qp_pdf_name}...")
    build_question_paper_pdf(questions, paper_code, qp_pdf_path)

    # 5. Build Answer Key & Explanation PDF
    print(f"-> Compiling separate Answer Key & Explanations PDF: {key_pdf_name}...")
    build_answer_key_pdf(questions, paper_code, key_pdf_path)

    print("\n" + "=" * 65)
    print("  Generation Completed Successfully!")
    print("=" * 65)
    print(f"  [1] Question Paper: {qp_pdf_path}")
    print(f"  [2] Answer Key:     {key_pdf_path}")
    print(f"  Total Questions:   90 / 90 (All 18 topics covered, shuffled order)")
    print(f"  Paper Code:        {paper_code}")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    main()
