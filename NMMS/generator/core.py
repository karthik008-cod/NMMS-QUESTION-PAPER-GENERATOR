"""
Core data structures for NMMS Question Paper Generator
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

@dataclass
class ExamQuestion:
    q_num: int
    stem: str
    options: List[str]
    correct_opt: int  # 1-indexed (1, 2, 3, or 4)
    explanation: str
    section_name: str
    directions: Optional[str] = None
    image_path: Optional[str] = None
    matrix_data: Optional[List[List[str]]] = None
    option_images: Optional[List[str]] = None

@dataclass
class SectionInfo:
    sec_num: int
    name: str
    directions: str
    q_range: str
    count: int

BLUEPRINT = [
    SectionInfo(1, "NUMBER SERIES", "In each of the following number series, one term is missing marked with '?'. Find the missing term from the given alternatives.", "1 - 10", 10),
    SectionInfo(2, "LETTER & ALPHANUMERIC SERIES", "In each of the following letter or alphanumeric series, choose the missing term marked with '?' from the given alternatives.", "11 - 18", 8),
    SectionInfo(3, "REPEATING PATTERN SERIES", "In each series, letters follow a specific repeating pattern with missing blanks. Choose the correct group of letters from the alternatives.", "19 - 24", 6),
    SectionInfo(4, "CODING & DECODING", "In each question, words/numbers are coded following a certain rule. Find the correct code/word for the given question.", "25 - 34", 10),
    SectionInfo(5, "WORD ANALOGY", "In each question, there is a certain relationship between the first two words. Establish the same relationship for the given word from alternatives.", "35 - 44", 10),
    SectionInfo(6, "NUMBER & LETTER ANALOGY", "Choose the alternative that bears the same relationship to the third term as the first term bears to the second.", "45 - 52", 8),
    SectionInfo(7, "CLASSIFICATION (ODD ONE OUT)", "In each question, four options are given. Three are alike in a certain way and form a group. Find the one that does not belong to the group.", "53 - 60", 8),
    SectionInfo(8, "LOGICAL SEQUENCE OF WORDS", "Arrange the given words in a meaningful, logical, and natural sequence and choose the correct order from the alternatives.", "61 - 66", 6),
    SectionInfo(9, "WORD FORMATION", "From the given alternative words, select the word which CAN or CANNOT be formed using the letters of the given word as instructed.", "67 - 72", 6),
    SectionInfo(10, "DICTIONARY & ALPHABETICAL ORDER", "Arrange the following words in the order in which they appear in an English dictionary, and choose the correct sequence.", "73 - 78", 6),
    SectionInfo(11, "BLOOD RELATIONS", "Analyze the given family relations and statements to find the exact relationship between the specified persons.", "79 - 86", 8),
    SectionInfo(12, "DIRECTION SENSE & PROBLEM SOLVING", "Solve the following problems based on cardinal directions, rank order, positioning, and logical reasoning puzzles.", "87 - 94", 8),
    SectionInfo(13, "CALENDAR PROBLEMS", "Solve the following calendar problems based on odd days, leap years, days of the week, and dates.", "95 - 102", 8),
    SectionInfo(14, "CLOCK PROBLEMS", "Solve the following problems based on the positions and angles between the hands of an analog clock, time gain/loss, and reflections.", "103 - 110", 8),
    SectionInfo(15, "ARITHMETIC PRINCIPLES & REASONING", "Solve the following mathematical and arithmetical reasoning word problems.", "111 - 120", 10),
    SectionInfo(16, "MATHEMATICAL SIGN INTERCHANGE", "Select the correct combination or interchange of mathematical signs/numbers that makes the given equation correct.", "121 - 130", 10),
    SectionInfo(17, "VENN DIAGRAMS & SURVEY ANALYSIS", "Analyze the given Venn diagrams and geometric survey representations to answer the questions.", "131 - 138", 8),
    SectionInfo(18, "NUMBER PUZZLES & GEOMETRIC MATRICES", "In each puzzle, numbers are placed according to a specific mathematical pattern. Find the missing number marked with '?'.", "139 - 148", 10),
    SectionInfo(19, "DICE & OPEN DICE PROBLEMS", "Analyze the given positions of a standard/non-standard dice or unfolded dice nets to determine opposite faces.", "149 - 154", 6),
    SectionInfo(20, "CUBES & PAINTED FACES PROBLEMS", "Analyze the painted faces and cuts of a three-dimensional cube to find the required number of smaller cubes.", "155 - 160", 6),
    SectionInfo(21, "MIRROR IMAGES", "Find the correct mirror image of the given word, number, or figure when the mirror is placed vertically along the line MN.", "161 - 166", 6),
    SectionInfo(22, "WATER IMAGES", "Find the correct water image (horizontal reflection) of the given word, number, or figure when reflected in water along the line MN.", "167 - 172", 6),
    SectionInfo(23, "PAPER FOLDING & PAPER CUTTING", "A square sheet of paper is folded and punched as shown in figures X, Y, and Z. Choose the correct figure showing how it will appear when unfolded.", "173 - 176", 4),
    SectionInfo(24, "EMBEDDED FIGURES & FIGURE COMPLETION", "Find the figure from the given alternatives in which the given question figure (X) is embedded/hidden.", "177 - 178", 2),
    SectionInfo(25, "DOT SITUATION & NON-VERBAL REASONING", "Analyze the geometric regions, dot placement conditions, and series transformations to choose the correct alternative.", "179 - 180", 2)
]
