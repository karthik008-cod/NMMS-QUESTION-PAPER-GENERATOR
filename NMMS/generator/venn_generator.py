"""
NMMS Venn Diagram Generator Engine
Contains 12 distinct Geometric Venn patterns (4 shapes) and 12 distinct Survey Venn patterns (3 shapes).
Guarantees:
- Publication-quality HD 300 DPI vector diagrams with mathematically verified centroids.
- Numbers placed with generous clearance from all boundaries.
- Precise multi-question groups (Q131-134 for Geometric, Q135-138 for Survey) with 100% consistent logic.
"""

import os
import random
from typing import List, Dict, Any, Tuple, Optional
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from .core import ExamQuestion, SectionInfo, BLUEPRINT
from .diagrams import VENN_4SHAPE_CENTROIDS, generate_four_shape_venn_diagram

def ensure_dir(path: str) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)

def helper_shuffle_options(opts: List[str], correct_idx: int) -> Tuple[List[str], int]:
    """Helper to shuffle options while preserving the correct answer index (1-indexed)."""
    if opts == ["(1)", "(2)", "(3)", "(4)"] or len(opts) != 4:
        return list(opts), correct_idx
    correct_val = opts[correct_idx - 1]
    shuffled = list(opts)
    random.shuffle(shuffled)
    new_correct_idx = shuffled.index(correct_val) + 1
    return shuffled, new_correct_idx


# ===========================================================================
# SURVEY VENN RENDERER (TRIANGLE, RECTANGLE, CIRCLE)
# ===========================================================================

def render_survey_venn(filepath: str, nums: Dict[str, Any]) -> str:
    """
    Renders 100% closed, vector-crisp survey Venn diagram with Triangle,
    Rectangle, and Circle. Numbers placed at safe non-overlapping centroids.
    """
    ensure_dir(filepath)
    fig, ax = plt.subplots(figsize=(4.2, 3.4), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')

    tri = patches.Polygon([[0.08, 0.22], [0.48, 0.94], [0.88, 0.22]], closed=True, fill=False, edgecolor='black', lw=2.4)
    rect = patches.Rectangle((0.36, 0.06), 0.52, 0.44, fill=False, edgecolor='black', lw=2.4)
    circ = patches.Circle((0.34, 0.30), 0.26, fill=False, edgecolor='black', lw=2.4)

    ax.add_patch(tri)
    ax.add_patch(rect)
    ax.add_patch(circ)

    centroids = {
        'T': (0.480, 0.666),
        'C': (0.275, 0.137),
        'TC': (0.256, 0.323),
        'ALL': (0.477, 0.337),
        'TR': (0.704, 0.324),
        'CR': (0.436, 0.144),
        'R': (0.641, 0.140)
    }

    for k, pos in centroids.items():
        if k in nums:
            ax.text(pos[0], pos[1], str(nums[k]), fontsize=15, fontweight='bold', ha='center', va='center')

    ax.set_xlim(-0.02, 0.98)
    ax.set_ylim(-0.02, 1.02)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath


# ===========================================================================
# 12 GEOMETRIC VENN PATTERNS (Q131 - Q134)
# ===========================================================================

VENN_GEOM_DEFINITIONS = [
    {
        'id': 'engineers_doctors_farmers_leaders',
        'intro': "In the following Venn diagram, Rectangle represents Engineers, Triangle represents Doctors, Square represents Farmers, and Circle represents Leaders. Answer questions 131 to 134 based on this figure.",
        'regions': {
            (1, 0, 0, 0): '19', (0, 1, 0, 0): '2', (0, 0, 1, 0): '17', (0, 0, 0, 1): '16',
            (1, 1, 0, 0): '7', (1, 1, 1, 0): '6', (1, 1, 1, 1): '4', (1, 0, 1, 1): '5', (0, 0, 1, 1): '9'
        },
        'questions': [
            ("How many people are only farmers?", ["2", "0", "1", "3"], 1, "Region inside Square only, excluding triangle, rectangle, and circle: number 2."),
            ("How many engineers are farmers and doctors, but NOT leaders?", ["6", "2", "4", "5"], 1, "Common to Rectangle (Engineers), Square (Farmers), and Triangle (Doctors), but outside Circle (Leaders) is number 6."),
            ("How many leaders are there who are also farmers, doctors and engineers?", ["4", "2", "6", "None"], 1, "Region common to all four geometric shapes contains number 4."),
            ("How many people are Doctors only?", ["19", "17", "16", "2"], 1, "Region lying solely inside Triangle (Doctors) is number 19.")
        ]
    },
    {
        'id': 'urban_educated_hardworking_employed',
        'intro': "In the following Venn diagram, Square represents Urban People, Circle represents Educated People, Triangle represents Hardworking People, and Rectangle represents Employed People. Answer questions 131 to 134 based on this figure.",
        'regions': {
            (1, 0, 0, 0): '11', (0, 1, 0, 0): '10', (0, 0, 1, 0): '15', (0, 0, 0, 1): '12',
            (1, 1, 0, 0): '8', (1, 1, 1, 0): '7', (1, 1, 1, 1): '5', (1, 0, 1, 1): '3', (0, 0, 1, 1): '9'
        },
        'questions': [
            ("Which number represents Educated people who are Hardworking and Employed, but NOT Urban?", ["3", "8", "7", "5"], 1, "Region common to Circle (Educated), Triangle (Hardworking), and Rectangle (Employed), outside Square (Urban) is number 3."),
            ("Which number represents Urban people who are Hardworking and Employed, but not Educated?", ["7", "10", "5", "9"], 1, "Common to Square, Triangle, and Rectangle, but strictly outside Circle is number 7."),
            ("Which number represents Hardworking people who are also Urban, Educated, and Employed?", ["5", "3", "7", "8"], 1, "Region common to all 4 geometric shapes contains number 5."),
            ("How many people are Educated only?", ["12", "11", "10", "15"], 1, "Region inside Circle only is number 12.")
        ]
    },
    {
        'id': 'artists_scientists_teachers_writers',
        'intro': "In the following Venn diagram, Circle represents Artists, Triangle represents Scientists, Square represents Teachers, and Rectangle represents Writers. Answer questions 131 to 134 based on this figure.",
        'regions': {
            (1, 0, 0, 0): '14', (0, 1, 0, 0): '8', (0, 0, 1, 0): '21', (0, 0, 0, 1): '13',
            (1, 1, 0, 0): '9', (1, 1, 1, 0): '5', (1, 1, 1, 1): '3', (1, 0, 1, 1): '6', (0, 0, 1, 1): '7'
        },
        'questions': [
            ("How many Scientists are Teachers, but neither Writers nor Artists?", ["9", "5", "3", "14"], 1, "Common to Triangle (Scientists) and Square (Teachers), outside Rectangle and Circle is number 9."),
            ("How many Writers are also Artists and Scientists, but NOT Teachers?", ["6", "7", "5", "3"], 1, "Common to Rectangle, Circle, and Triangle, outside Square is number 6."),
            ("How many individuals belong to all four categories (Artists, Scientists, Teachers, and Writers)?", ["3", "5", "6", "9"], 1, "Region common to all four shapes is number 3."),
            ("How many individuals are Writers only?", ["21", "14", "8", "13"], 1, "Region strictly inside Rectangle only is number 21.")
        ]
    },
    {
        'id': 'students_athletes_musicians_dancers',
        'intro': "In the following Venn diagram, Triangle represents Students, Circle represents Athletes, Rectangle represents Musicians, and Square represents Dancers. Answer questions 131 to 134 based on this figure.",
        'regions': {
            (1, 0, 0, 0): '18', (0, 1, 0, 0): '6', (0, 0, 1, 0): '22', (0, 0, 0, 1): '14',
            (1, 1, 0, 0): '7', (1, 1, 1, 0): '8', (1, 1, 1, 1): '4', (1, 0, 1, 1): '10', (0, 0, 1, 1): '5'
        },
        'questions': [
            ("How many Students are both Athletes and Musicians, but NOT Dancers?", ["10", "4", "5", "8"], 1, "Common to Triangle (Students), Rectangle (Musicians), and Circle (Athletes), outside Square (Dancers) contains number 10."),
            ("How many Dancers are also Students and Musicians, but NOT Athletes?", ["8", "7", "4", "6"], 1, "Common to Square (Dancers), Triangle (Students), and Rectangle (Musicians), outside Circle is number 8."),
            ("How many individuals are active in all four fields?", ["4", "10", "8", "5"], 1, "Region common to all four geometric figures contains number 4."),
            ("How many are Musicians only?", ["22", "18", "14", "6"], 1, "Region lying exclusively inside Rectangle is number 22.")
        ]
    },
    {
        'id': 'rural_literate_women_employed',
        'intro': "In the following Venn diagram, Rectangle represents Rural Residents, Circle represents Literate People, Triangle represents Employed Individuals, and Square represents Women. Answer questions 131 to 134 based on this figure.",
        'regions': {
            (1, 0, 0, 0): '15', (0, 1, 0, 0): '9', (0, 0, 1, 0): '25', (0, 0, 0, 1): '18',
            (1, 1, 0, 0): '10', (1, 1, 1, 0): '6', (1, 1, 1, 1): '4', (1, 0, 1, 1): '8', (0, 0, 1, 1): '12'
        },
        'questions': [
            ("How many Rural Residents are Literate, but neither Employed nor Women?", ["12", "25", "18", "8"], 1, "Common to Rectangle (Rural) and Circle (Literate), outside Triangle and Square is number 12."),
            ("How many Employed Women are Rural Residents, but NOT Literate?", ["6", "10", "4", "9"], 1, "Common to Triangle (Employed), Square (Women), and Rectangle (Rural), outside Circle is number 6."),
            ("How many Rural Employed Women are Literate?", ["4", "6", "8", "10"], 1, "Common to all four shapes is number 4."),
            ("How many Women are neither Employed, nor Rural, nor Literate?", ["9", "15", "25", "18"], 1, "Region inside Square only is number 9.")
        ]
    },
    {
        'id': 'singers_actors_directors_producers',
        'intro': "In the following Venn diagram, Circle represents Singers, Square represents Actors, Triangle represents Directors, and Rectangle represents Producers. Answer questions 131 to 134 based on this figure.",
        'regions': {
            (1, 0, 0, 0): '16', (0, 1, 0, 0): '11', (0, 0, 1, 0): '20', (0, 0, 0, 1): '17',
            (1, 1, 0, 0): '8', (1, 1, 1, 0): '7', (1, 1, 1, 1): '5', (1, 0, 1, 1): '6', (0, 0, 1, 1): '10'
        },
        'questions': [
            ("How many Directors are Actors, but neither Producers nor Singers?", ["8", "7", "5", "16"], 1, "Common to Triangle (Directors) and Square (Actors), outside Rectangle and Circle is number 8."),
            ("How many Producers are Singers and Directors, but NOT Actors?", ["6", "10", "7", "5"], 1, "Common to Rectangle, Circle, and Triangle, outside Square is number 6."),
            ("How many artists work as Singers, Actors, Directors, and Producers simultaneously?", ["5", "6", "7", "8"], 1, "Common to all four shapes is number 5."),
            ("How many people are Producers only?", ["20", "17", "16", "11"], 1, "Region strictly inside Rectangle is number 20.")
        ]
    },
    {
        'id': 'lawyers_judges_police_citizens',
        'intro': "In the following Venn diagram, Rectangle represents Lawyers, Triangle represents Judges, Square represents Police Officers, and Circle represents Senior Citizens. Answer questions 131 to 134 based on this figure.",
        'regions': {
            (1, 0, 0, 0): '13', (0, 1, 0, 0): '14', (0, 0, 1, 0): '24', (0, 0, 0, 1): '19',
            (1, 1, 0, 0): '6', (1, 1, 1, 0): '5', (1, 1, 1, 1): '2', (1, 0, 1, 1): '7', (0, 0, 1, 1): '8'
        },
        'questions': [
            ("How many Judges are Lawyers and Senior Citizens, but NOT Police Officers?", ["7", "8", "5", "2"], 1, "Common to Triangle (Judges), Rectangle (Lawyers), and Circle (Senior Citizens), outside Square is number 7."),
            ("How many Police Officers are both Judges and Lawyers?", ["7", "5", "2", "6"], 1, "Common to Square, Triangle, and Rectangle: 5 + 2 = 7."),
            ("How many Senior Citizens are Lawyers, Judges, and Police Officers?", ["2", "5", "7", "8"], 1, "Intersection of all four geometric shapes is number 2."),
            ("How many individuals are Judges only?", ["13", "14", "24", "19"], 1, "Region solely inside Triangle is number 13.")
        ]
    },
    {
        'id': 'cricketers_footballers_hockey_tennis',
        'intro': "In the following Venn diagram, Circle represents Cricketers, Triangle represents Footballers, Rectangle represents Hockey Players, and Square represents Tennis Players. Answer questions 131 to 134 based on this figure.",
        'regions': {
            (1, 0, 0, 0): '23', (0, 1, 0, 0): '7', (0, 0, 1, 0): '19', (0, 0, 0, 1): '15',
            (1, 1, 0, 0): '9', (1, 1, 1, 0): '6', (1, 1, 1, 1): '4', (1, 0, 1, 1): '5', (0, 0, 1, 1): '8'
        },
        'questions': [
            ("How many Footballers play both Tennis and Hockey, but NOT Cricket?", ["6", "9", "4", "5"], 1, "Common to Triangle (Footballers), Square (Tennis), and Rectangle (Hockey), outside Circle is number 6."),
            ("How many Cricketers play Hockey and Football, but NOT Tennis?", ["5", "8", "6", "4"], 1, "Common to Circle, Rectangle, and Triangle, outside Square is number 5."),
            ("How many athletes play all four sports?", ["4", "5", "6", "9"], 1, "Intersection of all 4 shapes is number 4."),
            ("How many athletes play Football only?", ["23", "19", "15", "7"], 1, "Region strictly inside Triangle is number 23.")
        ]
    },
    {
        'id': 'chemists_physicists_biologists_mathematicians',
        'intro': "In the following Venn diagram, Rectangle represents Chemists, Triangle represents Physicists, Square represents Biologists, and Circle represents Mathematicians. Answer questions 131 to 134 based on this figure.",
        'regions': {
            (1, 0, 0, 0): '17', (0, 1, 0, 0): '12', (0, 0, 1, 0): '26', (0, 0, 0, 1): '18',
            (1, 1, 0, 0): '8', (1, 1, 1, 0): '7', (1, 1, 1, 1): '3', (1, 0, 1, 1): '6', (0, 0, 1, 1): '9'
        },
        'questions': [
            ("How many Physicists are Chemists and Mathematicians, but NOT Biologists?", ["6", "9", "7", "3"], 1, "Common to Triangle (Physicists), Rectangle (Chemists), and Circle (Mathematicians), outside Square is number 6."),
            ("How many Biologists are both Physicists and Chemists?", ["10", "7", "3", "8"], 1, "Common to Square, Triangle, and Rectangle: 7 + 3 = 10."),
            ("How many scientists have expertise in all four branches?", ["3", "6", "7", "8"], 1, "Common to all four shapes is number 3."),
            ("How many are Chemists only?", ["26", "18", "17", "12"], 1, "Region strictly inside Rectangle is number 26.")
        ]
    },
    {
        'id': 'politicians_journalists_economists_historians',
        'intro': "In the following Venn diagram, Square represents Politicians, Circle represents Journalists, Triangle represents Economists, and Rectangle represents Historians. Answer questions 131 to 134 based on this figure.",
        'regions': {
            (1, 0, 0, 0): '15', (0, 1, 0, 0): '11', (0, 0, 1, 0): '23', (0, 0, 0, 1): '14',
            (1, 1, 0, 0): '7', (1, 1, 1, 0): '6', (1, 1, 1, 1): '4', (1, 0, 1, 1): '8', (0, 0, 1, 1): '9'
        },
        'questions': [
            ("How many Economists are Historians and Journalists, but NOT Politicians?", ["8", "9", "6", "4"], 1, "Common to Triangle (Economists), Rectangle (Historians), and Circle (Journalists), outside Square is number 8."),
            ("How many Politicians are Economists and Historians, but NOT Journalists?", ["6", "7", "4", "11"], 1, "Common to Square, Triangle, and Rectangle, outside Circle is number 6."),
            ("How many persons belong to all four categories?", ["4", "6", "7", "8"], 1, "Common to all four shapes is number 4."),
            ("How many are Historians only?", ["23", "15", "14", "11"], 1, "Region strictly inside Rectangle is number 23.")
        ]
    },
    {
        'id': 'bankers_accountants_auditors_managers',
        'intro': "In the following Venn diagram, Triangle represents Bankers, Rectangle represents Accountants, Square represents Auditors, and Circle represents Corporate Managers. Answer questions 131 to 134 based on this figure.",
        'regions': {
            (1, 0, 0, 0): '21', (0, 1, 0, 0): '9', (0, 0, 1, 0): '25', (0, 0, 0, 1): '16',
            (1, 1, 0, 0): '8', (1, 1, 1, 0): '5', (1, 1, 1, 1): '3', (1, 0, 1, 1): '7', (0, 0, 1, 1): '11'
        },
        'questions': [
            ("How many Bankers are Accountants and Managers, but NOT Auditors?", ["7", "11", "5", "3"], 1, "Common to Triangle (Bankers), Rectangle (Accountants), and Circle (Managers), outside Square is number 7."),
            ("How many Auditors are Bankers and Accountants, but NOT Managers?", ["5", "8", "3", "9"], 1, "Common to Square, Triangle, and Rectangle, outside Circle is number 5."),
            ("How many professionals hold all four roles?", ["3", "5", "7", "8"], 1, "Common to all four shapes is number 3."),
            ("How many professionals are Bankers only?", ["21", "25", "16", "9"], 1, "Region strictly inside Triangle is number 21.")
        ]
    },
    {
        'id': 'poets_novelists_painters_sculptors',
        'intro': "In the following Venn diagram, Circle represents Poets, Triangle represents Novelists, Square represents Painters, and Rectangle represents Sculptors. Answer questions 131 to 134 based on this figure.",
        'regions': {
            (1, 0, 0, 0): '18', (0, 1, 0, 0): '8', (0, 0, 1, 0): '22', (0, 0, 0, 1): '15',
            (1, 1, 0, 0): '7', (1, 1, 1, 0): '6', (1, 1, 1, 1): '4', (1, 0, 1, 1): '5', (0, 0, 1, 1): '10'
        },
        'questions': [
            ("How many Novelists are Sculptors and Poets, but NOT Painters?", ["5", "10", "6", "4"], 1, "Common to Triangle (Novelists), Rectangle (Sculptors), and Circle (Poets), outside Square is number 5."),
            ("How many Painters are both Novelists and Sculptors?", ["10", "6", "4", "7"], 1, "Common to Square, Triangle, and Rectangle: 6 + 4 = 10."),
            ("How many creative artists engage in all four art forms?", ["4", "5", "6", "7"], 1, "Common to all four shapes is number 4."),
            ("How many artists are Sculptors only?", ["22", "18", "15", "8"], 1, "Region strictly inside Rectangle is number 22.")
        ]
    }
]

VENN_GEOM_ALL_IDS: List[str] = [cfg['id'] for cfg in VENN_GEOM_DEFINITIONS]


# ===========================================================================
# 12 SURVEY VENN PATTERNS (Q135 - Q138)
# ===========================================================================

VENN_SURVEY_DEFINITIONS = [
    {
        'id': 'female_graduates_employed_loans',
        'intro': "The following diagram shows results of a survey: Triangle represents Female Graduates, Rectangle represents Self-Employed Females, and Circle represents Self-Employed Females with Bank Loan Facility. Answer questions 135 to 138 based on this figure.",
        'nums': {'T': 4, 'C': 1, 'TC': 7, 'ALL': 5, 'TR': 8, 'CR': 6, 'R': 3},
        'questions': [
            ("How many female graduates are self-employed?", ["13", "12", "15", "20"], 1, "Common region of Triangle and Rectangle contains 5 + 8 = 13."),
            ("How many female graduates are not self-employed?", ["11", "4", "8", "15"], 1, "Inside Triangle but outside Rectangle: 4 + 7 = 11."),
            ("How many non-graduate females are self-employed?", ["9", "7", "21", "15"], 1, "Inside Rectangle but outside Triangle: 6 + 3 = 9."),
            ("How many self-employed females have bank loan facility?", ["11", "5", "12", "15"], 1, "Inside Rectangle and Circle: 5 + 6 = 11.")
        ]
    },
    {
        'id': 'rural_computer_scholarship',
        'intro': "The following diagram shows results of a school survey: Triangle represents Rural Students, Rectangle represents Computer Literate Students, and Circle represents Scholarship Awardees. Answer questions 135 to 138 based on this figure.",
        'nums': {'T': 6, 'C': 2, 'TC': 8, 'ALL': 7, 'TR': 9, 'CR': 5, 'R': 4},
        'questions': [
            ("How many rural students are computer literate?", ["16", "9", "14", "18"], 1, "Common region of Triangle and Rectangle contains 7 + 9 = 16."),
            ("How many rural students are not computer literate?", ["14", "6", "8", "20"], 1, "Inside Triangle outside Rectangle: 6 + 8 = 14."),
            ("How many non-rural students are computer literate?", ["9", "4", "5", "12"], 1, "Inside Rectangle outside Triangle: 5 + 4 = 9."),
            ("How many computer literate students receive scholarships?", ["12", "7", "5", "16"], 1, "Inside Rectangle and Circle: 7 + 5 = 12.")
        ]
    },
    {
        'id': 'college_teachers_researchers_phd',
        'intro': "The following diagram shows results of a university survey: Triangle represents College Teachers, Rectangle represents Published Researchers, and Circle represents PhD Degree Holders. Answer questions 135 to 138 based on this figure.",
        'nums': {'T': 5, 'C': 3, 'TC': 6, 'ALL': 8, 'TR': 10, 'CR': 7, 'R': 4},
        'questions': [
            ("How many college teachers are published researchers?", ["18", "10", "15", "20"], 1, "Common region of Triangle and Rectangle contains 8 + 10 = 18."),
            ("How many college teachers are not published researchers?", ["11", "5", "6", "14"], 1, "Inside Triangle outside Rectangle: 5 + 6 = 11."),
            ("How many published researchers are not college teachers?", ["11", "7", "4", "15"], 1, "Inside Rectangle outside Triangle: 7 + 4 = 11."),
            ("How many published researchers hold a PhD degree?", ["15", "8", "7", "18"], 1, "Inside Rectangle and Circle: 8 + 7 = 15.")
        ]
    },
    {
        'id': 'science_athletes_ncc',
        'intro': "The following diagram shows results of a youth academy survey: Triangle represents Science Students, Rectangle represents Sports Athletes, and Circle represents NCC Cadets. Answer questions 135 to 138 based on this figure.",
        'nums': {'T': 7, 'C': 2, 'TC': 5, 'ALL': 6, 'TR': 11, 'CR': 8, 'R': 5},
        'questions': [
            ("How many science students are sports athletes?", ["17", "11", "14", "20"], 1, "Common region of Triangle and Rectangle contains 6 + 11 = 17."),
            ("How many science students are not sports athletes?", ["12", "7", "5", "16"], 1, "Inside Triangle outside Rectangle: 7 + 5 = 12."),
            ("How many sports athletes are not science students?", ["13", "8", "5", "18"], 1, "Inside Rectangle outside Triangle: 8 + 5 = 13."),
            ("How many sports athletes are NCC cadets?", ["14", "6", "8", "16"], 1, "Inside Rectangle and Circle: 6 + 8 = 14.")
        ]
    },
    {
        'id': 'languages_telugu_hindi_english',
        'intro': "The following diagram shows results of a survey on language proficiency: Triangle represents Telugu Speakers, Rectangle represents Hindi Speakers, and Circle represents English Speakers. Answer questions 135 to 138 based on this figure.",
        'nums': {'T': 9, 'C': 4, 'TC': 6, 'ALL': 7, 'TR': 12, 'CR': 5, 'R': 8},
        'questions': [
            ("How many people speak both Telugu and Hindi?", ["19", "12", "15", "22"], 1, "Common region of Triangle (Telugu) and Rectangle (Hindi): 7 + 12 = 19."),
            ("How many people speak Telugu but NOT Hindi?", ["15", "9", "6", "18"], 1, "Inside Triangle outside Rectangle: 9 + 6 = 15."),
            ("How many people speak Hindi but NOT Telugu?", ["13", "8", "5", "16"], 1, "Inside Rectangle outside Triangle: 8 + 5 = 13."),
            ("How many people speak both Hindi and English?", ["12", "7", "5", "15"], 1, "Inside Rectangle and Circle: 7 + 5 = 12.")
        ]
    },
    {
        'id': 'newspaper_hindu_times_express',
        'intro': "The following diagram represents a readership survey: Triangle represents The Hindu Readers, Rectangle represents Times of India Readers, and Circle represents Indian Express Readers. Answer questions 135 to 138 based on this figure.",
        'nums': {'T': 8, 'C': 3, 'TC': 7, 'ALL': 6, 'TR': 10, 'CR': 9, 'R': 5},
        'questions': [
            ("How many people read both The Hindu and Times of India?", ["16", "10", "13", "20"], 1, "Common region of Triangle and Rectangle: 6 + 10 = 16."),
            ("How many people read The Hindu but NOT Times of India?", ["15", "8", "7", "18"], 1, "Inside Triangle outside Rectangle: 8 + 7 = 15."),
            ("How many people read Times of India but NOT The Hindu?", ["14", "9", "5", "18"], 1, "Inside Rectangle outside Triangle: 9 + 5 = 14."),
            ("How many people read both Times of India and Indian Express?", ["15", "6", "9", "18"], 1, "Inside Rectangle and Circle: 6 + 9 = 15.")
        ]
    },
    {
        'id': 'vehicles_car_motorcycle_bicycle',
        'intro': "The following diagram shows vehicle ownership in a township: Triangle represents Car Owners, Rectangle represents Motorcycle Owners, and Circle represents Bicycle Commuters. Answer questions 135 to 138 based on this figure.",
        'nums': {'T': 6, 'C': 5, 'TC': 8, 'ALL': 9, 'TR': 11, 'CR': 6, 'R': 7},
        'questions': [
            ("How many residents own both a Car and a Motorcycle?", ["20", "11", "15", "22"], 1, "Common region of Triangle and Rectangle: 9 + 11 = 20."),
            ("How many residents own a Car but NOT a Motorcycle?", ["14", "6", "8", "18"], 1, "Inside Triangle outside Rectangle: 6 + 8 = 14."),
            ("How many residents own a Motorcycle but NOT a Car?", ["13", "7", "6", "16"], 1, "Inside Rectangle outside Triangle: 7 + 6 = 13."),
            ("How many residents own both a Motorcycle and a Bicycle?", ["15", "9", "6", "18"], 1, "Inside Rectangle and Circle: 9 + 6 = 15.")
        ]
    },
    {
        'id': 'beverages_tea_coffee_juice',
        'intro': "The following diagram shows beverage consumption in an office: Triangle represents Tea Drinkers, Rectangle represents Coffee Drinkers, and Circle represents Fresh Juice Consumers. Answer questions 135 to 138 based on this figure.",
        'nums': {'T': 10, 'C': 4, 'TC': 7, 'ALL': 8, 'TR': 13, 'CR': 6, 'R': 5},
        'questions': [
            ("How many employees drink both Tea and Coffee?", ["21", "13", "18", "25"], 1, "Common region of Triangle and Rectangle: 8 + 13 = 21."),
            ("How many employees drink Tea but NOT Coffee?", ["17", "10", "7", "20"], 1, "Inside Triangle outside Rectangle: 10 + 7 = 17."),
            ("How many employees drink Coffee but NOT Tea?", ["11", "5", "6", "15"], 1, "Inside Rectangle outside Triangle: 5 + 6 = 11."),
            ("How many employees drink both Coffee and Fresh Juice?", ["14", "8", "6", "16"], 1, "Inside Rectangle and Circle: 8 + 6 = 14.")
        ]
    },
    {
        'id': 'examination_math_physics_chemistry',
        'intro': "The following diagram shows examination results of students: Triangle represents Passed in Mathematics, Rectangle represents Passed in Physics, and Circle represents Passed in Chemistry. Answer questions 135 to 138 based on this figure.",
        'nums': {'T': 8, 'C': 3, 'TC': 9, 'ALL': 7, 'TR': 14, 'CR': 5, 'R': 6},
        'questions': [
            ("How many students passed in both Mathematics and Physics?", ["21", "14", "17", "25"], 1, "Common region of Triangle and Rectangle: 7 + 14 = 21."),
            ("How many students passed in Mathematics but NOT Physics?", ["17", "8", "9", "20"], 1, "Inside Triangle outside Rectangle: 8 + 9 = 17."),
            ("How many students passed in Physics but NOT Mathematics?", ["11", "6", "5", "14"], 1, "Inside Rectangle outside Triangle: 6 + 5 = 11."),
            ("How many students passed in both Physics and Chemistry?", ["12", "7", "5", "15"], 1, "Inside Rectangle and Circle: 7 + 5 = 12.")
        ]
    },
    {
        'id': 'farmers_cotton_paddy_sugarcane',
        'intro': "The following diagram shows agricultural crops grown by farmers: Triangle represents Cotton Growers, Rectangle represents Paddy Farmers, and Circle represents Sugarcane Cultivators. Answer questions 135 to 138 based on this figure.",
        'nums': {'T': 7, 'C': 4, 'TC': 8, 'ALL': 6, 'TR': 12, 'CR': 7, 'R': 9},
        'questions': [
            ("How many farmers grow both Cotton and Paddy?", ["18", "12", "15", "20"], 1, "Common region of Triangle and Rectangle: 6 + 12 = 18."),
            ("How many farmers grow Cotton but NOT Paddy?", ["15", "7", "8", "19"], 1, "Inside Triangle outside Rectangle: 7 + 8 = 15."),
            ("How many farmers grow Paddy but NOT Cotton?", ["16", "9", "7", "20"], 1, "Inside Rectangle outside Triangle: 9 + 7 = 16."),
            ("How many farmers cultivate both Paddy and Sugarcane?", ["13", "6", "7", "16"], 1, "Inside Rectangle and Circle: 6 + 7 = 13.")
        ]
    },
    {
        'id': 'library_fiction_history_biography',
        'intro': "The following diagram shows book reading habits in a public library: Triangle represents Fiction Readers, Rectangle represents History Readers, and Circle represents Biography Readers. Answer questions 135 to 138 based on this figure.",
        'nums': {'T': 9, 'C': 3, 'TC': 7, 'ALL': 8, 'TR': 11, 'CR': 6, 'R': 8},
        'questions': [
            ("How many patrons read both Fiction and History books?", ["19", "11", "15", "22"], 1, "Common region of Triangle and Rectangle: 8 + 11 = 19."),
            ("How many patrons read Fiction but NOT History books?", ["16", "9", "7", "20"], 1, "Inside Triangle outside Rectangle: 9 + 7 = 16."),
            ("How many patrons read History but NOT Fiction books?", ["14", "8", "6", "18"], 1, "Inside Rectangle outside Triangle: 8 + 6 = 14."),
            ("How many patrons read both History and Biography books?", ["14", "8", "6", "16"], 1, "Inside Rectangle and Circle: 8 + 6 = 14.")
        ]
    },
    {
        'id': 'musical_instruments_guitar_piano_drums',
        'intro': "The following diagram shows musical skills in a music academy: Triangle represents Guitar Players, Rectangle represents Piano Players, and Circle represents Drum Players. Answer questions 135 to 138 based on this figure.",
        'nums': {'T': 6, 'C': 4, 'TC': 8, 'ALL': 7, 'TR': 13, 'CR': 5, 'R': 7},
        'questions': [
            ("How many students play both Guitar and Piano?", ["20", "13", "17", "24"], 1, "Common region of Triangle and Rectangle: 7 + 13 = 20."),
            ("How many students play Guitar but NOT Piano?", ["14", "6", "8", "18"], 1, "Inside Triangle outside Rectangle: 6 + 8 = 14."),
            ("How many students play Piano but NOT Guitar?", ["12", "7", "5", "15"], 1, "Inside Rectangle outside Triangle: 7 + 5 = 12."),
            ("How many students play both Piano and Drums?", ["12", "7", "5", "16"], 1, "Inside Rectangle and Circle: 7 + 5 = 12.")
        ]
    }
]

VENN_SURVEY_ALL_IDS: List[str] = [cfg['id'] for cfg in VENN_SURVEY_DEFINITIONS]


# ===========================================================================
# DISPATCHER FUNCTIONS
# ===========================================================================

def generate_venn_geometric_group(
    pattern_id: str,
    output_img_dir: str,
    test_num: int,
    uid: str,
    start_q_num: int = 131
) -> List[ExamQuestion]:
    """Generates Q131-Q134 with fresh diagram and questions."""
    sec = BLUEPRINT[16]
    cfg = next((c for c in VENN_GEOM_DEFINITIONS if c['id'] == pattern_id), VENN_GEOM_DEFINITIONS[0])
    
    img_path = os.path.join(output_img_dir, f"test{test_num}_venn_geom_{pattern_id}_{uid}.png")
    generate_four_shape_venn_diagram(img_path, cfg['regions'])

    questions: List[ExamQuestion] = []
    for idx, (stem_text, opts, ans, exp) in enumerate(cfg['questions']):
        q_num = start_q_num + idx
        full_stem = f"{cfg['intro']}\n{stem_text}" if idx == 0 else stem_text
        shuffled_opts, new_ans = helper_shuffle_options(opts, ans)
        questions.append(ExamQuestion(
            q_num=q_num,
            stem=full_stem,
            options=shuffled_opts,
            correct_opt=new_ans,
            explanation=exp,
            section_name=(f"SECTION {sec.sec_num}: {sec.name}" if idx == 0 else None),
            directions=(sec.directions if idx == 0 else None),
            image_path=(img_path if idx == 0 else None)
        ))
    return questions


def generate_venn_survey_group(
    pattern_id: str,
    output_img_dir: str,
    test_num: int,
    uid: str,
    start_q_num: int = 135
) -> List[ExamQuestion]:
    """Generates Q135-Q138 with fresh diagram and questions."""
    sec = BLUEPRINT[16]
    cfg = next((c for c in VENN_SURVEY_DEFINITIONS if c['id'] == pattern_id), VENN_SURVEY_DEFINITIONS[0])

    img_path = os.path.join(output_img_dir, f"test{test_num}_venn_survey_{pattern_id}_{uid}.png")
    render_survey_venn(img_path, cfg['nums'])

    questions: List[ExamQuestion] = []
    for idx, (stem_text, opts, ans, exp) in enumerate(cfg['questions']):
        q_num = start_q_num + idx
        full_stem = f"{cfg['intro']}\n{stem_text}" if idx == 0 else stem_text
        shuffled_opts, new_ans = helper_shuffle_options(opts, ans)
        questions.append(ExamQuestion(
            q_num=q_num,
            stem=full_stem,
            options=shuffled_opts,
            correct_opt=new_ans,
            explanation=exp,
            section_name=None,
            directions=None,
            image_path=(img_path if idx == 0 else None)
        ))
    return questions
