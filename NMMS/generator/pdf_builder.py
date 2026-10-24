"""
ReportLab PDF Builder for NMMS Mental Ability Test Papers
Creates portrait mode, printer-friendly, two-column PDFs split by a vertical line.
Generates:
1. Question Paper PDF (NMMS Mental Ability Grand Test - N)
2. Separate Answer Key & Explanations PDF
"""

import os
from PIL import Image as PILImage
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Image as RLImage, Table, TableStyle, KeepTogether, PageBreak,
    NextPageTemplate
)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from .questions_bank import Question

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_LR = 26.0
MARGIN_TB = 30.0
PRINT_WIDTH = PAGE_WIDTH - 2 * MARGIN_LR
COL_GAP = 14.0
COL_WIDTH = (PRINT_WIDTH - COL_GAP) / 2.0
CENTER_X = PAGE_WIDTH / 2.0

class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas to dynamically compute and stamp total page count on footer.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

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
        self.setFont("Helvetica", 9)
        footer_text = f"Page {self._pageNumber} of {total_pages}"
        self.drawCentredString(CENTER_X, MARGIN_TB - 14, footer_text)
        self.restoreState()


def get_styles():
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'PaperTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=17,
        alignment=TA_CENTER,
        spaceAfter=3,
        textColor=colors.black
    )
    
    subtitle_style = ParagraphStyle(
        'PaperSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        alignment=TA_CENTER,
        spaceAfter=5,
        textColor=colors.black
    )
    
    q_stem_style = ParagraphStyle(
        'QuestionStem',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=11.6,
        alignment=TA_LEFT,
        spaceBefore=3,
        spaceAfter=2,
        textColor=colors.black
    )
    
    opt_style = ParagraphStyle(
        'OptionText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.0,
        alignment=TA_LEFT,
        textColor=colors.black
    )
    
    exp_header_style = ParagraphStyle(
        'ExpHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.6,
        leading=11.2,
        spaceBefore=3,
        spaceAfter=1,
        textColor=colors.black
    )
    
    exp_body_style = ParagraphStyle(
        'ExpBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.0,
        leading=10.5,
        alignment=TA_LEFT,
        spaceAfter=2,
        textColor=colors.black
    )
    
    return {
        'title': title_style,
        'subtitle': subtitle_style,
        'stem': q_stem_style,
        'option': opt_style,
        'exp_header': exp_header_style,
        'exp_body': exp_body_style
    }

def format_options_table(options: list[str], opt_style, col_width: float, option_images: Optional[list[str]] = None) -> Table:
    """
    Neatly aligns 4 options. Uses 2x2 grid if short, or 1x4 rows if longer.
    If option_images is provided, creates a 2x2 grid table with (1), (2), (3), (4) labels and images.
    """
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
                    target_w = min(c_w - 24.0, float(pw) * 0.34)
                    target_h = float(ph) * (target_w / float(pw))
                else:  # Square or tall card (diagrams, paper folds)
                    target_h = min(36.0, float(ph) * 0.28)
                    target_w = float(pw) * (target_h / float(ph))
                cell_tbl = Table([[num_par, RLImage(img_p, width=target_w, height=target_h)]], colWidths=[18, target_w + 2])
                cell_tbl.setStyle(TableStyle([
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('LEFTPADDING', (0, 0), (-1, -1), 0),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 1),
                    ('TOPPADDING', (0, 0), (-1, -1), 1),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
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

    max_len = max((len(opt) for opt in options), default=0)
    
    def opt_text(i: int, opt: str) -> str:
        s = str(opt).strip()
        if s.startswith(f"({i+1})"):
            return s
        return f"({i+1}) {s}"
    
    if max_len <= 15:
        c_w = col_width / 2.0
        data = [
            [Paragraph(opt_text(0, options[0]), opt_style), Paragraph(opt_text(1, options[1]), opt_style)],
            [Paragraph(opt_text(2, options[2]), opt_style), Paragraph(opt_text(3, options[3]), opt_style)]
        ]
        t = Table(data, colWidths=[c_w, c_w])
        t.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 2),
            ('RIGHTPADDING', (0, 0), (-1, -1), 2),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ]))
        return t
    else:
        data = [[Paragraph(opt_text(i, opt), opt_style)] for i, opt in enumerate(options)]
        t = Table(data, colWidths=[col_width])
        t.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 2),
            ('RIGHTPADDING', (0, 0), (-1, -1), 2),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ]))
        return t

def build_question_paper_pdf(questions: list[Question], paper_code: str, output_path: str):
    """
    Builds the 90-question test paper PDF in portrait 2-column mode.
    """
    test_title = f"NMMS Mental Ability Grand Test - {paper_code}"
    
    # Page template setup
    # Page 1 top header block
    h_header_p1 = 62.0
    frame_p1_left = Frame(MARGIN_LR, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - h_header_p1, id='col1_p1',
                          leftPadding=0, rightPadding=6, topPadding=4, bottomPadding=4)
    frame_p1_right = Frame(MARGIN_LR + COL_WIDTH + COL_GAP, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - h_header_p1, id='col2_p1',
                           leftPadding=6, rightPadding=0, topPadding=4, bottomPadding=4)
    
    # Later pages: 2 columns from top to bottom
    frame_later_left = Frame(MARGIN_LR, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 24, id='col1_later',
                             leftPadding=0, rightPadding=6, topPadding=4, bottomPadding=4)
    frame_later_right = Frame(MARGIN_LR + COL_WIDTH + COL_GAP, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 24, id='col2_later',
                              leftPadding=6, rightPadding=0, topPadding=4, bottomPadding=4)
    
    def on_first_page(c, doc):
        c.saveState()
        # Header block on Page 1
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 36, "NMMS Mental Ability Grand Test")
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(MARGIN_LR, PAGE_HEIGHT - 52, "Time: 90 Minutes")
        c.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 52, f"Paper Code: {paper_code}")
        c.drawRightString(PAGE_WIDTH - MARGIN_LR, PAGE_HEIGHT - 52, "Max. Marks: 90")
        c.setLineWidth(1.0)
        c.setStrokeColor(colors.black)
        c.line(MARGIN_LR, PAGE_HEIGHT - 58, PAGE_WIDTH - MARGIN_LR, PAGE_HEIGHT - 58)
        
        # Center dividing line between columns on Page 1
        c.setLineWidth(0.75)
        c.line(CENTER_X, MARGIN_TB, CENTER_X, PAGE_HEIGHT - 64)
        c.restoreState()

    def on_later_pages(c, doc):
        c.saveState()
        # Running header on Page 2+
        c.setFont("Helvetica-Bold", 9)
        c.drawString(MARGIN_LR, PAGE_HEIGHT - 30, f"NMMS Mental Ability Grand Test  |  Code: {paper_code}")
        c.setLineWidth(0.5)
        c.setStrokeColor(colors.black)
        c.line(MARGIN_LR, PAGE_HEIGHT - 34, PAGE_WIDTH - MARGIN_LR, PAGE_HEIGHT - 34)
        
        # Center dividing line between columns on Page 2+
        c.setLineWidth(0.75)
        c.line(CENTER_X, MARGIN_TB, CENTER_X, PAGE_HEIGHT - 40)
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

    # Assemble all questions
    for q in questions:
        q_elements = []
        stem_text = f"<b>{q.q_num}. {q.stem}</b>"
        q_elements.append(Paragraph(stem_text, styles['stem']))
        
        if q.image_path and os.path.exists(q.image_path):
            with PILImage.open(q.image_path) as pimg:
                img_w_px, img_h_px = pimg.size
            target_w = min(220.0, float(img_w_px) * 0.54)
            scale = target_w / float(img_w_px)
            target_h = float(img_h_px) * scale
            q_elements.append(Spacer(1, 2))
            q_elements.append(RLImage(q.image_path, width=target_w, height=target_h))
            q_elements.append(Spacer(1, 2))
            
        opt_table = format_options_table(q.options, styles['option'], COL_WIDTH - 8, option_images=getattr(q, 'option_images', None))
        q_elements.append(opt_table)
        q_elements.append(Spacer(1, 3))
        
        story.append(KeepTogether(q_elements))

    doc.build(story, canvasmaker=NumberedCanvas)
    return output_path

def build_answer_key_pdf(questions: list[Question], paper_code: str, output_path: str):
    """
    Builds the Answer Key and Step-by-Step Explanations PDF.
    Contains:
    1. Quick Reference OMR Grid on Page 1 (full width, no dividing line).
    2. Detailed step-by-step solutions for every single question in 2 columns (Pages 2+).
    """
    key_title = f"NMMS Mental Ability Grand Test - {paper_code} - Answer Key & Explanations"
    
    doc = BaseDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN_LR,
        rightMargin=MARGIN_LR,
        topMargin=MARGIN_TB,
        bottomMargin=MARGIN_TB
    )
    
    # Page 1: Single full-width frame for clean OMR Table
    frame_table_page = Frame(MARGIN_LR, MARGIN_TB, PRINT_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 10, id='single_table',
                             leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    
    # Explanations: 2 columns with center dividing line
    frame_left = Frame(MARGIN_LR, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 24, id='left',
                       leftPadding=0, rightPadding=6, topPadding=4, bottomPadding=4)
    frame_right = Frame(MARGIN_LR + COL_WIDTH + COL_GAP, MARGIN_TB, COL_WIDTH, PAGE_HEIGHT - MARGIN_TB*2 - 24, id='right',
                        leftPadding=6, rightPadding=0, topPadding=4, bottomPadding=4)

    def on_table_page(c, doc):
        # Full width page, no vertical line
        pass

    def on_expl_page(c, doc):
        c.saveState()
        # Running header on Explanations
        c.setFont("Helvetica-Bold", 9)
        c.drawString(MARGIN_LR, PAGE_HEIGHT - 30, f"NMMS MAT Explanations  |  Code: {paper_code}")
        c.setLineWidth(0.5)
        c.setStrokeColor(colors.black)
        c.line(MARGIN_LR, PAGE_HEIGHT - 34, PAGE_WIDTH - MARGIN_LR, PAGE_HEIGHT - 34)
        
        # Center vertical dividing line between columns
        c.setLineWidth(0.75)
        c.line(CENTER_X, MARGIN_TB, CENTER_X, PAGE_HEIGHT - 40)
        c.restoreState()

    t_single = PageTemplate(id='KeyTablePage', frames=[frame_table_page], onPage=on_table_page)
    t_two_col = PageTemplate(id='ExplPage', frames=[frame_left, frame_right], onPage=on_expl_page)
    doc.addPageTemplates([t_single, t_two_col])

    styles = get_styles()
    story = []

    # Title & Subtitle
    story.append(Paragraph(key_title, styles['title']))
    story.append(Paragraph(f"<b>OFFICIAL ANSWER KEY (QUESTIONS 1 TO 90)  |  PAPER CODE: {paper_code}</b>", styles['subtitle']))
    story.append(Spacer(1, 10))

    # Build 6-column answer key grid (15 questions per column)
    rows = 15
    cols = 6
    grid_data = []
    
    hdr = []
    for _ in range(cols):
        hdr.extend(["Q.No", "Ans"])
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

    col_widths = [44, 44] * cols
    key_table = Table(grid_data, colWidths=col_widths)
    key_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.92, 0.92, 0.92)),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8.5),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(key_table)
    story.append(Spacer(1, 20))

    # Queue transition to ExplPage template and break to page 2
    story.append(NextPageTemplate('ExplPage'))
    story.append(PageBreak())

    # Step-by-step explanations in 2 columns
    for q in questions:
        q_exp = []
        header = f"<b>Q{q.q_num}. Option ({q.correct_opt})</b>"
        q_exp.append(Paragraph(header, styles['exp_header']))
        q_exp.append(Paragraph(q.explanation, styles['exp_body']))
        story.append(KeepTogether(q_exp))

    doc.build(story, canvasmaker=NumberedCanvas)
    return output_path
