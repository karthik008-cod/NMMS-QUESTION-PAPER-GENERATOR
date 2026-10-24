import re

target_file = r'C:\AGC18052026\ZPHS KISTAPUR\NMMS\mega_180_data.py'

update_code = '''    qs.append(ExamQuestion(
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
        options=["(1)", "(2)", "(3)", "(4)"],
        correct_opt=3,
        explanation="When a vertical mirror is placed to the right of CAP, lateral inversion causes the reflection of each letter: P reflects to reversed P, A remains unchanged, and C reflects to reversed C, corresponding to alternative (3).",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/mega_180/fig_mirror_cap_q71.png"
    ))
    qs.append(ExamQuestion(
        q_num=180,
        stem="Choose the correct mirror-image of figure (X) from the four alternatives given along with it:",
        options=["(1)", "(2)", "(3)", "(4)"],
        correct_opt=1,
        explanation="In the vertical mirror reflection of the word 'bad', lateral inversion gives the exact pattern corresponding to alternative (1).",
        image_path="C:/AGC18052026/ZPHS KISTAPUR/NMMS/output/mega_180/fig_mirror_bad_q74.png"
    ))

    return qs
'''

with open(target_file, 'r', encoding='utf-8') as f:
    orig = f.read()

idx172 = orig.find('    qs.append(ExamQuestion(\n        q_num=172,')
if idx172 == -1:
    idx172 = orig.find('qs.append(ExamQuestion(\n        q_num=172,')
assert idx172 != -1, 'Could not find Q172 start'

new_content = orig[:idx172] + update_code + '\n'
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('mega_180_data.py successfully updated!')
