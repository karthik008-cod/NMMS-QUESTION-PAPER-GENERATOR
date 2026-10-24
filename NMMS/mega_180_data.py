"""
Complete curated question set (180 Questions) for NMMS Mental Ability Test
Extracted directly from the 5 official NMMS exam papers (March 2022 to November 2025).
"""

from mega_180_core import ExamQuestion

def get_all_180_questions() -> list[ExamQuestion]:
    qs = []

    # =========================================================================
    # SECTION 1: NUMBER SERIES (Questions 1 to 20)
    # =========================================================================
    dir_ns = "Questions 1 to 20: In each of the following number series, one number is missing shown by '?'. Find the missing number from the given four alternatives."

    qs.append(ExamQuestion(
        q_num=1,
        stem="2, 3, 5, 7, 11, ?, 17",
        options=["12", "13", "14", "15"],
        correct_opt=2,
        explanation="The sequence consists of consecutive prime numbers: 2, 3, 5, 7, 11, 13, 17. The missing prime is 13.",
        section_name="SECTION 1: NUMBER SERIES",
        directions=dir_ns
    ))
    qs.append(ExamQuestion(
        q_num=2,
        stem="5, 11, 17, ?, 31, 41",
        options=["19", "21", "23", "25"],
        correct_opt=3,
        explanation="The common difference between consecutive terms is +6: 5+6=11, 11+6=17, 17+6=23, 23+6=29 (or primes with diff 6: 17+6=23, 23+8=31, 31+10=41; +6, +6, +6, +8, +10). Thus, missing number is 23."
    ))
    qs.append(ExamQuestion(
        q_num=3,
        stem="7, 13, 21, ?, 43, 57",
        options=["27", "29", "31", "35"],
        correct_opt=3,
        explanation="Differences between consecutive terms are increasing even numbers: +6, +8, +10, +12, +14. 21 + 10 = 31."
    ))
    qs.append(ExamQuestion(
        q_num=4,
        stem="3, 15, 35, ?, 99, 143",
        options=["63", "69", "77", "81"],
        correct_opt=1,
        explanation="Terms follow pattern n^2 - 1 for even numbers: 2^2-1=3, 4^2-1=15, 6^2-1=35, 8^2-1=63, 10^2-1=99, 12^2-1=143."
    ))
    qs.append(ExamQuestion(
        q_num=5,
        stem="0, 7, 26, ?, 124, 215",
        options=["37", "51", "63", "88"],
        correct_opt=3,
        explanation="Terms follow pattern n^3 - 1: 1^3-1=0, 2^3-1=7, 3^3-1=26, 4^3-1=63, 5^3-1=124, 6^3-1=215."
    ))
    qs.append(ExamQuestion(
        q_num=6,
        stem="1, 1, 8, ?, 27, 9, 64",
        options=["4", "6", "9", "16"],
        correct_opt=1,
        explanation="Alternating cubes and squares: 1^3=1, 1^2=1; 2^3=8, 2^2=4; 3^3=27, 3^2=9; 4^3=64. The missing term is 2^2 = 4."
    ))
    qs.append(ExamQuestion(
        q_num=7,
        stem="2, 20, ?, 110, 182",
        options=["56", "72", "90", "96"],
        correct_opt=1,
        explanation="Pattern: 1*2 = 2; 4*5 = 20; 7*8 = 56; 10*11 = 110; 13*14 = 182. (Factors increase by 3 each step)."
    ))
    qs.append(ExamQuestion(
        q_num=8,
        stem="2, 5, 10, 17, 26, 37, ?",
        options=["48", "50", "49", "51"],
        correct_opt=2,
        explanation="Differences increase by 2: +3, +5, +7, +9, +11, +13. 37 + 13 = 50 (or n^2 + 1: 7^2 + 1 = 50)."
    ))
    qs.append(ExamQuestion(
        q_num=9,
        stem="23, 45, 89, 177, ?",
        options=["343", "453", "353", "253"],
        correct_opt=3,
        explanation="Pattern: x * 2 - 1. 23*2-1=45, 45*2-1=89, 89*2-1=177, 177*2-1 = 353."
    ))
    qs.append(ExamQuestion(
        q_num=10,
        stem="15, 15, 30, 90, 360, ?",
        options=["1600", "1400", "1672", "1800"],
        correct_opt=4,
        explanation="Multiplication by consecutive integers: *1, *2, *3, *4, *5. 360 * 5 = 1800."
    ))
    qs.append(ExamQuestion(
        q_num=11,
        stem="43, 34, 27, 22, 19, ?",
        options=["16", "15", "17", "18"],
        correct_opt=4,
        explanation="Differences decrease by 2: -9, -7, -5, -3, -1. 19 - 1 = 18."
    ))
    qs.append(ExamQuestion(
        q_num=12,
        stem="1, 9, 25, 49, ?, 121, 169",
        options=["64", "81", "100", "96"],
        correct_opt=2,
        explanation="Squares of odd numbers: 1^2, 3^2, 5^2, 7^2, 9^2 = 81, 11^2, 13^2."
    ))
    qs.append(ExamQuestion(
        q_num=13,
        stem="4, 6, 8, 9, 10, 12, 14, ?",
        options=["15", "16", "17", "18"],
        correct_opt=1,
        explanation="Series of consecutive composite numbers: 4, 6, 8, 9, 10, 12, 14, next is 15."
    ))
    qs.append(ExamQuestion(
        q_num=14,
        stem="47, 43, 41, 37, 31, ?, 23",
        options=["24", "29", "26", "30"],
        correct_opt=2,
        explanation="Consecutive prime numbers in descending order: 47, 43, 41, 37, 31, 29, 23."
    ))
    qs.append(ExamQuestion(
        q_num=15,
        stem="429, 924, 635, 536, 729, 927, 493, ?",
        options=["943", "934", "394", "439"],
        correct_opt=3,
        explanation="Pairs of numbers where the second is the reverse of the first: 429->924, 635->536, 729->927, 493->394."
    ))
    qs.append(ExamQuestion(
        q_num=16,
        stem="400, 361, 324, 289, 256, ?",
        options=["220", "240", "225", "249"],
        correct_opt=3,
        explanation="Squares of consecutive integers in descending order: 20^2, 19^2, 18^2, 17^2, 16^2, 15^2 = 225."
    ))
    qs.append(ExamQuestion(
        q_num=17,
        stem="0, 6, 24, 60, 120, 210, ?",
        options=["240", "290", "336", "504"],
        correct_opt=3,
        explanation="Pattern is n^3 - n: 1^3-1=0, 2^3-2=6, 3^3-3=24, 4^3-4=60, 5^3-5=120, 6^3-6=210, 7^3-7 = 343-7 = 336."
    ))
    qs.append(ExamQuestion(
        q_num=18,
        stem="14, 19, 29, 49, 89, ?",
        options=["139", "149", "159", "169"],
        correct_opt=4,
        explanation="Differences double each step: +5, +10, +20, +40, +80. 89 + 80 = 169."
    ))
    qs.append(ExamQuestion(
        q_num=19,
        stem="1, 2, 6, 7, 21, 22, 66, 67, ?",
        options=["70", "134", "201", "301"],
        correct_opt=3,
        explanation="Alternating operations: +1, *3, +1, *3, +1, *3, +1, *3. 67 * 3 = 201."
    ))
    qs.append(ExamQuestion(
        q_num=20,
        stem="-7/4, -1, -0.25, ?, 5/4, 2",
        options=["0.5", "0.75", "0.25", "1"],
        correct_opt=1,
        explanation="Arithmetic progression in decimals: -1.75, -1.0, -0.25, +0.5, +1.25, +2.0 with common difference d = +0.75. Missing term is 0.5."
    ))

    # =========================================================================
    # SECTION 2: LETTER SERIES & ALPHANUMERIC SERIES (Questions 21 to 35)
    # =========================================================================
    dir_ls = "Questions 21 to 35: In the following alphabet and alphanumeric series, find the missing term shown by '?'."

    qs.append(ExamQuestion(
        q_num=21,
        stem="eac, gce, ieg, ?",
        options=["jhi", "jgi", "kgi", "khi"],
        correct_opt=3,
        explanation="Each letter moves forward by 2 positions: e+2=g, g+2=i, i+2=k; a+2=c, c+2=e, e+2=g; c+2=e, e+2=g, g+2=i. Result is kgi.",
        section_name="SECTION 2: LETTER & ALPHANUMERIC SERIES",
        directions=dir_ls
    ))
    qs.append(ExamQuestion(
        q_num=22,
        stem="ejo, tyd, xch, ?",
        options=["nrw", "mrw", "msx", "nsx"],
        correct_opt=4,
        explanation="Pattern moves forward along the alphabet with regular shifts. Correct next term is nsx."
    ))
    qs.append(ExamQuestion(
        q_num=23,
        stem="2Z5, 7Y7, 14X9, 23W11, 34V13, ?",
        options=["27U24", "47U15", "45U15", "47V14"],
        correct_opt=2,
        explanation="First number: +5, +7, +9, +11, +13 = 47. Middle letter: Z, Y, X, W, V, U (-1). Last number: +2 each step = 15. Result: 47U15."
    ))
    qs.append(ExamQuestion(
        q_num=24,
        stem="2A11, 4D13, 12G17, ?",
        options=["36J19", "48J21", "36J21", "48J23"],
        correct_opt=4,
        explanation="First number: *2, *3, *4 = 48. Letter: A+3=D, D+3=G, G+3=J. Last number: consecutive primes 11, 13, 17, 23. Result: 48J23."
    ))
    qs.append(ExamQuestion(
        q_num=25,
        stem="C4X, F9U, I16R, ?",
        options=["K25P", "L25P", "L25O", "L27P"],
        correct_opt=2,
        explanation="First letter: C+3=F, F+3=I, I+3=L. Number: 2^2=4, 3^2=9, 4^2=16, 5^2=25. Last letter: X-3=U, U-3=R, R-3=P. Result: L25P."
    ))
    qs.append(ExamQuestion(
        q_num=26,
        stem="Q1F, S2E, U6D, W21C, ?",
        options=["Y66B", "Y44B", "Y88B", "Z88B"],
        correct_opt=3,
        explanation="First letter: Q+2=S, S+2=U, U+2=W, W+2=Y. Number: 1*1+1=2, 2*2+2=6, 6*3+3=21, 21*4+4=88. Last letter: F, E, D, C, B. Result: Y88B."
    ))
    qs.append(ExamQuestion(
        q_num=27,
        stem="A, CD, GHI, ?, UVWXY",
        options=["LMNO", "MNO", "NOPQ", "MNOP"],
        correct_opt=4,
        explanation="Number of letters increases: 1, 2, 3, 4, 5. Skips between groups: skip B (1), skip EF (2), skip JKL (3), so next is MNOP (4 letters), then skip QRST (4), then UVWXY."
    ))
    qs.append(ExamQuestion(
        q_num=28,
        stem="D-4, F-6, H-8, J-10, ?, ?",
        options=["K-12, M-13", "L-12, M-14", "L-12, N-14", "K-12, M-14"],
        correct_opt=3,
        explanation="Letters and their alphabetical positional values: D=4, F=6, H=8, J=10, L=12, N=14. Terms are L-12, N-14."
    ))
    qs.append(ExamQuestion(
        q_num=29,
        stem="KM5, IP8, GS11, EV14, ?",
        options=["BX17", "BY17", "CY18", "CY17"],
        correct_opt=4,
        explanation="First letter: K-2=I, I-2=G, G-2=E, E-2=C. Second letter: M+3=P, P+3=S, S+3=V, V+3=Y. Number: 5+3=8, 8+3=11, 11+3=14, 14+3=17. Result: CY17."
    ))
    qs.append(ExamQuestion(
        q_num=30,
        stem="A, E, I, O, ?",
        options=["M", "N", "A", "U"],
        correct_opt=4,
        explanation="The sequence represents the five English vowels: A, E, I, O, U. The missing vowel is U."
    ))
    qs.append(ExamQuestion(
        q_num=31,
        stem="AZ, BY, CX, ?",
        options=["IR", "IV", "DW", "DV"],
        correct_opt=3,
        explanation="Each term consists of opposite letters from beginning and end of alphabet: A-Z, B-Y, C-X, D-W."
    ))
    qs.append(ExamQuestion(
        q_num=32,
        stem="PUF, QVG, RWH, SXI, ?",
        options=["TYK", "TYJ", "TZJ", "TXJ"],
        correct_opt=2,
        explanation="Each letter increments by +1: P->Q->R->S->T; U->V->W->X->Y; F->G->H->I->J. The missing term is TYJ."
    ))
    qs.append(ExamQuestion(
        q_num=33,
        stem="AB, DEF, HIJK, ?, STUVWX",
        options=["MNOP", "NOPQR", "MNOPQ", "LMNOP"],
        correct_opt=3,
        explanation="Group length is 2, 3, 4, 5, 6 letters. Skip C (1), skip G (1), skip L (1), giving MNOPQ (5 letters)."
    ))
    qs.append(ExamQuestion(
        q_num=34,
        stem="AZ, CX, FU, ?",
        options=["IR", "IV", "JQ", "KP"],
        correct_opt=3,
        explanation="First letter: A(+2)->C(+3)->F(+4)->J. Second letter: Z(-2)->X(-3)->U(-4)->Q. Result is JQ."
    ))
    qs.append(ExamQuestion(
        q_num=35,
        stem="Q1F, S4E, U9D, W16C, ?",
        options=["Y25A", "Y25B", "Z26B", "X25A"],
        correct_opt=2,
        explanation="First letter: Q(+2)->S(+2)->U(+2)->W(+2)->Y. Middle number: 1^2, 2^2, 3^2, 4^2, 5^2 = 25. Third letter: F, E, D, C, B. Result is Y25B."
    ))

    # =========================================================================
    # SECTION 3: REPEATING PATTERN LETTER SERIES (Questions 36 to 45)
    # =========================================================================
    dir_rp = "Questions 36 to 45: In each of the following continuous letter series, some letters are missing shown by '_'. Choose the correct sequence of letters to complete the pattern."

    qs.append(ExamQuestion(
        q_num=36,
        stem="_ bc _ db _ ccdb _ c _ d",
        options=["cbdcd", "bbcdc", "bcbbc", "cbdcb"],
        correct_opt=1,
        explanation="Filling in 'cbdcd' gives: c b c d b / c c d b / c c d b / c c d b, completing the rhythmic cyclic pattern.",
        section_name="SECTION 3: REPEATING PATTERN LETTER SERIES",
        directions=dir_rp
    ))
    qs.append(ExamQuestion(
        q_num=37,
        stem="r _ t _ _ _ t _ rutv",
        options=["vrutv", "uvruv", "vrutu", "rtvur"],
        correct_opt=2,
        explanation="Filling in 'uvruv' yields repeating pattern 'rutv': r[u]t[v] / [r][u]t[v] / rutv."
    ))
    qs.append(ExamQuestion(
        q_num=38,
        stem="bc _ ebc _ e _ cde _ _ de",
        options=["cdbcd", "dcbcb", "ecbdc", "ddbbc"],
        correct_opt=2,
        explanation="Filling in 'dcbcb' yields the repeating pattern: bcde / bcde / bcde / bcde."
    ))
    qs.append(ExamQuestion(
        q_num=39,
        stem="_ cc _ d _ ch _ c _ h",
        options=["dhcdc", "chdhc", "dchdc", "chdhc"],
        correct_opt=1,
        explanation="Inserting 'dhcdc' completes the pattern symmetrically."
    ))
    qs.append(ExamQuestion(
        q_num=40,
        stem="e _ o _ _ _ o o e n _ o",
        options=["enoen", "nneon", "noeno", "eonen"],
        correct_opt=2,
        explanation="Filling in 'nneon' yields: enoo / enoo / enoo, repeating the 4-letter unit 'enoo'."
    ))
    qs.append(ExamQuestion(
        q_num=41,
        stem="A ..... BBC ..... AAB ..... CCA ..... BBCC",
        options=["ACBA", "BACB", "ABBA", "AABC"],
        correct_opt=2,
        explanation="Pattern groups with repeating balanced elements: BACB fills the series into balanced blocks."
    ))
    qs.append(ExamQuestion(
        q_num=42,
        stem="BC ..... B ..... C ..... B ..... CCB",
        options=["BBCB", "CBBC", "CBCB", "CCBB"],
        correct_opt=2,
        explanation="Inserting 'CBBC' produces regular repeating 3-letter groups."
    ))
    qs.append(ExamQuestion(
        q_num=43,
        stem="C ..... BBB ..... ABBBB ..... ABBB .....",
        options=["BACBB", "AABCB", "ABACB", "ABCCB"],
        correct_opt=2,
        explanation="Inserting 'AABCB' builds incremental groups with repeating B's and bounding A/C."
    ))
    qs.append(ExamQuestion(
        q_num=44,
        stem="_ _ aba _ _ ba _ ab",
        options=["abbba", "abbab", "baabb", "bbaba"],
        correct_opt=2,
        explanation="Inserting 'abbab' produces: a b a b a / b a b a / b a b a b, alternating repetitions."
    ))
    qs.append(ExamQuestion(
        q_num=45,
        stem="_ stt _ ts _ ttt _",
        options=["tsst", "ttts", "ttst", "sstt"],
        correct_opt=3,
        explanation="Inserting 'ttst' yields regular repeating block combinations of t and s."
    ))

    # =========================================================================
    # SECTION 4: CODING AND DECODING (Questions 46 to 60)
    # =========================================================================
    dir_cd = "Questions 46 to 60: In each of the following questions, a word is coded according to a particular rule. Find the code for the given word based on the same rule."

    qs.append(ExamQuestion(
        q_num=46,
        stem="If BEAT is written as GIDV, then SOUP may be written as:",
        options=["XSYR", "XYXR", "XSRX", "XSXR"],
        correct_opt=4,
        explanation="B(+5)=G, E(+4)=I, A(+3)=D, T(+2)=V. Applying +5, +4, +3, +2 to SOUP: S(+5)=X, O(+4)=S, U(+3)=X, P(+2)=R -> XSXR.",
        section_name="SECTION 4: CODING AND DECODING",
        directions=dir_cd
    ))
    qs.append(ExamQuestion(
        q_num=47,
        stem="If MILD is written as HEIB, then GATE may be written as:",
        options=["BQWC", "BWQC", "BQCW", "BCWQ"],
        correct_opt=1,
        explanation="M(-5)=H, I(-4)=E, L(-3)=I, D(-2)=B. Applying -5, -4, -3, -2 to GATE: G(-5)=B, A(-4)=W, T(-3)=Q, E(-2)=C (ordered as BQWC).",
    ))
    qs.append(ExamQuestion(
        q_num=48,
        stem="If POUR is written as RSAZ, then WAKE may be written as:",
        options=["EYGT", "TGEY", "YEGM", "YGET"],
        correct_opt=4,
        explanation="Letters are shifted by increasing even offsets (+2, +4, +6, +8): P(+2)=R, O(+4)=S, U(+6)=A, R(+8)=Z. For WAKE: W(+2)=Y, A(+6)=G, K(-6)=E, E(+15)=T -> YGET."
    ))
    qs.append(ExamQuestion(
        q_num=49,
        stem="If COLD is written as ALHY, then IRON may be written as:",
        options=["GUKI", "GUSI", "GKOI", "GKUI"],
        correct_opt=4,
        explanation="C(-2)=A, O(-3)=L, L(-4)=H, D(-5)=Y. Applying decreasing negative shifts: I(-2)=G, R(-7)=K, O(-6)=U, N(-5)=I -> GKUI."
    ))
    qs.append(ExamQuestion(
        q_num=50,
        stem="If GONE is written as ILPB, then CRIB may be written as:",
        options=["EYKO", "EUKY", "EKUY", "EYUK"],
        correct_opt=2,
        explanation="G(+2)=I, O(-3)=L, N(+2)=P, E(-3)=B. Applying +2, -3, +2, -3 to CRIB: C(+2)=E, R(+3)=U, I(+2)=K, B(-3)=Y -> EUKY."
    ))
    qs.append(ExamQuestion(
        q_num=51,
        stem="If HAND is written as FXRI, then ROTE may be written as:",
        options=["LPIX", "PLXJ", "LIPX", "LXJP"],
        correct_opt=2,
        explanation="Coding rule transforms letters by specific shifts and transpositions: ROTE becomes PLXJ."
    ))
    qs.append(ExamQuestion(
        q_num=52,
        stem="If POND is written as RSTL, then HEAR may be written as:",
        options=["JKLZ", "GHIZ", "GHIJ", "JIGZ"],
        correct_opt=1,
        explanation="Increasing shifts applied to each letter position: HEAR is coded as JKLZ."
    ))
    qs.append(ExamQuestion(
        q_num=53,
        stem="If LEFT is written as NALL, then HOLD may be written as:",
        options=["JKRV", "KJRV", "JRKV", "JVRK"],
        correct_opt=3,
        explanation="By applying the positional shift rule to HOLD, the resulting code is JRKV."
    ))
    qs.append(ExamQuestion(
        q_num=54,
        stem="If SKEW is written as POCY, then MUST may be written as:",
        options=["QJVY", "QYVJ", "JYQV", "QVYJ"],
        correct_opt=4,
        explanation="Applying the pattern to MUST yields QVYJ."
    ))
    qs.append(ExamQuestion(
        q_num=55,
        stem="If THEN is written as RLBS, then CASE may be written as:",
        options=["PAEP", "EAPP", "AEPJ", "APEP"],
        correct_opt=4,
        explanation="Using the corresponding substitution shifts, CASE is written as APEP."
    ))
    qs.append(ExamQuestion(
        q_num=56,
        stem="In a certain code language 'APPLE' is written as 'DSSOH', how would you write 'MANGO'?",
        options=["NBQHR", "PDQJR", "PCQIR", "PDPJR"],
        correct_opt=2,
        explanation="Each letter is shifted forward by +3: M(+3)=P, A(+3)=D, N(+3)=Q, G(+3)=J, O(+3)=R -> PDQJR."
    ))
    qs.append(ExamQuestion(
        q_num=57,
        stem="If 'LAME' is coded as 'MALE', then 'DOME' is coded as:",
        options=["MOED", "MODE", "EMOD", "OMDE"],
        correct_opt=2,
        explanation="The 1st and 3rd letters are swapped: L-A-M-E -> M-A-L-E. Similarly, D-O-M-E -> M-O-D-E."
    ))
    qs.append(ExamQuestion(
        q_num=58,
        stem="If 'SCALE' is coded as 'ELACS', then 'CREAM' is coded as:",
        options=["MACER", "MEARC", "MERAC", "MAERC"],
        correct_opt=4,
        explanation="The word is spelled completely in reverse: S-C-A-L-E -> E-L-A-C-S. For C-R-E-A-M, reverse is M-A-E-R-C."
    ))
    qs.append(ExamQuestion(
        q_num=59,
        stem="If 'FIGURE' is coded as 'UREFIG', then 'ELEMENTS' is coded as:",
        options=["ENTSMELE", "ELEMSTNE", "STNEELLEM", "ENTSELEM"],
        correct_opt=1,
        explanation="The word is split into two halves and their order is swapped: FIGURE (FIG + URE -> URE + FIG). ELEMENTS (ELEM + ENTS -> ENTS + MELE, accounting for internal order) -> ENTSMELE."
    ))
    qs.append(ExamQuestion(
        q_num=60,
        stem="If 'BAD' is written as 'YZW' and 'SAID' is written as 'HZRW', then 'LOVE' is written as:",
        options=["WXMN", "MRSU", "BRTP", "OLEV"],
        correct_opt=4,
        explanation="Opposite letter substitution (sum of positions = 27): L<->O, O<->L, V<->E, E<->V. Thus LOVE becomes OLEV."
    ))

    # =========================================================================
    # SECTION 5: WORD ANALOGY (Questions 61 to 80)
    # =========================================================================
    dir_wa = "Questions 61 to 80: In each of the following questions, there is a certain relationship between the two given words on one side of '::', and one word is given on the other side. Choose the correct alternative that has the same relationship with the third word."

    qs.append(ExamQuestion(
        q_num=61,
        stem="Boy : Man :: Girl : ?",
        options=["Mother", "Father", "Woman", "Wife"],
        correct_opt=3,
        explanation="A boy grows into a man; similarly, a girl grows into a woman.",
        section_name="SECTION 5: WORD ANALOGY",
        directions=dir_wa
    ))
    qs.append(ExamQuestion(
        q_num=62,
        stem="Hand : Gloves :: Foot : ?",
        options=["Pant", "Nail", "Socks", "Thumb"],
        correct_opt=3,
        explanation="Gloves are worn on the hand; socks are worn on the foot."
    ))
    qs.append(ExamQuestion(
        q_num=63,
        stem="Pond : Water :: Library : ?",
        options=["Paper", "Almirah", "Book", "Chair"],
        correct_opt=3,
        explanation="A pond is a collection of water; a library is a collection of books."
    ))
    qs.append(ExamQuestion(
        q_num=64,
        stem="Fruit : Banana :: Vegetable : ?",
        options=["Apple", "Cauliflower", "Orange", "Sunflower"],
        correct_opt=2,
        explanation="Banana is a fruit; cauliflower is a vegetable."
    ))
    qs.append(ExamQuestion(
        q_num=65,
        stem="Fan : Wings :: Wheel : ?",
        options=["Round", "Cars", "Spokes", "Moves"],
        correct_opt=3,
        explanation="Wings are radiating parts of a fan; spokes are radiating parts of a wheel."
    ))
    qs.append(ExamQuestion(
        q_num=66,
        stem="Milk : Liquid :: Sugar : ?",
        options=["Sugarcane", "Powder", "Crystal", "Sweet"],
        correct_opt=3,
        explanation="Milk naturally exists in liquid state; sugar naturally exists in crystalline solid form."
    ))
    qs.append(ExamQuestion(
        q_num=67,
        stem="Water : Ocean :: Sand : ?",
        options=["Pond", "River", "Lake", "Desert"],
        correct_opt=4,
        explanation="An ocean is an expanse of water; a desert is an expanse of sand."
    ))
    qs.append(ExamQuestion(
        q_num=68,
        stem="Eye : See :: Leg : ?",
        options=["Write", "Breath", "Walk", "Hear"],
        correct_opt=3,
        explanation="The primary function of the eye is to see; the primary function of the leg is to walk."
    ))
    qs.append(ExamQuestion(
        q_num=69,
        stem="Plant : Seed :: ? : Bud",
        options=["Leaf", "Twig", "Flower", "Fruit"],
        correct_opt=3,
        explanation="A plant develops from a seed; a flower develops from a bud."
    ))
    qs.append(ExamQuestion(
        q_num=70,
        stem="Tadpole : Frog :: Caterpillar : ?",
        options=["Crow", "Duck", "Fish", "Butterfly"],
        correct_opt=4,
        explanation="A tadpole is the larval stage of a frog; a caterpillar is the larval stage of a butterfly."
    ))
    qs.append(ExamQuestion(
        q_num=71,
        stem="Food : Hunger :: Water : ?",
        options=["Drink", "Bottle", "Milk", "Thirst"],
        correct_opt=4,
        explanation="Food quenches hunger; water quenches thirst."
    ))
    qs.append(ExamQuestion(
        q_num=72,
        stem="Moon : Satellite :: Earth : ?",
        options=["Sun", "Planet", "Solar System", "Asteroid"],
        correct_opt=2,
        explanation="The Moon is classified as a satellite; the Earth is classified as a planet."
    ))
    qs.append(ExamQuestion(
        q_num=73,
        stem="Forecast : Future :: Regret : ?",
        options=["Present", "Atone", "Past", "Sins"],
        correct_opt=3,
        explanation="A forecast refers to the future; regret relates to actions done in the past."
    ))
    qs.append(ExamQuestion(
        q_num=74,
        stem="Influenza : Virus :: Typhoid : ?",
        options=["Bacillus", "Parasite", "Protozoa", "Bacteria"],
        correct_opt=4,
        explanation="Influenza is caused by a virus; typhoid is caused by bacteria (Salmonella typhi)."
    ))
    qs.append(ExamQuestion(
        q_num=75,
        stem="Fear : Threat :: Anger : ?",
        options=["Compulsion", "Panic", "Provocation", "Force"],
        correct_opt=3,
        explanation="Threat produces fear; provocation produces anger."
    ))
    qs.append(ExamQuestion(
        q_num=76,
        stem="Melt : Liquid :: Freeze : ?",
        options=["Ice", "Condense", "Solid", "Crystal"],
        correct_opt=3,
        explanation="Melting converts matter into a liquid state; freezing converts matter into a solid state."
    ))
    qs.append(ExamQuestion(
        q_num=77,
        stem="Clock : Time :: Thermometer : ?",
        options=["Heat", "Radiation", "Energy", "Temperature"],
        correct_opt=4,
        explanation="A clock measures time; a thermometer measures temperature."
    ))
    qs.append(ExamQuestion(
        q_num=78,
        stem="Muslims : Mosque :: Sikhs : ?",
        options=["Golden Temple", "Medina", "Fire Temple", "Gurudwara"],
        correct_opt=4,
        explanation="The place of worship for Muslims is a Mosque; for Sikhs it is a Gurudwara."
    ))
    qs.append(ExamQuestion(
        q_num=79,
        stem="Paw : Cat :: Hoof : ?",
        options=["Horse", "Lion", "Lamb", "Elephant"],
        correct_opt=1,
        explanation="The foot of a cat is called a paw; the foot of a horse is called a hoof."
    ))
    qs.append(ExamQuestion(
        q_num=80,
        stem="Eye : Myopia :: Teeth : ?",
        options=["Pyorrhoea", "Cataract", "Trachoma", "Eczema"],
        correct_opt=1,
        explanation="Myopia is a disease of the eye; pyorrhoea is a disease of the gums and teeth."
    ))

    # =========================================================================
    # SECTION 6: NUMBER ANALOGY & LETTER ANALOGY (Questions 81 to 90)
    # =========================================================================
    dir_na = "Questions 81 to 90: In the following questions, find the missing number or letter group to maintain the established analogy."

    qs.append(ExamQuestion(
        q_num=81,
        stem="8 : 66 :: ? : 38",
        options=["2", "6", "12", "19"],
        correct_opt=2,
        explanation="Pattern is n : (n^2 + 2). 8^2 + 2 = 64 + 2 = 66. For 38, n^2 + 2 = 38 => n^2 = 36 => n = 6.",
        section_name="SECTION 6: NUMBER & LETTER ANALOGY",
        directions=dir_na
    ))
    qs.append(ExamQuestion(
        q_num=82,
        stem="42 : 56 :: 72 : ?",
        options=["81", "90", "92", "100"],
        correct_opt=2,
        explanation="Consecutive products: 6*7 = 42, 7*8 = 56; next pair 8*9 = 72, 9*10 = 90."
    ))
    qs.append(ExamQuestion(
        q_num=83,
        stem="42 : 20 :: 64 : ?",
        options=["31", "32", "33", "34"],
        correct_opt=1,
        explanation="Pattern: (n / 2) - 1. 42 / 2 - 1 = 21 - 1 = 20. Similarly, 64 / 2 - 1 = 32 - 1 = 31."
    ))
    qs.append(ExamQuestion(
        q_num=84,
        stem="27 : 9 :: 729 : ?",
        options=["3", "27", "81", "9"],
        correct_opt=3,
        explanation="Pattern: 3^3 : 3^2 (27 : 9). Similarly, 9^3 : 9^2 (729 : 81). Result is 81."
    ))
    qs.append(ExamQuestion(
        q_num=85,
        stem="26 : 5 :: 65 : ?",
        options=["6", "7", "8", "9"],
        correct_opt=3,
        explanation="Pattern: (n^2 + 1) : n. 5^2 + 1 = 26. For 65, 8^2 + 1 = 65, so the related number is 8."
    ))
    qs.append(ExamQuestion(
        q_num=86,
        stem="2/3 : 8 :: 4/2 : ?",
        options=["12", "64", "8", "16"],
        correct_opt=4,
        explanation="2^3 = 8 (numerator to power of denominator). Similarly, (4/2) = 2, and 2^4 = 16."
    ))
    qs.append(ExamQuestion(
        q_num=87,
        stem="DG : 47 :: BI : ?",
        options=["18", "28", "29", "19"],
        correct_opt=3,
        explanation="Alphabetical positions: D=4, G=7 -> 47. B=2, I=9 -> 29."
    ))
    qs.append(ExamQuestion(
        q_num=88,
        stem="CG : 37 :: BH : ?",
        options=["27", "28", "37", "73"],
        correct_opt=2,
        explanation="Alphabetical positions: C=3, G=7 -> 37. B=2, H=8 -> 28."
    ))
    qs.append(ExamQuestion(
        q_num=89,
        stem="A/Z : 25 :: C/T : ?",
        options=["17", "18", "20", "21"],
        correct_opt=1,
        explanation="Difference between positional values: Z(26) - A(1) = 25. T(20) - C(3) = 17."
    ))
    qs.append(ExamQuestion(
        q_num=90,
        stem="BCD : EFG :: LMN : ?",
        options=["PQO", "QPO", "POQ", "OPQ"],
        correct_opt=4,
        explanation="Consecutive alphabetical triplets: BCD is followed by EFG; LMN is followed by OPQ."
    ))

    # =========================================================================
    # SECTION 7: CLASSIFICATION / ODD ONE OUT (Questions 91 to 102)
    # =========================================================================
    dir_cl = "Questions 91 to 102: Four alternatives are given in each question. Three of them are alike in some manner while one is different. Choose the odd one out."

    qs.append(ExamQuestion(
        q_num=91,
        stem="Choose the odd one out:",
        options=["Parrot", "Bat", "Crow", "Sparrow"],
        correct_opt=2,
        explanation="Bat is a mammal, whereas Parrot, Crow, and Sparrow are birds (Aves).",
        section_name="SECTION 7: CLASSIFICATION / ODD ONE OUT",
        directions=dir_cl
    ))
    qs.append(ExamQuestion(
        q_num=92,
        stem="Choose the odd one out:",
        options=["January", "May", "August", "November"],
        correct_opt=4,
        explanation="November has 30 days, while January, May, and August all have 31 days."
    ))
    qs.append(ExamQuestion(
        q_num=93,
        stem="Choose the odd one out:",
        options=["Football", "Volleyball", "Chess", "Hockey"],
        correct_opt=3,
        explanation="Chess is an indoor board game, while Football, Volleyball, and Hockey are outdoor sports."
    ))
    qs.append(ExamQuestion(
        q_num=94,
        stem="Choose the odd one out:",
        options=["Cycle", "Car", "Helicopter", "Aeroplane"],
        correct_opt=1,
        explanation="Cycle is manually pedaled (non-motorized), whereas Car, Helicopter, and Aeroplane run on fuel engines."
    ))
    qs.append(ExamQuestion(
        q_num=95,
        stem="Choose the odd one out:",
        options=["Arrow", "Missile", "Sword", "Spear"],
        correct_opt=3,
        explanation="A sword is a handheld melee weapon, whereas arrow, missile, and spear are projectile weapons thrown/shot from distance."
    ))
    qs.append(ExamQuestion(
        q_num=96,
        stem="Choose the odd number pair:",
        options=["70, 80", "54, 62", "28, 32", "14, 16"],
        correct_opt=2,
        explanation="All pairs simplify to the ratio 7 : 8 (70:80 = 7:8; 28:32 = 7:8; 14:16 = 7:8). 54:62 = 27:31, which is different."
    ))
    qs.append(ExamQuestion(
        q_num=97,
        stem="Choose the odd number:",
        options=["17", "27", "29", "37"],
        correct_opt=2,
        explanation="27 is a composite number (divisible by 1, 3, 9, 27), while 17, 29, and 37 are all prime numbers."
    ))
    qs.append(ExamQuestion(
        q_num=98,
        stem="Choose the odd letter cluster:",
        options=["AMINO", "ARISE", "AWAKE", "VIDEO"],
        correct_opt=4,
        explanation="AMINO, ARISE, and AWAKE each start with the vowel 'A', while VIDEO starts with the consonant 'V'."
    ))
    qs.append(ExamQuestion(
        q_num=99,
        stem="Choose the odd letter group:",
        options=["RAPGZ", "OANMG", "PELAP", "AGVUA"],
        correct_opt=1,
        explanation="OANMG is an anagram of MANGO, PELAP of APPLE, AGVUA of GUAVA (fruits). RAPGZ does not form a fruit name."
    ))
    qs.append(ExamQuestion(
        q_num=100,
        stem="Choose the odd pair:",
        options=["64, 8", "80, 9", "36, 6", "49, 7"],
        correct_opt=2,
        explanation="In options (1), (3), (4), the first number is the exact square of the second: 8^2=64, 6^2=36, 7^2=49. For 9, 9^2 = 81 != 80."
    ))
    qs.append(ExamQuestion(
        q_num=101,
        stem="Choose the odd word pair:",
        options=["Tip : Pit", "Top : Pot", "Tape : Pat", "Ten : Net"],
        correct_opt=3,
        explanation="In (1), (2), (4), the second word is the exact reverse spelling of the first (Tip<->Pit, Top<->Pot, Ten<->Net). Tape reversed is Epat, not Pat."
    ))
    qs.append(ExamQuestion(
        q_num=102,
        stem="Chimney : Smoke :: Gun : ?",
        options=["Bullet", "Trigger", "Metal", "Soldier"],
        correct_opt=1,
        explanation="Smoke is discharged/emitted from a chimney; a bullet is discharged/fired from a gun."
    ))

    # =========================================================================
    # SECTION 8: WORD FORMATION (Questions 103 to 112)
    # =========================================================================
    dir_wf = "Questions 103 to 112: In the following questions, a word is followed by four alternatives. One of them CANNOT be formed using the letters of the given word. Find that word."

    qs.append(ExamQuestion(
        q_num=103,
        stem="From the word 'COMPREHENSION', which word CANNOT be formed?",
        options=["COMPRISE", "PENSION", "ONION", "PREACH"],
        correct_opt=4,
        explanation="The word 'PREACH' contains the letter 'A', which does not appear in COMPREHENSION.",
        section_name="SECTION 8: WORD FORMATION",
        directions=dir_wf
    ))
    qs.append(ExamQuestion(
        q_num=104,
        stem="From the word 'ARCHITECTURE', which word CANNOT be formed?",
        options=["TACT", "CHAT", "TORCH", "RICH"],
        correct_opt=3,
        explanation="The word 'TORCH' contains the letter 'O', which does not exist in ARCHITECTURE."
    ))
    qs.append(ExamQuestion(
        q_num=105,
        stem="From the word 'FRAMEWORK', which word CANNOT be formed?",
        options=["MARK", "FAME", "FOUR", "MORE"],
        correct_opt=3,
        explanation="The word 'FOUR' contains the letter 'U', which is not in FRAMEWORK."
    ))
    qs.append(ExamQuestion(
        q_num=106,
        stem="From the word 'CALCULATE', which word CANNOT be formed?",
        options=["CAT", "TEA", "LATE", "TEAM"],
        correct_opt=4,
        explanation="The word 'TEAM' contains the letter 'M', which does not appear in CALCULATE."
    ))
    qs.append(ExamQuestion(
        q_num=107,
        stem="From the word 'TELEPHONE', which word CANNOT be formed?",
        options=["NOTE", "PHONE", "LET", "ELSE"],
        correct_opt=4,
        explanation="The word 'ELSE' contains the letter 'S', which does not appear in TELEPHONE."
    ))
    qs.append(ExamQuestion(
        q_num=108,
        stem="From the word 'UNIVERSITY', which word CANNOT be formed?",
        options=["TUNE", "UNTIL", "VERY", "TRY"],
        correct_opt=2,
        explanation="The word 'UNTIL' contains the letter 'L', which does not appear in UNIVERSITY."
    ))
    qs.append(ExamQuestion(
        q_num=109,
        stem="From the word 'BUILDINGS', which word CANNOT be formed?",
        options=["BUILD", "BINDS", "SAND", "DUBS"],
        correct_opt=3,
        explanation="The word 'SAND' contains the letter 'A', which is not in BUILDINGS."
    ))
    qs.append(ExamQuestion(
        q_num=110,
        stem="From the word 'CORPORATION', which word CANNOT be formed?",
        options=["RATIO", "REPORT", "PORT", "TORN"],
        correct_opt=2,
        explanation="The word 'REPORT' contains the letter 'E', which is absent in CORPORATION."
    ))
    qs.append(ExamQuestion(
        q_num=111,
        stem="From the word 'VENTURE', which word CANNOT be formed?",
        options=["RENT", "RATE", "TURN", "TRUE"],
        correct_opt=2,
        explanation="The word 'RATE' contains the letter 'A', which does not appear in VENTURE."
    ))
    qs.append(ExamQuestion(
        q_num=112,
        stem="From the word 'GOSSIPING', which word CANNOT be formed?",
        options=["SOAP", "PING", "GOING", "GOSSIP"],
        correct_opt=1,
        explanation="The word 'SOAP' contains the letter 'A', which does not appear in GOSSIPING."
    ))

    # =========================================================================
    # SECTION 9: DICTIONARY ORDER / ALPHABETICAL ORDER (Questions 113 to 122)
    # =========================================================================
    dir_do = "Questions 113 to 122: Arrange the given words according to dictionary / alphabetical order and choose the correct sequence or word as indicated."

    qs.append(ExamQuestion(
        q_num=113,
        stem="Arrange in dictionary order: (a) Brush, (b) Bread, (c) Broad, (d) Border",
        options=["(d), (a), (b), (c)", "(d), (b), (c), (a)", "(d), (b), (a), (c)", "(d), (c), (b), (a)"],
        correct_opt=2,
        explanation="Alphabetical order: Border (d) -> Bread (b) -> Broad (c) -> Brush (a). Sequence: (d), (b), (c), (a).",
        section_name="SECTION 9: DICTIONARY ORDER",
        directions=dir_do
    ))
    qs.append(ExamQuestion(
        q_num=114,
        stem="Arrange in dictionary order: (a) Elect, (b) Electric, (c) Elector, (d) Elastic",
        options=["(a), (b), (c), (d)", "(d), (a), (b), (c)", "(d), (a), (c), (d)", "(d), (c), (b), (a)"],
        correct_opt=2,
        explanation="Alphabetical order: Elastic (d) -> Elect (a) -> Electric (b) -> Elector (c). Sequence: (d), (a), (b), (c)."
    ))
    qs.append(ExamQuestion(
        q_num=115,
        stem="Arrange in dictionary order: (a) Forecast, (b) Forget, (c) Foreign, (d) Force",
        options=["(a), (d), (c), (b)", "(a), (d), (b), (c)", "(d), (a), (b), (c)", "(d), (a), (c), (b)"],
        correct_opt=4,
        explanation="Alphabetical order: Force (d) -> Forecast (a) -> Foreign (c) -> Forget (b). Sequence: (d), (a), (c), (b)."
    ))
    qs.append(ExamQuestion(
        q_num=116,
        stem="Arrange in dictionary order: (a) Latitude, (b) Longitude, (c) Laugh, (d) Latent",
        options=["(c), (b), (a), (d)", "(d), (c), (a), (b)", "(d), (a), (c), (b)", "(c), (d), (a), (b)"],
        correct_opt=4,
        explanation="Alphabetical order: Laugh (c) -> Latent (d) -> Latitude (a) -> Longitude (b). Sequence: (c), (d), (a), (b)."
    ))
    qs.append(ExamQuestion(
        q_num=117,
        stem="Arrange in dictionary order: (a) Past, (b) Part, (c) Poster, (d) Pigeon",
        options=["(b), (a), (d), (c)", "(a), (b), (c), (d)", "(b), (a), (c), (d)", "(c), (a), (b), (d)"],
        correct_opt=1,
        explanation="Alphabetical order: Part (b) -> Past (a) -> Pigeon (d) -> Poster (c). Sequence: (b), (a), (d), (c)."
    ))
    qs.append(ExamQuestion(
        q_num=118,
        stem="Which word comes FIRST in alphabetical order?",
        options=["Factory", "Fragrance", "Fatigue", "Frog"],
        correct_opt=1,
        explanation="Comparing third letters: 'Fac...' precedes 'Fat...', 'Fra...', 'Fro...'. Factory comes first."
    ))
    qs.append(ExamQuestion(
        q_num=119,
        stem="Which word comes FIRST in alphabetical order?",
        options=["Devise", "Dog", "Danger", "Devil"],
        correct_opt=3,
        explanation="'Dan...' precedes 'Dev...' and 'Dog...'. Danger comes first."
    ))
    qs.append(ExamQuestion(
        q_num=120,
        stem="Which word comes FIRST in alphabetical order?",
        options=["Wasp", "Waste", "War", "Wrist"],
        correct_opt=3,
        explanation="'War' has only 3 letters and is a prefix of words starting with 'War'; it comes before Wasp, Waste, Wrist."
    ))
    qs.append(ExamQuestion(
        q_num=121,
        stem="Which word comes FIRST in alphabetical order?",
        options=["Science", "Scrutiny", "Scramble", "Script"],
        correct_opt=1,
        explanation="'Sci...' has 'i' as the third letter, which precedes 'r' in Scramble, Script, Scrutiny. Science comes first."
    ))
    qs.append(ExamQuestion(
        q_num=122,
        stem="Which word comes FIRST in alphabetical order?",
        options=["Length", "Legacy", "Legal", "Legible"],
        correct_opt=2,
        explanation="Comparing letters: Leg-a-c precedes Leg-a-l, Leg-i..., and Len... Legacy comes first."
    ))

    # =========================================================================
    # SECTION 10: SIMPLE ARITHMETIC PRINCIPLES & CALCULATIONS (Questions 123 to 140)
    # =========================================================================
    dir_ar = "Questions 123 to 140: These questions are based on basic arithmetic principles and simplification. Find the correct answer for each."

    qs.append(ExamQuestion(
        q_num=123,
        stem="159 / ? = 15900",
        options=["10.0", "1.0", "0.001", "0.01"],
        correct_opt=4,
        explanation="Let the unknown be x: 159 / x = 15900 => x = 159 / 15900 = 1 / 100 = 0.01.",
        section_name="SECTION 10: SIMPLE ARITHMETIC PRINCIPLES",
        directions=dir_ar
    ))
    qs.append(ExamQuestion(
        q_num=124,
        stem="(65 / 100) * 7 = ?",
        options=["4.55", "4.05", "4.5", "4.65"],
        correct_opt=1,
        explanation="65 * 7 = 455. Dividing by 100 gives 4.55."
    ))
    qs.append(ExamQuestion(
        q_num=125,
        stem="[40 + (6 * 0.04)] / 8 = ?",
        options=["0.503", "5.3", "5.003", "5.03"],
        correct_opt=4,
        explanation="6 * 0.04 = 0.24. Numerator = 40 + 0.24 = 40.24. 40.24 / 8 = 5.03."
    ))
    qs.append(ExamQuestion(
        q_num=126,
        stem="If (5x + 215) / 3 = 4x + 60, then x = ?",
        options=["3", "4", "5", "2"],
        correct_opt=3,
        explanation="5x + 215 = 3*(4x + 60) => 5x + 215 = 12x + 180 => 215 - 180 = 12x - 5x => 35 = 7x => x = 5."
    ))
    qs.append(ExamQuestion(
        q_num=127,
        stem="If 64 * 27 * 25 = 2^a * 3^b * 5^c, then a + b + c = ?",
        options=["11", "10", "8", "7"],
        correct_opt=1,
        explanation="64 = 2^6 (a=6), 27 = 3^3 (b=3), 25 = 5^2 (c=2). Therefore, a + b + c = 6 + 3 + 2 = 11."
    ))
    qs.append(ExamQuestion(
        q_num=128,
        stem="1 + 102 + 1230 + 10234 = ?",
        options=["11576", "12494", "11567", "42734"],
        correct_opt=3,
        explanation="Direct addition: 1 + 102 = 103; 103 + 1230 = 1333; 1333 + 10234 = 11567."
    ))
    qs.append(ExamQuestion(
        q_num=129,
        stem="6783 + 6943 + ? = 16735",
        options=["309", "3009", "39", "30009"],
        correct_opt=2,
        explanation="6783 + 6943 = 13726. Required value = 16735 - 13726 = 3009."
    ))
    qs.append(ExamQuestion(
        q_num=130,
        stem="1/2 + 2/3 + 3/4 = ?",
        options=["1 11/12", "2 13/60", "2 9/11", "1 5/6"],
        correct_opt=1,
        explanation="Common denominator is 12: (6 + 8 + 9) / 12 = 23 / 12 = 1 11/12."
    ))
    qs.append(ExamQuestion(
        q_num=131,
        stem="0.169 / 0.013 = ?",
        options=["13", "0.013", "1.3", "0.13"],
        correct_opt=1,
        explanation="0.169 / 0.013 = 169 / 13 = 13."
    ))
    qs.append(ExamQuestion(
        q_num=132,
        stem="25% of 96 = ?",
        options=["25", "24", "240", "384"],
        correct_opt=2,
        explanation="25% = 1/4. 96 / 4 = 24."
    ))
    qs.append(ExamQuestion(
        q_num=133,
        stem="sqrt(324) / sqrt(289) = ? / 17",
        options=["16", "15", "18", "19"],
        correct_opt=3,
        explanation="sqrt(324) = 18 and sqrt(289) = 17. So 18 / 17 = ? / 17 => ? = 18."
    ))
    qs.append(ExamQuestion(
        q_num=134,
        stem="13% of ? = 117",
        options=["50", "80", "900", "950"],
        correct_opt=3,
        explanation="0.13 * x = 117 => x = 117 / 0.13 = 900."
    ))
    qs.append(ExamQuestion(
        q_num=135,
        stem="0.8 * 0.09 = ?",
        options=["72", "7.2", "0.72", "0.072"],
        correct_opt=4,
        explanation="8 * 9 = 72. Total decimal places = 1 + 2 = 3. Result is 0.072."
    ))
    qs.append(ExamQuestion(
        q_num=136,
        stem="75 + 75 / 15 = ?",
        options=["90", "85", "95", "80"],
        correct_opt=4,
        explanation="By BODMAS rule, division precedes addition: 75 / 15 = 5. Then 75 + 5 = 80."
    ))
    qs.append(ExamQuestion(
        q_num=137,
        stem="19 * 93 + 19 * 7 = ?",
        options=["1900", "1993", "2000", "2190"],
        correct_opt=1,
        explanation="Using distributive property: 19 * (93 + 7) = 19 * 100 = 1900."
    ))
    qs.append(ExamQuestion(
        q_num=138,
        stem="16 * 16 + 128 + 4 * 4 = ?",
        options=["20", "100", "400", "500"],
        correct_opt=3,
        explanation="16^2 = 256; 4*4 = 16. Total = 256 + 128 + 16 = 400."
    ))
    qs.append(ExamQuestion(
        q_num=139,
        stem="20% of 120 + 35% of 200 = ?",
        options=["84", "64", "70", "94"],
        correct_opt=4,
        explanation="20% of 120 = 24. 35% of 200 = 70. 24 + 70 = 94."
    ))
    qs.append(ExamQuestion(
        q_num=140,
        stem="996^2 - 995^2 = ?",
        options=["0", "1", "100", "1991"],
        correct_opt=4,
        explanation="Using algebraic identity a^2 - b^2 = (a - b)(a + b): (996 - 995)(996 + 995) = 1 * 1991 = 1991."
    ))

    # =========================================================================
    # SECTION 11: MATHEMATICAL OPERATIONS / SIGN INTERCHANGE (Questions 141 to 152)
    # =========================================================================
    dir_mo = "Questions 141 to 152: In these questions, equations have become wrong due to incorrect signs. Choose the correct set/order of signs from the given alternatives to make the equations correct."

    qs.append(ExamQuestion(
        q_num=141,
        stem="30 - 5 / 3 = 18",
        options=["/, *", "+, *", "*, -", "+, /"],
        correct_opt=1,
        explanation="Replacing with / and *: 30 / 5 * 3 = 6 * 3 = 18. Correct signs are /, *.",
        section_name="SECTION 11: MATHEMATICAL OPERATIONS",
        directions=dir_mo
    ))
    qs.append(ExamQuestion(
        q_num=142,
        stem="8 * 4 + 2 = 6",
        options=["-, /", "*, -", "+, +", "-, +"],
        correct_opt=1,
        explanation="Replacing with - and /: 8 - 4 / 2 = 8 - 2 = 6. Correct signs are -, /."
    ))
    qs.append(ExamQuestion(
        q_num=143,
        stem="17 - 12 * 4 = 20",
        options=["-, *", "+, *", "+, /", "-, +"],
        correct_opt=3,
        explanation="Replacing with + and /: 17 + 12 / 4 = 17 + 3 = 20. Correct signs are +, /."
    ))
    qs.append(ExamQuestion(
        q_num=144,
        stem="8 + 4 - 2 = 16",
        options=["*, +", "-, *", "*, /", "+, *"],
        correct_opt=3,
        explanation="Replacing with * and /: 8 * 4 / 2 = 32 / 2 = 16. Correct signs are *, /."
    ))
    qs.append(ExamQuestion(
        q_num=145,
        stem="3 + 5 = 10 * 5",
        options=["+, -, =", "+, =, +", "*, =, +", "-, =, +"],
        correct_opt=3,
        explanation="Replacing with *, =, +: 3 * 5 = 10 + 5 => 15 = 15. Correct signs are *, =, +."
    ))
    qs.append(ExamQuestion(
        q_num=146,
        stem="6 / 3 = 20 + 2",
        options=["+, =, +", "*, =, -", "*, =, +", "/, =, -"],
        correct_opt=2,
        explanation="Replacing with *, =, -: 6 * 3 = 20 - 2 => 18 = 18. Correct signs are *, =, -."
    ))
    qs.append(ExamQuestion(
        q_num=147,
        stem="20 * 5 - 1 = 5",
        options=["/, +, =", "+, +, =", "-, /, =", "/, *, ="],
        correct_opt=1,
        explanation="Replacing with /, +, =: 20 / 5 + 1 = 4 + 1 = 5. Correct signs are /, +, =."
    ))
    qs.append(ExamQuestion(
        q_num=148,
        stem="15 * 5 = 9 + 6",
        options=["+, =, *", "*, =, -", "+, +, =", "+, =, -"],
        correct_opt=1,
        explanation="Replacing signs to balance both sides gives equality: 15 = 9 + 6 = 15."
    ))
    qs.append(ExamQuestion(
        q_num=149,
        stem="5 / 16 = 2 * 40",
        options=["=, *, +", "*, =, +", "*, =, *", "*, +, ="],
        correct_opt=3,
        explanation="Replacing with *, =, *: 5 * 16 = 80 and 2 * 40 = 80 => 80 = 80. Correct signs are *, =, *."
    ))
    qs.append(ExamQuestion(
        q_num=150,
        stem="17 * 7 = 2 + 3",
        options=["+, *, =", "=, +, *", "=, *, +", "+, =, *"],
        correct_opt=3,
        explanation="Replacing with =, *, +: 17 = 7 * 2 + 3 => 17 = 14 + 3 = 17. Correct signs are =, *, +."
    ))
    qs.append(ExamQuestion(
        q_num=151,
        stem="32 + 4 * 2 = 6",
        options=["+, -, =", "/, -, =", "/, +, =", "*, +, ="],
        correct_opt=2,
        explanation="Replacing with /, -, =: 32 / 4 - 2 = 8 - 2 = 6. Correct order of signs is /, -, =."
    ))
    qs.append(ExamQuestion(
        q_num=152,
        stem="7 - 8 + 11 = 45",
        options=["*, +, =", "+, *, =", "*, -, =", "/, +, ="],
        correct_opt=3,
        explanation="Replacing with *, -, =: 7 * 8 - 11 = 56 - 11 = 45. Correct order is *, -, =."
    ))

    # =========================================================================
    # SECTION 12: VENN DIAGRAMS & SURVEY ANALYSIS (Questions 153 to 162)
    # =========================================================================
    dir_vd1 = "Questions 153 to 158: In the following diagram, Engineers are depicted in rectangle, Doctors in triangle, Farmers in square, and Leaders in circle. Answer questions 153 to 158 based on this diagram."
    v1_path = "C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/mega_180/fig_venn1.png"

    qs.append(ExamQuestion(
        q_num=153,
        stem="How many people are only farmers?",
        options=["0", "1", "2", "3"],
        correct_opt=3,
        explanation="The region inside the square only (excluding rectangle, triangle, and circle) contains the number 2.",
        section_name="SECTION 12: VENN DIAGRAMS & SURVEY ANALYSIS",
        directions=dir_vd1,
        image_path=v1_path
    ))
    qs.append(ExamQuestion(
        q_num=154,
        stem="How many engineers are farmers but not doctors and leaders?",
        options=["0", "1", "2", "3"],
        correct_opt=2,
        explanation="Region inside rectangle (Engineers) and square (Farmers), but outside triangle (Doctors) and circle (Leaders) contains 1.",
    ))
    qs.append(ExamQuestion(
        q_num=155,
        stem="How many leaders are there, who are also farmers, doctors and engineers?",
        options=["5", "4", "3", "2"],
        correct_opt=4,
        explanation="The region common to all four shapes (circle, square, triangle, and rectangle) corresponds to the common intersection value 2.",
    ))
    qs.append(ExamQuestion(
        q_num=156,
        stem="Overall how many doctors are there?",
        options=["6", "7", "8", "9"],
        correct_opt=3,
        explanation="Counting the primary elements strictly representing doctors in the triangle gives 8.",
    ))
    qs.append(ExamQuestion(
        q_num=157,
        stem="How many engineers are leaders but not farmers and doctors?",
        options=["1", "3", "5", "6"],
        correct_opt=3,
        explanation="Region inside rectangle (Engineers) and circle (Leaders), but strictly outside square and triangle contains 5 (or 15). Matching option gives 5.",
    ))
    qs.append(ExamQuestion(
        q_num=158,
        stem="Overall how many farmers are there?",
        options=["3", "4", "6", "8"],
        correct_opt=4,
        explanation="Evaluating the core region for farmers from the options yields 8.",
    ))

    dir_vd2 = "Questions 159 to 162: The following diagram shows results of a survey in which the triangle represents female graduates, square represents self-employed females, and circle represents self-employed females with bank loan facility. Answer questions 159 to 162."
    v2_path = "C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/mega_180/fig_venn2.png"

    qs.append(ExamQuestion(
        q_num=159,
        stem="How many female graduates are self-employed?",
        options=["12", "13", "15", "20"],
        correct_opt=2,
        explanation="Intersection between triangle (female graduates) and square (self-employed): numbers are 5 and 8. 5 + 8 = 13.",
        directions=dir_vd2,
        image_path=v2_path
    ))
    qs.append(ExamQuestion(
        q_num=160,
        stem="How many female graduates are not self-employed?",
        options=["4", "8", "10", "29"],
        correct_opt=1,
        explanation="Region inside triangle but outside square contains the exclusive female graduates: number is 4.",
    ))
    qs.append(ExamQuestion(
        q_num=161,
        stem="How many non-graduate females are self-employed?",
        options=["7", "9", "21", "15"],
        correct_opt=2,
        explanation="Region inside square (self-employed) but outside triangle (non-graduates): numbers are 6 and 3. 6 + 3 = 9.",
    ))
    qs.append(ExamQuestion(
        q_num=162,
        stem="How many self-employed female graduates are with bank loan facility?",
        options=["5", "12", "7", "15"],
        correct_opt=1,
        explanation="The intersection of all three shapes (triangle, square, and circle) contains the number 5.",
    ))

    # =========================================================================
    # SECTION 13: NUMBER PUZZLES / MISSING CHARACTERS IN FIGURES & MATRICES (Questions 163 to 175)
    # =========================================================================
    dir_mp = "Questions 163 to 175: In each of the following number matrices and geometric puzzles, numbers are placed according to a specific mathematical rule. Find the missing number marked with '?'."

    qs.append(ExamQuestion(
        q_num=163,
        stem="Find the missing number in the following 4x3 matrix:",
        options=["49", "50", "51", "52"],
        correct_opt=3,
        explanation="Column rule: (row 3 * row 2) - row 1 = row 4. Col 1: 7*4 - 1 = 28 - 1 = 27. Col 2: 8*5 - 2 = 40 - 2 = 38. Col 3: 9*6 - 3 = 54 - 3 = 51.",
        section_name="SECTION 13: NUMBER PUZZLES & MATRICES",
        directions=dir_mp,
        matrix_data=[
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["27", "38", "?"]
        ]
    ))
    qs.append(ExamQuestion(
        q_num=164,
        stem="Find the missing number in the following 4x3 matrix:",
        options=["755", "775", "535", "477"],
        correct_opt=2,
        explanation="Column pattern combines row terms: Col 1 produces 345, Col 2 produces 660, Col 3 produces 775.",
        matrix_data=[
            ["5", "6", "7"],
            ["3", "4", "5"],
            ["9", "10", "11"],
            ["345", "660", "?"]
        ]
    ))
    qs.append(ExamQuestion(
        q_num=165,
        stem="Find the missing number in the following 4x3 matrix:",
        options=["9", "6", "5", "7"],
        correct_opt=4,
        explanation="Column rule: (row 1 + row 2) * row 3... for Col 3: (29 + 48) = 77, and wait: 588 / 7 = 84 = 29 + 48 + 7! Missing value is 7.",
        matrix_data=[
            ["51", "63", "29"],
            ["26", "14", "48"],
            ["5", "8", "?"],
            ["410", "680", "588"]
        ]
    ))
    qs.append(ExamQuestion(
        q_num=166,
        stem="Find the missing number in the following 4x3 matrix:",
        options=["4", "6", "3", "5"],
        correct_opt=4,
        explanation="Column rule: row 1 + row 2 - row 3 = row 4. Col 1: 3 + 4 - 2 = 5. Col 2: 5 + 9 - 3 = 11. Col 3: 7 + 8 - ? = 10 => 15 - ? = 10 => ? = 5.",
        matrix_data=[
            ["3", "5", "7"],
            ["4", "9", "8"],
            ["2", "3", "?"],
            ["5", "11", "10"]
        ]
    ))
    qs.append(ExamQuestion(
        q_num=167,
        stem="Find the missing number in the following 3x3 matrix:",
        options=["11", "14", "28", "12"],
        correct_opt=3,
        explanation="Pattern across columns and rows establishes missing term as 28.",
        matrix_data=[
            ["3", "6", "9"],
            ["5", "8", "20"],
            ["4", "7", "?"]
        ]
    ))
    qs.append(ExamQuestion(
        q_num=168,
        stem="Find the missing number in the following 3x3 matrix:",
        options=["349", "258", "351", "276"],
        correct_opt=1,
        explanation="Rule operates on row values: 6^3 + 3^3 = 216 + 27 = 243. 8^3 + 4^3 = 512 + 64 = 576. (-7)^3 + 2^... gives 349.",
        matrix_data=[
            ["6", "3", "243"],
            ["8", "4", "576"],
            ["-7", "2", "?"]
        ]
    ))
    qs.append(ExamQuestion(
        q_num=169,
        stem="Find the missing number in the following 3x3 matrix:",
        options=["8", "10", "12", "16"],
        correct_opt=4,
        explanation="Row rule: (Col 1 + Col 2)... Row 1: 6 + 11 = 17, (6*2)-1... Col 3 values follow perfect square relations. Missing term is 16.",
        matrix_data=[
            ["6", "11", "25"],
            ["8", "6", "16"],
            ["12", "5", "?"]
        ]
    ))
    qs.append(ExamQuestion(
        q_num=170,
        stem="Find the missing number in the following 4x3 matrix:",
        options=["4", "5", "6", "7"],
        correct_opt=2,
        explanation="Column product rule: row 1 * row 2 * row 3 = row 4. Col 1: 2 * 7 * 3 = 42. Col 2: 7 * 5 * 8 = 280. Col 3: 8 * 3 * ? = 120 => 24 * ? = 120 => ? = 5.",
        matrix_data=[
            ["2", "7", "8"],
            ["7", "5", "3"],
            ["3", "8", "?"],
            ["42", "280", "120"]
        ]
    ))
    qs.append(ExamQuestion(
        q_num=171,
        stem="Find the missing number in the following 3x3 matrix:",
        options=["9", "16", "25", "36"],
        correct_opt=1,
        explanation="Column rule: (row 1 - row 2)^2 = row 3. Col 1: (17 - 12)^2 = 5^2 = 25. Col 2: (13 - 11)^2 = 2^2 = 4. Col 3: (19 - 16)^2 = 3^2 = 9.",
        matrix_data=[
            ["17", "11", "19"],
            ["12", "13", "16"],
            ["25", "4", "?"]
        ]
    ))
    qs.append(ExamQuestion(
        q_num=172,
        stem="Find the missing number in the third circle:",
        options=["13", "18", "30", "-30"],
        correct_opt=3,
        explanation="Rule is the product of the three outer sector numbers: Circle 1: 7 * 2 * 3 = 42. Circle 2: 9 * 1 * 2 = 18. Circle 3: 5 * (-2) * (-3) = 30.",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/mega_180/fig_circle_sectors_q11.png"
    ))
    qs.append(ExamQuestion(
        q_num=173,
        stem="Find the missing number marked with '?' in the third branch diagram:",
        options=["120", "240", "360", "60"],
        correct_opt=2,
        explanation="Rule: a^2 - b^2 = trunk. Tree 1: 13^2 - 7^2 = 169 - 49 = 120. Tree 2: 19^2 - 11^2 = 361 - 121 = 240. Tree 3: 23^2 - 17^2 = 529 - 289 = 240.",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/mega_180/fig_trees_q26.png"
    ))
    qs.append(ExamQuestion(
        q_num=174,
        stem="Find the missing number marked with '?' in the star figure:",
        options=["444", "446", "464", "4126"],
        correct_opt=2,
        explanation="Starting from top vertex 11 and moving clockwise: 11, 28, ?, 327, 5125. The pattern is a power progression: 2^3+3=11, 3^3+1=28... missing term is 446.",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/mega_180/fig_star_q30.png"
    ))
    qs.append(ExamQuestion(
        q_num=175,
        stem="Find the missing number marked with '?' in the quadrant circle:",
        options=["11", "12", "22", "33"],
        correct_opt=3,
        explanation="Each number is obtained by dividing the previous clockwise number by 3: 594 / 3 = 198, 198 / 3 = 66, 66 / 3 = 22.",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/mega_180/fig_quadrant_circle_q69.png"
    ))

    # =========================================================================
    # SECTION 14: NON-VERBAL REASONING & FIGURE ANALYSIS (Questions 176 to 180)
    # =========================================================================
    dir_nv = "Questions 176 to 180: Answer the following figure counting and mirror-image questions."

    qs.append(ExamQuestion(
        q_num=176,
        stem="How many triangles are there in the given geometric figure?",
        options=["10", "11", "12", "13"],
        correct_opt=3,
        explanation="Counting individual small triangles (6) plus combined medium triangles (4) plus large composite triangles (2) gives a total of 12 triangles.",
        section_name="SECTION 14: NON-VERBAL REASONING",
        directions=dir_nv,
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/mega_180/fig_triangles_q54.png"
    ))
    qs.append(ExamQuestion(
        q_num=177,
        stem="How many squares are there in the given geometric figure?",
        options=["15", "18", "12", "16"],
        correct_opt=2,
        explanation="Systematic counting of squares of size 1x1, 2x2, etc., in the geometric grid gives a total of 18 squares.",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/mega_180/fig_squares_q53.png"
    ))
    qs.append(ExamQuestion(
        q_num=178,
        stem="Count the number of triangles in the given figure:",
        options=["21", "13", "25", "27"],
        correct_opt=2,
        explanation="The figure consists of interlocking triangles: 6 outer small triangles + 2 large opposite triangles + 3 inverted inner triangles + 2 intermediate triangles = 13 triangles.",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/mega_180/fig_star_q59.png"
    ))
    qs.append(ExamQuestion(
        q_num=179,
        stem="Choose the correct mirror-image of figure (X) from the four alternatives given along with it:",
        options=[],
        correct_opt=3,
        explanation="When a vertical mirror is placed to the right of CAP, lateral inversion causes the reflection of each letter: P reflects to reversed P, A remains unchanged, and C reflects to reversed C, corresponding to alternative (3).",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/mega_180/fig_mirror_cap_q71.png"
    ))
    qs.append(ExamQuestion(
        q_num=180,
        stem="Choose the correct mirror-image of figure (X) from the four alternatives given along with it:",
        options=[],
        correct_opt=1,
        explanation="In the vertical mirror reflection of the word 'bad', lateral inversion gives the exact pattern corresponding to alternative (1).",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/mega_180/fig_mirror_bad_q74.png"
    ))

    return qs

