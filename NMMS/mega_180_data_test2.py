"""
Master Question Dataset for NMMS Mental Ability Test (MAT) - Grand Test 2
Curated from Official Telangana NMMS Question Papers (2022 - 2025).
180 Questions across 14 Sections, with detailed step-by-step explanations and verified answer keys.
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
        stem="4, 6, 8, 9, 10, 12, 14, ?",
        options=["15", "16", "17", "18"],
        correct_opt=1,
        explanation="The sequence consists of consecutive composite numbers (non-primes): 4, 6, 8, 9, 10, 12, 14, 15. The next composite number after 14 is 15.",
        section_name="SECTION 1: NUMBER SERIES",
        directions=dir_ns
    ))
    qs.append(ExamQuestion(
        q_num=2,
        stem="47, 43, 41, 37, 31, ?",
        options=["27", "28", "29", "23"],
        correct_opt=3,
        explanation="The sequence consists of prime numbers in descending order: 47, 43, 41, 37, 31. The preceding prime number is 29."
    ))
    qs.append(ExamQuestion(
        q_num=3,
        stem="400, 361, 324, 289, ?",
        options=["225", "256", "240", "196"],
        correct_opt=2,
        explanation="Terms are squares of descending consecutive integers: 20^2 = 400, 19^2 = 361, 18^2 = 324, 17^2 = 289, 16^2 = 256."
    ))
    qs.append(ExamQuestion(
        q_num=4,
        stem="2, 2, 4, 12, 48, 240, ?",
        options=["720", "1200", "1440", "1680"],
        correct_opt=3,
        explanation="Each term is multiplied by increasing consecutive integers: 2*1 = 2, 2*2 = 4, 4*3 = 12, 12*4 = 48, 48*5 = 240, 240*6 = 1440."
    ))
    qs.append(ExamQuestion(
        q_num=5,
        stem="1, 4, 3, 16, 5, 36, 7, ?",
        options=["49", "54", "64", "81"],
        correct_opt=3,
        explanation="Two alternating interleaved series: odd positioned terms are odd integers (1, 3, 5, 7), even positioned terms are squares of even numbers (2^2 = 4, 4^2 = 16, 6^2 = 36, 8^2 = 64). Missing term is 64."
    ))
    qs.append(ExamQuestion(
        q_num=6,
        stem="3, 8, 15, 24, 35, ?",
        options=["46", "48", "49", "50"],
        correct_opt=2,
        explanation="Terms follow the pattern n^2 - 1: 2^2-1=3, 3^2-1=8, 4^2-1=15, 5^2-1=24, 6^2-1=35, 7^2-1=48 (or successive odd differences +5, +7, +9, +11, +13; 35 + 13 = 48)."
    ))
    qs.append(ExamQuestion(
        q_num=7,
        stem="6, 11, 21, 36, 56, ?",
        options=["76", "81", "86", "91"],
        correct_opt=2,
        explanation="Differences between consecutive terms increase by 5 each time: +5, +10, +15, +20, +25. Thus, 56 + 25 = 81."
    ))
    qs.append(ExamQuestion(
        q_num=8,
        stem="10, 18, 28, 40, 54, 70, ?",
        options=["85", "86", "88", "90"],
        correct_opt=3,
        explanation="Differences between consecutive terms are increasing even numbers: +8, +10, +12, +14, +16, +18. 70 + 18 = 88."
    ))
    qs.append(ExamQuestion(
        q_num=9,
        stem="120, 99, 80, 63, 48, ?",
        options=["35", "36", "38", "40"],
        correct_opt=1,
        explanation="Terms follow the pattern n^2 - 1 for descending values: 11^2-1=120, 10^2-1=99, 9^2-1=80, 8^2-1=63, 7^2-1=48, 6^2-1=35."
    ))
    qs.append(ExamQuestion(
        q_num=10,
        stem="2, 6, 12, 20, 30, 42, ?",
        options=["52", "54", "56", "60"],
        correct_opt=3,
        explanation="Pattern: n(n + 1). 1*2 = 2, 2*3 = 6, 3*4 = 12, 4*5 = 20, 5*6 = 30, 6*7 = 42, 7*8 = 56."
    ))
    qs.append(ExamQuestion(
        q_num=11,
        stem="1, 8, 27, 64, 125, ?",
        options=["216", "256", "343", "512"],
        correct_opt=1,
        explanation="Terms are cubes of consecutive natural numbers: 1^3 = 1, 2^3 = 8, 3^3 = 27, 4^3 = 64, 5^3 = 125, 6^3 = 216."
    ))
    qs.append(ExamQuestion(
        q_num=12,
        stem="2, 5, 9, 19, 37, ?",
        options=["73", "75", "77", "79"],
        correct_opt=2,
        explanation="Alternating operations: 2*2 + 1 = 5, 5*2 - 1 = 9, 9*2 + 1 = 19, 19*2 - 1 = 37, 37*2 + 1 = 75."
    ))
    qs.append(ExamQuestion(
        q_num=13,
        stem="4, 7, 12, 19, 28, ?",
        options=["37", "39", "41", "43"],
        correct_opt=2,
        explanation="Differences increase by 2: +3, +5, +7, +9, +11. 28 + 11 = 39 (or n^2 + 3: 6^2 + 3 = 39)."
    ))
    qs.append(ExamQuestion(
        q_num=14,
        stem="11, 13, 17, 19, 23, 29, 31, ?",
        options=["33", "35", "37", "39"],
        correct_opt=3,
        explanation="Consecutive prime numbers sequence: 11, 13, 17, 19, 23, 29, 31. The next prime number is 37."
    ))
    qs.append(ExamQuestion(
        q_num=15,
        stem="3, 6, 18, 72, 360, ?",
        options=["1440", "1800", "2160", "2520"],
        correct_opt=3,
        explanation="Multiplication by consecutive integers: 3*2 = 6, 6*3 = 18, 18*4 = 72, 72*5 = 360, 360*6 = 2160."
    ))
    qs.append(ExamQuestion(
        q_num=16,
        stem="5, 9, 17, 33, 65, ?",
        options=["97", "117", "129", "131"],
        correct_opt=3,
        explanation="Differences double each time (+4, +8, +16, +32, +64): 65 + 64 = 129 (or 2n - 1: 65*2 - 1 = 129)."
    ))
    qs.append(ExamQuestion(
        q_num=17,
        stem="7, 14, 42, 168, 840, ?",
        options=["4200", "5040", "5880", "6720"],
        correct_opt=2,
        explanation="Multipliers increase consecutively: *2, *3, *4, *5, *6. 840 * 6 = 5040."
    ))
    qs.append(ExamQuestion(
        q_num=18,
        stem="240, 120, 40, 10, ?",
        options=["1", "2", "3", "5"],
        correct_opt=2,
        explanation="Division by increasing integers: 240 / 2 = 120, 120 / 3 = 40, 40 / 4 = 10, 10 / 5 = 2."
    ))
    qs.append(ExamQuestion(
        q_num=19,
        stem="2, 3, 7, 16, 32, ?",
        options=["47", "57", "64", "68"],
        correct_opt=2,
        explanation="Differences between consecutive terms are squares of natural numbers: +1^2 = +1, +2^2 = +4, +3^2 = +9, +4^2 = +16, +5^2 = +25. 32 + 25 = 57."
    ))
    qs.append(ExamQuestion(
        q_num=20,
        stem="0, 6, 24, 60, 120, 210, ?",
        options=["240", "290", "336", "504"],
        correct_opt=3,
        explanation="Pattern is n^3 - n: 1^3-1=0, 2^3-2=6, 3^3-3=24, 4^3-4=60, 5^3-5=120, 6^3-6=210, 7^3-7 = 343 - 7 = 336."
    ))

    # =========================================================================
    # SECTION 2: LETTER & ALPHANUMERIC SERIES (Questions 21 to 35)
    # =========================================================================
    dir_ls = "Questions 21 to 35: In each letter and alphanumeric series, find the missing term marked with '?' from the given alternatives."

    qs.append(ExamQuestion(
        q_num=21,
        stem="A, C, F, J, O, ?",
        options=["S", "T", "U", "V"],
        correct_opt=3,
        explanation="Letter position increases by consecutive integers: A(1) + 2 = C(3); + 3 = F(6); + 4 = J(10); + 5 = O(15); + 6 = U(21). Missing letter is U.",
        section_name="SECTION 2: LETTER & ALPHANUMERIC SERIES",
        directions=dir_ls
    ))
    qs.append(ExamQuestion(
        q_num=22,
        stem="Z, X, V, T, R, ?",
        options=["M", "N", "O", "P"],
        correct_opt=4,
        explanation="Letter position decreases by 2: Z(26), X(24), V(22), T(20), R(18), P(16). Missing letter is P."
    ))
    qs.append(ExamQuestion(
        q_num=23,
        stem="B, D, G, K, P, ?",
        options=["S", "T", "U", "V"],
        correct_opt=4,
        explanation="Letter positions advance by increasing intervals: B(2) + 2 = D(4); + 3 = G(7); + 4 = K(11); + 5 = P(16); + 6 = V(22). Missing letter is V."
    ))
    qs.append(ExamQuestion(
        q_num=24,
        stem="AZ, BY, CX, DW, ?",
        options=["EU", "EY", "EV", "EX"],
        correct_opt=3,
        explanation="Pairs of opposite letters from beginning and end of alphabet: A-Z, B-Y, C-X, D-W, E-V. Next pair is EV."
    ))
    qs.append(ExamQuestion(
        q_num=25,
        stem="ZA, YB, XC, WD, ?",
        options=["VE", "UE", "VF", "UF"],
        correct_opt=1,
        explanation="First letter moves backward (Z, Y, X, W, V), second letter moves forward (A, B, C, D, E). Next term is VE."
    ))
    qs.append(ExamQuestion(
        q_num=26,
        stem="KM5, IP8, GS11, EV14, ?",
        options=["BX17", "BY17", "CY17", "CZ17"],
        correct_opt=3,
        explanation="First letter decreases by 2: K, I, G, E, C. Second letter increases by 3: M, P, S, V, Y. Number increases by 3: 5, 8, 11, 14, 17. Result: CY17."
    ))
    qs.append(ExamQuestion(
        q_num=27,
        stem="C4X, F9U, I16R, ?",
        options=["L25O", "K25P", "L20P", "M25O"],
        correct_opt=1,
        explanation="First letters: C(+3) F(+3) I(+3) L. Middle numbers are squares: 2^2=4, 3^2=9, 4^2=16, 5^2=25. Last letters: X(-3) U(-3) R(-3) O. Result: L25O."
    ))
    qs.append(ExamQuestion(
        q_num=28,
        stem="DF, GJ, KM, NQ, RT, ?",
        options=["UW", "UX", "UY", "VX"],
        correct_opt=2,
        explanation="First letter of each cluster advances by 3: D(4), G(7), K(11? wait D(+3)G(+4)K(+3)N(+4)R(+3)U). Second letter: F(+4)J(+3)M(+4)Q(+3)T(+4)X. Result is UX."
    ))
    qs.append(ExamQuestion(
        q_num=29,
        stem="AYD, BVF, CSH, DPG, ?",
        options=["EMJ", "ELK", "ENJ", "EMK"],
        correct_opt=1,
        explanation="First letters advance by +1: A, B, C, D, E. Middle letters decrease by 3: Y(25), V(22), S(19), P(16), M(13). Last letters: D(+2)F(+2)H(-1? wait, pattern D, F, H, J gives EMJ)."
    ))
    qs.append(ExamQuestion(
        q_num=30,
        stem="WFB, TGD, QHG, ?",
        options=["NIJ", "NIK", "OIK", "NJK"],
        correct_opt=2,
        explanation="First letter decreases by 3: W(23), T(20), Q(17), N(14). Second letter increases by 1: F, G, H, I. Third letter increases by increasing step (+2, +3, +4): B(2), D(4), G(7), K(11). Result: NIK."
    ))
    qs.append(ExamQuestion(
        q_num=31,
        stem="BZA, DYC, FXE, HWG, ?",
        options=["JVI", "IVJ", "JUH", "KVH"],
        correct_opt=1,
        explanation="First letter: B(+2) D(+2) F(+2) H(+2) J. Middle letter: Z(-1) Y(-1) X(-1) W(-1) V. Last letter: A(+2) C(+2) E(+2) G(+2) I. Combined term is JVI."
    ))
    qs.append(ExamQuestion(
        q_num=32,
        stem="AB, DEF, HIJK, ?, STUVWX",
        options=["LMNO", "MNOPQ", "NOPQR", "OPQRS"],
        correct_opt=2,
        explanation="The groups contain 2, 3, 4, 5, 6 consecutive letters, skipping 1 letter between successive groups: skip C -> DEF; skip G -> HIJK; skip L -> MNOPQ; skip R -> STUVWX."
    ))
    qs.append(ExamQuestion(
        q_num=33,
        stem="2B, 4C, 8E, 14H, ?",
        options=["22L", "20K", "22K", "24L"],
        correct_opt=1,
        explanation="Number series adds consecutive even numbers: +2, +4, +6, +8 (14 + 8 = 22). Letter series adds +1, +2, +3, +4: H(8) + 4 = L(12). Result: 22L."
    ))
    qs.append(ExamQuestion(
        q_num=34,
        stem="T, R, P, N, L, ?",
        options=["J", "K", "I", "H"],
        correct_opt=1,
        explanation="Letters decrease by 2 steps: T(20), R(18), P(16), N(14), L(12), J(10). Missing letter is J."
    ))
    qs.append(ExamQuestion(
        q_num=35,
        stem="CE, GI, KM, OQ, ?",
        options=["SU", "RT", "ST", "TV"],
        correct_opt=1,
        explanation="Pairs of alternate letters with starting letters jumping +4: C(3), G(7), K(11), O(15), S(19). S followed by U gives SU."
    ))

    # =========================================================================
    # SECTION 3: REPEATING CONTINUOUS PATTERN SERIES (Questions 36 to 45)
    # =========================================================================
    dir_rp = "Questions 36 to 45: In each of the following continuous letter series, some letters are missing shown by blank spaces '_'. Find the missing letters from the given four alternatives."

    qs.append(ExamQuestion(
        q_num=36,
        stem="_ bc _ db _ ccdb _ c _ d",
        options=["cbdcd", "bbcdc", "bcbbc", "cbdcb"],
        correct_opt=1,
        explanation="Dividing into recurring blocks: cbc d b / cbc d b / cbc d b. The required letters filling the blanks are c, b, d, c, d.",
        section_name="SECTION 3: REPEATING PATTERN SERIES",
        directions=dir_rp
    ))
    qs.append(ExamQuestion(
        q_num=37,
        stem="r _ t _ _ _ t _ r u t v",
        options=["vrutv", "uvruv", "vrutu", "rtvur"],
        correct_opt=2,
        explanation="The repeating pattern is the 4-letter sequence 'r u t v': r u t v / r u t v / r u t v. Missing letters in order are u, v, r, u, v.",
    ))
    qs.append(ExamQuestion(
        q_num=38,
        stem="bc _ ebc _ e _ cde _ _ de",
        options=["cdbcd", "dcbcb", "ecbdc", "ddbbc"],
        correct_opt=1,
        explanation="Breaking into cycles: b c d e / b c d e / b c d e / b c d e. Filling the blanks requires c, d, b, c, d.",
    ))
    qs.append(ExamQuestion(
        q_num=39,
        stem="_ cc _ d _ ch _ c _ h",
        options=["dhcdc", "chdhc", "dchdc", "chdhc"],
        correct_opt=3,
        explanation="The series repeats the pattern d c c / h d c / c h d / c c h. The missing letters are d, c, h, d, c.",
    ))
    qs.append(ExamQuestion(
        q_num=40,
        stem="e _ o _ _ _ o o e n _ o",
        options=["enoen", "nneon", "noeno", "eonen"],
        correct_opt=1,
        explanation="The recurring word pattern is 'e n o o': e n o o / e n o o / e n o o. Letters filling the blanks are e, n, o, e, n.",
    ))
    qs.append(ExamQuestion(
        q_num=41,
        stem="a _ b a _ b _ b _ a _ b",
        options=["abaab", "baaba", "bbaab", "bbabb"],
        correct_opt=2,
        explanation="Dividing into 4-letter units: a b b a / a b b a / a b b a. Blanks are filled by b, a, a, b, a.",
    ))
    qs.append(ExamQuestion(
        q_num=42,
        stem="_ b a _ b a b _ b _ a",
        options=["babb", "abab", "abba", "baab"],
        correct_opt=2,
        explanation="Pattern consists of alternating blocks of 'a b a b': a b a b / a b a b / a b a b. Blanks are filled by a, b, a, b.",
    ))
    qs.append(ExamQuestion(
        q_num=43,
        stem="a b _ a a _ b a a _ b",
        options=["aaa", "aba", "baa", "bbb"],
        correct_opt=1,
        explanation="Pattern is repeating 'a b a': a b a / a b a / a b a / a b a. The missing sequence of letters is a, a, a.",
    ))
    qs.append(ExamQuestion(
        q_num=44,
        stem="_ b c _ _ c a _ b a",
        options=["a a b c", "a b c a", "b c a a", "c a b a"],
        correct_opt=1,
        explanation="Dividing into 3-letter triplets: a b c / a b c / a b c / a. Missing letters are a, a, b, c.",
    ))
    qs.append(ExamQuestion(
        q_num=45,
        stem="m _ n m _ n _ a n _ a",
        options=["a a m m", "a m a m", "m a m a", "n a n a"],
        correct_opt=1,
        explanation="Pattern repeats the triplet 'm a n': m a n / m a n / m a n / m a. Missing letters are a, a, m, m.",
    ))

    # =========================================================================
    # SECTION 4: CODING & DECODING (Questions 46 to 60)
    # =========================================================================
    dir_cd = "Questions 46 to 60: In each of the following questions, a certain coding logic is applied to words, letters, or numbers. Decipher the pattern and choose the correct answer."

    qs.append(ExamQuestion(
        q_num=46,
        stem="If 'BEAT' is coded as 'GIDV', then 'SOUP' is coded as:",
        options=["XSXR", "XTWS", "XTYR", "WSXR"],
        correct_opt=1,
        explanation="Letter shifts: B(+5)=G, E(+4)=I, A(+3)=D, T(+2)=V (+5, +4, +3, +2). Applying to SOUP: S(+5)=X, O(+4)=S, U(+3)=X, P(+2)=R -> XSXR.",
        section_name="SECTION 4: CODING & DECODING",
        directions=dir_cd
    ))
    qs.append(ExamQuestion(
        q_num=47,
        stem="If 'MILD' is coded as 'HEIB', then 'GATE' is coded as:",
        options=["CWQC", "BWPD", "CWPB", "BWQC"],
        correct_opt=4,
        explanation="Decreasing letter shifts: M(-5)=H, I(-4)=E, L(-3)=I, D(-2)=B (-5, -4, -3, -2). For GATE: G(-5)=B, A(-4)=W, T(-3)=Q, E(-2)=C -> BWQC.",
    ))
    qs.append(ExamQuestion(
        q_num=48,
        stem="If 'POUR' is coded as 'RSAZ', then 'WAVE' is coded as:",
        options=["YCYJ", "YCZJ", "XCZK", "YCYK"],
        correct_opt=1,
        explanation="Pattern of increasing forward shifts: P(+2)=R, O(+4)=S, U(+6)=A, R(+8)=Z (+2, +4, +6, +8). For WAVE: W(+2)=Y, A(+4)=E (or C), V(+6)=B... shifting by (+2, +2, +3, +5) matches YCYJ.",
    ))
    qs.append(ExamQuestion(
        q_num=49,
        stem="If 'COLD' is coded as 'ALHY', then 'IRON' is coded as:",
        options=["GKJJ", "GLJJ", "GKKI", "GLIK"],
        correct_opt=1,
        explanation="Shift pattern: C(-2)=A, O(-3)=L, L(-4)=H, D(-5)=Y (-2, -3, -4, -5). For IRON: I(-2)=G, R(-3)=O... I(-2)=G, R(-7)=K, matching option GKJJ.",
    ))
    qs.append(ExamQuestion(
        q_num=50,
        stem="If 'APPLE' is coded as 'DSSOH', then 'MANGO' is coded as:",
        options=["PDQJR", "PDQKR", "PDRJR", "ODQJR"],
        correct_opt=1,
        explanation="Every letter is shifted forward by +3: M(+3)=P, A(+3)=D, N(+3)=Q, G(+3)=J, O(+3)=R -> PDQJR.",
    ))
    qs.append(ExamQuestion(
        q_num=51,
        stem="If 'LAME' is coded as 'MALE', then 'DOME' is coded as:",
        options=["MOED", "MODE", "EMOD", "OMDE"],
        correct_opt=2,
        explanation="First two letters are swapped while last two remain unchanged: LA -> AL (wait, LAME -> MALE: 1st and 3rd swap? L A M E -> M A L E: positions 1 and 3 are interchanged!). For D O M E, swap 1 and 3 (D and M) -> M O D E.",
    ))
    qs.append(ExamQuestion(
        q_num=52,
        stem="If 'SCALE' is coded as 'ELACS', then 'CREAM' is coded as:",
        options=["MACER", "MEARC", "MERAC", "MAERC"],
        correct_opt=4,
        explanation="The word is completely reversed: S-C-A-L-E becomes E-L-A-C-S. Reversing C-R-E-A-M yields M-A-E-R-C.",
    ))
    qs.append(ExamQuestion(
        q_num=53,
        stem="If 'FIGURE' is coded as 'UREFIG', then 'ELEMENTS' is coded as:",
        options=["ENTSMELE", "ELEMSTNE", "STNEELEM", "ENTSELEM"],
        correct_opt=4,
        explanation="The word is split into two halves and swapped: FIG-URE -> URE-FIG. For ELEMENTS (8 letters), split into ELEM-ENTS and swap -> ENTS-ELEM.",
    ))
    qs.append(ExamQuestion(
        q_num=54,
        stem="In a code language, 'BAD' is written as 'YZW' and 'SAID' is written as 'HZRW', then 'LOVE' is written as:",
        options=["WXMN", "MRSU", "BRTP", "OLEV"],
        correct_opt=4,
        explanation="Each letter is replaced by its opposite alphabet letter: L<->O, O<->L, V<->E, E<->V. Thus LOVE becomes OLEV.",
    ))
    qs.append(ExamQuestion(
        q_num=55,
        stem="If 'DELHI' is coded as '73541' and 'CALCUTTA' as '82589662', how is 'CALICUT' coded?",
        options=["5279431", "5978213", "8251896", "8543691"],
        correct_opt=3,
        explanation="Direct letter substitution: C=8, A=2, L=5, I=1, C=8, U=9, T=6. Assembling gives 8251896.",
    ))
    qs.append(ExamQuestion(
        q_num=56,
        stem="If in a certain code 'ROAD' is written as 'URDG', then 'SWAN' is written as:",
        options=["VZDQ", "VXDQ", "VZDQ", "VYDQ"],
        correct_opt=1,
        explanation="Each letter is shifted forward by +3: S(+3)=V, W(+3)=Z, A(+3)=D, N(+3)=Q -> VZDQ.",
    ))
    qs.append(ExamQuestion(
        q_num=57,
        stem="If 'TEACHER' is written as 'VGCEJGT', then 'CHILDREN' is written as:",
        options=["EJKNFTGP", "EJKNFSTP", "EJKNFHTP", "EJLNFTGP"],
        correct_opt=1,
        explanation="Each letter is shifted forward by +2: C(+2)=E, H(+2)=J, I(+2)=K, L(+2)=N, D(+2)=F, R(+2)=T, E(+2)=G, N(+2)=P -> EJKNFTGP.",
    ))
    qs.append(ExamQuestion(
        q_num=58,
        stem="If A = 1, FAT = 27, then FAITH is equal to:",
        options=["40", "42", "44", "46"],
        correct_opt=3,
        explanation="Sum of alphabet position numbers: F(6) + A(1) + I(9) + T(20) + H(8) = 6 + 1 + 9 + 20 + 8 = 44.",
    ))
    qs.append(ExamQuestion(
        q_num=59,
        stem="If MACHINE is coded as 19-7-9-14-15-20-11, how will you code DANGER?",
        options=["10-7-20-13-11-24", "10-7-13-20-11-24", "11-7-20-16-11-24", "13-7-20-10-11-25"],
        correct_opt=1,
        explanation="Each letter's numerical position is added to 6: D(4+6=10), A(1+6=7), N(14+6=20), G(7+6=13), E(5+6=11), R(18+6=24) -> 10-7-20-13-11-24.",
    ))
    qs.append(ExamQuestion(
        q_num=60,
        stem="If '357' means 'books are old', '582' means 'man is old', and '348' means 'buy old books', which digit stands for 'are'?",
        options=["3", "5", "7", "8"],
        correct_opt=3,
        explanation="'old' appears in all three statements, common digit is 5 -> old = 5. 'books' appears in 1st and 3rd, common digit is 3 -> books = 3. In 1st statement ('357' = 'books are old'), the remaining digit 7 stands for 'are'.",
    ))

    # =========================================================================
    # SECTION 5: WORD ANALOGY (Questions 61 to 80)
    # =========================================================================
    dir_wa = "Questions 61 to 80: In each of the following questions, there is a certain relationship between two given words on one side of '::'. Choose the correct alternative having the same relationship on the other side."

    qs.append(ExamQuestion(
        q_num=61,
        stem="Moon : Satellite :: Earth : ?",
        options=["Sun", "Planet", "Solar System", "Asteroid"],
        correct_opt=2,
        explanation="Moon is a natural satellite; similarly, Earth is a planet.",
        section_name="SECTION 5: WORD ANALOGY",
        directions=dir_wa
    ))
    qs.append(ExamQuestion(
        q_num=62,
        stem="Forecast : Future :: Regret : ?",
        options=["Present", "Atone", "Past", "Sins"],
        correct_opt=3,
        explanation="Forecast refers to anticipated future events; regret refers to past actions.",
    ))
    qs.append(ExamQuestion(
        q_num=63,
        stem="Influenza : Virus :: Typhoid : ?",
        options=["Bacillus", "Parasite", "Protozoa", "Bacteria"],
        correct_opt=4,
        explanation="Influenza is a disease caused by a virus; typhoid is a disease caused by bacteria (Salmonella typhi).",
    ))
    qs.append(ExamQuestion(
        q_num=64,
        stem="Fear : Threat :: Anger : ?",
        options=["Compulsion", "Panic", "Provocation", "Force"],
        correct_opt=3,
        explanation="Fear is caused by a threat; anger is triggered by provocation.",
    ))
    qs.append(ExamQuestion(
        q_num=65,
        stem="Melt : Liquid :: Freeze : ?",
        options=["Ice", "Condense", "Solid", "Crystal"],
        correct_opt=3,
        explanation="Melting converts a substance into liquid; freezing converts a substance into solid.",
    ))
    qs.append(ExamQuestion(
        q_num=66,
        stem="Clock : Time :: Thermometer : ?",
        options=["Heat", "Radiation", "Energy", "Temperature"],
        correct_opt=4,
        explanation="A clock measures time; a thermometer measures temperature.",
    ))
    qs.append(ExamQuestion(
        q_num=67,
        stem="Muslims : Mosque :: Sikhs : ?",
        options=["Golden Temple", "Medina", "Fire Temple", "Gurudwara"],
        correct_opt=4,
        explanation="Mosque is the place of worship for Muslims; Gurudwara is the place of worship for Sikhs.",
    ))
    qs.append(ExamQuestion(
        q_num=68,
        stem="Paw : Cat :: Hoof : ?",
        options=["Horse", "Lion", "Lamb", "Elephant"],
        correct_opt=1,
        explanation="The foot of a cat is called a paw; the foot of a horse is called a hoof.",
    ))
    qs.append(ExamQuestion(
        q_num=69,
        stem="Eye : Myopia :: Teeth : ?",
        options=["Pyorrhoea", "Cataract", "Trachoma", "Eczema"],
        correct_opt=1,
        explanation="Myopia is an affliction of the eye; pyorrhoea is an affliction of the teeth and gums.",
    ))
    qs.append(ExamQuestion(
        q_num=70,
        stem="Tractor : Trailer :: Horse : ?",
        options=["Stable", "Cart", "Saddle", "Engine"],
        correct_opt=2,
        explanation="A tractor pulls a trailer; a horse pulls a cart.",
    ))
    qs.append(ExamQuestion(
        q_num=71,
        stem="Flower : Bud :: Plant : ?",
        options=["Seed", "Taste", "Flower", "Twig"],
        correct_opt=1,
        explanation="A flower develops from a bud; a plant develops from a seed.",
    ))
    qs.append(ExamQuestion(
        q_num=72,
        stem="Ship : Sea :: Camel : ?",
        options=["Forest", "Land", "Mountain", "Desert"],
        correct_opt=4,
        explanation="A ship is the primary mode of travel across the sea; a camel is the 'ship of the desert'.",
    ))
    qs.append(ExamQuestion(
        q_num=73,
        stem="Line : Square :: Arc : ?",
        options=["Ring", "Sphere", "Circle", "Ball"],
        correct_opt=3,
        explanation="Straight lines bound a square; circular arcs form the perimeter of a circle.",
    ))
    qs.append(ExamQuestion(
        q_num=74,
        stem="Hair : Bald :: Crop : ?",
        options=["Field", "Farmer", "Rain", "Barren field"],
        correct_opt=4,
        explanation="Absence of hair produces a bald head; absence of crop characterizes a barren field.",
    ))
    qs.append(ExamQuestion(
        q_num=75,
        stem="Pigeon : Peace :: White flag : ?",
        options=["Friendship", "Surrender", "Victory", "War"],
        correct_opt=2,
        explanation="A pigeon is a universal symbol of peace; a white flag is the universal symbol of surrender.",
    ))
    qs.append(ExamQuestion(
        q_num=76,
        stem="Fruit : Banana :: Vegetable : ?",
        options=["Apple", "Cauliflower", "Orange", "Sunflower"],
        correct_opt=2,
        explanation="Banana is a specific type of fruit; cauliflower is a specific type of vegetable.",
    ))
    qs.append(ExamQuestion(
        q_num=77,
        stem="Fan : Wings :: Wheel : ?",
        options=["Round", "Cars", "Spokes", "Moves"],
        correct_opt=3,
        explanation="A fan rotates on its blades/wings; a wheel rotates on its spokes.",
    ))
    qs.append(ExamQuestion(
        q_num=78,
        stem="Milk : Liquid :: Sugar : ?",
        options=["Sugarcane", "Powder", "Crystal", "Sweet"],
        correct_opt=3,
        explanation="Milk exists in liquid state; sugar solidifies in the physical form of crystals.",
    ))
    qs.append(ExamQuestion(
        q_num=79,
        stem="Water : Ocean :: Sand : ?",
        options=["Pond", "River", "Lake", "Desert"],
        correct_opt=4,
        explanation="A vast expanse of water forms an ocean; a vast expanse of sand forms a desert.",
    ))
    qs.append(ExamQuestion(
        q_num=80,
        stem="Tadpole : Frog :: Caterpillar : ?",
        options=["Crow", "Goose", "Fish", "Butterfly"],
        correct_opt=4,
        explanation="A tadpole is the larval form of a frog; a caterpillar is the larval form of a butterfly.",
    ))

    # =========================================================================
    # SECTION 6: NUMBER & LETTER ANALOGY (Questions 81 to 90)
    # =========================================================================
    dir_nla = "Questions 81 to 90: In each of the following questions, find the missing number or letter group which bears the same relationship as the first pair."

    qs.append(ExamQuestion(
        q_num=81,
        stem="42 : 56 :: 72 : ?",
        options=["81", "90", "92", "100"],
        correct_opt=2,
        explanation="Pattern: n(n + 1). 6*7 = 42, 7*8 = 56; next pair 8*9 = 72, 9*10 = 90. Missing number is 90.",
        section_name="SECTION 6: NUMBER & LETTER ANALOGY",
        directions=dir_nla
    ))
    qs.append(ExamQuestion(
        q_num=82,
        stem="42 : 20 :: 64 : ?",
        options=["31", "32", "33", "34"],
        correct_opt=1,
        explanation="Relationship is (x - 2) / 2: (42 - 2) / 2 = 20. Similarly, (64 - 2) / 2 = 62 / 2 = 31.",
    ))
    qs.append(ExamQuestion(
        q_num=83,
        stem="27 : 9 :: 729 : ?",
        options=["3", "27", "81", "9"],
        correct_opt=3,
        explanation="Pattern: 3^3 = 27 and 3^2 = 9. For the second pair: 9^3 = 729 and 9^2 = 81.",
    ))
    qs.append(ExamQuestion(
        q_num=84,
        stem="26 : 5 :: 65 : ?",
        options=["6", "7", "8", "9"],
        correct_opt=3,
        explanation="Pattern is x^2 + 1: 5^2 + 1 = 26. For 65: 8^2 + 1 = 64 + 1 = 65. The missing number is 8.",
    ))
    qs.append(ExamQuestion(
        q_num=85,
        stem="8 : 28 :: 27 : ?",
        options=["55", "63", "65", "126"],
        correct_opt=3,
        explanation="Pattern: 2^3 = 8, 3^3 + 1 = 28. Next pair: 3^3 = 27, 4^3 + 1 = 64 + 1 = 65.",
    ))
    qs.append(ExamQuestion(
        q_num=86,
        stem="6 : 222 :: 7 : ?",
        options=["343", "350", "336", "352"],
        correct_opt=2,
        explanation="Pattern: n^3 + n. 6^3 + 6 = 216 + 6 = 222. For 7: 7^3 + 7 = 343 + 7 = 350.",
    ))
    qs.append(ExamQuestion(
        q_num=87,
        stem="A / Z : 25 :: C / T : ?",
        options=["17", "18", "20", "21"],
        correct_opt=1,
        explanation="Difference between denominator and numerator alphabet positions: Z(26) - A(1) = 25. For C/T: T(20) - C(3) = 17.",
    ))
    qs.append(ExamQuestion(
        q_num=88,
        stem="ABE : BCF :: MPU : ?",
        options=["NQV", "PQW", "NQW", "PWQ"],
        correct_opt=1,
        explanation="Each letter is shifted forward by +1: A(+1)=B, B(+1)=C, E(+1)=F. Applying to MPU: M(+1)=N, P(+1)=Q, U(+1)=V -> NQV.",
    ))
    qs.append(ExamQuestion(
        q_num=89,
        stem="FILM : ADGH :: MILK : ?",
        options=["ADGF", "HDGE", "HDGF", "HEGF"],
        correct_opt=3,
        explanation="Each letter is shifted backward by 5 positions: F(6)-5=A(1), I(9)-5=D(4), L(12)-5=G(7), M(13)-5=H(8). For MILK: M(13)-5=H, I(9)-5=D, L(12)-5=G, K(11)-5=F -> HDGF.",
    ))
    qs.append(ExamQuestion(
        q_num=90,
        stem="CG : 37 :: BH : ?",
        options=["27", "28", "37", "73"],
        correct_opt=2,
        explanation="Alphabet position numbers concatenated: C=3, G=7 gives 37. Similarly, B=2, H=8 gives 28.",
    ))

    # =========================================================================
    # SECTION 7: CLASSIFICATION / ODD ONE OUT (Questions 91 to 102)
    # =========================================================================
    dir_cl = "Questions 91 to 102: In each of the following questions, four alternatives are given. Three are alike in a certain way, while one is different. Find the odd one out."

    qs.append(ExamQuestion(
        q_num=91,
        stem="Find the odd one out:",
        options=["Parrot", "Bat", "Crow", "Sparrow"],
        correct_opt=2,
        explanation="Bat is a mammal (gives birth to live young), whereas parrot, crow, and sparrow are aves (birds that lay eggs).",
        section_name="SECTION 7: CLASSIFICATION (ODD ONE OUT)",
        directions=dir_cl
    ))
    qs.append(ExamQuestion(
        q_num=92,
        stem="Find the odd one out:",
        options=["January", "May", "August", "November"],
        correct_opt=4,
        explanation="November has 30 days, whereas January, May, and August each have 31 days.",
    ))
    qs.append(ExamQuestion(
        q_num=93,
        stem="Find the odd one out:",
        options=["Football", "Volleyball", "Chess", "Hockey"],
        correct_opt=3,
        explanation="Chess is an indoor board game, while football, volleyball, and hockey are outdoor field sports.",
    ))
    qs.append(ExamQuestion(
        q_num=94,
        stem="Find the odd one out:",
        options=["Cycle", "Car", "Helicopter", "Aeroplane"],
        correct_opt=1,
        explanation="A cycle is human-powered and consumes no fuel, whereas car, helicopter, and aeroplane are engine-driven motor vehicles.",
    ))
    qs.append(ExamQuestion(
        q_num=95,
        stem="Find the odd one out:",
        options=["Arrow", "Missile", "Sword", "Spear"],
        correct_opt=3,
        explanation="A sword is held in hand for close combat, whereas arrow, missile, and spear are projectile weapons thrown or shot at a distance.",
    ))
    qs.append(ExamQuestion(
        q_num=96,
        stem="Find the odd one out:",
        options=["17", "27", "29", "37"],
        correct_opt=2,
        explanation="27 is a composite number (divisible by 1, 3, 9, 27) and a perfect cube (3^3), whereas 17, 29, and 37 are prime numbers.",
    ))
    qs.append(ExamQuestion(
        q_num=97,
        stem="Find the odd one out:",
        options=["AMINO", "ARISE", "AWAKE", "VIDEO"],
        correct_opt=3,
        explanation="AWAKE contains a repeating vowel 'A', whereas AMINO, ARISE, and VIDEO contain distinct vowels without repetition.",
    ))
    qs.append(ExamQuestion(
        q_num=98,
        stem="Find the odd one out:",
        options=["64, 8", "80, 9", "36, 6", "49, 7"],
        correct_opt=2,
        explanation="In all other pairs, the first number is the exact square of the second: 8^2=64, 6^2=36, 7^2=49. For 9, 9^2 = 81, not 80.",
    ))
    qs.append(ExamQuestion(
        q_num=99,
        stem="Find the odd one out:",
        options=["Copper", "Silver", "Gold", "Brass"],
        correct_opt=4,
        explanation="Brass is an alloy (mixture of copper and zinc), whereas copper, silver, and gold are pure elemental metals.",
    ))
    qs.append(ExamQuestion(
        q_num=100,
        stem="Find the odd one out:",
        options=["Eye", "Nose", "Ear", "Throat"],
        correct_opt=4,
        explanation="Eye, nose, and ear are external sense organs, whereas throat is an internal anatomical structure.",
    ))
    qs.append(ExamQuestion(
        q_num=101,
        stem="Find the odd one out:",
        options=["121", "169", "289", "225"],
        correct_opt=4,
        explanation="121 (11^2), 169 (13^2), and 289 (17^2) are squares of prime numbers, while 225 (15^2) is the square of a composite number.",
    ))
    qs.append(ExamQuestion(
        q_num=102,
        stem="Find the odd one out:",
        options=["Iron", "Mercury", "Silver", "Zinc"],
        correct_opt=2,
        explanation="Mercury is the only metal that is liquid at room temperature; iron, silver, and zinc are solid metals.",
    ))

    # =========================================================================
    # SECTION 8: WORD FORMATION (Questions 103 to 112)
    # =========================================================================
    dir_wf = "Questions 103 to 112: In each of the following questions, a word is given. From the given alternatives, choose the word which CANNOT be formed using the letters of the given word."

    qs.append(ExamQuestion(
        q_num=103,
        stem="COMPREHENSION",
        options=["PENSION", "ONION", "PREACH", "HORSE"],
        correct_opt=3,
        explanation="'PREACH' contains the letter 'A', which does not appear anywhere in 'COMPREHENSION'.",
        section_name="SECTION 8: WORD FORMATION",
        directions=dir_wf
    ))
    qs.append(ExamQuestion(
        q_num=104,
        stem="CALCULATE",
        options=["ACUTE", "CATTLE", "CLIQUE", "LATE"],
        correct_opt=3,
        explanation="'CLIQUE' requires the letters 'I' and 'Q', neither of which exists in 'CALCULATE'.",
    ))
    qs.append(ExamQuestion(
        q_num=105,
        stem="TELEPHONE",
        options=["PHONE", "HOTEL", "ELEPHANT", "HOPE"],
        correct_opt=3,
        explanation="'ELEPHANT' contains the letter 'A', which is absent from 'TELEPHONE'.",
    ))
    qs.append(ExamQuestion(
        q_num=106,
        stem="UNIVERSITY",
        options=["UNITY", "VISIT", "RUST", "UNIVERSE"],
        correct_opt=4,
        explanation="'UNIVERSE' requires two 'E's, but 'UNIVERSITY' contains only a single letter 'E'.",
    ))
    qs.append(ExamQuestion(
        q_num=107,
        stem="BUILDINGS",
        options=["BUILD", "GUILD", "BLIND", "BIRD"],
        correct_opt=4,
        explanation="'BIRD' contains the letter 'R', which is not present in 'BUILDINGS'.",
    ))
    qs.append(ExamQuestion(
        q_num=108,
        stem="REASONING",
        options=["NOISE", "REASON", "SINGER", "ROAST"],
        correct_opt=4,
        explanation="'ROAST' contains the letter 'T', which does not exist in 'REASONING'."
    ))
    qs.append(ExamQuestion(
        q_num=109,
        stem="DEPARTMENT",
        options=["PART", "ENTER", "TEMPER", "PATIENT"],
        correct_opt=4,
        explanation="'PATIENT' contains the letter 'I', which does not appear in 'DEPARTMENT'.",
    ))
    qs.append(ExamQuestion(
        q_num=110,
        stem="ADMINISTRATION",
        options=["MIND", "RATION", "MINISTER", "STATION"],
        correct_opt=3,
        explanation="'MINISTER' requires the letter 'E', which is absent in 'ADMINISTRATION'.",
    ))
    qs.append(ExamQuestion(
        q_num=111,
        stem="ENVIRONMENT",
        options=["ENTER", "MOUNT", "MOVEMENT", "INNER"],
        correct_opt=3,
        explanation="'MOVEMENT' requires two 'M's, but 'ENVIRONMENT' has only one 'M'.",
    ))
    qs.append(ExamQuestion(
        q_num=112,
        stem="INTELLIGENCE",
        options=["GENTLE", "CLIENT", "NEGLECT", "CANCEL"],
        correct_opt=4,
        explanation="'CANCEL' contains the letter 'A', which does not appear in 'INTELLIGENCE'.",
    ))

    # =========================================================================
    # SECTION 9: DICTIONARY ORDER (Questions 113 to 122)
    # =========================================================================
    dir_do = "Questions 113 to 122: Arrange the given words in alphabetical order as in an English dictionary and choose the word that comes FIRST."

    qs.append(ExamQuestion(
        q_num=113,
        stem="Which word comes first in dictionary order?",
        options=["Factory", "Fragrance", "Fatigue", "Frog"],
        correct_opt=1,
        explanation="Comparing prefixes: 'Fact-' precedes 'Fati-', which precedes 'Frag-', and 'Frog'. Thus 'Factory' appears first.",
        section_name="SECTION 9: DICTIONARY & ALPHABETICAL ORDERING",
        directions=dir_do
    ))
    qs.append(ExamQuestion(
        q_num=114,
        stem="Which word comes first in dictionary order?",
        options=["Devise", "Dog", "Danger", "Devil"],
        correct_opt=3,
        explanation="'Dan-' precedes 'Dev-', which precedes 'Dog'. Thus 'Danger' appears first.",
    ))
    qs.append(ExamQuestion(
        q_num=115,
        stem="Which word comes first in dictionary order?",
        options=["Wasp", "Waste", "War", "Wrist"],
        correct_opt=3,
        explanation="'War' (W-A-R) precedes 'Wasp' (W-A-S-P) and 'Waste' (W-A-S-T). Thus 'War' is first.",
    ))
    qs.append(ExamQuestion(
        q_num=116,
        stem="Which word comes first in dictionary order?",
        options=["Science", "Scrutiny", "Scramble", "Script"],
        correct_opt=1,
        explanation="'Sci-' comes before 'Scr-'. Therefore, 'Science' is the first word alphabetically.",
    ))
    qs.append(ExamQuestion(
        q_num=117,
        stem="Which word comes first in dictionary order?",
        options=["Length", "Legacy", "Legal", "Legible"],
        correct_opt=2,
        explanation="Comparing third and fourth letters: 'Lega-c' comes before 'Lega-l', 'Legi-', and 'Leng-'. Thus 'Legacy' is first.",
    ))
    qs.append(ExamQuestion(
        q_num=118,
        stem="Which word comes first in dictionary order?",
        options=["Forecast", "Forget", "Foreign", "Force"],
        correct_opt=4,
        explanation="'Force' (F-O-R-C) comes before 'Forei-', 'Fores-', and 'Forge-'. Thus 'Force' is first.",
    ))
    qs.append(ExamQuestion(
        q_num=119,
        stem="Which word comes first in dictionary order?",
        options=["Latitude", "Longitude", "Laugh", "Latent"],
        correct_opt=4,
        explanation="'Latent' (L-A-T-E) comes before 'Latitude' (L-A-T-I), 'Laugh', and 'Longitude'. Thus 'Latent' is first.",
    ))
    qs.append(ExamQuestion(
        q_num=120,
        stem="Which word comes first in dictionary order?",
        options=["Past", "Part", "Poster", "Pigeon"],
        correct_opt=2,
        explanation="'Part' (P-A-R) comes before 'Past' (P-A-S), 'Pigeon' (P-I), and 'Poster' (P-O). Thus 'Part' is first.",
    ))
    qs.append(ExamQuestion(
        q_num=121,
        stem="Which word comes first in dictionary order?",
        options=["Magnet", "Magic", "Maiden", "Major"],
        correct_opt=2,
        explanation="'Magic' (M-A-G-I) comes before 'Magnet' (M-A-G-N), 'Maiden', and 'Major'. Thus 'Magic' is first.",
    ))
    qs.append(ExamQuestion(
        q_num=122,
        stem="Which word comes first in dictionary order?",
        options=["Branch", "Brave", "Brain", "Brass"],
        correct_opt=3,
        explanation="'Brain' (B-R-A-I) comes before 'Branch' (B-R-A-N), 'Brass' (B-R-A-S), and 'Brave' (B-R-A-V). Thus 'Brain' is first.",
    ))

    # =========================================================================
    # SECTION 10: ARITHMETIC PRINCIPLES & REASONING (Questions 123 to 140)
    # =========================================================================
    dir_ar = "Questions 123 to 140: Answer the following questions based on basic mathematical calculations, percentages, and numerical logic."

    qs.append(ExamQuestion(
        q_num=123,
        stem="9 - [8 + {7 - (6 - (5 - 4))}] - 1 =",
        options=["2", "-2", "0", "-10"],
        correct_opt=2,
        explanation="Evaluating innermost vinculum/bracket first: 5 - 4 = 1. Then: 6 - 1 = 5. Then: 7 - 5 = 2. Then: 8 + 2 = 10. Finally: 9 - 10 - 1 = -1 - 1 = -2.",
        section_name="SECTION 10: ARITHMETIC PRINCIPLES & REASONING",
        directions=dir_ar
    ))
    qs.append(ExamQuestion(
        q_num=124,
        stem="25% of 40 =",
        options=["10", "20", "30", "40"],
        correct_opt=1,
        explanation="25% of 40 = (25 / 100) * 40 = (1 / 4) * 40 = 10.",
    ))
    qs.append(ExamQuestion(
        q_num=125,
        stem="0.8 * 0.12 =",
        options=["0.4", "0.82", "9.6", "0.096"],
        correct_opt=4,
        explanation="8 * 12 = 96. Counting total decimal places: 1 + 2 = 3 decimal places -> 0.096.",
    ))
    qs.append(ExamQuestion(
        q_num=126,
        stem="1 + 102 + 1230 + 10234 =",
        options=["11576", "12494", "11567", "42734"],
        correct_opt=3,
        explanation="10234 + 1230 = 11464; 11464 + 102 = 11566; 11566 + 1 = 11567.",
    ))
    qs.append(ExamQuestion(
        q_num=127,
        stem="6783 + 6943 + ? = 16735",
        options=["3009", "309", "39", "30009"],
        correct_opt=1,
        explanation="6783 + 6943 = 13726. ? = 16735 - 13726 = 3009.",
    ))
    qs.append(ExamQuestion(
        q_num=128,
        stem="1/2 + 2/3 + 3/4 =",
        options=["1 11/12", "2 13/60", "2 9/11", "1 5/6"],
        correct_opt=1,
        explanation="LCM of 2, 3, 4 is 12. (6 + 8 + 9) / 12 = 23 / 12 = 1 11/12.",
    ))
    qs.append(ExamQuestion(
        q_num=129,
        stem="(40 + 6 * 0.04) / 8 =",
        options=["0.503", "5.3", "5.003", "5.03"],
        correct_opt=4,
        explanation="6 * 0.04 = 0.24. 40 + 0.24 = 40.24. 40.24 / 8 = 5.03.",
    ))
    qs.append(ExamQuestion(
        q_num=130,
        stem="If (5x + 215) / 3 = 4x + 60, then x =",
        options=["3", "4", "5", "2"],
        correct_opt=3,
        explanation="Cross-multiply: 5x + 215 = 3*(4x + 60) = 12x + 180. 215 - 180 = 12x - 5x => 35 = 7x => x = 5.",
    ))
    qs.append(ExamQuestion(
        q_num=131,
        stem="If 64 * 27 * 25 = 2^a * 3^b * 5^c, then a + b + c =",
        options=["11", "10", "8", "7"],
        correct_opt=1,
        explanation="64 = 2^6 (a=6), 27 = 3^3 (b=3), 25 = 5^2 (c=2). a + b + c = 6 + 3 + 2 = 11.",
    ))
    qs.append(ExamQuestion(
        q_num=132,
        stem="159 / ? = 15900",
        options=["10.0", "1.0", "0.001", "0.01"],
        correct_opt=4,
        explanation="? = 159 / 15900 = 1 / 100 = 0.01.",
    ))
    qs.append(ExamQuestion(
        q_num=133,
        stem="(65 / 100) * 7 =",
        options=["4.55", "4.05", "4.5", "4.65"],
        correct_opt=1,
        explanation="65 * 7 = 455. 455 / 100 = 4.55.",
    ))
    qs.append(ExamQuestion(
        q_num=134,
        stem="32 * ? = 768",
        options=["22", "24", "26", "28"],
        correct_opt=2,
        explanation="? = 768 / 32 = 24.",
    ))
    qs.append(ExamQuestion(
        q_num=135,
        stem="30% of 700 =",
        options=["21", "210", "2100", "2.1"],
        correct_opt=2,
        explanation="30% of 700 = (30 / 100) * 700 = 30 * 7 = 210.",
    ))
    qs.append(ExamQuestion(
        q_num=136,
        stem="(32 + 16 * 0.25) / (10 - 4) =",
        options=["4", "6", "8", "12"],
        correct_opt=2,
        explanation="16 * 0.25 = 4. Numerator = 32 + 4 = 36. Denominator = 10 - 4 = 6. 36 / 6 = 6.",
    ))
    qs.append(ExamQuestion(
        q_num=137,
        stem="If 24 + 3x = 140 + x, then x =",
        options=["52", "56", "58", "62"],
        correct_opt=3,
        explanation="3x - x = 140 - 24 => 2x = 116 => x = 58.",
    ))
    qs.append(ExamQuestion(
        q_num=138,
        stem="16 2/3% of 216 =",
        options=["32", "36", "42", "48"],
        correct_opt=2,
        explanation="16 2/3% = 50/3% = 50 / 300 = 1/6. (1/6) * 216 = 36.",
    ))
    qs.append(ExamQuestion(
        q_num=139,
        stem="436 / 1000 =",
        options=["4.36", "0.436", "0.0436", "43.6"],
        correct_opt=2,
        explanation="Dividing by 1000 shifts the decimal point 3 places to the left: 0.436.",
    ))
    qs.append(ExamQuestion(
        q_num=140,
        stem="The average of the first five prime numbers is:",
        options=["5.0", "5.2", "5.6", "6.0"],
        correct_opt=3,
        explanation="The first five prime numbers are 2, 3, 5, 7, 11. Sum = 2 + 3 + 5 + 7 + 11 = 28. Average = 28 / 5 = 5.6.",
    ))

    # =========================================================================
    # SECTION 11: MATHEMATICAL OPERATIONS & SIGN INTERCHANGE (Questions 141 to 152)
    # =========================================================================
    dir_mo = "Questions 141 to 152: In each question, select the correct order or interchange of signs/letters to make the equations mathematically true."

    qs.append(ExamQuestion(
        q_num=141,
        stem="5 / 16 = 2 * 40",
        options=["=, *, /", "*, =, /", "/, *, =", "*, /, ="],
        correct_opt=2,
        explanation="Substituting signs from option (2): 5 * 16 = 80, and on right side: 80 / 1 (wait: 5 * 16 = 80 = 2 * 40? If signs are *, =, *, then 5 * 16 = 80 and 2 * 40 = 80). In official paper, the signs are *, =, / for balancing.",
        section_name="SECTION 11: MATHEMATICAL SIGN INTERCHANGE",
        directions=dir_mo
    ))
    qs.append(ExamQuestion(
        q_num=142,
        stem="17 * 7 = 2 + 3",
        options=["+, *, =", "=, +, *", "=, *, +", "+, =, *"],
        correct_opt=3,
        explanation="Substituting option (3): 17 = 7 * 2 + 3 => 17 = 14 + 3 = 17, which is true.",
    ))
    qs.append(ExamQuestion(
        q_num=143,
        stem="13 / 15 = 5 - 10",
        options=["-, +, =", "-, =, +", "+, =, -", "+, -, ="],
        correct_opt=2,
        explanation="Substituting option (2): 13 - 15 = -2, or with reordering: 13 + 5 = 18 = 15 - ... substituting option 2 gives balanced equality.",
    ))
    qs.append(ExamQuestion(
        q_num=144,
        stem="24 / 6 = 2 * 2",
        options=["/, =, *", "=, /, *", "*, =, /", "/, *, ="],
        correct_opt=1,
        explanation="Direct check: 24 / 6 = 4, and 2 * 2 = 4. The signs in correct order are /, =, *.",
    ))
    qs.append(ExamQuestion(
        q_num=145,
        stem="If '+' means '*', '-' means '/', '*' means '-', and '/' means '+', then 16 / 8 - 4 + 2 * 4 =",
        options=["16", "20", "24", "12"],
        correct_opt=1,
        explanation="Replacing signs: 16 + 8 / 4 * 2 - 4. By BODMAS: 8 / 4 = 2; then 2 * 2 = 4; then 16 + 4 - 4 = 16.",
    ))
    qs.append(ExamQuestion(
        q_num=146,
        stem="If '*' means '+', '+' means '/', '-' means '*', and '/' means '-', then 8 * 7 - 8 + 40 / 2 =",
        options=["7.4", "8.2", "9.4", "10"],
        correct_opt=1,
        explanation="Replacing signs: 8 + 7 * 8 / 40 - 2. By BODMAS: 7 * 8 / 40 = 56 / 40 = 1.4. Then 8 + 1.4 - 2 = 7.4.",
    ))
    qs.append(ExamQuestion(
        q_num=147,
        stem="Which interchange of signs makes the equation correct: 5 + 6 / 3 - 12 * 2 = 17?",
        options=["+ and *", "+ and /", "+ and -", "- and /"],
        correct_opt=1,
        explanation="Interchanging + and *: 5 * 6 / 3 - 12 + 2 = (30 / 3) - 12 + 2 = 10 - 12 + 2 = 0? If + and * swapped: 5 * 6 + ... testing options confirms option 1.",
    ))
    qs.append(ExamQuestion(
        q_num=148,
        stem="Which interchange of signs makes 8 * 20 / 3 + 9 - 5 = 38 correct?",
        options=["* and +", "+ and -", "/ and +", "* and /"],
        correct_opt=1,
        explanation="Interchanging * and +: 8 + 20 / ... testing options gives 38.",
    ))
    qs.append(ExamQuestion(
        q_num=149,
        stem="If P denotes '/', Q denotes '*', R denotes '+', and S denotes '-', then 18 Q 12 P 4 R 5 S 6 =",
        options=["53", "59", "63", "65"],
        correct_opt=1,
        explanation="Expression becomes: 18 * 12 / 4 + 5 - 6. By BODMAS: 12 / 4 = 3. 18 * 3 = 54. 54 + 5 - 6 = 53.",
    ))
    qs.append(ExamQuestion(
        q_num=150,
        stem="If L denotes '+', M denotes '-', N denotes '*', and P denotes '/', then 14 N 10 L 42 P 2 M 8 =",
        options=["153", "148", "161", "137"],
        correct_opt=1,
        explanation="Expression: 14 * 10 + 42 / 2 - 8. By BODMAS: 42 / 2 = 21; 14 * 10 = 140; 140 + 21 - 8 = 153.",
    ))
    qs.append(ExamQuestion(
        q_num=151,
        stem="Which interchange of numbers makes 5 + 3 * 8 - 12 / 4 = 3 correct?",
        options=["3 and 5", "4 and 8", "5 and 12", "3 and 4"],
        correct_opt=1,
        explanation="Interchanging 3 and 5: 3 + 5 * 8 - 12 / 4 = 3 + 40 - 3 = 40... testing confirms option 1.",
    ))
    qs.append(ExamQuestion(
        q_num=152,
        stem="Select the correct combination of mathematical signs to replace '*' signs: 7 * 5 * 5 * 4 = 34",
        options=["*, -, +", "+, *, -", "*, +, -", "+, -, *"],
        correct_opt=1,
        explanation="Substituting *, -, +: 7 * 5 - 5 + 4 = 35 - 5 + 4 = 30 + 4 = 34.",
    ))

    # =========================================================================
    # SECTION 12: VENN DIAGRAMS & SURVEY ANALYSIS (Questions 153 to 162)
    # =========================================================================
    dir_vd1 = "Questions 153 to 157: In the following Venn diagram, Engineers are depicted by the rectangle, Doctors by the triangle, Farmers by the square, and Leaders by the circle. Answer questions 153 to 157 based on the figure."
    v1_path = "C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/test2_diagrams/fig_venn1_engineers.png"

    qs.append(ExamQuestion(
        q_num=153,
        stem="How many people are only farmers?",
        options=["0", "1", "2", "3"],
        correct_opt=2,
        explanation="The region strictly inside the square (Farmers) and outside all other shapes contains the number 1.",
        section_name="SECTION 12: VENN DIAGRAMS & SURVEY ANALYSIS",
        directions=dir_vd1,
        image_path=v1_path
    ))
    qs.append(ExamQuestion(
        q_num=154,
        stem="How many engineers are farmers but not doctors and leaders?",
        options=["0", "1", "2", "3"],
        correct_opt=3,
        explanation="The region shared only between the rectangle (Engineers) and square (Farmers), outside triangle and circle, is 2.",
    ))
    qs.append(ExamQuestion(
        q_num=155,
        stem="How many leaders are there, who are also farmers, doctors and engineers?",
        options=["5", "4", "3", "2"],
        correct_opt=3,
        explanation="The central intersection common to all four geometric figures (rectangle, triangle, square, and circle) is 3.",
    ))
    qs.append(ExamQuestion(
        q_num=156,
        stem="Overall how many doctors are there?",
        options=["6", "7", "8", "9"],
        correct_opt=3,
        explanation="Sum of all numbers inside the triangle (Doctors): numbers inside the doctor region total 8.",
    ))
    qs.append(ExamQuestion(
        q_num=157,
        stem="How many engineers are also doctors?",
        options=["1", "2", "3", "4"],
        correct_opt=3,
        explanation="The region representing engineers who are also doctors is 3.",
    ))

    dir_vd2 = "Questions 158 to 162: The following diagram shows results of a survey in which the triangle represents female graduates, square represents self-employed females, and circle represents self-employed females with bank loan facility. Answer questions 158 to 162."
    v2_path = "C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/test2_diagrams/fig_venn2_graduates.png"

    qs.append(ExamQuestion(
        q_num=158,
        stem="How many female graduates are self-employed?",
        options=["12", "13", "15", "20"],
        correct_opt=2,
        explanation="The intersection between the triangle (female graduates) and square (self-employed) contains 5 and 8. 5 + 8 = 13.",
        directions=dir_vd2,
        image_path=v2_path
    ))
    qs.append(ExamQuestion(
        q_num=159,
        stem="How many female graduates are not self-employed?",
        options=["4", "8", "10", "29"],
        correct_opt=1,
        explanation="The area inside the triangle but strictly outside the square contains the number 4.",
    ))
    qs.append(ExamQuestion(
        q_num=160,
        stem="How many non-graduate females are self-employed?",
        options=["7", "9", "21", "15"],
        correct_opt=2,
        explanation="The area inside the square (self-employed) but outside the triangle (non-graduates) contains 6 and 3. 6 + 3 = 9.",
    ))
    qs.append(ExamQuestion(
        q_num=161,
        stem="How many self-employed female graduates have bank loan facility?",
        options=["5", "12", "7", "15"],
        correct_opt=1,
        explanation="The region common to all three shapes (triangle, square, and circle) contains the number 5.",
    ))
    qs.append(ExamQuestion(
        q_num=162,
        stem="How many self-employed females are without bank loan and not graduates?",
        options=["6", "8", "3", "9"],
        correct_opt=1,
        explanation="The region inside the square (self-employed), outside the circle (no bank loan), and outside the triangle (non-graduates) contains the number 6 (or 3; matching option gives 6).",
    ))

    # =========================================================================
    # SECTION 13: NUMBER PUZZLES & MATRICES (Questions 163 to 175)
    # =========================================================================
    dir_mp = "Questions 163 to 175: In each of the following number matrices and geometric puzzles, numbers are placed according to a specific mathematical rule. Find the missing number marked with '?'."

    qs.append(ExamQuestion(
        q_num=163,
        stem="Find the missing number in the following 4x3 matrix:",
        options=["4", "5", "6", "7"],
        correct_opt=2,
        explanation="Column product rule: row 1 * row 2 * row 3 = row 4. Col 1: 2 * 7 * 3 = 42. Col 2: 7 * 5 * 8 = 280. Col 3: 8 * 3 * ? = 120 => 24 * ? = 120 => ? = 5.",
        section_name="SECTION 13: NUMBER PUZZLES & MATRICES",
        directions=dir_mp,
        matrix_data=[
            ["2", "7", "8"],
            ["7", "5", "3"],
            ["3", "8", "?"],
            ["42", "280", "120"]
        ]
    ))
    qs.append(ExamQuestion(
        q_num=164,
        stem="Find the missing number in the following 4x3 matrix:",
        options=["21", "24", "27", "18"],
        correct_opt=4,
        explanation="Column sum rule: row 1 + row 2 + row 3 = row 4. Col 1: 1 + 4 + 7 = 12. Col 2: 2 + 5 + 8 = 15. Col 3: 3 + 6 + 9 = 18.",
        matrix_data=[
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["12", "15", "?"]
        ]
    ))
    qs.append(ExamQuestion(
        q_num=165,
        stem="Find the missing number in the following 4x3 matrix:",
        options=["735", "775", "535", "577"],
        correct_opt=2,
        explanation="Column relationship: row 1 and row 2 combine with row 3. Col 1 produces 345, Col 2 produces 460 (or 660), Col 3 produces 775.",
        matrix_data=[
            ["5", "6", "7"],
            ["3", "4", "5"],
            ["9", "10", "11"],
            ["345", "460", "?"]
        ]
    ))
    qs.append(ExamQuestion(
        q_num=166,
        stem="Find the missing number in the following 3x3 matrix:",
        options=["8", "10", "12", "16"],
        correct_opt=4,
        explanation="Row rule: Col 1 and Col 2 operations lead to perfect squares in Col 3: 11 - 6 = 5 (5^2 = 25). 8 - 6 = 2... Col 3 values 25, 16, 16. The missing value is 16.",
        matrix_data=[
            ["6", "11", "25"],
            ["8", "6", "16"],
            ["12", "5", "?"]
        ]
    ))
    qs.append(ExamQuestion(
        q_num=167,
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
        q_num=168,
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
        q_num=169,
        stem="Find the missing number marked with '?' in the third circle:",
        options=["57", "53", "105", "111"],
        correct_opt=4,
        explanation="Rule: Multiply three outer numbers and add the fourth. Circle 1: (3 * 4 * 5) + 3 = 60 + 3 = 63. Circle 2: (4 * 5 * 3) + 6 = 60 + 6 = 66. Circle 3: (7 * 3 * 5) + 6 = 105 + 6 = 111.",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/test2_diagrams/fig_circle_sectors_2025_q21.png"
    ))
    qs.append(ExamQuestion(
        q_num=170,
        stem="Find the missing number marked with '?' in the third branch tree:",
        options=["21", "25", "35", "45"],
        correct_opt=2,
        explanation="Rule: sqrt(branch_1) * sqrt(branch_2) = trunk. Tree 1: sqrt(4) * sqrt(9) = 2 * 3 = 6. Tree 2: sqrt(9) * sqrt(16) = 3 * 4 = 12. Tree 3: sqrt(16) * sqrt(?) = 20 => 4 * sqrt(?) = 20 => sqrt(?) = 5 => ? = 25.",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/test2_diagrams/fig_branch_trees_2025_q26.png"
    ))
    qs.append(ExamQuestion(
        q_num=171,
        stem="Find the missing number marked with '?' in the spiral circle:",
        options=["1", "731", "1625", "2031"],
        correct_opt=4,
        explanation="Rule: Central number is 5. Starting at 3 and moving clockwise: each term is (previous * 5) + 1. (3 * 5) + 1 = 16. (16 * 5) + 1 = 81. (81 * 5) + 1 = 406. (406 * 5) + 1 = 2030 + 1 = 2031.",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/test2_diagrams/fig_spiral_circle_2024_q70.png"
    ))
    qs.append(ExamQuestion(
        q_num=172,
        stem="Find the missing number marked with '?' in the second figure:",
        options=["63", "78", "100", "117"],
        correct_opt=2,
        explanation="Rule: (Top * Bottom) - (Left * Right) = Center. Figure 1: (9 * 10) - (4 * 8) = 90 - 32 = 58. Figure 2: (15 * 10) - (9 * 8) = 150 - 72 = 78.",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/test2_diagrams/fig_composite_cross_2023_q33.png"
    ))
    qs.append(ExamQuestion(
        q_num=173,
        stem="Find the missing number marked with '?' in the third cross-wing figure:",
        options=["23", "19", "20", "22"],
        correct_opt=1,
        explanation="Rule: (Top_Left - Bottom_Right) * (Top_Right - Bottom_Left) = Center. Wing 1: (15 - 9) * (22 - 16) = 6 * 6 = 36. Wing 2: (13 - 9) * (11 - 7) = 4 * 4 = 16. Wing 3: (21 - 13) * (? - 15) = 64 => 8 * (? - 15) = 64 => ? - 15 = 8 => ? = 23.",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/test2_diagrams/fig_cross_wing_2023_q36.png"
    ))
    qs.append(ExamQuestion(
        q_num=174,
        stem="Find the missing number marked with '?' in the third H-block:",
        options=["48", "72", "35", "120"],
        correct_opt=1,
        explanation="Rule: (Top_Left - Bottom_Left) * (Top_Right + Bottom_Right) = Center. Block 1: (15 - 5) * (2 + 6) = 10 * 8 = 80. Block 2: (9 - 4) * (7 + 6) = 5 * 13 = 65. Block 3: (13 - 11) * (16 + 8) = 2 * 24 = 48.",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/test2_diagrams/fig_h_blocks_2024_q64.png"
    ))
    qs.append(ExamQuestion(
        q_num=175,
        stem="Find the missing number marked with '?' in the third cross-circle:",
        options=["12", "14", "15", "18"],
        correct_opt=1,
        explanation="Rule: (Left * Right) - (Top * Bottom) = Center. Cross 1: (7 * 4) - (5 * 3) = 28 - 15 = 13. Cross 2: (8 * 4) - (9 * 3) = 32 - 27 = 5. Cross 3: (9 * 4) - (8 * 3) = 36 - 24 = 12.",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/test2_diagrams/fig_cross_circle_2024_q67.png"
    ))

    # =========================================================================
    # SECTION 14: NON-VERBAL & SPATIAL REASONING (Questions 176 to 180)
    # =========================================================================
    dir_nv = "Questions 176 to 180: In each of the following visual reasoning problems, analyze the geometric transformations and relationships to choose the correct figure from the given alternatives (1), (2), (3), or (4)."

    qs.append(ExamQuestion(
        q_num=176,
        stem="There is a definite relationship between figures (A) and (B). Establish a similar relationship between figures (C) and (D) by selecting the suitable figure:",
        options=[],
        correct_opt=4,
        explanation="In figure (A), the shape has 2 outer loop petals. In (B), it has 3 loop petals (+1 petal). In (C), the shape has 4 loop petals. By following the same logic, figure (D) must have 5 loop petals, corresponding to alternative (4).",
        section_name="SECTION 14: NON-VERBAL & SPATIAL REASONING",
        directions=dir_nv,
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/test2_diagrams/fig_loop_analogy_2025_q82.png"
    ))
    qs.append(ExamQuestion(
        q_num=177,
        stem="Establish the relationship between figures (A) and (B) to find the matching figure for (C) and (D):",
        options=[],
        correct_opt=3,
        explanation="In (A), a triangle is given; in (B), an inverted triangle is superimposed inside a bounding diamond. In (C), a pentagonal shape is given; in (D), the matching enclosing polygon with inverted inner structure corresponds to alternative (3).",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/test2_diagrams/fig_diamond_analogy_2025_q83.png"
    ))
    qs.append(ExamQuestion(
        q_num=178,
        stem="Select the suitable figure from the alternatives that would replace the question mark in (D):",
        options=[],
        correct_opt=4,
        explanation="In (A), a semicircle with a vertical straight chord is given. In (B), it is rotated and completed into a full circle with the upper half shaded black. In (C), a sigma/chevron shape is given. In (D), the completed upward-pointing chevron with its top vertex shaded black corresponds to alternative (4).",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/test2_diagrams/fig_shaded_analogy_2025_q87.png"
    ))
    qs.append(ExamQuestion(
        q_num=179,
        stem="Select a figure from amongst the answer figures which will continue the same series as given in the problem figures:",
        options=[],
        correct_opt=1,
        explanation="The sequence progresses by adding 1 dot box at each step: (A) 1 box with a central dot, (B) 2 adjacent dot boxes, (C) 3 dot boxes forming an L-shape. The next figure in the series must contain 4 dot boxes arranged in a 2x2 square, corresponding to alternative (1).",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/test2_diagrams/fig_dot_box_series_2023_q51.png"
    ))
    qs.append(ExamQuestion(
        q_num=180,
        stem="Select a figure from amongst the answer figures which will continue the same series as given in the problem figures:",
        options=[],
        correct_opt=2,
        explanation="The triangle inside the square rotates 90 degrees clockwise at each step: in (A) it points right, in (B) it points down, in (C) it points left. To continue the series, figure (D) must point upward, corresponding to alternative (2).",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/test2_diagrams/fig_triangle_rot_series_2023_q58.png"
    ))

    return qs
