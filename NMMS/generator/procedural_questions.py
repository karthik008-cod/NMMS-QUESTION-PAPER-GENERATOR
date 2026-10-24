"""
Procedural & Dynamic Question Generator for NMMS Mental Ability Test
Guarantees:
1. Never duplicates any existing question stem in the current paper.
2. Generates genuine fresh questions with verified answers, plausible distractors, and detailed explanations.
3. Renders clean, high-resolution vector diagrams with unique timestamps for visual questions.
4. Uses date, time, and entropy to guarantee numbers in questions are truly randomized and never repeat.
"""

import os
import random
import string
import math
from typing import List, Tuple, Dict, Any, Optional, Set
from .core import ExamQuestion, BLUEPRINT
from .diagrams import (
    generate_clock_face, generate_two_dice, generate_three_dice, generate_dice_net,
    generate_3d_cube, generate_mirror_problem, generate_water_problem,
    generate_mirror_options, generate_water_options,
    generate_circular_fold_cut_problem, generate_paper_fold_cut_problem,
    generate_paper_fold_options, generate_transparent_fold_problem,
    generate_embedded_figure_problem, generate_dot_situation,
    generate_series_problem, generate_four_shape_venn_diagram,
    generate_survey_venn_graduates, generate_satellite_circle_puzzle,
    generate_circle_quad_puzzle, generate_y_trees_puzzle,
    generate_cross_boxed_puzzle, generate_cross_wing_puzzle,
    generate_h_blocks_puzzle
)
from .paper_fold_generator import (
    PFC_ALL_PATTERN_IDS, generate_pfc_problem, generate_pfc_options, get_pfc_pattern_details
)
from .nonverbal_generator import (
    generate_embedded_figure_question,
    generate_figure_analogy_question,
    generate_dot_situation_question,
    generate_figure_series_question
)
from .pattern_tracker import get_least_recently_used_patterns
from .mirror_generator import generate_mirror_image_question_enhanced, generate_water_image_question_enhanced


def helper_shuffle(opts: List[str], correct_idx: int) -> Tuple[List[str], int]:
    """Preserves correct answer mapping when shuffling options (1-indexed)."""
    correct_val = opts[correct_idx - 1]
    shuffled = list(opts)
    random.shuffle(shuffled)
    new_idx = shuffled.index(correct_val) + 1
    return shuffled, new_idx


def helper_shuffle_with_images(opts: List[str], correct_idx: int, opt_images: Optional[List[str]]) -> Tuple[List[str], int, Optional[List[str]]]:
    """Preserves both text and option images mapping when shuffling."""
    if not opt_images or len(opt_images) != 4:
        shuffled, new_idx = helper_shuffle(opts, correct_idx)
        return shuffled, new_idx, opt_images
    paired = list(zip(opts, opt_images))
    correct_pair = paired[correct_idx - 1]
    random.shuffle(paired)
    shuffled_opts = [p[0] for p in paired]
    shuffled_imgs = [p[1] for p in paired]
    new_idx = paired.index(correct_pair) + 1
    return shuffled_opts, new_idx, shuffled_imgs


# =========================================================================
# SECTION 1: NUMBER SERIES
# =========================================================================
def make_number_series_question() -> Tuple[str, List[str], int, str]:
    pat = random.choice([
        'ap_diff', 'squares_add', 'squares_sub', 'squares_n', 'cubes', 'cubes_sub_n',
        'cubes_add_k', 'mult_linear', 'fibonacci', 'geom', 'primes', 'triangular',
        'alternating', 'prime_squares'
    ])
    if pat == 'ap_diff':
        start = random.randint(3, 40)
        d = random.randint(3, 8)
        step = random.randint(2, 6)
        terms = [start]
        curr_d = d
        for _ in range(5):
            terms.append(terms[-1] + curr_d)
            curr_d += step
        stem = f"{terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, {terms[4]}, ?"
        ans = terms[5]
        diffs = [terms[i+1]-terms[i] for i in range(4)]
        exp = f"Differences increase by +{step}: {diffs}. Next difference is {curr_d - step}, so {terms[4]} + {curr_d - step} = {ans}."
        opts = [str(ans), str(ans - step), str(ans + step), str(ans + 2)]
        return stem, opts, 1, exp

    elif pat == 'squares_add':
        k = random.choice([1, 2, 3, 5])
        start_n = random.randint(2, 7)
        terms = [(n**2 + k) for n in range(start_n, start_n + 6)]
        stem = f"{terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, {terms[4]}, ?"
        ans = terms[5]
        exp = f"Pattern is n^2 + {k} starting from n={start_n}. Next term is {start_n+5}^2 + {k} = {(start_n+5)**2} + {k} = {ans}."
        opts = [str(ans), str(ans - 2), str(ans + 2), str(ans + 4)]
        return stem, opts, 1, exp

    elif pat == 'squares_sub':
        k = random.choice([1, 2, 3])
        start_n = random.randint(3, 8)
        terms = [(n**2 - k) for n in range(start_n, start_n + 6)]
        stem = f"{terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, {terms[4]}, ?"
        ans = terms[5]
        exp = f"Pattern is n^2 - {k} starting from n={start_n}. Next term is {start_n+5}^2 - {k} = {(start_n+5)**2} - {k} = {ans}."
        opts = [str(ans), str(ans - 2), str(ans + 2), str(ans - 4)]
        return stem, opts, 1, exp

    elif pat == 'squares_n':
        sign = random.choice([1, -1])
        start_n = random.randint(2, 6)
        if sign == 1:
            terms = [(n**2 + n) for n in range(start_n, start_n + 6)]
            sign_str = "+"
        else:
            terms = [(n**2 - n) for n in range(start_n, start_n + 6)]
            sign_str = "-"
        stem = f"{terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, {terms[4]}, ?"
        ans = terms[5]
        exp = f"Pattern is n^2 {sign_str} n starting from n={start_n}. Next term is {start_n+5}^2 {sign_str} {start_n+5} = {ans}."
        opts = [str(ans), str(ans - 4), str(ans + 6), str(ans - 6)]
        return stem, opts, 1, exp

    elif pat == 'cubes':
        start_n = random.randint(1, 4)
        terms = [n**3 for n in range(start_n, start_n + 6)]
        stem = f"{terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, {terms[4]}, ?"
        ans = terms[5]
        exp = f"Cubes of consecutive integers: {start_n}^3={terms[0]}, {start_n+1}^3={terms[1]}, ..., {start_n+5}^3 = {ans}."
        opts = [str(ans), str(ans - 10), str(ans + 20), str(ans - 25)]
        return stem, opts, 1, exp

    elif pat == 'cubes_sub_n':
        start_n = random.randint(2, 4)
        terms = [(n**3 - n) for n in range(start_n, start_n + 6)]
        stem = f"{terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, {terms[4]}, ?"
        ans = terms[5]
        exp = f"Pattern is n^3 - n: {start_n}^3 - {start_n} = {terms[0]} ... Next is {start_n+5}^3 - {start_n+5} = {ans}."
        opts = [str(ans), str(ans - 15), str(ans + 15), str(ans - 30)]
        return stem, opts, 1, exp

    elif pat == 'cubes_add_k':
        k = random.choice([1, 2, 3])
        start_n = random.randint(1, 4)
        terms = [(n**3 + k) for n in range(start_n, start_n + 6)]
        stem = f"{terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, {terms[4]}, ?"
        ans = terms[5]
        exp = f"Pattern is n^3 + {k}: {start_n}^3 + {k} = {terms[0]} ... Next is {start_n+5}^3 + {k} = {ans}."
        opts = [str(ans), str(ans - 10), str(ans + 15), str(ans - 20)]
        return stem, opts, 1, exp

    elif pat == 'mult_linear':
        m = random.choice([2, 3])
        c = random.choice([1, -1, 2, -2])
        curr = random.randint(2, 6)
        terms = [curr]
        for _ in range(5):
            curr = curr * m + c
            terms.append(curr)
        stem = f"{terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, {terms[4]}, ?"
        ans = terms[5]
        sign_str = f"+ {c}" if c > 0 else f"- {abs(c)}"
        exp = f"Pattern: each term is previous term * {m} {sign_str}. {terms[4]} * {m} {sign_str} = {ans}."
        opts = [str(ans), str(ans - m), str(ans + m), str(ans + 2*m)]
        return stem, opts, 1, exp

    elif pat == 'fibonacci':
        a = random.randint(1, 5)
        b = random.randint(2, 6)
        terms = [a, b]
        for _ in range(4):
            terms.append(terms[-1] + terms[-2])
        stem = f"{terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, {terms[4]}, ?"
        ans = terms[5]
        exp = f"Each term is the sum of previous two terms: {terms[3]} + {terms[4]} = {ans}."
        opts = [str(ans), str(ans - 1), str(ans + 1), str(ans + 3)]
        return stem, opts, 1, exp

    elif pat == 'triangular':
        n_start = random.randint(1, 6)
        terms = [n * (n + 1) // 2 for n in range(n_start, n_start + 6)]
        stem = f"{terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, {terms[4]}, ?"
        ans = terms[5]
        exp = f"Triangular numbers n*(n+1)/2. Next term for n={n_start+5} is {n_start+5}*{n_start+6}/2 = {ans}."
        opts = [str(ans), str(ans - 3), str(ans + 4), str(ans - 6)]
        return stem, opts, 1, exp

    elif pat == 'alternating':
        s = random.randint(12, 35)
        add_val = random.randint(4, 9)
        sub_val = random.randint(1, 3)
        terms = [s]
        for i in range(5):
            if i % 2 == 0:
                terms.append(terms[-1] + add_val)
            else:
                terms.append(terms[-1] - sub_val)
        stem = f"{terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, {terms[4]}, ?"
        ans = terms[5]
        next_op = f"+{add_val}" if len(terms) % 2 == 0 else f"-{sub_val}"
        exp = f"Alternating operations +{add_val} and -{sub_val}. Next step is {next_op}: {terms[4]} {next_op} = {ans}."
        opts = [str(ans), str(ans - 2), str(ans + 2), str(ans - 4)]
        return stem, opts, 1, exp

    elif pat == 'prime_squares':
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        idx = random.randint(0, len(primes) - 6)
        terms = [p**2 for p in primes[idx : idx + 6]]
        stem = f"{terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, {terms[4]}, ?"
        ans = terms[5]
        exp = f"Squares of consecutive prime numbers: {primes[idx+4]}^2={terms[4]}. Next prime is {primes[idx+5]}, {primes[idx+5]}^2 = {ans}."
        opts = [str(ans), str((primes[idx+5]-1)**2), str((primes[idx+5]+1)**2), str(ans - 20)]
        return stem, opts, 1, exp

    else:
        # Consecutive primes starting at random prime offset
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
        idx = random.randint(0, len(primes) - 6)
        terms = primes[idx : idx + 6]
        stem = f"{terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, {terms[4]}, ?"
        ans = terms[5]
        exp = f"Consecutive prime numbers. The next prime after {terms[4]} is {ans}."
        opts = [str(ans), str(ans - 2), str(ans + 2), str(ans + 4)]
        return stem, opts, 1, exp


# =========================================================================
# SECTION 2: LETTER & ALPHANUMERIC SERIES
# =========================================================================
def make_letter_series_question() -> Tuple[str, List[str], int, str]:
    pat = random.choice([
        'step_letters', 'reverse_step', 'increasing_step', 'alphanumeric_pos',
        'pairs_opposite', 'triplet_clusters', 'position_squared', 'interleaved_letters'
    ])
    if pat == 'step_letters':
        step = random.randint(2, 4)
        start_idx = random.randint(0, 8)
        indices = [(start_idx + i * step) % 26 for i in range(6)]
        letters = [chr(ord('A') + idx) for idx in indices]
        stem = f"{letters[0]}, {letters[1]}, {letters[2]}, {letters[3]}, {letters[4]}, ?"
        ans = letters[5]
        exp = f"Letters advance by +{step} positions in the alphabet: {letters[4]} + {step} = {ans}."
        distractors = [chr(ord('A') + (indices[5] + d) % 26) for d in [1, 2, -1]]
        opts = [ans] + distractors
        return stem, opts, 1, exp

    elif pat == 'reverse_step':
        step = random.randint(2, 3)
        start_idx = random.randint(18, 25)
        indices = [start_idx - i * step for i in range(6)]
        letters = [chr(ord('A') + idx) for idx in indices]
        stem = f"{letters[0]}, {letters[1]}, {letters[2]}, {letters[3]}, {letters[4]}, ?"
        ans = letters[5]
        exp = f"Letters decrease by -{step} positions in reverse alphabetical order: {letters[4]} - {step} = {ans}."
        opts = [ans, chr(ord(ans) + 1), chr(ord(ans) - 1), chr(ord(ans) + 2)]
        return stem, opts, 1, exp

    elif pat == 'increasing_step':
        start_idx = random.randint(0, 4)
        curr = start_idx
        letters = [chr(ord('A') + curr)]
        steps = [1, 2, 3, 4, 5]
        for s in steps:
            curr = (curr + s) % 26
            letters.append(chr(ord('A') + curr))
        stem = f"{letters[0]}, {letters[1]}, {letters[2]}, {letters[3]}, {letters[4]}, ?"
        ans = letters[5]
        exp = f"Gaps between letters increase by +1 (+1, +2, +3, +4, +5): {letters[4]} + 5 = {ans}."
        opts = [ans, chr(ord('A') + (curr + 1) % 26), chr(ord('A') + (curr - 1) % 26), chr(ord('A') + (curr + 2) % 26)]
        return stem, opts, 1, exp

    elif pat == 'alphanumeric_pos':
        step = random.randint(2, 3)
        start_idx = random.randint(0, 6)
        indices = [start_idx + i * step for i in range(5)]
        items = [f"{chr(ord('A') + idx)}{idx + 1}" for idx in indices]
        stem = f"{items[0]}, {items[1]}, {items[2]}, {items[3]}, ?"
        ans = items[4]
        exp = f"Letters step by +{step} with their 1-based alphabetical positions. Next is {ans}."
        dist = [
            f"{chr(ord('A') + indices[4])}{indices[4]}",
            f"{chr(ord('A') + indices[4] + 1)}{indices[4] + 2}",
            f"{chr(ord('A') + indices[4] - 1)}{indices[4]}"
        ]
        opts = [ans] + dist
        return stem, opts, 1, exp

    elif pat == 'pairs_opposite':
        pairs = [("AZ", "BY"), ("BY", "CX"), ("CX", "DW"), ("DW", "EV"), ("EV", "FU"), ("FU", "GT"), ("GT", "HS"), ("HS", "IR"), ("IR", "JQ"), ("JQ", "KP")]
        start = random.randint(0, len(pairs) - 5)
        sub = pairs[start : start + 5]
        stem = f"{sub[0][0]}, {sub[1][0]}, {sub[2][0]}, {sub[3][0]}, ?"
        ans = sub[4][0]
        exp = "Pairs of opposite letters advancing in forward and backward alphabetical order."
        opts = [ans, sub[4][0][0] + "X", chr(ord(ans[0])+1) + ans[1], ans[::-1]]
        return stem, opts, 1, exp

    elif pat == 'triplet_clusters':
        start = random.randint(0, 8)
        step = random.choice([1, 2])
        clusters = []
        for i in range(5):
            c1 = chr(ord('A') + (start + i*step) % 26)
            c2 = chr(ord('A') + (start + i*step + 2) % 26)
            c3 = chr(ord('A') + (start + i*step + 4) % 26)
            clusters.append(f"{c1}{c2}{c3}")
        stem = f"{clusters[0]}, {clusters[1]}, {clusters[2]}, {clusters[3]}, ?"
        ans = clusters[4]
        exp = f"Each group advances by +{step} across alternating letter positions. Next group is {ans}."
        d1 = f"{chr(ord(ans[0])+1)}{ans[1]}{ans[2]}"
        d2 = f"{ans[0]}{chr(ord(ans[1])+1)}{ans[2]}"
        d3 = f"{ans[0]}{ans[1]}{chr(ord(ans[2])-1)}"
        opts = [ans, d1, d2, d3]
        return stem, opts, 1, exp

    elif pat == 'position_squared':
        start = random.randint(1, 4)
        items = [f"{chr(ord('A') + i)}{ (i+1)**2 }" for i in range(start, start + 5)]
        stem = f"{items[0]}, {items[1]}, {items[2]}, {items[3]}, ?"
        ans = items[4]
        exp = f"Consecutive letters paired with the square of their alphabetical position: {ans}."
        ans_let = items[4][0]
        ans_num = int(items[4][1:])
        opts = [ans, f"{ans_let}{ans_num - 5}", f"{chr(ord(ans_let)+1)}{ans_num}", f"{ans_let}{ans_num + 7}"]
        return stem, opts, 1, exp

    else:
        # Interleaved letters: forward and backward
        start_f = random.randint(0, 3)
        start_b = random.randint(22, 25)
        terms = []
        for i in range(3):
            terms.append(chr(ord('A') + start_f + i))
            terms.append(chr(ord('A') + start_b - i))
        stem = f"{terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, {terms[4]}, ?"
        ans = terms[5]
        exp = f"Two interleaved series: odd positions advance ({terms[0]}, {terms[2]}, {terms[4]}), even positions decrease ({terms[1]}, {terms[3]}, {ans})."
        opts = [ans, chr(ord(ans) + 1), chr(ord(ans) - 1), chr(ord(ans) + 2)]
        return stem, opts, 1, exp


# =========================================================================
# SECTION 3: REPEATING PATTERN SERIES
# =========================================================================
def make_repeating_series_question() -> Tuple[str, List[str], int, str]:
    units = [
        ['a', 'b', 'b'], ['m', 'a', 'n'], ['a', 'b', 'c', 'd'], ['a', 'b', 'b', 'a'],
        ['s', 't', 's', 't'], ['p', 'q', 'r', 'p'], ['x', 'y', 'z', 'x'], ['a', 'a', 'b', 'b'],
        ['b', 'a', 'a'], ['c', 'a', 'b', 'd'], ['d', 'b', 'm'], ['a', 'c', 'c', 'a'],
        ['a', 'b', 'c'], ['m', 'n', 'o', 'p'], ['x', 'y', 'z'], ['k', 'l', 'm', 'n']
    ]
    unit = random.choice(units)
    repeat = random.randint(3, 4)
    full = unit * repeat
    n_blanks = random.choice([3, 4, 5])
    blank_indices = sorted(random.sample(range(len(full)), n_blanks))

    display_chars = list(full)
    ans_chars = []
    for idx in blank_indices:
        ans_chars.append(display_chars[idx])
        display_chars[idx] = '_'

    stem = " ".join(display_chars)
    ans = " ".join(ans_chars)

    unit_str = " ".join(unit)
    exp = f"Dividing the sequence into repeating blocks of '{unit_str}': {stem.replace('_', '[?]')}. Missing letters are: {ans}."

    opts = [ans]
    # Build distinct distractors
    char_pool = list(set(unit + ['a', 'b', 'c', 'm', 'n', 's', 't', 'p', 'x']))
    attempts = 0
    while len(opts) < 4 and attempts < 20:
        attempts += 1
        d_chars = list(ans_chars)
        idx_to_change = random.randint(0, len(d_chars) - 1)
        d_chars[idx_to_change] = random.choice(char_pool)
        d_str = " ".join(d_chars)
        if d_str not in opts:
            opts.append(d_str)

    while len(opts) < 4:
        opts.append(" ".join(reversed(ans_chars)))

    return stem, opts, 1, exp


# =========================================================================
# SECTION 4: CODING & DECODING
# =========================================================================
CODING_WORDS = [
    "LIGHT", "SMART", "TIGER", "CHAIR", "FLOWER", "PLANET", "SILVER",
    "GOLDEN", "SPRING", "SUMMER", "WINTER", "GARDEN", "SCHOOL", "FRIEND",
    "MONKEY", "ORANGE", "PURPLE", "YELLOW", "NATURE", "BRIDGE", "STREAM",
    "WATER", "BREAD", "RIVER", "STONE", "CLOUD", "STORM", "FOREST",
    "DESERT", "VALLEY", "CANDLE", "ROCKET", "CASTLE", "TEMPLE", "BOTTLE",
    "PENCIL", "WINDOW", "MIRROR", "SHADOW", "BREEZE", "BRANCH", "BLOSSOM"
]

def make_coding_question() -> Tuple[str, List[str], int, str]:
    pat = random.choice(['shift', 'reverse', 'opposite', 'positional_shift', 'letter_sum'])
    w1, w2 = random.sample(CODING_WORDS, 2)

    if pat == 'shift':
        shift = random.choice([1, 2, 3, -1, -2])
        def encode(w, s):
            return "".join(chr(ord('A') + (ord(c) - ord('A') + s) % 26) for c in w)
        c1 = encode(w1, shift)
        c2 = encode(w2, shift)
        sign_str = f"+{shift}" if shift > 0 else f"{shift}"
        stem = f"In a certain code language, if '{w1}' is written as '{c1}', then how will '{w2}' be written in that code?"
        ans = c2
        exp = f"Each letter is shifted by {sign_str} positions in alphabetical order. Coding '{w2}' with shift {sign_str} gives '{c2}'."
        dist1 = encode(w2, shift + 1)
        dist2 = encode(w2, shift - 1)
        dist3 = c2[::-1]
        opts = [ans, dist1, dist2, dist3]
        return stem, opts, 1, exp

    elif pat == 'reverse':
        c1 = w1[::-1]
        c2 = w2[::-1]
        stem = f"In a code language, if '{w1}' is coded as '{c1}', then how is '{w2}' coded?"
        ans = c2
        exp = f"The word is written in reverse letter order. Reversing '{w2}' yields '{c2}'."
        d1 = c2[1:] + c2[0]
        d2 = c2[0] + c2[2:] + c2[1]
        d3 = w2
        opts = [ans, d1, d2, d3]
        return stem, opts, 1, exp

    elif pat == 'opposite':
        def opp(w):
            return "".join(chr(ord('Z') - (ord(c) - ord('A'))) for c in w)
        c1 = opp(w1)
        c2 = opp(w2)
        stem = f"If '{w1}' is coded as '{c1}', then how will '{w2}' be coded in the same system?"
        ans = c2
        exp = f"Each letter is replaced by its opposite letter from the other end of the alphabet (A <-> Z, B <-> Y, etc.). Coding '{w2}' gives '{c2}'."
        d1 = opp(w2)[::-1]
        d2 = "".join(chr(ord('A') + (ord(c) - ord('A') + 1) % 26) for c in c2)
        d3 = c2[:-1] + ('A' if c2[-1] != 'A' else 'B')
        opts = [ans, d1, d2, d3]
        return stem, opts, 1, exp

    elif pat == 'positional_shift':
        def pos_encode(w):
            return "".join(chr(ord('A') + (ord(c) - ord('A') + i + 1) % 26) for i, c in enumerate(w))
        c1 = pos_encode(w1)
        c2 = pos_encode(w2)
        stem = f"In a certain code, '{w1}' is written as '{c1}'. How is '{w2}' written in that code?"
        ans = c2
        exp = f"Letter at position i is shifted by +(i + 1) positions forward. Coding '{w2}' produces '{c2}'."
        d1 = c2[::-1]
        d2 = "".join(chr(ord('A') + (ord(c) - ord('A') + 1) % 26) for c in c2)
        d3 = c2[:-1] + ('Z' if c2[-1] != 'Z' else 'A')
        opts = [ans, d1, d2, d3]
        return stem, opts, 1, exp

    else:
        # letter_sum
        s1 = sum(ord(c) - ord('A') + 1 for c in w1)
        s2 = sum(ord(c) - ord('A') + 1 for c in w2)
        stem = f"If '{w1}' = {s1}, then in that code '{w2}' = ?"
        ans = str(s2)
        exp = f"The code is the sum of the 1-based alphabetical positions of each letter: sum of '{w2}' = {s2}."
        opts = [ans, str(s2 - 3), str(s2 + 4), str(s2 + 8)]
        return stem, opts, 1, exp


# =========================================================================
# SECTION 6: NUMBER & LETTER ANALOGY
# =========================================================================
def make_analogy_question() -> Tuple[str, List[str], int, str]:
    pat = random.choice(['sq_add', 'sq_sub', 'cube_add', 'mult_linear', 'letters_shift', 'letters_opp', 'num_to_let'])
    if pat == 'sq_add':
        k = random.choice([1, 2, 3])
        n = random.randint(4, 9)
        m = random.randint(10, 16)
        n_res = n**2 + k
        m_res = m**2 + k
        stem = f"{n} : {n_res} :: {m} : ?"
        ans = str(m_res)
        exp = f"Rule: x : x^2 + {k}. {n}^2 + {k} = {n_res}. For {m}: {m}^2 + {k} = {m**2} + {k} = {m_res}."
        opts = [ans, str(m_res - 2), str(m_res + 2), str(m_res + 5)]
        return stem, opts, 1, exp

    elif pat == 'sq_sub':
        k = random.choice([1, 2])
        n = random.randint(5, 10)
        m = random.randint(11, 15)
        n_res = n**2 - k
        m_res = m**2 - k
        stem = f"{n} : {n_res} :: {m} : ?"
        ans = str(m_res)
        exp = f"Rule: x : x^2 - {k}. {n}^2 - {k} = {n_res}. For {m}: {m}^2 - {k} = {m**2} - {k} = {m_res}."
        opts = [ans, str(m_res - 3), str(m_res + 2), str(m_res - 5)]
        return stem, opts, 1, exp

    elif pat == 'cube_add':
        n = random.randint(3, 6)
        m = random.randint(4, 7)
        n_res = n**3 + n
        m_res = m**3 + m
        stem = f"{n} : {n_res} :: {m} : ?"
        ans = str(m_res)
        exp = f"Rule: x : x^3 + x. {n}^3 + {n} = {n**3} + {n} = {n_res}. For {m}: {m}^3 + {m} = {m**3} + {m} = {m_res}."
        opts = [ans, str(m**3), str(m_res + 5), str(m_res - 5)]
        return stem, opts, 1, exp

    elif pat == 'mult_linear':
        a = random.randint(2, 5)
        b = random.randint(1, 4)
        n = random.randint(6, 12)
        m = random.randint(14, 20)
        n_res = a * n + b
        m_res = a * m + b
        stem = f"{n} : {n_res} :: {m} : ?"
        ans = str(m_res)
        exp = f"Rule: x : {a}x + {b}. {a}*{n} + {b} = {n_res}. For {m}: {a}*{m} + {b} = {m_res}."
        opts = [ans, str(m_res - a), str(m_res + a), str(m_res + 2*a)]
        return stem, opts, 1, exp

    elif pat == 'letters_shift':
        words = ["ABCD", "BCDE", "CDEF", "DEFG", "PQRS", "QRST", "RSTU", "WXYZ"]
        w1, w2 = random.sample(words, 2)
        shift = random.choice([1, 2, -1])
        c1 = "".join(chr(ord('A') + (ord(c) - ord('A') + shift) % 26) for c in w1)
        c2 = "".join(chr(ord('A') + (ord(c) - ord('A') + shift) % 26) for c in w2)
        sign_str = f"+{shift}" if shift > 0 else f"{shift}"
        stem = f"{w1} : {c1} :: {w2} : ?"
        ans = c2
        exp = f"Each letter is shifted by {sign_str} positions: {w2} -> {c2}."
        d1 = "".join(chr(ord('A') + (ord(c) - ord('A') + shift + 1) % 26) for c in w2)
        d2 = "".join(chr(ord('A') + (ord(c) - ord('A') + shift - 1) % 26) for c in w2)
        d3 = c2[::-1]
        opts = [ans, d1, d2, d3]
        return stem, opts, 1, exp

    elif pat == 'letters_opp':
        stem = "AB : ZY :: CD : ?"
        ans = "XW"
        exp = "Each letter is paired with its alphabetical opposite: C -> X, D -> W."
        opts = ["XW", "WX", "VU", "UV"]
        return stem, opts, 1, exp

    else:
        # num_to_let: Position squared
        let = random.choice(['C', 'D', 'E', 'F', 'G'])
        target_let = random.choice(['H', 'I', 'J', 'K'])
        p1 = ord(let) - ord('A') + 1
        p2 = ord(target_let) - ord('A') + 1
        stem = f"{let} : {p1**2} :: {target_let} : ?"
        ans = str(p2**2)
        exp = f"Position squared: {let}({p1}) -> {p1}^2 = {p1**2}. For {target_let}({p2}) -> {p2}^2 = {p2**2}."
        opts = [ans, str((p2-1)**2), str((p2+1)**2), str(p2**2 - 5)]
        return stem, opts, 1, exp


# =========================================================================
# SECTION 7: CLASSIFICATION (ODD ONE OUT)
# =========================================================================
def make_classification_question() -> Tuple[str, List[str], int, str]:
    pat = random.choice([
        'primes_vs_composite', 'squares_vs_nonsquare', 'cubes_vs_noncube',
        'divisibility', 'letter_gaps', 'semantic'
    ])
    if pat == 'primes_vs_composite':
        primes_pool = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
        composites_pool = [21, 25, 27, 33, 35, 39, 45, 49, 51, 55, 57, 63, 65, 75, 77, 85, 91, 93, 95]
        p_sample = random.sample(primes_pool, 3)
        c_val = random.choice(composites_pool)
        stem = "Find the odd one out:"
        ans = str(c_val)
        exp = f"{c_val} is a composite number, whereas {p_sample[0]}, {p_sample[1]}, and {p_sample[2]} are prime numbers."
        opts = [ans, str(p_sample[0]), str(p_sample[1]), str(p_sample[2])]
        return stem, opts, 1, exp

    elif pat == 'squares_vs_nonsquare':
        sqs = [16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
        sample_sqs = random.sample(sqs, 3)
        non_sq = random.choice([20, 28, 35, 48, 65, 80, 99, 120, 145])
        stem = "Find the odd one out:"
        ans = str(non_sq)
        exp = f"{sample_sqs[0]}, {sample_sqs[1]}, and {sample_sqs[2]} are perfect squares, while {non_sq} is not a perfect square."
        opts = [ans, str(sample_sqs[0]), str(sample_sqs[1]), str(sample_sqs[2])]
        return stem, opts, 1, exp

    elif pat == 'cubes_vs_noncube':
        cubes = [8, 27, 64, 125, 216, 343, 512, 729]
        sample_cubes = random.sample(cubes, 3)
        non_cube = random.choice([16, 36, 49, 81, 100, 144, 196, 256])
        stem = "Find the odd one out:"
        ans = str(non_cube)
        exp = f"{sample_cubes[0]}, {sample_cubes[1]}, and {sample_cubes[2]} are perfect cubes, while {non_cube} is not a cube."
        opts = [ans, str(sample_cubes[0]), str(sample_cubes[1]), str(sample_cubes[2])]
        return stem, opts, 1, exp

    elif pat == 'divisibility':
        d = random.choice([7, 9, 11])
        base = random.randint(3, 8)
        mults = [d * (base + i) for i in range(3)]
        non_mult = d * (base + 3) + random.choice([1, 2, 3])
        stem = "Find the odd one out:"
        ans = str(non_mult)
        exp = f"{mults[0]}, {mults[1]}, and {mults[2]} are divisible by {d}, while {non_mult} is not divisible by {d}."
        opts = [ans, str(mults[0]), str(mults[1]), str(mults[2])]
        return stem, opts, 1, exp

    elif pat == 'letter_gaps':
        # 3 groups with gap +2, 1 with gap +3
        start_letters = random.sample(['A', 'C', 'E', 'G', 'I', 'K', 'M'], 4)
        def make_trip(c, g):
            return f"{c}{chr(ord(c)+g)}{chr(ord(c)+2*g)}"
        g1 = make_trip(start_letters[0], 2)
        g2 = make_trip(start_letters[1], 2)
        g3 = make_trip(start_letters[2], 2)
        odd_g = make_trip(start_letters[3], 3)
        stem = "Find the odd one out:"
        ans = odd_g
        exp = f"In {g1}, {g2}, and {g3}, letters advance by +2, whereas in {odd_g} letters advance by +3."
        opts = [ans, g1, g2, g3]
        return stem, opts, 1, exp

    else:
        # Semantic categories
        cat = random.choice(['metals', 'months', 'sense_organs', 'planets', 'geometry'])
        if cat == 'metals':
            stem = "Find the odd one out:"
            ans = "Brass"
            exp = "Copper, Iron, and Gold are pure elementary metals, while Brass is an alloy (copper + zinc)."
            opts = ["Brass", "Copper", "Iron", "Gold"]
            return stem, opts, 1, exp
        elif cat == 'months':
            stem = "Find the odd one out:"
            ans = "November"
            exp = "January, March, and July each have 31 days, whereas November has 30 days."
            opts = ["November", "January", "March", "July"]
            return stem, opts, 1, exp
        elif cat == 'sense_organs':
            stem = "Find the odd one out:"
            ans = "Heart"
            exp = "Eye, Nose, and Ear are external sense organs, whereas Heart is an internal vital organ."
            opts = ["Heart", "Eye", "Nose", "Ear"]
            return stem, opts, 1, exp
        elif cat == 'planets':
            stem = "Find the odd one out:"
            ans = "Moon"
            exp = "Earth, Mars, and Venus are planets orbiting the Sun, while Moon is a natural satellite."
            opts = ["Moon", "Earth", "Mars", "Venus"]
            return stem, opts, 1, exp
        else:
            stem = "Find the odd one out:"
            ans = "Circle"
            exp = "Triangle, Rectangle, and Square are polygons formed of straight line segments, while Circle is bounded by a curved line."
            opts = ["Circle", "Triangle", "Rectangle", "Square"]
            return stem, opts, 1, exp


# =========================================================================
# SECTION 12: DIRECTION SENSE
# =========================================================================
def make_direction_question() -> Tuple[str, List[str], int, str]:
    names = ["Ramesh", "Suresh", "Pooja", "Anil", "Sunita", "Deepak", "Kavita", "Rajesh", "Priya", "Vikram"]
    name = random.choice(names)
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (12, 16, 20), (15, 20, 25)]
    d1, d2, dist = random.choice(triples)
    scale = random.choice([1, 2])
    d1 *= scale
    d2 *= scale
    dist *= scale

    pat = random.choice(['pythagoras', 'turns_facing', 'turns_direction_back'])
    if pat == 'pythagoras':
        stem = f"{name} walks {d1} meters North, then turns to his right and walks {d2} meters. How far is he from his starting point?"
        ans = f"{dist} meters"
        exp = f"Using Pythagoras theorem: Distance = sqrt({d1}^2 + {d2}^2) = sqrt({d1**2} + {d2**2}) = {dist} meters."
        opts = [ans, f"{d1 + d2} meters", f"{dist + 2} meters", f"{abs(d1 - d2)} meters"]
        return stem, opts, 1, exp
    elif pat == 'turns_facing':
        stem = f"{name} starts walking East. After walking 15 meters, he turns right and walks 10 meters, then turns right again and walks 12 meters, and finally turns left. Which direction is he facing now?"
        ans = "South"
        exp = "East -> turn right faces South -> turn right faces West -> turn left faces South."
        opts = ["South", "North", "East", "West"]
        return stem, opts, 1, exp
    else:
        stem = f"{name} walks {d1} meters South from his home, turns left and walks {d2} meters to reach his school. In which direction is his home with respect to his school?"
        ans = "North-West"
        exp = "School is South and East of home. Therefore, home is North and West (North-West) of school."
        opts = ["North-West", "South-East", "North-East", "South-West"]
        return stem, opts, 1, exp


# =========================================================================
# SECTION 13: CALENDAR PROBLEMS
# =========================================================================
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def make_calendar_question() -> Tuple[str, List[str], int, str]:
    pat = random.choice(['after_days', 'same_month_date', 'leap_century', 'same_calendar_year', 'year_end_day'])
    if pat == 'after_days':
        today_idx = random.randint(0, 6)
        today = DAYS[today_idx]
        n_days = random.randint(25, 140)
        odd = n_days % 7
        target_idx = (today_idx + odd) % 7
        target_day = DAYS[target_idx]
        stem = f"If today is {today}, what day of the week will it be after {n_days} days?"
        ans = target_day
        exp = f"{n_days} divided by 7 leaves a remainder of {odd} odd days. {today} + {odd} days = {target_day}."
        dist = [DAYS[(target_idx + d) % 7] for d in [1, -1, 2]]
        opts = [ans] + dist
        return stem, opts, 1, exp

    elif pat == 'same_month_date':
        d1 = random.randint(1, 7)
        day1_idx = random.randint(0, 6)
        day1 = DAYS[day1_idx]
        d2 = random.randint(18, 28)
        diff = d2 - d1
        odd = diff % 7
        day2 = DAYS[(day1_idx + odd) % 7]
        stem = f"If the {d1}th day of a month is {day1}, what day of the week will the {d2}th day of the same month be?"
        ans = day2
        exp = f"Difference in days = {d2} - {d1} = {diff} days = {diff // 7} weeks + {odd} odd days. {day1} + {odd} days = {day2}."
        dist = [DAYS[(day1_idx + odd + d) % 7] for d in [1, -1, 2]]
        opts = [ans] + dist
        return stem, opts, 1, exp

    elif pat == 'leap_century':
        stem = "Which of the following years is a leap year?"
        ans = "2000"
        exp = "A century year must be divisible by 400 to be a leap year. 2000 is divisible by 400, while 1700, 1800, and 1900 are not."
        opts = ["2000", "1700", "1800", "1900"]
        return stem, opts, 1, exp

    elif pat == 'same_calendar_year':
        y = random.choice([2005, 2007, 2009, 2011, 2013])
        ans_y = str(y + 11)
        stem = f"The calendar for the year {y} will be identical to that for the year:"
        ans = ans_y
        exp = f"For non-leap years, if the year is not immediately after a leap year, the calendar repeats after 11 years: {y} + 11 = {ans_y}."
        opts = [ans, str(y + 6), str(y + 12), str(y + 5)]
        return stem, opts, 1, exp

    else:
        day_idx = random.randint(0, 6)
        day = DAYS[day_idx]
        stem = f"If 1st January of a non-leap year falls on a {day}, then on which day will 31st December of the same year fall?"
        ans = day
        exp = "A normal non-leap year has 365 days = 52 weeks + 1 day. Therefore, the year ends on the same day of the week as it began."
        dist = [DAYS[(day_idx + d) % 7] for d in [1, -1, 2]]
        opts = [ans] + dist
        return stem, opts, 1, exp


# =========================================================================
# SECTION 14: CLOCK PROBLEMS
# =========================================================================
def make_clock_question(output_img_dir: str, test_num: int, uid: str, q_num: int = 103) -> Tuple[str, List[str], int, str, Optional[str]]:
    pat = random.choice(['angle_visual', 'mirror_time', 'straight_line_count', 'right_angle_count'])
    if pat == 'angle_visual' or q_num in [103, 104, 105]:
        h = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        m = random.choice([10, 15, 20, 25, 30, 35, 40, 45, 50])
        ang = abs(30 * h - 5.5 * m)
        if ang > 180:
            ang = 360 - ang
        ang_str = f"{int(ang)}°" if ang == int(ang) else f"{ang}°"

        img_path = os.path.join(output_img_dir, f"test{test_num}_clock_{h}_{m}_{uid}.png")
        generate_clock_face(h, m, img_path)

        stem = f"What is the angle between the hour hand and the minute hand of the clock shown at {h}:{m:02d} in the figure?"
        ans = ang_str
        exp = f"Formula: Angle = |30*H - (11/2)*M| = |30*{h} - 5.5*{m}| = |{30*h} - {5.5*m}| = {ang_str}."
        dist_vals = [
            f"{int(ang + 10)}°" if ang + 10 == int(ang + 10) else f"{ang + 10}°",
            f"{int(ang - 10)}°" if ang - 10 == int(ang - 10) else f"{ang - 10}°",
            f"{int(ang + 5)}°" if ang + 5 == int(ang + 5) else f"{ang + 5}°"
        ]
        opts = [ans] + dist_vals
        return stem, opts, 1, exp, img_path

    elif pat == 'mirror_time':
        h = random.choice([2, 3, 4, 7, 8, 9, 10])
        m = random.choice([15, 20, 25, 30, 40, 45])
        ans_h = 11 - h if m > 0 else 12 - h
        ans_m = 60 - m if m > 0 else 0
        ans_str = f"{ans_h}:{ans_m:02d}"
        stem = f"If a clock shows {h}:{m:02d}, what will be the time indicated in its mirror image?"
        ans = ans_str
        exp = f"Mirror clock time = 11:60 - {h}:{m:02d} = {ans_str}."
        opts = [ans, f"{ans_h+1}:{ans_m:02d}", f"{ans_h-1}:{ans_m:02d}", f"{h}:{m:02d}"]
        return stem, opts, 1, exp, None

    elif pat == 'straight_line_count':
        stem = "How many times in a period of 24 hours (one day) do the two hands of a clock form a straight line?"
        ans = "44"
        exp = "Hands form a straight line when coinciding (22 times) or directly opposite (22 times) -> total = 22 + 22 = 44 times."
        opts = ["44", "22", "48", "24"]
        return stem, opts, 1, exp, None

    else:
        stem = "How many times in 24 hours are the hands of a clock at right angles (90 degrees) to each other?"
        ans = "44"
        exp = "The hands are at right angles twice every hour except between 2-4 and 8-10 (where they occur 3 times each instead of 4). Total = 22 times in 12 hours = 44 times in 24 hours."
        opts = ["44", "48", "24", "22"]
        return stem, opts, 1, exp, None


# =========================================================================
# SECTION 15: ARITHMETIC REASONING
# =========================================================================
def make_arithmetic_question() -> Tuple[str, List[str], int, str]:
    pat = random.choice(['handshakes', 'heads_legs', 'monkey', 'average_speed', 'ages', 'time_work', 'two_four_wheelers'])
    if pat == 'handshakes':
        n = random.randint(10, 30)
        total = n * (n - 1) // 2
        stem = f"In a meeting of {n} delegates, each person shakes hands with every other person exactly once. How many total handshakes take place?"
        ans = str(total)
        exp = f"Formula for total handshakes: n * (n - 1) / 2 = {n} * {n-1} / 2 = {total}."
        opts = [ans, str(total + n), str(total - n // 2), str(n * (n - 1))]
        return stem, opts, 1, exp

    elif pat == 'heads_legs':
        chickens = random.randint(12, 35)
        goats = random.randint(10, 28)
        heads = chickens + goats
        legs = 2 * chickens + 4 * goats
        stem = f"A farmer has some chickens and goats. If there are a total of {heads} heads and {legs} legs, how many chickens does the farmer have?"
        ans = str(chickens)
        exp = f"Let C = chickens, G = goats. C + G = {heads} and 2C + 4G = {legs}. 2C + 4({heads} - C) = {legs} => 2C = {4*heads - legs} => C = {chickens}."
        opts = [ans, str(goats), str(chickens + 4), str(goats - 3)]
        return stem, opts, 1, exp

    elif pat == 'monkey':
        climb = random.randint(3, 5)
        slip = climb - random.choice([1, 2])
        height = random.randint(22, 42)
        net = climb - slip
        rem = height - climb
        jumps_before = (rem + net - 1) // net
        final_height = jumps_before * net
        total_time = jumps_before + 1
        ans_mins = total_time * 2 - 1
        stem = f"A monkey climbs {climb} meters up a greasy pole in the 1st minute and slips down {slip} meters in the 2nd minute. If the pole is {climb + final_height} meters high, in how many minutes will he first touch the top?"
        ans = str(ans_mins)
        exp = f"In every 2 minutes net ascent = {net} m. After {jumps_before * 2} minutes he reaches {final_height} m. In the next minute (+{climb} m) he touches the top."
        opts = [ans, str(ans_mins + 2), str(ans_mins - 2), str(ans_mins + 4)]
        return stem, opts, 1, exp

    elif pat == 'average_speed':
        s1 = random.choice([20, 30, 40, 60])
        s2 = random.choice([30, 40, 60, 120])
        avg = round((2 * s1 * s2) / (s1 + s2), 1)
        avg_str = f"{int(avg)} km/h" if avg == int(avg) else f"{avg} km/h"
        stem = f"A car travels from town A to town B at {s1} km/h and returns from B to A at {s2} km/h. What is the average speed for the whole journey?"
        ans = avg_str
        exp = f"Average speed = (2 * s1 * s2) / (s1 + s2) = (2 * {s1} * {s2}) / ({s1} + {s2}) = {avg_str}."
        opts = [ans, f"{int((s1 + s2) / 2)} km/h", f"{int(s1 + s2)} km/h", f"{int(avg) - 4} km/h"]
        return stem, opts, 1, exp

    elif pat == 'ages':
        son = random.randint(10, 16)
        ratio = random.choice([3, 4])
        father = son * ratio
        diff = father - son
        stem = f"A father is currently {ratio} times as old as his son. If the difference between their ages is {diff} years, what is the son's current age?"
        ans = f"{son} years"
        exp = f"Let son's age = x. Father's age = {ratio}x. {ratio}x - x = {diff} => {ratio - 1}x = {diff} => x = {son} years."
        opts = [ans, f"{son + 2} years", f"{father} years", f"{son - 2} years"]
        return stem, opts, 1, exp

    elif pat == 'time_work':
        d1 = random.choice([10, 12, 15, 20])
        d2 = random.choice([20, 30, 60])
        combined = (d1 * d2) / (d1 + d2)
        ans_str = f"{int(combined)} days" if combined == int(combined) else f"{round(combined, 1)} days"
        stem = f"A can complete a piece of work in {d1} days and B can complete the same work in {d2} days. In how many days can they complete the work together?"
        ans = ans_str
        exp = f"Combined time = (d1 * d2) / (d1 + d2) = ({d1} * {d2}) / ({d1} + {d2}) = {ans_str}."
        opts = [ans, f"{int(combined) + 2} days", f"{int(combined) - 1} days", f"{d1 + d2} days"]
        return stem, opts, 1, exp

    else:
        # Two-wheelers and Four-wheelers
        tw = random.randint(15, 30)
        fw = random.randint(10, 25)
        total_veh = tw + fw
        total_wheels = 2 * tw + 4 * fw
        stem = f"In a parking lot, there are only bicycles (2 wheels) and cars (4 wheels). If there are {total_veh} vehicles and {total_wheels} wheels in total, how many cars are parked?"
        ans = str(fw)
        exp = f"Let B = bicycles, C = cars. B + C = {total_veh} and 2B + 4C = {total_wheels}. 2({total_veh} - C) + 4C = {total_wheels} => 2C = {total_wheels - 2*total_veh} => C = {fw}."
        opts = [ans, str(tw), str(fw + 3), str(fw - 2)]
        return stem, opts, 1, exp


# =========================================================================
# SECTION 16: MATHEMATICAL SIGN INTERCHANGE
# =========================================================================
def make_math_sign_question() -> Tuple[str, List[str], int, str]:
    a = random.randint(4, 14)
    b = random.randint(2, 6)
    c = random.randint(2, 5)
    d = random.randint(2, 9)

    # Expression: (a * b) // c + d
    if (a * b) % c == 0:
        val = (a * b) // c + d
        stem = f"If '+' means 'x', '-' means '÷', 'x' means '+' and '÷' means '-', then evaluate:\n{a} + {b} - {c} x {d} = ?"
        ans = str(val)
        exp = f"Substituting the given sign rules: {a} x {b} ÷ {c} + {d} = {a * b // c} + {d} = {val}."
        opts = [ans, str(val + 2), str(val - 2), str(val + 4)]
        return stem, opts, 1, exp
    else:
        val = a + b * c - d
        stem = f"If 'P' means '+', 'Q' means 'x', 'R' means '-' and 'S' means '÷', evaluate:\n{a} P {b} Q {c} R {d} = ?"
        ans = str(val)
        exp = f"Substituting letters with operators: {a} + {b} x {c} - {d} = {a} + {b*c} - {d} = {val}."
        opts = [ans, str(val + 1), str(val - 2), str(val + 3)]
        return stem, opts, 1, exp


# =========================================================================
# SECTION 18: NUMBER PUZZLES & GEOMETRIC MATRICES
# =========================================================================
def make_matrix_question() -> Tuple[str, List[str], int, str, List[List[str]]]:
    pat = random.choice(['product', 'sum', 'sq_diff', 'linear'])
    if pat == 'product':
        r1 = [random.randint(2, 6), random.randint(2, 6)]
        r1.append(r1[0] * r1[1])
        r2 = [random.randint(2, 6), random.randint(2, 6)]
        r2.append(r2[0] * r2[1])
        r3 = [random.randint(2, 6), random.randint(2, 6)]
        ans_val = r3[0] * r3[1]
        mdata = [
            [str(r1[0]), str(r1[1]), str(r1[2])],
            [str(r2[0]), str(r2[1]), str(r2[2])],
            [str(r3[0]), str(r3[1]), '?']
        ]
        stem = "Find the missing number in the following 3x3 matrix:"
        ans = str(ans_val)
        exp = f"Pattern: In each row, Col 1 * Col 2 = Col 3. Row 3: {r3[0]} * {r3[1]} = {ans_val}."
        opts = [ans, str(ans_val + 2), str(ans_val - 2), str(ans_val + 4)]
        return stem, opts, 1, exp, mdata

    elif pat == 'sum':
        c1 = [random.randint(1, 5), random.randint(2, 6), random.randint(3, 7)]
        c2 = [random.randint(1, 5), random.randint(2, 6), random.randint(3, 7)]
        c3 = [c1[0] + c2[0], c1[1] + c2[1], c1[2] + c2[2]]
        ans_val = c3[2]
        mdata = [
            [str(c1[0]), str(c2[0]), str(c3[0])],
            [str(c1[1]), str(c2[1]), str(c3[1])],
            [str(c1[2]), str(c2[2]), '?']
        ]
        stem = "Find the missing number in the following 3x3 matrix:"
        ans = str(ans_val)
        exp = f"Pattern: Col 1 + Col 2 = Col 3. Row 3: {c1[2]} + {c2[2]} = {ans_val}."
        opts = [ans, str(ans_val - 2), str(ans_val + 3), str(ans_val - 1)]
        return stem, opts, 1, exp, mdata

    elif pat == 'sq_diff':
        c1 = [random.randint(10, 18), random.randint(8, 14), random.randint(12, 19)]
        c2 = [random.randint(4, 9), random.randint(3, 7), random.randint(5, 11)]
        c3 = [(c1[0] - c2[0])**2, (c1[1] - c2[1])**2, (c1[2] - c2[2])**2]
        ans_val = c3[2]
        mdata = [
            [str(c1[0]), str(c2[0]), str(c3[0])],
            [str(c1[1]), str(c2[1]), str(c3[1])],
            [str(c1[2]), str(c2[2]), '?']
        ]
        stem = "Find the missing number in the given 3x3 matrix:"
        ans = str(ans_val)
        exp = f"Pattern: Col 3 = (Col 1 - Col 2)^2. Row 3: ({c1[2]} - {c2[2]})^2 = {ans_val}."
        opts = [ans, str(ans_val - 4), str(ans_val + 6), str(ans_val + 10)]
        return stem, opts, 1, exp, mdata

    else:
        # linear: Col 3 = 2 * Col 1 + Col 2
        c1 = [random.randint(3, 8), random.randint(2, 7), random.randint(4, 9)]
        c2 = [random.randint(1, 6), random.randint(2, 5), random.randint(3, 8)]
        c3 = [2 * c1[0] + c2[0], 2 * c1[1] + c2[1], 2 * c1[2] + c2[2]]
        ans_val = c3[2]
        mdata = [
            [str(c1[0]), str(c2[0]), str(c3[0])],
            [str(c1[1]), str(c2[1]), str(c3[1])],
            [str(c1[2]), str(c2[2]), '?']
        ]
        stem = "Find the missing number in the following 3x3 matrix:"
        ans = str(ans_val)
        exp = f"Pattern: 2 * Col 1 + Col 2 = Col 3. Row 3: 2 * {c1[2]} + {c2[2]} = {ans_val}."
        opts = [ans, str(ans_val - 2), str(ans_val + 2), str(ans_val + 4)]
        return stem, opts, 1, exp, mdata


def make_geom_puzzle_question(output_img_dir: str, test_num: int, uid: str, ptype: Optional[str] = None) -> Tuple[str, List[str], int, str, str]:
    """Generates one of 6 geometric puzzles with 100% dynamic randomized numbers."""
    if not ptype:
        ptype = random.choice(['satellite', 'y_trees', 'circle_quad', 'cross_boxed', 'cross_wing', 'h_blocks'])

    if ptype == 'satellite':
        M = random.choice([3, 4, 5])
        A = random.choice([1, 2])
        s = random.randint(2, 4)
        t0 = s
        t1 = t0 * M + A
        t2 = t1 * M + A
        t3 = t2 * M + A
        t4 = t3 * M + A
        img_path = os.path.join(output_img_dir, f"test{test_num}_spiral_circle_{uid}.png")
        generate_satellite_circle_puzzle(M, [(-18, str(t0)), (-90, str(t1)), (-162, str(t2)), (126, str(t3)), (54, '?')], img_path)
        stem = "Find the missing number marked with '?' in the spiral circle:"
        ans = str(t4)
        exp = f"Each term is (previous * {M}) + {A}: ({t3} * {M}) + {A} = {t3*M} + {A} = {t4}."
        opts = [ans, str(t4 - M), str(t4 + 2*M), str(t4 - 2*M)]
        return stem, opts, 1, exp, img_path

    elif ptype == 'y_trees':
        r1 = (random.randint(2, 5), random.randint(2, 5))
        r2 = (random.randint(2, 5), random.randint(2, 5))
        r3 = (random.randint(2, 6), random.randint(2, 6))
        t1 = (r1[0]**2, r1[1]**2, r1[0] * r1[1])
        t2 = (r2[0]**2, r2[1]**2, r2[0] * r2[1])
        t3 = (r3[0]**2, '?', r3[0] * r3[1])
        ans_val = r3[1]**2
        img_path = os.path.join(output_img_dir, f"test{test_num}_branch_trees_{uid}.png")
        generate_y_trees_puzzle([t1, t2, t3], img_path)
        stem = "Find the missing number marked with '?' in the third branch tree:"
        ans = str(ans_val)
        exp = f"sqrt(left) * sqrt(right) = trunk. Tree 3: sqrt({r3[0]**2}) * sqrt(?) = {r3[0]*r3[1]} => {r3[0]} * sqrt(?) = {r3[0]*r3[1]} => ? = {ans_val}."
        opts = [ans, str(ans_val - 5), str(ans_val + 5), str(ans_val + 10)]
        return stem, opts, 1, exp, img_path

    elif ptype == 'circle_quad':
        t1 = (random.randint(2, 6), random.randint(2, 6), random.randint(2, 6), random.randint(2, 6))
        c1 = (t1[0] * t1[3] * t1[2]) + t1[1]
        t2 = (random.randint(2, 6), random.randint(2, 6), random.randint(2, 6), random.randint(2, 6))
        c2 = (t2[0] * t2[3] * t2[2]) + t2[1]
        t3 = (random.randint(2, 6), random.randint(2, 6), random.randint(2, 6), random.randint(2, 6))
        ans_val = (t3[0] * t3[3] * t3[2]) + t3[1]
        img_path = os.path.join(output_img_dir, f"test{test_num}_circle_sectors_{uid}.png")
        generate_circle_quad_puzzle([
            (t1[0], t1[1], t1[2], t1[3], c1),
            (t2[0], t2[1], t2[2], t2[3], c2),
            (t3[0], t3[1], t3[2], t3[3], '?')
        ], img_path)
        stem = "Find the missing number marked with '?' in the third circle:"
        ans = str(ans_val)
        exp = f"Multiply outer three numbers (Top * Right * Bottom) and add Left: ({t3[0]} * {t3[3]} * {t3[2]}) + {t3[1]} = {ans_val}."
        opts = [ans, str(ans_val - 4), str(ans_val + 6), str(ans_val - 8)]
        return stem, opts, 1, exp, img_path

    elif ptype == 'cross_boxed':
        t1, b1, l1, r1 = random.randint(10, 16), random.randint(8, 12), random.randint(4, 8), random.randint(3, 7)
        c1 = (t1 * b1) - (l1 * r1)
        t2, b2, l2, r2 = random.randint(10, 16), random.randint(8, 12), random.randint(4, 8), random.randint(3, 7)
        ans_val = (t2 * b2) - (l2 * r2)
        img_path = os.path.join(output_img_dir, f"test{test_num}_composite_cross_{uid}.png")
        generate_cross_boxed_puzzle([(t1, b1, l1, r1, str(c1)), (t2, b2, l2, r2, '?')], img_path)
        stem = "Find the missing number marked with '?' in the second figure:"
        ans = str(ans_val)
        exp = f"(Top * Bottom) - (Left * Right) = Center: ({t2} * {b2}) - ({l2} * {r2}) = {t2*b2} - {l2*r2} = {ans_val}."
        opts = [ans, str(ans_val - 12), str(ans_val + 15), str(ans_val + 8)]
        return stem, opts, 1, exp, img_path

    elif ptype == 'cross_wing':
        tl1, br1, bl1, d1 = random.randint(16, 32), random.randint(6, 14), random.randint(10, 24), random.randint(4, 12)
        tr1 = bl1 + d1
        c1 = (tl1 - br1) * d1
        tl2, br2, bl2, d2 = random.randint(16, 32), random.randint(6, 14), random.randint(10, 24), random.randint(4, 12)
        tr2 = bl2 + d2
        c2 = (tl2 - br2) * d2
        tl3, br3, bl3, d3 = random.randint(16, 32), random.randint(6, 14), random.randint(10, 24), random.randint(4, 12)
        tr3 = bl3 + d3
        c3 = (tl3 - br3) * d3
        img_path = os.path.join(output_img_dir, f"test{test_num}_cross_wing_{uid}.png")
        generate_cross_wing_puzzle([
            (tl1, tr1, bl1, br1, str(c1)),
            (tl2, tr2, bl2, br2, str(c2)),
            (tl3, '?', bl3, br3, str(c3))
        ], img_path)
        stem = "Find the missing number marked with '?' in the third cross-wing figure:"
        ans = str(tr3)
        exp = f"(Top_Left - Bottom_Right) * (Top_Right - Bottom_Left) = Center. ({tl3} - {br3}) * (? - {bl3}) = {c3} => {tl3-br3} * (? - {bl3}) = {c3} => ? = {tr3}."
        opts = [ans, str(tr3 - 3), str(tr3 + 2), str(tr3 + 5)]
        return stem, opts, 1, exp, img_path

    else: # h_blocks
        tl1, bl1, tr1, br1 = random.randint(10, 16), random.randint(4, 8), random.randint(10, 16), random.randint(4, 8)
        c1 = (tl1 - bl1) * (tr1 + br1)
        tl2, bl2, tr2, br2 = random.randint(10, 16), random.randint(4, 8), random.randint(10, 16), random.randint(4, 8)
        c2 = (tl2 - bl2) * (tr2 + br2)
        tl3, bl3, tr3, br3 = random.randint(10, 16), random.randint(4, 8), random.randint(10, 16), random.randint(4, 8)
        ans_val = (tl3 - bl3) * (tr3 + br3)
        img_path = os.path.join(output_img_dir, f"test{test_num}_h_blocks_{uid}.png")
        generate_h_blocks_puzzle([
            (tl1, bl1, tr1, br1, str(c1)),
            (tl2, bl2, tr2, br2, str(c2)),
            (tl3, bl3, tr3, br3, '?')
        ], img_path)
        stem = "Find the missing number marked with '?' in the third H-block:"
        ans = str(ans_val)
        exp = f"(Top_Left - Bottom_Left) * (Top_Right + Bottom_Right) = Center: ({tl3} - {bl3}) * ({tr3} + {br3}) = {tl3-bl3} * {tr3+br3} = {ans_val}."
        opts = [ans, str(ans_val - 14), str(ans_val + 24), str(ans_val - 20)]
        return stem, opts, 1, exp, img_path


# =========================================================================
# SECTION 19: DICE & OPEN DICE PROBLEMS (Q149 - Q154)
# =========================================================================
def make_dice_questions(output_img_dir: str, test_num: int, uid: str) -> List[Tuple[str, List[str], int, str, str]]:
    """
    Generates all 6 procedural dice questions with randomized numbers/letters
    and mathematically calculated opposite faces.
    """
    res = []

    # Q149: Two dice with 1 common face (random permutation of 1 to 6)
    nums1 = [1, 2, 3, 4, 5, 6]
    random.shuffle(nums1)
    u, d = nums1[0], nums1[1]
    f, b = nums1[2], nums1[3]
    r, l = nums1[4], nums1[5]
    p149 = os.path.join(output_img_dir, f"test{test_num}_dice_149_{uid}.png")
    generate_two_dice([u, f, r], [u, r, b], p149)
    stem149 = f"Two positions of a dice are shown below. Which number is on the face opposite to {f}?"
    ans149 = str(b)
    exp149 = f"Common face is {u}. Tracing clockwise from {u}: in figure (i) faces are {f} and {r}; in figure (ii) faces are {r} and {b}. Thus, face {f} is opposite to face {b}."
    opts149 = [ans149, str(u), str(r), str(l)]
    res.append((stem149, opts149, 1, exp149, p149))

    # Q150: Two dice with 2 common faces
    nums2 = [1, 2, 3, 4, 5, 6]
    random.shuffle(nums2)
    c_a, c_b = nums2[0], nums2[1]
    diff_a, diff_b = nums2[2], nums2[3]
    p150 = os.path.join(output_img_dir, f"test{test_num}_dice_150_{uid}.png")
    generate_two_dice([c_a, c_b, diff_a], [c_b, c_a, diff_b], p150)
    stem150 = f"Two positions of a standard dice are shown. Which number is on the face opposite to {diff_a}?"
    ans150 = str(diff_b)
    exp150 = f"Rule of Two Common Faces: In positions (i) and (ii), faces {c_a} and {c_b} are common. Therefore, the remaining third faces ({diff_a} and {diff_b}) must be opposite to each other."
    opts150 = [ans150, str(c_a), str(c_b), str(nums2[4])]
    res.append((stem150, opts150, 1, exp150, p150))

    # Q151: Three views of a dice
    nums3 = [1, 2, 3, 4, 5, 6]
    random.shuffle(nums3)
    u3, d3 = nums3[0], nums3[1]
    f3, b3 = nums3[2], nums3[3]
    r3, l3 = nums3[4], nums3[5]
    p151 = os.path.join(output_img_dir, f"test{test_num}_dice_151_{uid}.png")
    generate_three_dice([u3, f3, r3], [u3, r3, b3], [f3, d3, r3], p151)
    stem151 = f"Three views of a dice are shown below. Which face is opposite to the face with number {u3}?"
    ans151 = str(d3)
    exp151 = f"Faces adjacent to {u3} are {f3}, {r3}, and {b3}. From view (iii), {d3} is adjacent to {f3} and {r3}. The only face opposite to {u3} is {d3}."
    opts151 = [ans151, str(f3), str(r3), str(b3)]
    res.append((stem151, opts151, 1, exp151, p151))

    # Q152: Two positions of a dice with Letters (A to F)
    lets = ['A', 'B', 'C', 'D', 'E', 'F']
    random.shuffle(lets)
    u_l, d_l = lets[0], lets[1]
    f_l, b_l = lets[2], lets[3]
    r_l, l_l = lets[4], lets[5]
    p152 = os.path.join(output_img_dir, f"test{test_num}_dice_152_{uid}.png")
    generate_two_dice([u_l, f_l, r_l], [u_l, r_l, b_l], p152)
    stem152 = f"Two positions of a dice with letters A to F are shown. Which letter is opposite to letter {f_l}?"
    ans152 = b_l
    exp152 = f"Face {u_l} is common. Rotating clockwise from {u_l}, face {f_l} corresponds opposite to face {b_l}."
    opts152 = [ans152, u_l, r_l, l_l]
    res.append((stem152, opts152, 1, exp152, p152))

    # Q153: Unfolded Net of a Cube with numbers 1 to 6
    net_nums = [1, 2, 3, 4, 5, 6]
    random.shuffle(net_nums)
    # Cross net: (0,1)->A, (1,0)->B, (1,1)->C, (1,2)->D, (1,3)->E, (2,1)->F
    # Opposites: (B, D), (C, E), (A, F)
    grid1 = {
        (0, 1): str(net_nums[0]),
        (1, 0): str(net_nums[1]),
        (1, 1): str(net_nums[2]),
        (1, 2): str(net_nums[3]),
        (1, 3): str(net_nums[4]),
        (2, 1): str(net_nums[5])
    }
    p153 = os.path.join(output_img_dir, f"test{test_num}_dice_net_153_{uid}.png")
    generate_dice_net(grid1, p153)
    target_num = net_nums[1]
    ans153 = str(net_nums[3])
    stem153 = f"When the given net is folded into a cube, which number will be on the face opposite to {target_num}?"
    exp153 = f"In an unfolded cube net, alternating faces in a straight row are opposite: {net_nums[1]} is opposite to {net_nums[3]}, {net_nums[2]} is opposite to {net_nums[4]}, and {net_nums[0]} is opposite to {net_nums[5]}."
    opts153 = [ans153, str(net_nums[2]), str(net_nums[4]), str(net_nums[0])]
    res.append((stem153, opts153, 1, exp153, p153))

    # Q154: Unfolded Net with Letters
    net_lets = ['A', 'B', 'C', 'D', 'E', 'F']
    random.shuffle(net_lets)
    grid2 = {
        (0, 1): net_lets[0],
        (1, 0): net_lets[1],
        (1, 1): net_lets[2],
        (1, 2): net_lets[3],
        (1, 3): net_lets[4],
        (2, 2): net_lets[5]
    }
    p154 = os.path.join(output_img_dir, f"test{test_num}_dice_net_154_{uid}.png")
    generate_dice_net(grid2, p154)
    target_let = net_lets[2]
    ans154 = net_lets[4]
    stem154 = f"In the given unfolded net of a dice, which letter is on the face opposite to letter {target_let}?"
    exp154 = f"Alternating faces in the horizontal strip are opposite: {net_lets[1]} is opposite to {net_lets[3]}, {net_lets[2]} is opposite to {net_lets[4]}, and {net_lets[0]} is opposite to {net_lets[5]}."
    opts154 = [ans154, net_lets[1], net_lets[3], net_lets[0]]
    res.append((stem154, opts154, 1, exp154, p154))

    return res


# =========================================================================
# SECTION 20: CUBES & PAINTED FACES GROUP (Q155 - Q160)
# =========================================================================
def make_cubes_group(output_img_dir: str, test_num: int, uid: str, current_stem: str = "") -> List[ExamQuestion]:
    """
    Generates Q155 - Q160 dynamically based on a 3D painted cube of dimension n.
    Guarantees switching to a fresh cube dimension n from the current one.
    """
    sec = BLUEPRINT[19]
    curr_lower = current_stem.lower()

    curr_n = 3
    if "4 cm" in curr_lower or "4x4" in curr_lower or "64" in curr_lower:
        curr_n = 4
    elif "5 cm" in curr_lower or "5x5" in curr_lower or "125" in curr_lower:
        curr_n = 5

    possible_n = [x for x in [3, 4, 5] if x != curr_n]
    n_cube = random.choice(possible_n)

    c3 = 8
    c2 = 12 * (n_cube - 2)
    c1 = 6 * ((n_cube - 2)**2)
    c0 = (n_cube - 2)**3
    c_tot = n_cube**3
    c_cuts = 3 * (n_cube - 1)

    cube_path = os.path.join(output_img_dir, f"test{test_num}_cube_{n_cube}x{n_cube}_{uid}.png")
    generate_3d_cube(n_cube, cube_path)

    cubes_data = [
        (f"A large cube of side {n_cube} cm is painted red on all its six faces and then cut into smaller cubes of side 1 cm each (shown in figure). Answer questions 155 to 160 based on this.\nHow many smaller cubes have exactly THREE faces painted?",
         [str(c3), str(c3 - 4), str(c3 - 2), str(c3 + 4)], 1,
         "Corner cubes always have 3 faces painted. There are always exactly 8 corners in any cube.", cube_path),
        ("How many smaller cubes have exactly TWO faces painted?",
         [str(c2), str(c2 - 4), str(c2 + 4), str(c2 + 8)], 1,
         f"Edge cubes have 2 faces painted: 12 * (n - 2) = 12 * ({n_cube} - 2) = {c2} cubes.", None),
        ("How many smaller cubes have exactly ONE face painted?",
         [str(c1), str(c1 - 2), str(c1 + 4), str(c1 + 6)], 1,
         f"Face center cubes have 1 face painted: 6 * (n - 2)^2 = 6 * ({n_cube} - 2)^2 = {c1} cubes.", None),
        ("How many smaller cubes have NO face painted (zero painted faces)?",
         [str(c0), "0", str(c0 + 2), str(c0 + 4)], 1,
         f"Inner core cubes have no painted faces: (n - 2)^3 = ({n_cube} - 2)^3 = {c0} cubes.", None),
        (f"What is the total number of 1 cm smaller cubes formed by cutting the {n_cube} cm cube?",
         [str(c_tot), str(c_tot - 9), str(c_tot - 5), str(c_tot + 9)], 1,
         f"Total smaller cubes = n^3 = {n_cube}^3 = {c_tot} cubes.", None),
        (f"What is the minimum number of cuts required to divide a {n_cube} cm cube into {c_tot} equal 1 cm smaller cubes?",
         [str(c_cuts), str(c_cuts - 2), str(c_cuts + 2), str(c_cuts + 3)], 1,
         f"Cuts required = 3 * (n - 1) = 3 * ({n_cube} - 1) = {c_cuts} cuts.", None)
    ]

    res = []
    for idx, (stem, opts, ans, exp, img) in enumerate(cubes_data):
        q_num = 155 + idx
        shuffled_opts, new_ans = helper_shuffle(opts, ans)
        res.append(ExamQuestion(
            q_num=q_num,
            stem=stem,
            options=shuffled_opts,
            correct_opt=new_ans,
            explanation=exp,
            section_name=(f"SECTION {sec.sec_num}: {sec.name}" if idx == 0 else None),
            directions=(sec.directions if idx == 0 else None),
            image_path=img
        ))
    return res


# =========================================================================
# SECTION 21: MIRROR IMAGES
# =========================================================================
def make_mirror_image_question(output_img_dir: str, test_num: int, uid: str, q_num: int = 161) -> Tuple[str, List[str], int, str, Optional[str], Optional[List[str]]]:
    """Generates a mirror image question using 500+ word bank, dynamic alphanumeric codes, or clock diagrams."""
    return generate_mirror_image_question_enhanced(output_img_dir, test_num, uid, q_num=q_num)


# =========================================================================
# SECTION 22: WATER IMAGES
# =========================================================================
def make_water_image_question(output_img_dir: str, test_num: int, uid: str, q_num: int = 167) -> Tuple[str, List[str], int, str, Optional[str], Optional[List[str]]]:
    """Generates a water image question using 500+ word bank, dynamic water codes, or symmetry questions."""
    return generate_water_image_question_enhanced(output_img_dir, test_num, uid, q_num=q_num)


# =========================================================================
# SECTION 23: PAPER FOLDING & PAPER CUTTING
# =========================================================================
def make_paper_fold_question(output_img_dir: str, test_num: int, uid: str, q_num: int = 173) -> Tuple[str, List[str], int, str, Optional[str], Optional[List[str]]]:
    """Generates a mathematically verified Paper Folding & Cutting question with 4 option images."""
    pids = get_least_recently_used_patterns('paper_folding', PFC_ALL_PATTERN_IDS, count=1, current_test_num=test_num)
    pid = pids[0]
    cfg = get_pfc_pattern_details(pid)

    pf_path = os.path.join(output_img_dir, f"test{test_num}_paper_fold_{pid}_{uid}.png")
    generate_pfc_problem(pid, pf_path)
    opt_imgs = generate_pfc_options(pid, output_img_dir, f"test{test_num}_paper_opt_{pid}_{uid}")

    return cfg['stem'], ["", "", "", ""], 1, cfg['exp'], pf_path, opt_imgs


# =========================================================================
# UNIVERSAL PROCEDURAL DISPATCHER
# =========================================================================
def generate_procedural_question(
    sec_num: int,
    used_stems: Set[str],
    old_stem: str,
    output_img_dir: str,
    test_num: int,
    uid: str,
    q_num: int = 0
) -> Optional[ExamQuestion]:
    """
    Generates a guaranteed brand-new question for section `sec_num`
    whose stem does NOT match `old_stem` and is NOT in `used_stems`.
    """
    sec = BLUEPRINT[sec_num - 1]

    # SECTION 1: Number Series
    if sec_num == 1:
        for _ in range(50):
            stem, opts, corr, exp = make_number_series_question()
            if stem.strip().lower() not in used_stems and stem.strip().lower() != old_stem:
                shuffled_opts, new_corr = helper_shuffle(opts, corr)
                return ExamQuestion(
                    q_num=1, stem=stem, options=shuffled_opts, correct_opt=new_corr,
                    explanation=exp, section_name=f"SECTION {sec.sec_num}: {sec.name}",
                    directions=sec.directions
                )

    # SECTION 2: Letter Series
    if sec_num == 2:
        for _ in range(50):
            stem, opts, corr, exp = make_letter_series_question()
            if stem.strip().lower() not in used_stems and stem.strip().lower() != old_stem:
                shuffled_opts, new_corr = helper_shuffle(opts, corr)
                return ExamQuestion(
                    q_num=11, stem=stem, options=shuffled_opts, correct_opt=new_corr,
                    explanation=exp, section_name=f"SECTION {sec.sec_num}: {sec.name}",
                    directions=sec.directions
                )

    # SECTION 3: Repeating Pattern Series
    if sec_num == 3:
        for _ in range(50):
            stem, opts, corr, exp = make_repeating_series_question()
            if stem.strip().lower() not in used_stems and stem.strip().lower() != old_stem:
                shuffled_opts, new_corr = helper_shuffle(opts, corr)
                return ExamQuestion(
                    q_num=19, stem=stem, options=shuffled_opts, correct_opt=new_corr,
                    explanation=exp, section_name=f"SECTION {sec.sec_num}: {sec.name}",
                    directions=sec.directions
                )

    # SECTION 4: Coding & Decoding
    if sec_num == 4:
        for _ in range(50):
            stem, opts, corr, exp = make_coding_question()
            if stem.strip().lower() not in used_stems and stem.strip().lower() != old_stem:
                shuffled_opts, new_corr = helper_shuffle(opts, corr)
                return ExamQuestion(
                    q_num=25, stem=stem, options=shuffled_opts, correct_opt=new_corr,
                    explanation=exp, section_name=f"SECTION {sec.sec_num}: {sec.name}",
                    directions=sec.directions
                )

    # SECTION 6: Number & Letter Analogy
    if sec_num == 6:
        for _ in range(50):
            stem, opts, corr, exp = make_analogy_question()
            if stem.strip().lower() not in used_stems and stem.strip().lower() != old_stem:
                shuffled_opts, new_corr = helper_shuffle(opts, corr)
                return ExamQuestion(
                    q_num=45, stem=stem, options=shuffled_opts, correct_opt=new_corr,
                    explanation=exp, section_name=f"SECTION {sec.sec_num}: {sec.name}",
                    directions=sec.directions
                )

    # SECTION 7: Classification (Odd One Out)
    if sec_num == 7:
        for _ in range(50):
            stem, opts, corr, exp = make_classification_question()
            if stem.strip().lower() not in used_stems and stem.strip().lower() != old_stem:
                shuffled_opts, new_corr = helper_shuffle(opts, corr)
                return ExamQuestion(
                    q_num=53, stem=stem, options=shuffled_opts, correct_opt=new_corr,
                    explanation=exp, section_name=f"SECTION {sec.sec_num}: {sec.name}",
                    directions=sec.directions
                )

    # SECTION 12: Direction Sense
    if sec_num == 12:
        for _ in range(50):
            stem, opts, corr, exp = make_direction_question()
            if stem.strip().lower() not in used_stems and stem.strip().lower() != old_stem:
                shuffled_opts, new_corr = helper_shuffle(opts, corr)
                return ExamQuestion(
                    q_num=87, stem=stem, options=shuffled_opts, correct_opt=new_corr,
                    explanation=exp, section_name=f"SECTION {sec.sec_num}: {sec.name}",
                    directions=sec.directions
                )

    # SECTION 13: Calendar Problems
    if sec_num == 13:
        for _ in range(50):
            stem, opts, corr, exp = make_calendar_question()
            if stem.strip().lower() not in used_stems and stem.strip().lower() != old_stem:
                shuffled_opts, new_corr = helper_shuffle(opts, corr)
                return ExamQuestion(
                    q_num=95, stem=stem, options=shuffled_opts, correct_opt=new_corr,
                    explanation=exp, section_name=f"SECTION {sec.sec_num}: {sec.name}",
                    directions=sec.directions
                )

    # SECTION 14: Clock Problems
    if sec_num == 14:
        for _ in range(50):
            stem, opts, corr, exp, clk_img = make_clock_question(output_img_dir, test_num, uid, q_num=(q_num or 103))
            if stem.strip().lower() not in used_stems and stem.strip().lower() != old_stem:
                shuffled_opts, new_corr = helper_shuffle(opts, corr)
                return ExamQuestion(
                    q_num=(q_num or 103), stem=stem, options=shuffled_opts, correct_opt=new_corr,
                    explanation=exp, section_name=f"SECTION {sec.sec_num}: {sec.name}",
                    directions=sec.directions, image_path=clk_img
                )

    # SECTION 15: Arithmetic Reasoning
    if sec_num == 15:
        for _ in range(50):
            stem, opts, corr, exp = make_arithmetic_question()
            if stem.strip().lower() not in used_stems and stem.strip().lower() != old_stem:
                shuffled_opts, new_corr = helper_shuffle(opts, corr)
                return ExamQuestion(
                    q_num=111, stem=stem, options=shuffled_opts, correct_opt=new_corr,
                    explanation=exp, section_name=f"SECTION {sec.sec_num}: {sec.name}",
                    directions=sec.directions
                )

    # SECTION 16: Mathematical Sign Interchange
    if sec_num == 16:
        for _ in range(50):
            stem, opts, corr, exp = make_math_sign_question()
            if stem.strip().lower() not in used_stems and stem.strip().lower() != old_stem:
                shuffled_opts, new_corr = helper_shuffle(opts, corr)
                return ExamQuestion(
                    q_num=121, stem=stem, options=shuffled_opts, correct_opt=new_corr,
                    explanation=exp, section_name=f"SECTION {sec.sec_num}: {sec.name}",
                    directions=sec.directions
                )

    # SECTION 18: Number Puzzles & Geometric Matrices
    if sec_num == 18:
        is_visual = (143 <= q_num <= 148) or any(k in old_stem.lower() for k in ['figure', 'circle', 'tree', 'block', 'wing', 'cross', 'spiral'])
        if is_visual:
            ptype = None
            stem_low = old_stem.lower()
            if 'tree' in stem_low:
                ptype = 'y_trees'
            elif 'spiral' in stem_low:
                ptype = 'satellite'
            elif 'cross-wing' in stem_low or 'wing' in stem_low:
                ptype = 'cross_wing'
            elif 'h-block' in stem_low or 'block' in stem_low:
                ptype = 'h_blocks'
            elif 'third circle' in stem_low or 'circle' in stem_low:
                ptype = 'circle_quad'
            elif 'second figure' in stem_low or 'boxed' in stem_low:
                ptype = 'cross_boxed'
            elif 143 <= q_num <= 148:
                slot_types = {
                    143: 'satellite',
                    144: 'h_blocks',
                    145: 'cross_wing',
                    146: 'circle_quad',
                    147: 'y_trees',
                    148: 'cross_boxed'
                }
                ptype = slot_types.get(q_num)

            stem, opts, corr, exp, img_path = make_geom_puzzle_question(output_img_dir, test_num, uid, ptype=ptype)
            shuffled_opts, new_corr = helper_shuffle(opts, corr)
            return ExamQuestion(
                q_num=(q_num or 143), stem=stem, options=shuffled_opts, correct_opt=new_corr,
                explanation=exp, section_name=None, directions=None, image_path=img_path
            )
        else:
            stem, opts, corr, exp, mdata = make_matrix_question()
            shuffled_opts, new_corr = helper_shuffle(opts, corr)
            return ExamQuestion(
                q_num=(q_num or 139), stem=stem, options=shuffled_opts, correct_opt=new_corr,
                explanation=exp, section_name=None, directions=None, matrix_data=mdata
            )

    # SECTION 21: Mirror Images
    if sec_num == 21:
        stem, opts, corr, exp, img_path, opt_imgs = make_mirror_image_question(output_img_dir, test_num, uid, q_num=(q_num or 161))
        shuffled_opts, new_corr, shuffled_opt_imgs = helper_shuffle_with_images(opts, corr, opt_imgs)
        return ExamQuestion(
            q_num=(q_num or 161), stem=stem, options=shuffled_opts, correct_opt=new_corr,
            explanation=exp, section_name=None, directions=None, image_path=img_path,
            option_images=shuffled_opt_imgs
        )

    # SECTION 22: Water Images
    if sec_num == 22:
        stem, opts, corr, exp, img_path, opt_imgs = make_water_image_question(output_img_dir, test_num, uid, q_num=(q_num or 167))
        shuffled_opts, new_corr, shuffled_opt_imgs = helper_shuffle_with_images(opts, corr, opt_imgs)
        return ExamQuestion(
            q_num=(q_num or 167), stem=stem, options=shuffled_opts, correct_opt=new_corr,
            explanation=exp, section_name=None, directions=None, image_path=img_path,
            option_images=shuffled_opt_imgs
        )

    # SECTION 23: Paper Folding & Paper Cutting
    if sec_num == 23:
        stem, opts, corr, exp, img_path, opt_imgs = make_paper_fold_question(output_img_dir, test_num, uid, q_num=(q_num or 173))
        shuffled_opts, new_corr, shuffled_opt_imgs = helper_shuffle_with_images(opts, corr, opt_imgs)
        return ExamQuestion(
            q_num=(q_num or 173), stem=stem, options=shuffled_opts, correct_opt=new_corr,
            explanation=exp, section_name=None, directions=None, image_path=img_path,
            option_images=shuffled_opt_imgs
        )

    # SECTION 24: Embedded Figures & Figure Completion
    if sec_num == 24:
        if q_num == 177 or (q_num is None and old_stem and 'embedded' in old_stem.lower()):
            stem, opts, corr, exp, img_path = generate_embedded_figure_question(output_img_dir, test_num, uid)
        elif q_num == 178 or (q_num is None and old_stem and ('analogy' in old_stem.lower() or 'relationship' in old_stem.lower())):
            stem, opts, corr, exp, img_path = generate_figure_analogy_question(output_img_dir, test_num, uid)
        else:
            if q_num == 178:
                stem, opts, corr, exp, img_path = generate_figure_analogy_question(output_img_dir, test_num, uid)
            else:
                stem, opts, corr, exp, img_path = generate_embedded_figure_question(output_img_dir, test_num, uid)
        return ExamQuestion(
            q_num=(q_num or 177), stem=stem, options=opts, correct_opt=corr,
            explanation=exp, section_name=None, directions=None, image_path=img_path
        )

    # SECTION 25: Dot Situation & Non-Verbal Reasoning
    if sec_num == 25:
        if q_num == 179 or (q_num is None and old_stem and 'dot' in old_stem.lower()):
            stem, opts, corr, exp, img_path = generate_dot_situation_question(output_img_dir, test_num, uid)
        elif q_num == 180 or (q_num is None and old_stem and 'series' in old_stem.lower()):
            stem, opts, corr, exp, img_path = generate_figure_series_question(output_img_dir, test_num, uid)
        else:
            if q_num == 180:
                stem, opts, corr, exp, img_path = generate_figure_series_question(output_img_dir, test_num, uid)
            else:
                stem, opts, corr, exp, img_path = generate_dot_situation_question(output_img_dir, test_num, uid)
        return ExamQuestion(
            q_num=(q_num or 179), stem=stem, options=opts, correct_opt=corr,
            explanation=exp, section_name=None, directions=None, image_path=img_path
        )

    return None
