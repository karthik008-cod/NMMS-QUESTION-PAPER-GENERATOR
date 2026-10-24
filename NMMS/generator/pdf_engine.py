"""
Professional Two-Column PDF Layout & Rendering Engine for NMMS Question Paper Generator
"""

import os
from typing import List, Optional
from PIL import Image as PILImage
import pymupdf

from datetime import datetime

from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Image as RLImage, Table, TableStyle, KeepTogether, PageBreak,
    NextPageTemplate, FrameBreak
)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfgen import canvas

from .core import ExamQuestion, BLUEPRINT

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_LR = 24.0
MARGIN_TB = 28.0
PRINT_WIDTH = PAGE_WIDTH - 2 * MARGIN_LR
COL_GAP = 12.0
COL_WIDTH = (PRINT_WIDTH - COL_GAP) / 2.0
CENTER_X = PAGE_WIDTH / 2.0

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []
        self.doc_title = getattr(self, 'doc_title', 'NMMS MEGA GRAND TEST - 180 QUESTIONS')

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_footer(num_pages)
            super().showPage()
        super().save()

    def draw_footer(self, total_pages):
        self.saveState()
        self.setFont("Helvetica", 8)
        footer_text = f"Page {self._pageNumber} of {total_pages}"
        self.drawCentredString(CENTER_X, MARGIN_TB - 14, footer_text)
        self.drawString(MARGIN_LR, MARGIN_TB - 14, "NMMS MEGA GRAND TEST - 180 QUESTIONS")
        self.drawRightString(PAGE_WIDTH - MARGIN_LR, MARGIN_TB - 14, "MENTAL ABILITY TEST (MAT)")
        self.restoreState()

def get_engine_styles():
    styles = getSampleStyleSheet()
    return {
        'title': ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=11, leading=14, alignment=TA_CENTER, spaceAfter=2),
        'subtitle': ParagraphStyle('DocSub', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11, alignment=TA_CENTER, spaceAfter=2),
        'sec_header': ParagraphStyle('SecHdr', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.2, leading=10.5, spaceBefore=3.5, spaceAfter=1.5, textColor=colors.HexColor('#990000')),
        'directions': ParagraphStyle('DirText', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=7.0, leading=9.0, spaceBefore=1.5, spaceAfter=2.5, textColor=colors.HexColor('#222222')),
        'stem': ParagraphStyle('QStem', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.8, leading=9.8, alignment=TA_LEFT, spaceBefore=2.0, spaceAfter=1.0),
        'option': ParagraphStyle('QOpt', parent=styles['Normal'], fontName='Helvetica', fontSize=7.4, leading=9.2, alignment=TA_LEFT),
        'exp_qhdr': ParagraphStyle('ExpHdr', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.8, leading=10.0, spaceBefore=2.0, spaceAfter=1.0, textColor=colors.HexColor('#003366')),
        'exp_body': ParagraphStyle('ExpTxt', parent=styles['Normal'], fontName='Helvetica', fontSize=7.2, leading=9.2, spaceAfter=2.0),
    }

def format_options_table(options: List[str], opt_style, col_width: float, option_images: Optional[List[str]] = None) -> Table:
    if option_images and any(option_images):
        c_w = col_width / 2.0
        cells = []
        for i in range(4):
            img_p = option_images[i] if i < len(option_images) else None
            num_par = Paragraph(f"<b>({i+1})</b>", opt_style)
            if img_p and os.path.isfile(img_p):
                with PILImage.open(img_p) as pimg:
                    pw, ph = pimg.size
                aspect = float(pw) / float(ph)
                if aspect > 1.8:  # Wide text card (words, codes)
                    target_w = min(c_w - 20.0, float(pw) * 0.30)
                    target_h = float(ph) * (target_w / float(pw))
                else:  # Square or tall card (diagrams, paper folds)
                    target_h = min(28.0, float(ph) * 0.24)
                    target_w = float(pw) * (target_h / float(ph))
                cell_tbl = Table([[num_par, RLImage(img_p, width=target_w, height=target_h)]], colWidths=[16, target_w + 2])
                cell_tbl.setStyle(TableStyle([
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('LEFTPADDING', (0, 0), (-1, -1), 0),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 1),
                    ('TOPPADDING', (0, 0), (-1, -1), 0.5),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 0.5),
                ]))
                cells.append(cell_tbl)
            else:
                opt_str = options[i] if i < len(options) else ""
                cells.append(Paragraph(f"({i+1}) {opt_str}", opt_style))
        data = [
            [cells[0], cells[1]],
            [cells[2], cells[3]]
        ]
        t = Table(data, colWidths=[c_w, c_w])
        t.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 1),
            ('RIGHTPADDING', (0, 0), (-1, -1), 1),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ]))
        return t

    def clean_opt(i: int, txt: str) -> str:
        s = str(txt).strip()
        if s.startswith(f"({i+1})") or s.startswith(f"{i+1})"):
            return s
        return f"({i+1}) {s}"

    max_len = max(len(str(o)) for o in options)
    if all(len(str(o).strip()) <= 5 for o in options) and len(options) == 4:
        c_w = col_width / 4.0
        data = [[
            Paragraph(clean_opt(0, options[0]), opt_style),
            Paragraph(clean_opt(1, options[1]), opt_style),
            Paragraph(clean_opt(2, options[2]), opt_style),
            Paragraph(clean_opt(3, options[3]), opt_style)
        ]]
        t = Table(data, colWidths=[c_w, c_w, c_w, c_w])
    elif max_len <= 15:
        c_w = col_width / 2.0
        data = [
            [Paragraph(clean_opt(0, options[0]), opt_style), Paragraph(clean_opt(1, options[1]), opt_style)],
            [Paragraph(clean_opt(2, options[2]), opt_style), Paragraph(clean_opt(3, options[3]), opt_style)]
        ]
        t = Table(data, colWidths=[c_w, c_w])
    elif max_len <= 28:
        c_w = col_width / 2.0
        data = [
            [Paragraph(clean_opt(0, options[0]), opt_style), Paragraph(clean_opt(1, options[1]), opt_style)],
            [Paragraph(clean_opt(2, options[2]), opt_style), Paragraph(clean_opt(3, options[3]), opt_style)]
        ]
        t = Table(data, colWidths=[c_w, c_w])
    else:
        data = [[Paragraph(clean_opt(i, opt), opt_style)] for i, opt in enumerate(options)]
        t = Table(data, colWidths=[col_width])

    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 1),
        ('RIGHTPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 0.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.5),
    ]))
    return t

def format_matrix_table(matrix: List[List[str]]) -> Table:
    num_cols = len(matrix[0])
    cell_w = 26.0
    t = Table(matrix, colWidths=[cell_w] * num_cols)
    t.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('GRID', (0,0), (-1,-1), 0.75, colors.black),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8F9FA')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    return t

def build_question_paper_pdf(questions: List[ExamQuestion], output_path: str, test_num: int = 3, frame_break_q: Optional[int] = None, paper_code: Optional[str] = None):
    if not paper_code:
        paper_code = f"{datetime.now():%Y%m%d}{test_num:03d}"

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
        c.setFont("Helvetica-Bold", 10.5)
        c.drawCentredString(CENTER_X, PAGE_HEIGHT - 38, "NATIONAL MEANS-CUM-MERIT SCHOLARSHIP (NMMS) EXAMINATION")
        c.setFont("Helvetica-Bold", 9.0)
        c.drawCentredString(CENTER_X, PAGE_HEIGHT - 51, f"MENTAL ABILITY GRAND TEST - {test_num}")
        
        c.setFont("Helvetica-Bold", 8.0)
        c.drawString(MARGIN_LR + 4, PAGE_HEIGHT - 65, "Time: 180 Minutes")
        c.drawCentredString(CENTER_X, PAGE_HEIGHT - 65, "Total Questions: 180   |   Max Marks: 180")
        c.drawRightString(PAGE_WIDTH - MARGIN_LR - 4, PAGE_HEIGHT - 65, f"PAPER CODE: {paper_code}")
        
        c.setLineWidth(1.0)
        c.setStrokeColor(colors.HexColor('#222222'))
        c.rect(MARGIN_LR, PAGE_HEIGHT - 72, PRINT_WIDTH, 46)
        
        c.setFont("Helvetica", 7.5)
        c.drawString(MARGIN_LR + 4, PAGE_HEIGHT - 83, f"Candidate Name: _____________________   Roll No: ______________   Date: __________   Code: {paper_code}")
        c.setLineWidth(0.5)
        c.line(MARGIN_LR, PAGE_HEIGHT - 88, PAGE_WIDTH - MARGIN_LR, PAGE_HEIGHT - 88)

        c.setLineWidth(0.5)
        c.setStrokeColor(colors.HexColor('#777777'))
        c.line(CENTER_X, MARGIN_TB, CENTER_X, PAGE_HEIGHT - 94)
        c.restoreState()

    def on_later_pages(c, doc):
        c.saveState()
        c.setFont("Helvetica-Bold", 8)
        c.drawString(MARGIN_LR, PAGE_HEIGHT - 26, f"NMMS MENTAL ABILITY GRAND TEST - {test_num}  |  180 QUESTIONS")
        c.drawRightString(PAGE_WIDTH - MARGIN_LR, PAGE_HEIGHT - 26, f"PAPER CODE: {paper_code}  |  PART - I : MAT")
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

    first_template = PageTemplate(id='FirstPage', frames=[frame_p1_left, frame_p1_right], onPage=on_first_page)
    later_template = PageTemplate(id='LaterPages', frames=[frame_later_left, frame_later_right], onPage=on_later_pages)
    doc.addPageTemplates([first_template, later_template])

    styles = get_engine_styles()
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
            max_h = 58.0
            max_w = COL_WIDTH - 12.0
            scale = min(max_w / float(img_w_px), max_h / float(img_h_px))
            target_w = float(img_w_px) * scale
            target_h = float(img_h_px) * scale
            q_elements.append(Spacer(1, 1.0))
            q_elements.append(RLImage(q.image_path, width=target_w, height=target_h))
            q_elements.append(Spacer(1, 1.0))

        if q.options:
            opt_table = format_options_table(q.options, styles['option'], COL_WIDTH - 6, option_images=getattr(q, 'option_images', None))
            q_elements.append(opt_table)

        q_elements.append(Spacer(1, 1.5))
        story.append(KeepTogether(q_elements))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Question Paper PDF generated at: {output_path}")

def build_key_solutions_pdf(questions: List[ExamQuestion], output_path: str, test_num: int = 3, paper_code: Optional[str] = None):
    if not paper_code:
        paper_code = f"{datetime.now():%Y%m%d}{test_num:03d}"

    styles = get_engine_styles()

    frame_p1 = Frame(MARGIN_LR, MARGIN_TB, PRINT_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 40,
                     id='full_p1', leftPadding=0, rightPadding=0, topPadding=4, bottomPadding=4)

    frame_later_left = Frame(MARGIN_LR, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 20,
                             id='sol_col1', leftPadding=0, rightPadding=5, topPadding=3, bottomPadding=3)
    frame_later_right = Frame(MARGIN_LR + COL_WIDTH + COL_GAP, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 20,
                              id='sol_col2', leftPadding=5, rightPadding=0, topPadding=3, bottomPadding=3)

    def on_first_page_key(c, doc):
        c.saveState()
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(CENTER_X, PAGE_HEIGHT - 38, f"NMMS MENTAL ABILITY MEGA GRAND TEST - {test_num} (180 QUESTIONS)")
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(CENTER_X, PAGE_HEIGHT - 51, f"OFFICIAL ANSWER KEY GRID  |  PAPER CODE: {paper_code}")
        c.restoreState()

    def on_later_pages_key(c, doc):
        c.saveState()
        c.setFont("Helvetica-Bold", 8)
        c.drawString(MARGIN_LR, PAGE_HEIGHT - 26, f"NMMS MEGA GRAND TEST - {test_num} : DETAILED SOLUTIONS")
        c.drawRightString(PAGE_WIDTH - MARGIN_LR, PAGE_HEIGHT - 26, f"PAPER CODE: {paper_code}  |  MAT SOLUTIONS")
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

    tmpl_p1 = PageTemplate(id='KeyP1', frames=[frame_p1], onPage=on_first_page_key)
    tmpl_later = PageTemplate(id='KeyLater', frames=[frame_later_left, frame_later_right], onPage=on_later_pages_key)
    doc.addPageTemplates([tmpl_p1, tmpl_later])

    story = [NextPageTemplate('KeyLater')]

    # Build 10 columns of 18 rows OMR key table
    col_headers = []
    for c in range(10):
        col_headers.extend(['Q', 'Ans'])

    table_data = [col_headers]
    for row in range(18):
        row_cells = []
        for col in range(10):
            q_idx = col * 18 + row
            if q_idx < len(questions):
                q = questions[q_idx]
                row_cells.extend([str(q.q_num), f"({q.correct_opt})"])
            else:
                row_cells.extend(["", ""])
        table_data.append(row_cells)

    q_col_w = 22.0
    ans_col_w = 32.5
    col_widths = [q_col_w, ans_col_w] * 10

    t_key = Table(table_data, colWidths=col_widths, repeatRows=1)
    t_key.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 6.5),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('TOPPADDING', (0,0), (-1,-1), 1.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.2),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 6.8),
    ]))
    for r in range(1, len(table_data)):
        if r % 2 == 0:
            t_key.setStyle(TableStyle([('BACKGROUND', (0, r), (-1, r), colors.HexColor('#F4F6F9'))]))

    story.append(t_key)
    story.append(Spacer(1, 10))

    # Blueprint distribution summary table
    bp_data = [["Sec", "Topic Name", "Q. Nos", "Count", "Sec", "Topic Name", "Q. Nos", "Count"]]
    half = (len(BLUEPRINT) + 1) // 2
    for i in range(half):
        s1 = BLUEPRINT[i]
        row_cells = [str(s1.sec_num), s1.name, s1.q_range, str(s1.count)]
        if i + half < len(BLUEPRINT):
            s2 = BLUEPRINT[i + half]
            row_cells.extend([str(s2.sec_num), s2.name, s2.q_range, str(s2.count)])
        else:
            row_cells.extend(["", "", "", ""])
        bp_data.append(row_cells)

    bp_data.append(["", "TOTAL QUESTIONS", "", "", "", "", "1 - 180", "180"])

    bp_col_w = [18, 145, 45, 25, 18, 145, 45, 25]
    t_bp = Table(bp_data, colWidths=bp_col_w)
    t_bp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#222222')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 6.0),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('ALIGN', (1,1), (1,-2), 'LEFT'),
        ('ALIGN', (5,1), (5,-2), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('TOPPADDING', (0,0), (-1,-1), 0.8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.8),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 5.8),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#E8EDF5')),
        ('FONTNAME', (0,-1), (-1,-1), 'Helvetica-Bold'),
    ]))
    story.append(t_bp)
    story.append(PageBreak())

    # Pages 2+: Step-by-Step Solutions
    for q in questions:
        sol_elements = []
        hdr_txt = f"<b>Q{q.q_num}. Correct Option: ({q.correct_opt})</b>"
        sol_elements.append(Paragraph(hdr_txt, styles['exp_qhdr']))

        q_stem_short = q.stem if len(q.stem) <= 120 else q.stem[:117] + "..."
        sol_elements.append(Paragraph(f"<b>Question:</b> {q_stem_short}", styles['exp_body']))
        sol_elements.append(Paragraph(f"<b>Explanation:</b> {q.explanation}", styles['exp_body']))
        sol_elements.append(Spacer(1, 2.0))
        story.append(KeepTogether(sol_elements))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Answer Key & Solutions PDF generated at: {output_path}")

def build_complete_master_pdf(qp_path: str, key_path: str, complete_path: str):
    qp_doc = pymupdf.open(qp_path)
    key_doc = pymupdf.open(key_path)

    complete_doc = pymupdf.open()
    complete_doc.insert_pdf(qp_doc)
    complete_doc.insert_pdf(key_doc)
    complete_doc.save(complete_path)
    print(f"Master Combined PDF generated at: {complete_path} ({len(complete_doc)} pages)")
