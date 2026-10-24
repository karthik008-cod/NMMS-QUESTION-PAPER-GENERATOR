"""
Comprehensive Dynamic & Procedural Mirror Image Engine for NMMS Question Paper Generator
Features:
1. Massive 500+ Curated NMMS Curriculum Word Bank with persistent Least-Recently-Used (LRU) tracking.
2. Dynamic Alphanumeric Code Generator producing infinite unique 5 to 7 character strings.
3. Word Symmetry & Palindrome Mirror Questions testing lateral inversion vs word symmetry.
4. Procedural Analog Clock Face Mirror Image Questions with HD vector clock diagrams for problem and options.
5. Conceptual and Quantitative mirror reflection questions (lowercase, symmetric letter counting, digit symmetry).
"""

import os
import random
import time
from typing import List, Tuple, Dict, Any, Optional
from .diagrams import (
    generate_mirror_problem, generate_mirror_options, generate_clock_face
)
from .pattern_tracker import get_least_recently_used_patterns

# =========================================================================
# 1. 500+ CURATED NMMS CURRICULUM WORD BANK
# =========================================================================
ALL_MIRROR_WORDS = [
    # Science & Nature (140)
    "GRAVITY", "SPECTRUM", "OXYGEN", "MAGNET", "FRICTION", "SATELLITE", "CIRCUIT",
    "VOLTAGE", "PHOTOSYNTHESIS", "CHLOROPHYLL", "TELESCOPE", "MICROSCOPE", "MOLECULE",
    "ATOM", "ELECTRON", "NEUTRON", "PROTON", "ENERGY", "MOTION", "INERTIA", "VELOCITY",
    "ACCELERATION", "PRESSURE", "DENSITY", "TEMPERATURE", "ATMOSPHERE", "REFRACTION",
    "REFLECTION", "CURRENT", "CONDUCTOR", "INSULATOR", "RESISTANCE", "SOLVENT", "SOLUTION",
    "MINERAL", "ELEMENT", "COMPOUND", "MIXTURE", "FOSSIL", "EVOLUTION", "ECOSYSTEM",
    "HABITAT", "BIOLOGY", "CHEMISTRY", "PHYSICS", "ASTRONOMY", "GEOLOGY", "METEOROLOGY",
    "GLUCOSE", "HORMONES", "ENZYME", "NUTRIENT", "VITAMIN", "PROTEIN", "CALCIUM",
    "NITROGEN", "HYDROGEN", "CARBON", "SULPHUR", "SODIUM", "POTASSIUM", "MAGNESIUM",
    "CHLORINE", "URANIUM", "TITANIUM", "ALUMINIUM", "BACTERIA", "VIRUS", "FUNGI",
    "PARASITE", "VACCINE", "ANTIBIOTIC", "CELL", "TISSUE", "ORGAN", "RESPIRATION",
    "CIRCULATION", "EXCRETION", "DIGESTION", "REPRODUCTION", "METABOLISM", "HEREDITY",
    "GENETICS", "CHROMOSOME", "ORGANISM", "MAMMAL", "REPTILE", "AMPHIBIAN", "POLLINATION",
    "GERMINATION", "TRANSPIRATION", "CARNIVORE", "HERBIVORE", "OMNIVORE", "PREDATOR",
    "PRISM", "RAY", "BEAM", "FOCUS", "CONVEX", "CONCAVE", "MIRROR", "LENS", "IMAGE",
    "OBJECT", "SHADOW", "LIGHT", "OPTICS", "WAVE", "SOUND", "ECHO", "FREQUENCY",
    "PITCH", "AMPLITUDE", "DECIBEL", "VIBRATION", "VACUUM", "MEDIUM", "FORCE",
    "WEIGHT", "MASS", "VOLUME", "MATTER", "SOLID", "LIQUID", "GAS", "PLASMA",
    "FUSION", "FISSION", "HEAT", "RADIATION", "CONVECTION", "CONDUCTION", "BOILING",
    "MELTING", "FREEZING", "EVAPORATION", "CONDENSATION", "SUBLIMATION",
    "AMPLIFIER", "BAROMETER", "CENTRIFUGE", "DIFFUSION", "ELECTROLYTE", "FLUID",
    "GRAVITATION", "HYDROELECTRIC", "INCLINED", "JOULE", "KILOWATT", "LUMINESCENCE",
    "MICROWAVE", "NEWTON", "OSMOSIS", "PULLEY", "QUANTUM", "RADIOMETER",
    "SEMICONDUCTOR", "THERMODYNAMICS", "ULTRASONIC", "VISCOSITY", "WAVELENGTH",
    "ZOOLOGY", "CRYSTALLIZATION", "DISTILLATION", "NEUTRALIZATION", "COMBUSTION",
    "PHOTOVOLTAIC", "RADIOACTIVITY", "SPECTROSCOPY", "GALVANOMETER", "AMMETER",
    "VOLTMETER", "HYGROMETER", "MANOMETER", "PYROMETER", "SPECTROMETER",

    # Mathematics & Geometry (110)
    "TRIANGLE", "POLYGON", "CYLINDER", "FRACTION", "EQUATION", "SYMMETRY", "PYRAMID",
    "DIAMETER", "PERIMETER", "RADIUS", "PARALLEL", "VERTICAL", "HORIZONTAL", "DIAGONAL",
    "BISECTOR", "CHORD", "TANGENT", "SECANT", "SEGMENT", "SECTOR", "QUADRANT",
    "RECTANGLE", "RHOMBUS", "TRAPEZIUM", "OCTAGON", "HEXAGON", "PENTAGON", "DECAGON",
    "PARALLELOGRAM", "SPHERE", "HEMISPHERE", "CONE", "PRISM", "POLYHEDRON", "VERTEX",
    "EDGES", "SURFACE", "PROBABILITY", "STATISTICS", "AVERAGE", "MEDIAN", "PERCENTAGE",
    "RATIO", "PROPORTION", "INTEGER", "DECIMAL", "FACTORIAL", "MULTIPLE", "DIVISOR",
    "COEFFICIENT", "VARIABLE", "CONSTANT", "POLYNOMIAL", "BINOMIAL", "LOGARITHM",
    "QUADRATIC", "ALGEBRA", "GEOMETRY", "CALCULUS", "ARITHMETIC", "THEOREM", "AXIOM",
    "COROLLARY", "POSTULATE", "HYPOTENUSE", "ALTITUDE", "MEDIAN", "CENTROID", "ORTHOCENTER",
    "INCENTER", "CIRCUMCENTER", "CONGRUENT", "SIMILAR", "TRANSVERSAL", "SUPPLEMENTARY",
    "COMPLEMENTARY", "ADJACENT", "PERPENDICULAR", "COLLINEAR", "CONCURRENT", "INTERSECTING",
    "ASYMPTOTE", "COORDINATE", "ABSCISSA", "ORDINATE", "QUADRATIC", "EXPONENT", "RADICAL",
    "NUMERATOR", "DENOMINATOR", "RECIPROCAL", "INVERSE", "EQUIVALENT", "PROPORTIONAL",
    "SEQUENCE", "SERIES", "PROGRESSION", "MATRIX", "DETERMINANT", "VECTOR", "SCALAR",

    # Geography, Environment & Social Studies (90)
    "CONTINENT", "LATITUDE", "LONGITUDE", "HORIZON", "ECLIPSE", "ALTITUDE", "MONSOON",
    "CYCLONE", "TSUNAMI", "EARTHQUAKE", "VOLCANO", "GLACIER", "PLATEAU", "VALLEY",
    "CANYON", "DESERT", "PENINSULA", "ARCHIPELAGO", "STRAIT", "EQUATOR", "TROPICS",
    "MERIDIAN", "TUNDRA", "SAVANNA", "FOREST", "RAINFOREST", "TRIBUTARY", "ESTUARY",
    "DELTA", "RIVER", "OCEAN", "HARBOUR", "ISLAND", "MOUNTAIN", "TERRAIN", "CLIMATE",
    "WEATHER", "HUMIDITY", "DEMOCRACY", "CONSTITUTION", "PARLIAMENT", "REPUBLIC",
    "SOVEREIGN", "JUSTICE", "LIBERTY", "EQUALITY", "FRATERNITY", "CITIZEN", "ELECTION",
    "MONARCHY", "EMPIRE", "CIVILIZATION", "HERITAGE", "MONUMENT", "CULTURE", "TRADITION",
    "COMMERCE", "INDUSTRY", "AGRICULTURE", "HARVEST", "IRRIGATION", "FERTILIZER", "PESTICIDE",
    "DROUGHT", "FAMINE", "CONSERVATION", "POLLUTION", "RECYCLING", "BIOSPHERE", "ATMOSPHERE",
    "HYDROSPHERE", "LITHOSPHERE", "CRUST", "MANTLE", "CORE", "MINERAL", "MAGMA", "LAVA",
    "SEDIMENTARY", "IGNEOUS", "METAMORPHIC", "EROSION", "WEATHERING", "DEPOSITION",

    # Technology, Modern Concepts & Devices (80)
    "COMPUTER", "INTERNET", "SOFTWARE", "HARDWARE", "KEYBOARD", "MONITOR", "PRINTER",
    "SCANNER", "NETWORK", "DATABASE", "ALGORITHM", "PROGRAM", "BROWSER", "WEBSITE",
    "DIGITAL", "WIRELESS", "BLUETOOTH", "ROBOTICS", "AUTOMATION", "PROCESSOR",
    "STORAGE", "DISPLAY", "PROJECTOR", "CAMERA", "BATTERY", "CHARGER", "TELEPHONE",
    "ANTENNA", "TRANSMITTER", "RECEIVER", "SILICON", "ENGINE", "TURBINE", "GENERATOR",
    "DYNAMO", "REACTOR", "SOLAR", "NUCLEAR", "ROCKET", "SPACECRAFT", "SHUTTLE",
    "AIRCRAFT", "RADAR", "SONAR", "LASER", "OPTICAL", "FIBER", "COMMUNICATION",
    "NAVIGATION", "SENSOR", "ACTUATOR", "MICROCHIP", "INTEGRATED", "NANOTECHNOLOGY",
    "ARTIFICIAL", "INTELLIGENCE", "AUTOMOBILE", "ELECTRIC", "HYBRID", "LOCOMOTIVE",
    "SUBMARINE", "HOVERCRAFT", "HELICOPTER", "SUPERSONIC", "ASTRONAUT", "COSMONAUT",

    # Mental Ability & High-Frequency English Words (100)
    "REASONING", "KNOWLEDGE", "QUALITY", "NATIONAL", "DISCOVERY", "CHAMPION",
    "STRENGTH", "COURAGE", "WISDOM", "SUCCESS", "FREEDOM", "TRIUMPH", "VICTORY",
    "HARMONY", "BALANCE", "PROGRESS", "CREATIVE", "DYNAMIC", "GENIUS", "TALENT",
    "STUDENT", "TEACHER", "LIBRARY", "SCIENCE", "COLLEGE", "STATION", "HOSPITAL",
    "FACTORY", "AIRPORT", "JOURNEY", "MISSION", "VENTURE", "PURSUIT", "DESTINY",
    "PURPOSE", "PROMISE", "HONESTY", "PATIENCE", "CHARITY", "BRAVERY", "LOYALTY",
    "VIRTUE", "RESPECT", "FRIEND", "PARTNER", "BROTHER", "SISTER", "FAMILY", "LEADER",
    "OFFICER", "DOCTOR", "SOLDIER", "ARTIST", "AUTHOR", "PAINTER", "CAPTAIN", "SAILOR",
    "PILOT", "ENGINEER", "SCIENTIST", "EXPLORER", "INVENTOR", "DIRECTOR", "PRESIDENT",
    "MINISTER", "GOVERNOR", "JUDGE", "LAWYER", "CITIZEN", "SPEAKER", "WARRIOR",
    "GUARDIAN", "CHAMPION", "HERO", "PIONEER", "PATRIOT", "SCHOLAR", "THINKER",
    "MASTER", "BUILDER", "CREATOR", "ORGANIZER", "ANALYST", "EXAMINER", "OBSERVER",
    "INSPECTOR", "MANAGER", "ADVISOR", "COUNSEL", "COMMANDER", "ARCHITECT"
]

# Ensure uniqueness and standard uppercase formatting
ALL_MIRROR_WORDS = sorted(list(set(w.strip().upper() for w in ALL_MIRROR_WORDS if len(w.strip()) >= 3)))


# =========================================================================
# 2. DYNAMIC ALPHANUMERIC CODE GENERATOR
# =========================================================================
def generate_dynamic_mirror_code(length: Optional[int] = None) -> str:
    """
    Generates a fresh, realistic alphanumeric code (5 to 7 characters)
    with a controlled balance of asymmetric characters and digits to guarantee
    clear lateral inversion recognition in mirror reflection tests.
    """
    if not length:
        length = random.choice([5, 6, 7])

    asym_letters = ['B', 'C', 'D', 'E', 'F', 'G', 'J', 'K', 'L', 'N', 'P', 'Q', 'R', 'S', 'Z']
    sym_letters = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y']
    asym_digits = ['2', '3', '4', '5', '6', '7', '9']
    sym_digits = ['0', '8']

    pattern_type = random.choice(['mixed_sandwich', 'alternating_let_dig', 'block_code'])

    if pattern_type == 'alternating_let_dig':
        chars = []
        start_with_letter = random.choice([True, False])
        for i in range(length):
            if (i % 2 == 0 and start_with_letter) or (i % 2 == 1 and not start_with_letter):
                # Letter: 70% asymmetric, 30% symmetric
                c = random.choice(asym_letters if random.random() < 0.7 else sym_letters)
            else:
                # Digit: 75% asymmetric, 25% symmetric
                c = random.choice(asym_digits if random.random() < 0.75 else sym_digits)
            chars.append(c)
        return "".join(chars)

    elif pattern_type == 'mixed_sandwich':
        # E.g. BR4AQ16 or DL9Q25
        n_prefix = random.randint(1, 2)
        n_digits1 = random.randint(1, 2)
        n_mid = random.randint(1, 2)
        n_digits2 = max(1, length - (n_prefix + n_digits1 + n_mid))

        p1 = [random.choice(asym_letters) for _ in range(n_prefix)]
        d1 = [random.choice(asym_digits) for _ in range(n_digits1)]
        m1 = [random.choice(sym_letters + asym_letters) for _ in range(n_mid)]
        d2 = [random.choice(asym_digits + sym_digits) for _ in range(n_digits2)]
        code = "".join(p1 + d1 + m1 + d2)
        return code[:length]

    else:
        # Block code: 2 digits + 3 letters + 1 digit or 2 letters + 2 digits + 2 letters
        pool = asym_letters + asym_digits + sym_letters + sym_digits
        # Ensure at least 2 asymmetric letters and 1 digit
        res = [random.choice(asym_letters), random.choice(asym_letters), random.choice(asym_digits)]
        while len(res) < length:
            res.append(random.choice(pool))
        random.shuffle(res)
        return "".join(res)


# =========================================================================
# 3. WORD SYMMETRY MIRROR QUESTIONS
# =========================================================================
SYMMETRIC_PALINDROMES = [
    "TOOT", "OTTO", "MOM", "WOW", "TIT", "HAH", "TAT", "MAM", "AHA", "WAW", "YAY", "OXO"
]

ASYMMETRIC_PALINDROMES = [
    "MADAM", "RADAR", "LEVEL", "NOON", "REFER", "ROTOR", "KAYAK", "CIVIC", "DEED", "POP"
]

def make_word_symmetry_question() -> Tuple[str, List[str], int, str]:
    """
    Generates a high-concept NMMS question testing lateral inversion vs word symmetry:
    'Which of the following words reads the EXACT SAME when viewed in a plane mirror?'
    """
    correct_word = random.choice(SYMMETRIC_PALINDROMES)
    distractors = random.sample(ASYMMETRIC_PALINDROMES, 3)
    opts = [correct_word] + distractors

    stem = "Which of the following words reads the EXACT SAME when viewed in a plane mirror?"
    exp = (
        f"A word appears unchanged in a vertical plane mirror ONLY IF it is a palindrome AND every single letter "
        f"has vertical line symmetry (A, H, I, M, O, T, U, V, W, X, Y). In '{correct_word}', every letter has vertical "
        f"line symmetry and the word is a palindrome. In words like '{distractors[0]}' and '{distractors[1]}', "
        f"asymmetric letters (such as D, R, E, L, N) laterally invert in a mirror."
    )
    return stem, opts, 1, exp


# =========================================================================
# 4. PROCEDURAL CLOCK FACE MIRROR QUESTION (WITH HD DIAGRAMS)
# =========================================================================
def make_clock_mirror_diagram_question(
    output_img_dir: str,
    test_num: int,
    uid: str
) -> Tuple[str, List[str], int, str, str, List[str]]:
    """
    Generates an analog clock mirror question with:
    - 1 problem clock figure showing time H:M
    - 4 option clock figures showing the mirror reflection and plausible distractors.
    """
    h = random.choice([2, 3, 4, 7, 8, 9, 10])
    m = random.choice([10, 15, 20, 25, 30, 40, 45, 50])

    # Formula: Mirror Time = 11:60 - H:M
    ans_h = 11 - h if m > 0 else 12 - h
    if ans_h == 0:
        ans_h = 12
    ans_m = (60 - m) % 60

    prob_img = os.path.join(output_img_dir, f"test{test_num}_clock_prob_{h}_{m}_{uid}.png")
    generate_clock_face(h, m, prob_img)

    # 4 Option images
    opt1_img = os.path.join(output_img_dir, f"test{test_num}_clock_opt1_{ans_h}_{ans_m}_{uid}.png")
    generate_clock_face(ans_h, ans_m, opt1_img)  # Correct

    opt2_img = os.path.join(output_img_dir, f"test{test_num}_clock_opt2_{h}_{m}_{uid}.png")
    generate_clock_face(h, m, opt2_img)          # Unreflected original

    d_h3 = (ans_h + 1) if ans_h < 12 else 1
    opt3_img = os.path.join(output_img_dir, f"test{test_num}_clock_opt3_{d_h3}_{ans_m}_{uid}.png")
    generate_clock_face(d_h3, ans_m, opt3_img)    # Distractor 1

    d_h4 = (ans_h - 1) if ans_h > 1 else 12
    opt4_img = os.path.join(output_img_dir, f"test{test_num}_clock_opt4_{d_h4}_{m}_{uid}.png")
    generate_clock_face(d_h4, m, opt4_img)        # Distractor 2

    stem = f"The clock shown in the problem figure shows time {h}:{m:02d}. Which of the answer figures represents its correct mirror image in a vertical plane mirror MN?"
    ans_time_str = f"{ans_h}:{ans_m:02d}"
    exp = f"Mirror Time formula: 11:60 - Actual Time = 11:60 - {h}:{m:02d} = {ans_time_str}."

    return stem, ["", "", "", ""], 1, exp, prob_img, [opt1_img, opt2_img, opt3_img, opt4_img]


# =========================================================================
# 5. CONCEPTUAL & QUANTITATIVE MIRROR QUESTIONS
# =========================================================================
def make_conceptual_mirror_question() -> Tuple[str, List[str], int, str]:
    """Generates varied analytical questions on mirror symmetry properties."""
    pat = random.choice([
        'lowercase_count', 'digit_symmetry', 'word_symmetric_count',
        'capital_symmetry_count', 'single_letter_symmetry'
    ])

    if pat == 'lowercase_count':
        stem = "How many lowercase letters of the English alphabet (a to z) have identical mirror images?"
        ans = "6"
        exp = "Exactly 6 lowercase letters possess vertical line symmetry in standard typeface: i, l, o, v, w, x."
        opts = ["6", "4", "8", "5"]
        return stem, opts, 1, exp

    elif pat == 'digit_symmetry':
        stem = "Which pair of single-digit numbers does NOT change its appearance when viewed in a plane mirror?"
        ans = "0 and 8"
        exp = "Digits 0 and 8 have vertical bilateral symmetry and remain unchanged in a vertical plane mirror."
        opts = ["0 and 8", "1 and 7", "3 and 8", "2 and 5"]
        return stem, opts, 1, exp

    elif pat == 'word_symmetric_count':
        word_candidates = [
            ("MATHEMATICS", 8, "M, A, T, H, M, A, T, I"),
            ("AUTOMOBILE", 6, "A, U, T, O, M, I"),
            ("HIGHWAY", 6, "H, I, H, W, A, Y"),
            ("MAXIMUM", 7, "M, A, X, I, M, U, M"),
            ("NATIONAL", 4, "A, T, I, O")
        ]
        w, count, sym_letters = random.choice(word_candidates)
        stem = f"How many letters in the word '{w}' remain completely UNCHANGED when viewed in a plane mirror?"
        ans = str(count)
        exp = f"Letters with vertical line symmetry in '{w}' are: {sym_letters} (total = {count} letters)."
        opts = [ans, str(count - 2), str(count + 2), str(count - 1)]
        return stem, opts, 1, exp

    elif pat == 'single_letter_symmetry':
        letters_sym = ["A", "H", "I", "M", "O", "T", "U", "V", "W", "X", "Y"]
        letters_asym = ["B", "C", "D", "E", "F", "G", "J", "K", "L", "N", "P", "Q", "R", "S", "Z"]
        c_ans = random.choice(letters_sym)
        c_dist = random.sample(letters_asym, 3)
        stem = "Which of the following capital English letters does NOT change its appearance in a plane mirror?"
        ans = c_ans
        exp = f"The letter '{c_ans}' has vertical line symmetry, so its reflection in a plane mirror is identical."
        opts = [ans] + c_dist
        return stem, opts, 1, exp

    else:
        stem = "How many capital letters of the English alphabet (A to Z) have identical mirror images?"
        ans = "11"
        exp = "Exactly 11 capital letters: A, H, I, M, O, T, U, V, W, X, Y."
        opts = ["11", "9", "13", "15"]
        return stem, opts, 1, exp


# =========================================================================
# 6. UNIVERSAL MIRROR IMAGE QUESTION DISPATCHER
# =========================================================================
def generate_mirror_image_question_enhanced(
    output_img_dir: str,
    test_num: int,
    uid: str,
    q_num: int = 161
) -> Tuple[str, List[str], int, str, Optional[str], Optional[List[str]]]:
    """
    Generates a guaranteed brand-new mirror image question for slot `q_num` (161 to 166).
    Uses 500+ Word Bank with LRU tracking, dynamic alphanumeric generator, word symmetry,
    and procedural analog clock mirror diagrams.
    """
    # Q161 & Q162: Word Mirror Images with HD Option Cards (from 500+ Word Bank via LRU)
    if q_num in [161, 162] or q_num == 0:
        words = get_least_recently_used_patterns('mirror_words', ALL_MIRROR_WORDS, count=1, current_test_num=test_num)
        word = words[0]
        stem = f"Choose the correct mirror image of the word '{word}' when the mirror is placed along MN:"
        m_img = os.path.join(output_img_dir, f"test{test_num}_mirror_{word}_{uid}.png")
        generate_mirror_problem(word, m_img)
        opt_imgs = generate_mirror_options(word, output_img_dir, f"test{test_num}_mirror_opt_{word}_{uid}")
        exp = f"In a vertical mirror MN on the right, letter order reverses with lateral inversion of asymmetric letters."
        return stem, ["", "", "", ""], 1, exp, m_img, opt_imgs

    # Q163: Dynamic Alphanumeric Code Mirror Image (Infinite Unique Combinations)
    elif q_num == 163:
        code = generate_dynamic_mirror_code()
        stem = f"Choose the correct mirror image of the alphanumeric code '{code}' along MN:"
        m_img = os.path.join(output_img_dir, f"test{test_num}_mirror_{code}_{uid}.png")
        generate_mirror_problem(code, m_img)
        opt_imgs = generate_mirror_options(code, output_img_dir, f"test{test_num}_mirror_opt_{code}_{uid}")
        exp = f"Sequence reverses with horizontal lateral inversion of each character."
        return stem, ["", "", "", ""], 1, exp, m_img, opt_imgs

    # Q164: Procedural Analog Clock Face Mirror Question (with HD Clock Diagrams)
    elif q_num == 164:
        stem, opts, ans, exp, prob_img, opt_imgs = make_clock_mirror_diagram_question(output_img_dir, test_num, uid)
        return stem, opts, ans, exp, prob_img, opt_imgs

    # Q165: Word Symmetry & Palindrome Challenge (Lateral Inversion vs Symmetry)
    elif q_num == 165:
        stem, opts, ans, exp = make_word_symmetry_question()
        return stem, opts, ans, exp, None, None

    # Q166: Conceptual / Quantitative Letter & Digit Mirror Properties
    else:  # 166
        stem, opts, ans, exp = make_conceptual_mirror_question()
        return stem, opts, ans, exp, None, None


# =========================================================================
# 7. WATER IMAGE DYNAMIC & PROCEDURAL EXTENSIONS (SECTION 22)
# =========================================================================
def generate_dynamic_water_code(length: Optional[int] = None) -> str:
    """Generates an alphanumeric code balanced for water reflection (vertical flip)."""
    if not length:
        length = random.choice([5, 6, 7])
    horiz_sym_letters = ['B', 'C', 'D', 'E', 'H', 'I', 'K', 'O', 'X']
    vert_flip_letters = ['A', 'F', 'G', 'J', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']
    digits_sym = ['0', '3', '8']
    digits_asym = ['1', '2', '4', '5', '6', '7', '9']

    # Ensure a mix of flipping and non-flipping characters
    res = [random.choice(vert_flip_letters), random.choice(digits_asym), random.choice(horiz_sym_letters)]
    pool = horiz_sym_letters + vert_flip_letters + digits_sym + digits_asym
    while len(res) < length:
        res.append(random.choice(pool))
    random.shuffle(res)
    return "".join(res)


WATER_SYMMETRIC_WORDS = [
    "BED", "CODE", "BITE", "DICE", "HIKE", "CHICK", "CHECK", "DECK", "BOOK",
    "BOX", "KICK", "COOK", "ECHO", "DECIDE", "CHIDE", "HIDE", "KID", "COCK"
]

WATER_ASYMMETRIC_WORDS = [
    "MOM", "WOW", "TOOT", "MAX", "ATOM", "SUN", "RAIN", "BIRD", "FISH", "STAR"
]

def make_water_symmetry_question() -> Tuple[str, List[str], int, str]:
    """Generates a question on words whose water reflection is identical."""
    corr = random.choice(WATER_SYMMETRIC_WORDS)
    dist = random.sample(WATER_ASYMMETRIC_WORDS, 3)
    stem = "Which of the following words remains completely UNCHANGED in its water image?"
    ans = corr
    exp = (
        f"In horizontal water reflection, left-to-right order remains unchanged, but each letter flips vertically. "
        f"Letters with horizontal line symmetry (B, C, D, E, H, I, K, O, X) remain unchanged. "
        f"Since all letters in '{corr}' have horizontal symmetry, the word appears identical in water."
    )
    opts = [ans] + dist
    return stem, opts, 1, exp


def generate_water_image_question_enhanced(
    output_img_dir: str,
    test_num: int,
    uid: str,
    q_num: int = 167
) -> Tuple[str, List[str], int, str, Optional[str], Optional[List[str]]]:
    """
    Generates a guaranteed brand-new water image question for slot `q_num` (167 to 172).
    Uses 500+ Word Bank with LRU tracking, dynamic water code generator, and word symmetry.
    """
    from .diagrams import generate_water_problem, generate_water_options

    if q_num in [167, 168] or q_num == 0:
        words = get_least_recently_used_patterns('water_words', ALL_MIRROR_WORDS, count=1, current_test_num=test_num)
        word = words[0]
        stem = f"Choose the correct water image of the word '{word}' along line MN:"
        w_img = os.path.join(output_img_dir, f"test{test_num}_water_{word}_{uid}.png")
        generate_water_problem(word, w_img)
        opt_imgs = generate_water_options(word, output_img_dir, f"test{test_num}_water_opt_{word}_{uid}")
        exp = f"In horizontal water reflection, letters flip vertically while keeping left-to-right order."
        return stem, ["", "", "", ""], 1, exp, w_img, opt_imgs

    elif q_num == 169:
        code = generate_dynamic_water_code()
        stem = f"Choose the correct water image of the alphanumeric sequence '{code}':"
        w_img = os.path.join(output_img_dir, f"test{test_num}_water_{code}_{uid}.png")
        generate_water_problem(code, w_img)
        opt_imgs = generate_water_options(code, output_img_dir, f"test{test_num}_water_opt_{code}_{uid}")
        exp = f"Each character is reflected across the horizontal line MN."
        return stem, ["", "", "", ""], 1, exp, w_img, opt_imgs

    elif q_num == 170:
        return make_water_symmetry_question() + (None, None)

    elif q_num == 171:
        stem = "How many capital letters in the English alphabet have identical water images?"
        opts = ["9", "7", "8", "10"]
        exp = "Exactly 9 capital letters possess horizontal line symmetry: B, C, D, E, H, I, K, O, X."
        return stem, opts, 1, exp, None, None

    else:  # 172
        stem = "Which pair of digits has the exact same appearance in their water images?"
        opts = ["0 and 8", "1 and 7", "2 and 5", "3 and 9"]
        exp = "Digits '0' and '8' possess horizontal bilateral symmetry and remain unchanged in water."
        return stem, opts, 1, exp, None, None
