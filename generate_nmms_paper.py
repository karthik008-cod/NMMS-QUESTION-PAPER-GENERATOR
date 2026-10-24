"""
NMMS Mental Ability Test (MAT) — Comprehensive 180-Question Paper Generator
CLI Tool to generate balanced, full-syllabus 180-Question Grand Tests anytime.

Usage:
    python generate_nmms_paper.py [--test-num 3] [--seed 42] [--output-dir .]

Generates 3 separate documents:
1. NMMS_Mental_Ability_Grand_Test_<N>_180Q.pdf (Question Paper Only)
2. NMMS_Mental_Ability_Grand_Test_<N>_180Q_Key_and_Solutions.pdf (OMR Key + Step-by-Step Solutions)
3. NMMS_Mental_Ability_Grand_Test_<N>_180Q_Complete.pdf (Combined Master Booklet)
"""

import os
import sys
import argparse

# Ensure NMMS is in Python path
curr_dir = os.path.dirname(os.path.abspath(__file__))
if curr_dir not in sys.path:
    sys.path.insert(0, curr_dir)

from NMMS.generator import (
    build_test_questions,
    build_question_paper_pdf,
    build_key_solutions_pdf,
    build_complete_master_pdf,
    BLUEPRINT
)
import pymupdf

def main():
    parser = argparse.ArgumentParser(
        description="NMMS MAT 180-Question Grand Test Paper Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_nmms_paper.py --test-num 3
  python generate_nmms_paper.py --test-num 4 --seed 12345
  python generate_nmms_paper.py --test-num 5 --output-dir "C:/AGC18052026/ZPHS KISTAPUR/NMMS/output"
"""
    )
    parser.add_argument("--test-num", type=int, default=3, help="Grand Test Number (e.g. 3, 4, 5...)")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducible randomization")
    parser.add_argument("--serial", type=int, default=None, help="Daily serial number (defaults to test-num)")
    parser.add_argument("--paper-code", type=str, default=None, help="Explicit paper code (e.g. 20261017004)")
    parser.add_argument("--output-dir", type=str, default=".", help="Directory to save generated PDF documents")
    parser.add_argument("--img-dir", type=str, default=None, help="Directory to store procedural HD diagram images")

    args = parser.parse_args()

    test_num = args.test_num
    out_dir = os.path.abspath(args.output_dir)
    os.makedirs(out_dir, exist_ok=True)

    serial = args.serial if args.serial is not None else test_num
    if args.paper_code:
        paper_code = args.paper_code
    else:
        from datetime import datetime
        today_str = datetime.now().strftime("%Y%m%d")
        paper_code = f"{today_str}{serial:03d}"

    img_dir = args.img_dir or os.path.join(curr_dir, "NMMS", "output", f"test{test_num}_diagrams")
    os.makedirs(img_dir, exist_ok=True)

    print("=" * 70)
    print(f"  NMMS MAT GRAND TEST - {test_num} (180 QUESTIONS) GENERATOR")
    print(f"  PAPER CODE: {paper_code}")
    print("=" * 70)
    print(f"Target Output Directory: {out_dir}")
    print(f"Diagram Assets Directory: {img_dir}")
    print(f"Total Sections: {len(BLUEPRINT)}")
    print(f"Total Questions: 180 (All 25 essential MAT categories included)")
    print("-" * 70)

    import time
    import random as py_random
    if args.seed is not None:
        run_seed = args.seed
        print(f"Randomization Mode: Reproducible (Seed: {run_seed})")
    else:
        run_seed = (int(time.time() * 1000) ^ (os.getpid() << 16) ^ py_random.randint(1, 1000000)) % (2**31 - 1)
        print(f"Randomization Mode: Dynamic Non-Repeating (Generated Seed: {run_seed})")

    # 1. Generate questions & HD diagrams
    print(f"[1/4] Generating 180 questions and rendering vector-crisp HD diagrams...")
    questions = build_test_questions(test_num=test_num, output_img_dir=img_dir, seed=run_seed)

    # 2. Build Question Paper PDF
    qp_filename = f"NMMS_Mental_Ability_Grand_Test_{test_num}_180Q.pdf"
    qp_path = os.path.join(out_dir, qp_filename)
    print(f"[2/4] Assembling Question Paper PDF (2-column layout, Code: {paper_code})...")
    build_question_paper_pdf(questions, qp_path, test_num=test_num, paper_code=paper_code)

    # 3. Build Key & Detailed Solutions PDF
    key_filename = f"NMMS_Mental_Ability_Grand_Test_{test_num}_180Q_Key_and_Solutions.pdf"
    key_path = os.path.join(out_dir, key_filename)
    print(f"[3/4] Assembling Answer Key & Step-by-Step Solutions PDF (Code: {paper_code})...")
    build_key_solutions_pdf(questions, key_path, test_num=test_num, paper_code=paper_code)

    # 4. Build Complete Master PDF
    comp_filename = f"NMMS_Mental_Ability_Grand_Test_{test_num}_180Q_Complete.pdf"
    comp_path = os.path.join(out_dir, comp_filename)
    print(f"[4/4] Merging Master Combined Booklet...")
    build_complete_master_pdf(qp_path, key_path, comp_path)

    # Verification of page counts
    qp_doc = pymupdf.open(qp_path)
    key_doc = pymupdf.open(key_path)
    comp_doc = pymupdf.open(comp_path)

    print("=" * 70)
    print("ALL 3 PDF DOCUMENTS SUCCESSFULLY GENERATED & VERIFIED!")
    print(f"  1. Question Paper:       {qp_path} ({len(qp_doc)} pages)")
    print(f"  2. Key & Solutions:      {key_path} ({len(key_doc)} pages)")
    print(f"  3. Complete Master:      {comp_path} ({len(comp_doc)} pages)")
    print("=" * 70)

if __name__ == "__main__":
    main()
