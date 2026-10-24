"""
Master 180-Question Paper Generator for NMMS Mental Ability Test (MAT)
Curated from Official Telangana NMMS Question Papers (2022 - 2025)
Covering all 14 major topics with 180 authentic questions, answer key, and detailed solutions.
"""

import os
import sys
from dataclasses import dataclass
from typing import Optional, List
from PIL import Image as PILImage

from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Image as RLImage, Table, TableStyle, KeepTogether, PageBreak,
    NextPageTemplate
)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfgen import canvas

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_LR = 24.0
MARGIN_TB = 28.0
PRINT_WIDTH = PAGE_WIDTH - 2 * MARGIN_LR
COL_GAP = 12.0
COL_WIDTH = (PRINT_WIDTH - COL_GAP) / 2.0
CENTER_X = PAGE_WIDTH / 2.0

@dataclass
class ExamQuestion:
    q_num: int
    stem: str
    options: List[str]
    correct_opt: int
    explanation: str
    section_name: Optional[str] = None
    directions: Optional[str] = None
    image_path: Optional[str] = None
    matrix_data: Optional[List[List[str]]] = None

class NumberedCanvas(canvas.Canvas):
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
        self.setFont("Helvetica", 8)
        footer_text = f"Page {self._pageNumber} of {total_pages}"
        self.drawCentredString(CENTER_X, MARGIN_TB - 14, footer_text)
        self.drawString(MARGIN_LR, MARGIN_TB - 14, "NMMS MEGA GRAND TEST - 180 QUESTIONS")
        self.drawRightString(PAGE_WIDTH - MARGIN_LR, MARGIN_TB - 14, "MENTAL ABILITY TEST (MAT)")
        self.restoreState()

def get_styles():
    styles = getSampleStyleSheet()
    return {
        'title': ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=12, leading=15, alignment=TA_CENTER, spaceAfter=2),
        'subtitle': ParagraphStyle('DocSub', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11, alignment=TA_CENTER, spaceAfter=3),
        'sec_header': ParagraphStyle('SecHdr', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11, spaceBefore=4, spaceAfter=2, textColor=colors.HexColor('#990000')),
        'directions': ParagraphStyle('DirText', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=7.6, leading=9.8, spaceBefore=2, spaceAfter=3, textColor=colors.HexColor('#222222')),
        'stem': ParagraphStyle('QStem', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.0, leading=10.4, alignment=TA_LEFT, spaceBefore=2.5, spaceAfter=1.5),
        'option': ParagraphStyle('QOpt', parent=styles['Normal'], fontName='Helvetica', fontSize=7.8, leading=9.8, alignment=TA_LEFT),
        'exp_qhdr': ParagraphStyle('ExpHdr', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.0, leading=10.5, spaceBefore=2.5, spaceAfter=1, textColor=colors.HexColor('#003366')),
        'exp_body': ParagraphStyle('ExpTxt', parent=styles['Normal'], fontName='Helvetica', fontSize=7.4, leading=9.5, spaceAfter=2),
    }

def format_options_table(options: List[str], opt_style, col_width: float) -> Table:
    def clean_opt(i: int, txt: str) -> str:
        s = str(txt).strip()
        if s.startswith(f"({i+1})") or s.startswith(f"{i+1})"):
            return s
        return f"({i+1}) {s}"

    max_len = max(len(str(o)) for o in options)
    if max_len <= 14:
        c_w = col_width / 2.0
        data = [
            [Paragraph(clean_opt(0, options[0]), opt_style), Paragraph(clean_opt(1, options[1]), opt_style)],
            [Paragraph(clean_opt(2, options[2]), opt_style), Paragraph(clean_opt(3, options[3]), opt_style)]
        ]
        t = Table(data, colWidths=[c_w, c_w])
    elif max_len <= 26:
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
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.75, colors.black),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8F9FA')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    return t
