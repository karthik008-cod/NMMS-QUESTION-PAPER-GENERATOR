"""
NMMS Question Paper Generator Package
"""

from .core import ExamQuestion, BLUEPRINT
from .diagrams import (
    generate_two_dice, generate_three_dice, generate_dice_net,
    generate_3d_cube, generate_clock_face, generate_mirror_problem,
    generate_water_problem, generate_paper_fold_cut_problem,
    generate_transparent_fold_problem, generate_circular_fold_cut_problem,
    generate_embedded_figure_problem, generate_analogy_problem,
    generate_dot_situation, generate_series_problem,
    generate_survey_venn_graduates, generate_embedded_problem
)
from .questions import build_test_questions
from .single_question_generator import (
    generate_single_replacement_question,
    generate_entire_section
)
from .pdf_engine import (
    build_question_paper_pdf, build_key_solutions_pdf, build_complete_master_pdf
)

__all__ = [
    'ExamQuestion', 'BLUEPRINT',
    'build_test_questions',
    'generate_single_replacement_question',
    'generate_entire_section',
    'build_question_paper_pdf',
    'build_key_solutions_pdf',
    'build_complete_master_pdf',
    'generate_survey_venn_graduates',
    'generate_transparent_fold_problem',
    'generate_circular_fold_cut_problem',
    'generate_embedded_figure_problem',
    'generate_analogy_problem',
    'generate_dot_situation',
    'generate_series_problem'
]
