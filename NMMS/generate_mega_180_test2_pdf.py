"""
Master PDF Generator for NMMS Mega Grand Test 2 (180 Questions)
Produces:
1. NMMS_Mental_Ability_Grand_Test_2_180Q.pdf (Question Paper ONLY, 180 questions)
2. NMMS_Mental_Ability_Grand_Test_2_180Q_Key_and_Solutions.pdf (Answer Key & Solutions)
3. NMMS_Mental_Ability_Grand_Test_2_180Q_Complete.pdf (Combined Master Booklet)
"""

import os
import sys
from PIL import Image as PILImage

from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Image as RLImage, Table, TableStyle, KeepTogether, PageBreak,
    NextPageTemplate, FrameBreak
)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT

from mega_180_core import (
    PAGE_WIDTH, PAGE_HEIGHT, MARGIN_LR, MARGIN_TB, PRINT_WIDTH,
    COL_GAP, COL_WIDTH, CENTER_X, ExamQuestion, NumberedCanvas,
    get_styles, format_options_table, format_matrix_table
)
from mega_180_data_test2 import get_all_180_questions

def build_question_paper_pdf(questions: list[ExamQuestion], output_path: str, frame_break_q: int = 179):
    """
    Builds the 180-Question Paper PDF in portrait two-column layout.
    """
    h_header_p1 = 98.0
    frame_p1_left = Frame(MARGIN_LR, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - h_header_p1,
                          id='col1_p1', leftPadding=0, rightPadding=5, topPadding=3, bottomPadding=3)
    frame_p1_right = Frame(MARGIN_LR + COL_WIDTH + COL_GAP, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - h_header_p1,
                           id='col2_p1', leftPadding=5, rightPadding=0, topPadding=3, bottomPadding=3)

    frame_later_left = Frame(MARGIN_LR, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 20,
                             id='col1_later', leftPadding=0, rightPadding=5, topPadding=3, bottomPadding=3)
    frame_later_right = Frame(MARGIN_LR + COL_WIDTH + COL_GAP, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 20,
                              id='col2_later', leftPadding=5, rightPadding=0, topPadding=3, bottomPadding=3)

    def on_first_page(c, doc):
        c.saveState()
        # Top Header Box
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(CENTER_X, PAGE_HEIGHT - 38, "NATIONAL MEANS-CUM-MERIT SCHOLARSHIP (NMMS) EXAMINATION")
        c.setFont("Helvetica-Bold", 9.5)
        c.drawCentredString(CENTER_X, PAGE_HEIGHT - 51, "MENTAL ABILITY GRAND TEST - 2")
        
        # Details bar
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(MARGIN_LR + 4, PAGE_HEIGHT - 66, "Time: 180 Minutes")
        c.drawCentredString(CENTER_X, PAGE_HEIGHT - 66, "Total Questions: 180")
        c.drawRightString(PAGE_WIDTH - MARGIN_LR - 4, PAGE_HEIGHT - 66, "Maximum Marks: 180")
        
        # Border box around header
        c.setLineWidth(1.0)
        c.setStrokeColor(colors.HexColor('#222222'))
        c.rect(MARGIN_LR, PAGE_HEIGHT - 74, PRINT_WIDTH, 48)
        
        # Candidate Info Box
        c.setFont("Helvetica", 7.5)
        c.drawString(MARGIN_LR + 4, PAGE_HEIGHT - 85, "Candidate Name: ___________________________    Roll No: ____________________    Date: ______________")
        c.setLineWidth(0.5)
        c.line(MARGIN_LR, PAGE_HEIGHT - 90, PAGE_WIDTH - MARGIN_LR, PAGE_HEIGHT - 90)

        # Center dividing line between columns on Page 1
        c.setLineWidth(0.5)
        c.setStrokeColor(colors.HexColor('#777777'))
        c.line(CENTER_X, MARGIN_TB, CENTER_X, PAGE_HEIGHT - 96)
        c.restoreState()

    def on_later_pages(c, doc):
        c.saveState()
        # Running header on Page 2+
        c.setFont("Helvetica-Bold", 8)
        c.drawString(MARGIN_LR, PAGE_HEIGHT - 26, "NMMS MENTAL ABILITY GRAND TEST - 2  |  180 QUESTIONS")
        c.drawRightString(PAGE_WIDTH - MARGIN_LR, PAGE_HEIGHT - 26, "PART - I : MAT")
        c.setLineWidth(0.5)
        c.setStrokeColor(colors.HexColor('#555555'))
        c.line(MARGIN_LR, PAGE_HEIGHT - 30, PAGE_WIDTH - MARGIN_LR, PAGE_HEIGHT - 30)

        # Center dividing line between columns on Page 2+
        c.setLineWidth(0.5)
        c.setStrokeColor(colors.HexColor('#777777'))
        c.line(CENTER_X, MARGIN_TB, CENTER_X, PAGE_HEIGHT - 34)
        c.restoreState()

    doc = BaseDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN_LR,
        rightMargin=MARGIN_LR,
        topMargin=MARGIN_TB,
        bottomMargin=MARGIN_TB
    )

    first_template = PageTemplate(id='FirstPage', frames=[frame_p1_left, frame_p1_right], onPage=on_first_page)
    later_template = PageTemplate(id='LaterPages', frames=[frame_later_left, frame_later_right], onPage=on_later_pages)
    doc.addPageTemplates([first_template, later_template])

    styles = get_styles()
    story = [NextPageTemplate('LaterPages')]

    for q in questions:
        if frame_break_q and q.q_num == frame_break_q:
            story.append(FrameBreak())
            
        q_elements = []

        if q.section_name:
            q_elements.append(Paragraph(f"<b>{q.section_name}</b>", styles['sec_header']))
        if q.directions:
            q_elements.append(Paragraph(q.directions, styles['directions']))

        stem_text = f"<b>{q.q_num}. {q.stem}</b>"
        q_elements.append(Paragraph(stem_text, styles['stem']))

        if q.matrix_data:
            q_elements.append(Spacer(1, 1.5))
            q_elements.append(format_matrix_table(q.matrix_data))
            q_elements.append(Spacer(1, 1.5))

        if q.image_path and os.path.exists(q.image_path):
            with PILImage.open(q.image_path) as pimg:
                img_w_px, img_h_px = pimg.size
            max_h = 84.0
            max_w = COL_WIDTH - 12.0
            scale = min(max_w / float(img_w_px), max_h / float(img_h_px))
            target_w = float(img_w_px) * scale
            target_h = float(img_h_px) * scale
            q_elements.append(Spacer(1, 1.5))
            q_elements.append(RLImage(q.image_path, width=target_w, height=target_h))
            q_elements.append(Spacer(1, 1.5))

        if q.options:
            opt_table = format_options_table(q.options, styles['option'], COL_WIDTH - 6)
            q_elements.append(opt_table)
            q_elements.append(Spacer(1, 2.5))

        story.append(KeepTogether(q_elements))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Question Paper PDF generated at: {output_path}")
    return output_path

def build_answer_key_pdf(questions: list[ExamQuestion], output_path: str):
    """
    Builds the Answer Key & Detailed Step-by-Step Explanations PDF.
    Page 1: Quick Reference Answer Key Table (1 to 180) in 10 columns.
    Pages 2+: Two-column detailed solutions.
    """
    frame_table_page = Frame(MARGIN_LR, MARGIN_TB, PRINT_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 8,
                             id='single_table', leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    frame_left = Frame(MARGIN_LR, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 20,
                       id='left', leftPadding=0, rightPadding=5, topPadding=3, bottomPadding=3)
    frame_right = Frame(MARGIN_LR + COL_WIDTH + COL_GAP, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 20,
                        id='right', leftPadding=5, rightPadding=0, topPadding=3, bottomPadding=3)

    def on_table_page(c, doc):
        pass

    def on_expl_page(c, doc):
        c.saveState()
        c.setFont("Helvetica-Bold", 8)
        c.drawString(MARGIN_LR, PAGE_HEIGHT - 26, "NMMS MEGA GRAND TEST - 2 : DETAILED SOLUTIONS  |  180 QUESTIONS")
        c.drawRightString(PAGE_WIDTH - MARGIN_LR, PAGE_HEIGHT - 26, "MAT SOLUTIONS")
        c.setLineWidth(0.5)
        c.setStrokeColor(colors.HexColor('#555555'))
        c.line(MARGIN_LR, PAGE_HEIGHT - 30, PAGE_WIDTH - MARGIN_LR, PAGE_HEIGHT - 30)

        c.setLineWidth(0.5)
        c.setStrokeColor(colors.HexColor('#777777'))
        c.line(CENTER_X, MARGIN_TB, CENTER_X, PAGE_HEIGHT - 34)
        c.restoreState()

    doc = BaseDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN_LR,
        rightMargin=MARGIN_LR,
        topMargin=MARGIN_TB,
        bottomMargin=MARGIN_TB
    )

    t_single = PageTemplate(id='KeyTablePage', frames=[frame_table_page], onPage=on_table_page)
    t_two_col = PageTemplate(id='ExplPage', frames=[frame_left, frame_right], onPage=on_expl_page)
    doc.addPageTemplates([t_single, t_two_col])

    styles = get_styles()
    story = []

    # Title & Subtitle on Page 1
    story.append(Paragraph("NMMS MENTAL ABILITY MEGA GRAND TEST - 2 (180 QUESTIONS)", styles['title']))
    story.append(Paragraph("<b>OFFICIAL ANSWER KEY GRID (QUESTIONS 1 TO 180)</b>", styles['subtitle']))
    story.append(Spacer(1, 8))

    # Grid for 180 questions: 18 rows x 10 columns (each column = Q.No + Ans)
    rows = 18
    cols = 10
    grid_data = []

    hdr = []
    for _ in range(cols):
        hdr.extend(["Q", "Ans"])
    grid_data.append(hdr)

    for r in range(rows):
        row = []
        for c in range(cols):
            q_num = c * rows + (r + 1)
            if q_num <= len(questions):
                q = questions[q_num - 1]
                row.extend([str(q.q_num), f"({q.correct_opt})"])
            else:
                row.extend(["", ""])
        grid_data.append(row)

    col_w_q = 26.5
    col_w_ans = 27.5
    col_widths = [col_w_q, col_w_ans] * cols
    key_table = Table(grid_data, colWidths=col_widths)
    key_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#003366')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7.2),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F2F5F8')]),
    ]))
    story.append(key_table)
    story.append(Spacer(1, 12))

    # Section-wise syllabus breakdown summary table
    summary_data = [
        ["Sec", "Topic Name", "Q. Nos", "Count", "Sec", "Topic Name", "Q. Nos", "Count"],
        ["1", "Number Series", "1 - 20", "20", "8", "Word Formation", "103 - 112", "10"],
        ["2", "Letter & Alphanumeric Series", "21 - 35", "15", "9", "Dictionary Order", "113 - 122", "10"],
        ["3", "Repeating Pattern Series", "36 - 45", "10", "10", "Arithmetic Principles", "123 - 140", "18"],
        ["4", "Coding & Decoding", "46 - 60", "15", "11", "Mathematical Operations", "141 - 152", "12"],
        ["5", "Word Analogy", "61 - 80", "20", "12", "Venn Diagrams & Survey", "153 - 162", "10"],
        ["6", "Number & Letter Analogy", "81 - 90", "10", "13", "Number Puzzles & Matrices", "163 - 175", "13"],
        ["7", "Classification (Odd One)", "91 - 102", "12", "14", "Non-Verbal & Spatial", "176 - 180", "5"],
        ["", "TOTAL QUESTIONS", "", "", "", "", "1 - 180", "180"]
    ]
    sum_table = Table(summary_data, colWidths=[24, 155, 50, 38, 24, 155, 50, 38])
    sum_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#333333')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6.8),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('ALIGN', (5, 0), (5, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#999999')),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#E8EEF5')),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))
    story.append(sum_table)

    # Next page for detailed solutions in 2 columns
    story.append(NextPageTemplate('ExplPage'))
    story.append(PageBreak())

    for q in questions:
        q_exp = []
        header = f"<b>Q{q.q_num}. Correct Option: ({q.correct_opt})</b>"
        q_exp.append(Paragraph(header, styles['exp_qhdr']))
        q_exp.append(Paragraph(f"<b>Question:</b> {q.stem}", styles['exp_body']))
        q_exp.append(Paragraph(f"<b>Explanation:</b> {q.explanation}", styles['exp_body']))
        story.append(KeepTogether(q_exp))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Answer Key PDF generated at: {output_path}")
    return output_path

def build_combined_complete_pdf(questions: list[ExamQuestion], output_path: str, frame_break_q: int = 179):
    """
    Builds a single master PDF containing Question Paper followed by Answer Key & Solutions.
    """
    h_header_p1 = 98.0
    frame_p1_left = Frame(MARGIN_LR, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - h_header_p1,
                          id='qp_p1_l', leftPadding=0, rightPadding=5, topPadding=3, bottomPadding=3)
    frame_p1_right = Frame(MARGIN_LR + COL_WIDTH + COL_GAP, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - h_header_p1,
                           id='qp_p1_r', leftPadding=5, rightPadding=0, topPadding=3, bottomPadding=3)

    frame_later_left = Frame(MARGIN_LR, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 20,
                             id='qp_lat_l', leftPadding=0, rightPadding=5, topPadding=3, bottomPadding=3)
    frame_later_right = Frame(MARGIN_LR + COL_WIDTH + COL_GAP, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 20,
                              id='qp_lat_r', leftPadding=5, rightPadding=0, topPadding=3, bottomPadding=3)

    frame_table = Frame(MARGIN_LR, MARGIN_TB, PRINT_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 8,
                        id='key_grid', leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

    def on_first_page(c, doc):
        c.saveState()
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(CENTER_X, PAGE_HEIGHT - 38, "NATIONAL MEANS-CUM-MERIT SCHOLARSHIP (NMMS) EXAMINATION")
        c.setFont("Helvetica-Bold", 9.5)
        c.drawCentredString(CENTER_X, PAGE_HEIGHT - 51, "MENTAL ABILITY GRAND TEST - 2")
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(MARGIN_LR + 4, PAGE_HEIGHT - 66, "Time: 180 Minutes")
        c.drawCentredString(CENTER_X, PAGE_HEIGHT - 66, "Total Questions: 180")
        c.drawRightString(PAGE_WIDTH - MARGIN_LR - 4, PAGE_HEIGHT - 66, "Maximum Marks: 180")
        c.setLineWidth(1.0)
        c.setStrokeColor(colors.HexColor('#222222'))
        c.rect(MARGIN_LR, PAGE_HEIGHT - 74, PRINT_WIDTH, 48)
        c.setFont("Helvetica", 7.5)
        c.drawString(MARGIN_LR + 4, PAGE_HEIGHT - 85, "Candidate Name: ___________________________    Roll No: ____________________    Date: ______________")
        c.setLineWidth(0.5)
        c.line(MARGIN_LR, PAGE_HEIGHT - 90, PAGE_WIDTH - MARGIN_LR, PAGE_HEIGHT - 90)
        c.setLineWidth(0.5)
        c.setStrokeColor(colors.HexColor('#777777'))
        c.line(CENTER_X, MARGIN_TB, CENTER_X, PAGE_HEIGHT - 96)
        c.restoreState()

    def on_later_pages(c, doc):
        c.saveState()
        c.setFont("Helvetica-Bold", 8)
        c.drawString(MARGIN_LR, PAGE_HEIGHT - 26, "NMMS MENTAL ABILITY GRAND TEST - 2  |  180 QUESTIONS")
        c.drawRightString(PAGE_WIDTH - MARGIN_LR, PAGE_HEIGHT - 26, "PART - I : MAT")
        c.setLineWidth(0.5)
        c.setStrokeColor(colors.HexColor('#555555'))
        c.line(MARGIN_LR, PAGE_HEIGHT - 30, PAGE_WIDTH - MARGIN_LR, PAGE_HEIGHT - 30)
        c.setLineWidth(0.5)
        c.setStrokeColor(colors.HexColor('#777777'))
        c.line(CENTER_X, MARGIN_TB, CENTER_X, PAGE_HEIGHT - 34)
        c.restoreState()

    def on_table_page(c, doc):
        pass

    doc = BaseDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN_LR,
        rightMargin=MARGIN_LR,
        topMargin=MARGIN_TB,
        bottomMargin=MARGIN_TB
    )

    t_first = PageTemplate(id='FirstPage', frames=[frame_p1_left, frame_p1_right], onPage=on_first_page)
    t_later = PageTemplate(id='LaterPages', frames=[frame_later_left, frame_later_right], onPage=on_later_pages)
    t_table = PageTemplate(id='KeyTablePage', frames=[frame_table], onPage=on_table_page)
    doc.addPageTemplates([t_first, t_later, t_table])

    styles = get_styles()
    story = [NextPageTemplate('LaterPages')]

    # 1. Question Paper
    for q in questions:
        if frame_break_q and q.q_num == frame_break_q:
            story.append(FrameBreak())
        q_elements = []
        if q.section_name:
            q_elements.append(Paragraph(f"<b>{q.section_name}</b>", styles['sec_header']))
        if q.directions:
            q_elements.append(Paragraph(q.directions, styles['directions']))

        stem_text = f"<b>{q.q_num}. {q.stem}</b>"
        q_elements.append(Paragraph(stem_text, styles['stem']))

        if q.matrix_data:
            q_elements.append(Spacer(1, 1.5))
            q_elements.append(format_matrix_table(q.matrix_data))
            q_elements.append(Spacer(1, 1.5))

        if q.image_path and os.path.exists(q.image_path):
            with PILImage.open(q.image_path) as pimg:
                img_w_px, img_h_px = pimg.size
            max_h = 84.0
            max_w = COL_WIDTH - 12.0
            scale = min(max_w / float(img_w_px), max_h / float(img_h_px))
            target_w = float(img_w_px) * scale
            target_h = float(img_h_px) * scale
            q_elements.append(Spacer(1, 1.5))
            q_elements.append(RLImage(q.image_path, width=target_w, height=target_h))
            q_elements.append(Spacer(1, 1.5))

        if q.options:
            opt_table = format_options_table(q.options, styles['option'], COL_WIDTH - 6)
            q_elements.append(opt_table)
            q_elements.append(Spacer(1, 2.5))
        story.append(KeepTogether(q_elements))

    # Transition to Answer Key
    story.append(NextPageTemplate('KeyTablePage'))
    story.append(PageBreak())

    story.append(Paragraph("NMMS MENTAL ABILITY MEGA GRAND TEST - 2 (180 QUESTIONS)", styles['title']))
    story.append(Paragraph("<b>OFFICIAL ANSWER KEY GRID (QUESTIONS 1 TO 180)</b>", styles['subtitle']))
    story.append(Spacer(1, 8))

    rows = 18
    cols = 10
    grid_data = []
    hdr = []
    for _ in range(cols):
        hdr.extend(["Q", "Ans"])
    grid_data.append(hdr)

    for r in range(rows):
        row = []
        for c in range(cols):
            q_num = c * rows + (r + 1)
            if q_num <= len(questions):
                q = questions[q_num - 1]
                row.extend([str(q.q_num), f"({q.correct_opt})"])
            else:
                row.extend(["", ""])
        grid_data.append(row)

    col_widths = [26.5, 27.5] * cols
    key_table = Table(grid_data, colWidths=col_widths)
    key_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#003366')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7.2),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F2F5F8')]),
    ]))
    story.append(key_table)
    story.append(Spacer(1, 12))

    # Transition to Explanations in 2 columns
    story.append(NextPageTemplate('LaterPages'))
    story.append(PageBreak())

    for q in questions:
        q_exp = []
        header = f"<b>Q{q.q_num}. Correct Option: ({q.correct_opt})</b>"
        q_exp.append(Paragraph(header, styles['exp_qhdr']))
        q_exp.append(Paragraph(f"<b>Question:</b> {q.stem}", styles['exp_body']))
        q_exp.append(Paragraph(f"<b>Explanation:</b> {q.explanation}", styles['exp_body']))
        story.append(KeepTogether(q_exp))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Combined Complete Master PDF generated at: {output_path}")
    return output_path

if __name__ == '__main__':
    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    questions = get_all_180_questions()
    print(f"Loaded {len(questions)} verified questions for Grand Test 2.")

    qp_path = os.path.join(output_dir, "NMMS_Mental_Ability_Grand_Test_2_180Q.pdf")
    key_path = os.path.join(output_dir, "NMMS_Mental_Ability_Grand_Test_2_180Q_Key_and_Solutions.pdf")
    complete_path = os.path.join(output_dir, "NMMS_Mental_Ability_Grand_Test_2_180Q_Complete.pdf")

    build_question_paper_pdf(questions, qp_path)
    build_answer_key_pdf(questions, key_path)
    build_combined_complete_pdf(questions, complete_path)

    print("ALL THREE PDF DOCUMENTS GENERATED SUCCESSFULLY!")
