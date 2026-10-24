"""
High-Resolution Diagram Engine for NMMS Mental Ability Test
Generates clean, printer-friendly, crisp black & white diagrams with bold, large text.
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont

# Font configuration
FONT_PATH = "C:\\Windows\\Fonts\\arialbd.ttf"
if not os.path.exists(FONT_PATH):
    FONT_PATH = "C:\\Windows\\Fonts\\arial.ttf"

def get_font(size: int):
    try:
        return ImageFont.truetype(FONT_PATH, size)
    except Exception:
        return ImageFont.load_default()

def draw_text_centered(draw, pos, text, font, fill="black"):
    bbox = draw.textbbox((0, 0), str(text), font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = pos[0] - w / 2
    y = pos[1] - h / 2 - bbox[1]
    draw.text((x, y), str(text), font=font, fill=fill)

def create_matrix_diagram(grid: list[list[str]], output_path: str):
    """
    Renders a 3x3 or 4x3 number matrix with large bold numbers.
    """
    rows = len(grid)
    cols = len(grid[0])
    cell_w, cell_h = 75, 55
    margin = 15
    img_w = cols * cell_w + 2 * margin
    img_h = rows * cell_h + 2 * margin

    img = Image.new("RGB", (img_w, img_h), "white")
    draw = ImageDraw.Draw(img)
    font = get_font(24)

    # Outer border
    draw.rectangle([margin, margin, img_w - margin, img_h - margin], outline="black", width=3)

    # Vertical lines
    for c in range(1, cols):
        x = margin + c * cell_w
        draw.line([x, margin, x, img_h - margin], fill="black", width=2)

    # Horizontal lines
    for r in range(1, rows):
        y = margin + r * cell_h
        draw.line([margin, y, img_w - margin, y], fill="black", width=2)

    # Numbers
    for r in range(rows):
        for c in range(cols):
            val = str(grid[r][c])
            cx = margin + c * cell_w + cell_w / 2
            cy = margin + r * cell_h + cell_h / 2
            draw_text_centered(draw, (cx, cy), val, font)

    img.save(output_path, "PNG", dpi=(300, 300))
    return output_path

def create_triangles_puzzle(triangles_data: list[tuple], output_path: str):
    """
    triangles_data: list of 3 tuples: [(top, left, right, center), ...]
    Renders 3 triangles side-by-side with vertex numbers and center number.
    """
    count = len(triangles_data)
    tri_w, tri_h = 130, 120
    spacing = 20
    margin = 15
    img_w = count * tri_w + (count - 1) * spacing + 2 * margin
    img_h = tri_h + 2 * margin + 25

    img = Image.new("RGB", (img_w, img_h), "white")
    draw = ImageDraw.Draw(img)
    font_num = get_font(22)
    font_center = get_font(24)

    for i, (top, left, right, center) in enumerate(triangles_data):
        base_x = margin + i * (tri_w + spacing)
        base_y = margin + 20

        # Triangle vertices
        p_top = (base_x + tri_w / 2, base_y + 10)
        p_left = (base_x + 20, base_y + tri_h - 15)
        p_right = (base_x + tri_w - 20, base_y + tri_h - 15)

        draw.polygon([p_top, p_left, p_right], outline="black", width=3)

        # Numbers
        # Top vertex
        draw_text_centered(draw, (p_top[0], p_top[1] - 15), top, font_num)
        # Left vertex
        draw_text_centered(draw, (p_left[0] - 12, p_left[1] + 12), left, font_num)
        # Right vertex
        draw_text_centered(draw, (p_right[0] + 12, p_right[1] + 12), right, font_num)
        # Center number (inside circle or clean)
        c_x = base_x + tri_w / 2
        c_y = base_y + tri_h * 0.62
        draw_text_centered(draw, (c_x, c_y), center, font_center)

    img.save(output_path, "PNG", dpi=(300, 300))
    return output_path

def create_circle_sectors_puzzle(circles_data: list[list[str]], output_path: str):
    """
    circles_data: list of 3 circles, each has 4 sector values [TL, TR, BL, BR].
    """
    count = len(circles_data)
    d = 120
    spacing = 20
    margin = 15
    img_w = count * d + (count - 1) * spacing + 2 * margin
    img_h = d + 2 * margin

    img = Image.new("RGB", (img_w, img_h), "white")
    draw = ImageDraw.Draw(img)
    font = get_font(22)

    for i, sectors in enumerate(circles_data):
        cx = margin + i * (d + spacing) + d / 2
        cy = margin + d / 2
        r = d / 2 - 4

        # Draw circle
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline="black", width=3)
        # Quadrant dividing lines
        draw.line([cx - r, cy, cx + r, cy], fill="black", width=2)
        draw.line([cx, cy - r, cx, cy + r], fill="black", width=2)

        # Numbers in 4 quadrants
        offset = r * 0.52
        draw_text_centered(draw, (cx - offset, cy - offset), sectors[0], font) # TL
        draw_text_centered(draw, (cx + offset, cy - offset), sectors[1], font) # TR
        draw_text_centered(draw, (cx - offset, cy + offset), sectors[2], font) # BL
        draw_text_centered(draw, (cx + offset, cy + offset), sectors[3], font) # BR

    img.save(output_path, "PNG", dpi=(300, 300))
    return output_path

def create_cross_box_puzzle(boxes_data: list[dict], output_path: str):
    """
    boxes_data: list of 3 dicts: {'top': x, 'bottom': x, 'left': x, 'right': x, 'center': x}
    """
    count = len(boxes_data)
    cell = 34
    w_box = cell * 3
    h_box = cell * 3
    spacing = 25
    margin = 15
    img_w = count * w_box + (count - 1) * spacing + 2 * margin
    img_h = h_box + 2 * margin

    img = Image.new("RGB", (img_w, img_h), "white")
    draw = ImageDraw.Draw(img)
    font = get_font(20)

    for i, data in enumerate(boxes_data):
        bx = margin + i * (w_box + spacing)
        by = margin

        # Top box
        draw.rectangle([bx + cell, by, bx + 2*cell, by + cell], outline="black", width=2)
        draw_text_centered(draw, (bx + 1.5*cell, by + 0.5*cell), data['top'], font)

        # Bottom box
        draw.rectangle([bx + cell, by + 2*cell, bx + 2*cell, by + 3*cell], outline="black", width=2)
        draw_text_centered(draw, (bx + 1.5*cell, by + 2.5*cell), data['bottom'], font)

        # Left box
        draw.rectangle([bx, by + cell, bx + cell, by + 2*cell], outline="black", width=2)
        draw_text_centered(draw, (bx + 0.5*cell, by + 1.5*cell), data['left'], font)

        # Right box
        draw.rectangle([bx + 2*cell, by + cell, bx + 3*cell, by + 2*cell], outline="black", width=2)
        draw_text_centered(draw, (bx + 2.5*cell, by + 1.5*cell), data['right'], font)

        # Center box
        draw.rectangle([bx + cell, by + cell, bx + 2*cell, by + 2*cell], outline="black", width=2)
        draw_text_centered(draw, (bx + 1.5*cell, by + 1.5*cell), data['center'], font)

    img.save(output_path, "PNG", dpi=(300, 300))
    return output_path

def create_survey_venn_diagram(regions: dict, output_path: str):
    """
    Renders 3 overlapping shapes: Rectangle, Circle, Triangle with large bold numbers
    placed in clean, open space with generous clearance from all lines.
    """
    w, h = 480, 300
    rx1, ry1, rx2, ry2 = 40, 100, 310, 240
    cx, cy, r = 165, 120, 85
    tri_pts = [(230, 20), (140, 280), (430, 280)]

    img = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(img)
    font = get_font(24)

    # Draw shapes with clear crisp strokes
    draw.rectangle([rx1, ry1, rx2, ry2], outline="black", width=3)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline="black", width=3)
    draw.polygon(tri_pts, outline="black", width=3)

    # Perfectly verified centroid coordinates with zero line overlap
    centers = {
        'outside': (35, 35),
        'rect_only': (76, 204),
        'circle_only': (158, 67),
        'tri_only': (349, 240),
        'rect_circle': (137, 144),
        'circle_tri': (225, 83),
        'rect_tri': (265, 198),
        'all_three': (217, 142)
    }

    for key, pt in centers.items():
        val = str(regions.get(key, ''))
        if val:
            draw_text_centered(draw, pt, val, font)

    img.save(output_path, "PNG", dpi=(300, 300))
    return output_path

def create_concept_venn_options(output_path: str):
    """
    Renders 4 Venn diagram options: (1), (2), (3), (4)
    """
    img_w, img_h = 360, 100
    img = Image.new("RGB", (img_w, img_h), "white")
    draw = ImageDraw.Draw(img)
    font_lbl = get_font(18)

    box_w = 80
    for i in range(4):
        bx = 10 + i * (box_w + 10)
        by = 10
        draw.rectangle([bx, by, bx + box_w, by + 65], outline="black", width=1)
        draw_text_centered(draw, (bx + box_w/2, by + 78), f"({i+1})", font_lbl)

        cx, cy = bx + box_w/2, by + 32
        if i == 0:
            # Concentric
            draw.ellipse([cx - 26, cy - 26, cx + 26, cy + 26], outline="black", width=2)
            draw.ellipse([cx - 17, cy - 17, cx + 17, cy + 17], outline="black", width=2)
            draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], outline="black", width=2)
        elif i == 1:
            # 2 separate inside 1
            draw.ellipse([cx - 32, cy - 22, cx + 32, cy + 22], outline="black", width=2)
            draw.ellipse([cx - 24, cy - 12, cx - 4, cy + 12], outline="black", width=2)
            draw.ellipse([cx + 4, cy - 12, cx + 24, cy + 12], outline="black", width=2)
        elif i == 2:
            # 3 disjoint
            draw.ellipse([cx - 30, cy - 10, cx - 12, cy + 10], outline="black", width=2)
            draw.ellipse([cx - 9, cy - 10, cx + 9, cy + 10], outline="black", width=2)
            draw.ellipse([cx + 12, cy - 10, cx + 30, cy + 10], outline="black", width=2)
        elif i == 3:
            # 2 intersecting circles inside 1 large enclosing circle
            draw.ellipse([cx - 32, cy - 22, cx + 32, cy + 22], outline="black", width=2)
            draw.ellipse([cx - 22, cy - 14, cx + 4, cy + 14], outline="black", width=2)
            draw.ellipse([cx - 4, cy - 14, cx + 22, cy + 14], outline="black", width=2)

    img.save(output_path, "PNG", dpi=(300, 300))
    return output_path

def create_figure_counting_diagram(fig_type: str, output_path: str):
    """
    Renders various geometric figures for analytical counting:
    - 'tri_sub_20': triangle with 4 base partitions, 1 midline (20 triangles)
    - 'tri_sub_12': triangle with 3 base partitions, 1 midline (12 triangles)
    - 'sq_diag_8': 1 square with both diagonals (8 triangles)
    - 'two_sq_diag_18': 2 joined squares side-by-side with diagonals (18 triangles)
    - 'grid_3x3_14': 3x3 square grid without diagonals (14 squares)
    - 'grid_2x2_5': 2x2 square grid without diagonals (5 squares)
    - 'star_10': 5-pointed regular star (10 triangles)
    """
    img_w, img_h = 220, 160
    img = Image.new("RGB", (img_w, img_h), "white")
    draw = ImageDraw.Draw(img)

    if fig_type == 'tri_sub_20':
        top = (110, 20)
        left = (20, 140)
        right = (200, 140)
        draw.polygon([top, left, right], outline="black", width=3)
        draw.line([top[0], top[1], 65, 140], fill="black", width=2)
        draw.line([top[0], top[1], 110, 140], fill="black", width=2)
        draw.line([top[0], top[1], 155, 140], fill="black", width=2)
        mid_l = ((top[0] + left[0])/2, (top[1] + left[1])/2)
        mid_r = ((top[0] + right[0])/2, (top[1] + right[1])/2)
        draw.line([mid_l[0], mid_l[1], mid_r[0], mid_r[1]], fill="black", width=2)

    elif fig_type == 'tri_sub_12':
        top = (110, 20)
        left = (25, 140)
        right = (195, 140)
        draw.polygon([top, left, right], outline="black", width=3)
        # 3 base parts: lines at 1/3 and 2/3
        draw.line([top[0], top[1], 82, 140], fill="black", width=2)
        draw.line([top[0], top[1], 138, 140], fill="black", width=2)
        mid_l = ((top[0] + left[0])/2, (top[1] + left[1])/2)
        mid_r = ((top[0] + right[0])/2, (top[1] + right[1])/2)
        draw.line([mid_l[0], mid_l[1], mid_r[0], mid_r[1]], fill="black", width=2)

    elif fig_type == 'sq_diag_8':
        draw.rectangle([65, 35, 155, 125], outline="black", width=3)
        draw.line([65, 35, 155, 125], fill="black", width=2)
        draw.line([65, 125, 155, 35], fill="black", width=2)

    elif fig_type == 'two_sq_diag_18':
        # Single outer rectangle with middle line to prevent overlap
        draw.rectangle([30, 40, 190, 120], outline="black", width=3)
        draw.line([110, 40, 110, 120], fill="black", width=3)
        # Diagonals of left square
        draw.line([30, 40, 110, 120], fill="black", width=2)
        draw.line([30, 120, 110, 40], fill="black", width=2)
        # Diagonals of right square
        draw.line([110, 40, 190, 120], fill="black", width=2)
        draw.line([110, 120, 190, 40], fill="black", width=2)

    elif fig_type == 'grid_3x3_14':
        draw.rectangle([45, 15, 175, 145], outline="black", width=3)
        s = 130 / 3
        draw.line([45 + s, 15, 45 + s, 145], fill="black", width=2)
        draw.line([45 + 2*s, 15, 45 + 2*s, 145], fill="black", width=2)
        draw.line([45, 15 + s, 175, 15 + s], fill="black", width=2)
        draw.line([45, 15 + 2*s, 175, 15 + 2*s], fill="black", width=2)

    elif fig_type == 'grid_2x2_5':
        draw.rectangle([50, 20, 170, 140], outline="black", width=3)
        draw.line([110, 20, 110, 140], fill="black", width=2)
        draw.line([50, 80, 170, 80], fill="black", width=2)

    elif fig_type == 'star_10':
        # Pentagram with 5 lines
        cx, cy, R = 110, 80, 65
        pts = [(cx + R * math.cos(-math.pi/2 + i * 2 * math.pi / 5), cy + R * math.sin(-math.pi/2 + i * 2 * math.pi / 5)) for i in range(5)]
        p_order = [pts[0], pts[2], pts[4], pts[1], pts[3], pts[0]]
        draw.line(p_order, fill="black", width=3)

    else:
        # Default fallback
        top = (110, 20)
        left = (20, 140)
        right = (200, 140)
        draw.polygon([top, left, right], outline="black", width=3)

    img.save(output_path, "PNG", dpi=(300, 300))
    return output_path

def create_figure_counting_triangle(output_path: str):
    return create_figure_counting_diagram('tri_sub_20', output_path)

def create_figure_counting_square(output_path: str):
    return create_figure_counting_diagram('grid_3x3_14', output_path)

def create_cube_net_diagram(faces: list[str], output_path: str, net_type: str = 'cross'):
    """
    Renders standard unfolded cube net.
    net_type: 'cross' (1-4-1) or 'stepped' (1-3-2)
    """
    img_w, img_h = 240, 180
    img = Image.new("RGB", (img_w, img_h), "white")
    draw = ImageDraw.Draw(img)
    font = get_font(24)

    s = 40
    if net_type == 'cross':
        ox, oy = 40, 10
        layout = [
            (1, 0, faces[0]),
            (0, 1, faces[1]),
            (1, 1, faces[2]),
            (2, 1, faces[3]),
            (3, 1, faces[4]),
            (1, 2, faces[5]),
        ]
    else: # stepped net
        ox, oy = 40, 25
        layout = [
            (0, 0, faces[0]),
            (1, 0, faces[1]),
            (1, 1, faces[2]),
            (2, 1, faces[3]),
            (2, 2, faces[4]),
            (3, 2, faces[5]),
        ]

    for c, r, val in layout:
        x1 = ox + c * s
        y1 = oy + r * s
        draw.rectangle([x1, y1, x1 + s, y1 + s], outline="black", width=3)
        draw_text_centered(draw, (x1 + s/2, y1 + s/2), val, font)

    img.save(output_path, "PNG", dpi=(300, 300))
    return output_path

def create_mirror_image_question(word: str, mirrored_options: list[str], output_path: str):
    """
    Renders problem figure (X) with mirror line and 4 answer options.
    """
    img_w, img_h = 360, 110
    img = Image.new("RGB", (img_w, img_h), "white")
    draw = ImageDraw.Draw(img)
    font_word = get_font(24)
    font_lbl = get_font(18)

    # Problem box
    draw.rectangle([10, 15, 80, 75], outline="black", width=2)
    draw_text_centered(draw, (45, 45), word, font_word)
    draw_text_centered(draw, (45, 92), "(X)", font_lbl)

    # Mirror line
    draw.line([95, 10, 95, 80], fill="black", width=3)
    for y in range(10, 80, 8):
        draw.line([95, y, 100, y + 4], fill="black", width=1)

    # 4 Option boxes
    opt_w = 58
    for i, opt_text in enumerate(mirrored_options):
        bx = 110 + i * (opt_w + 6)
        by = 15
        draw.rectangle([bx, by, bx + opt_w, by + 60], outline="black", width=2)
        draw_text_centered(draw, (bx + opt_w/2, by + 30), opt_text, font_word)
        draw_text_centered(draw, (bx + opt_w/2, by + 78), f"({i+1})", font_lbl)

    img.save(output_path, "PNG", dpi=(300, 300))
    return output_path

def create_nonverbal_series_diagram(steps: list[int], options_data: list[int], output_path: str):
    """
    Renders 4 problem figures + '?' and 4 answer options.
    """
    img_w, img_h = 360, 150
    img = Image.new("RGB", (img_w, img_h), "white")
    draw = ImageDraw.Draw(img)
    font_lbl = get_font(15)

    # Top row: 5 boxes (A, B, C, D, ?)
    bw = 48
    gap = 14
    for i in range(5):
        bx = 15 + i * (bw + gap)
        by = 10
        draw.rectangle([bx, by, bx + bw, by + bw], outline="black", width=2)
        lbl = ["A", "B", "C", "D", "?"][i]
        draw_text_centered(draw, (bx + bw/2, by + bw + 12), f"({lbl})", font_lbl)

        cx, cy = bx + bw/2, by + bw/2
        if i < 4:
            deg = steps[i]
            rad = math.radians(deg)
            ex = cx + 18 * math.cos(rad)
            ey = cy + 18 * math.sin(rad)
            draw.line([cx, cy, ex, ey], fill="black", width=3)
            draw.ellipse([ex - 4, ey - 4, ex + 4, ey + 4], fill="black")
        else:
            draw_text_centered(draw, (cx, cy), "?", get_font(24))

    # Bottom row: 4 answer options (1, 2, 3, 4)
    for i in range(4):
        bx = 35 + i * (bw + gap + 16)
        by = 85
        draw.rectangle([bx, by, bx + bw, by + bw], outline="black", width=2)
        draw_text_centered(draw, (bx + bw/2, by + bw + 12), f"({i+1})", font_lbl)

        cx, cy = bx + bw/2, by + bw/2
        deg = options_data[i]
        rad = math.radians(deg)
        ex = cx + 18 * math.cos(rad)
        ey = cy + 18 * math.sin(rad)
        draw.line([cx, cy, ex, ey], fill="black", width=3)
        draw.ellipse([ex - 4, ey - 4, ex + 4, ey + 4], fill="black")

    img.save(output_path, "PNG", dpi=(300, 300))
    return output_path

def create_dice_question_diagram(dice_faces: list[tuple[str, str, str]], output_path: str):
    """
    Renders 2 or 3 views of a cube/die with labeled faces (Top, Front, Right).
    dice_faces: list of tuples (Top, Front, Right)
    """
    count = len(dice_faces)
    dw = 90
    spacing = 20
    margin = 15
    img_w = count * dw + (count - 1) * spacing + 2 * margin
    img_h = 100

    img = Image.new("RGB", (img_w, img_h), "white")
    draw = ImageDraw.Draw(img)
    font = get_font(18)

    for i, (top_v, front_v, right_v) in enumerate(dice_faces):
        ox = margin + i * (dw + spacing) + 10
        oy = 15

        # Isometric cube points
        p_c = (ox + 35, oy + 40)
        p_t = (ox + 35, oy + 5)
        p_tl = (ox + 5, oy + 22)
        p_tr = (ox + 65, oy + 22)
        p_bl = (ox + 5, oy + 65)
        p_br = (ox + 65, oy + 65)
        p_b = (ox + 35, oy + 82)

        # Top face
        draw.polygon([p_t, p_tr, p_c, p_tl], outline="black", width=2)
        draw_text_centered(draw, (ox + 35, oy + 22), top_v, font)

        # Front-left face
        draw.polygon([p_tl, p_c, p_b, p_bl], outline="black", width=2)
        draw_text_centered(draw, (ox + 20, oy + 52), front_v, font)

        # Front-right face
        draw.polygon([p_c, p_tr, p_br, p_b], outline="black", width=2)
        draw_text_centered(draw, (ox + 50, oy + 52), right_v, font)

    img.save(output_path, "PNG", dpi=(300, 300))
    return output_path

def create_embedded_figure_question(output_path: str, correct_opt: int, motif_type: str = 'Z'):
    """
    Renders an embedded figure question:
    Problem figure (X) on the left, and 4 option figures (1, 2, 3, 4) on the right.
    motif_type can be: 'Z', 'T', 'arrow', 'cross', 'stair'.
    All lines across (X) and all options use strict uniform width=2 (no bold lines in options!).
    """
    img_w, img_h = 360, 110
    img = Image.new("RGB", (img_w, img_h), "white")
    draw = ImageDraw.Draw(img)
    font_lbl = get_font(16)
    W = 2  # Strict uniform line width for all lines!

    # Box (X)
    draw.rectangle([10, 12, 70, 72], outline="black", width=W)
    draw_text_centered(draw, (40, 88), "(X)", font_lbl)

    def draw_motif_x(ox, oy):
        if motif_type == 'Z':
            draw.line([(ox + 16, oy + 18), (ox + 44, oy + 18)], fill="black", width=W)
            draw.line([(ox + 44, oy + 18), (ox + 16, oy + 42)], fill="black", width=W)
            draw.line([(ox + 16, oy + 42), (ox + 44, oy + 42)], fill="black", width=W)
        elif motif_type == 'T':
            # Inverted T (perpendicular)
            draw.line([(ox + 15, oy + 42), (ox + 45, oy + 42)], fill="black", width=W)
            draw.line([(ox + 30, oy + 42), (ox + 30, oy + 18)], fill="black", width=W)
        elif motif_type == 'arrow':
            draw.line([(ox + 18, oy + 18), (ox + 18, oy + 42)], fill="black", width=W)
            draw.line([(ox + 18, oy + 42), (ox + 42, oy + 42)], fill="black", width=W)
            draw.line([(ox + 18, oy + 30), (ox + 30, oy + 42)], fill="black", width=W)
        elif motif_type == 'cross':
            draw.line([(ox + 26, oy + 16), (ox + 26, oy + 44)], fill="black", width=W)
            draw.line([(ox + 14, oy + 30), (ox + 42, oy + 30)], fill="black", width=W)
            draw.line([(ox + 42, oy + 30), (ox + 42, oy + 18)], fill="black", width=W)
        else: # stair
            draw.line([(ox + 14, oy + 42), (ox + 24, oy + 42)], fill="black", width=W)
            draw.line([(ox + 24, oy + 42), (ox + 24, oy + 30)], fill="black", width=W)
            draw.line([(ox + 24, oy + 30), (ox + 34, oy + 30)], fill="black", width=W)
            draw.line([(ox + 34, oy + 30), (ox + 34, oy + 18)], fill="black", width=W)
            draw.line([(ox + 34, oy + 18), (ox + 44, oy + 18)], fill="black", width=W)

    draw_motif_x(10, 12)

    bw = 55
    spacing = 10
    start_x = 95

    def draw_figure_for_option(bx, by, opt_num, is_correct):
        ox, oy = bx + 5, by + 5
        if motif_type == 'Z':
            if is_correct:
                # Rectangle with horizontal lines, vertical sides and both diagonals (contains Z)
                draw.rectangle([ox + 5, oy + 5, ox + 40, oy + 45], outline="black", width=W)
                draw.line([(ox + 5, oy + 5), (ox + 40, oy + 45)], fill="black", width=W)
                draw.line([(ox + 40, oy + 5), (ox + 5, oy + 45)], fill="black", width=W)
            else:
                if opt_num == 1:
                    # Rectangle with opposite diagonal only
                    draw.rectangle([ox + 5, oy + 5, ox + 40, oy + 45], outline="black", width=W)
                    draw.line([(ox + 5, oy + 5), (ox + 40, oy + 45)], fill="black", width=W)
                elif opt_num == 2:
                    # Rectangle with vertical and horizontal bisectors
                    draw.rectangle([ox + 5, oy + 5, ox + 40, oy + 45], outline="black", width=W)
                    draw.line([(ox + 5, oy + 25), (ox + 40, oy + 25)], fill="black", width=W)
                    draw.line([(ox + 22, oy + 5), (ox + 22, oy + 45)], fill="black", width=W)
                else:
                    # Rectangle with horizontal bisector and single diagonal
                    draw.rectangle([ox + 5, oy + 5, ox + 40, oy + 45], outline="black", width=W)
                    draw.line([(ox + 5, oy + 25), (ox + 40, oy + 25)], fill="black", width=W)
                    draw.line([(ox + 5, oy + 5), (ox + 40, oy + 45)], fill="black", width=W)

        elif motif_type == 'T':
            if is_correct:
                # Rectangle with inverted T (horizontal baseline + vertical stem) and upper diagonals
                draw.rectangle([ox + 5, oy + 5, ox + 40, oy + 45], outline="black", width=W)
                draw.line([(ox + 5, oy + 45), (ox + 40, oy + 45)], fill="black", width=W)
                draw.line([(ox + 22, oy + 15), (ox + 22, oy + 45)], fill="black", width=W)
                draw.line([(ox + 5, oy + 15), (ox + 40, oy + 15)], fill="black", width=W)
                draw.line([(ox + 5, oy + 15), (ox + 40, oy + 45)], fill="black", width=W)
            else:
                if opt_num == 1:
                    # Rectangle with diagonals only
                    draw.rectangle([ox + 5, oy + 5, ox + 40, oy + 45], outline="black", width=W)
                    draw.line([(ox + 5, oy + 5), (ox + 40, oy + 45)], fill="black", width=W)
                    draw.line([(ox + 40, oy + 5), (ox + 5, oy + 45)], fill="black", width=W)
                elif opt_num == 2:
                    # Rectangle with upright T (hanging from top)
                    draw.rectangle([ox + 5, oy + 5, ox + 40, oy + 45], outline="black", width=W)
                    draw.line([(ox + 5, oy + 25), (ox + 40, oy + 25)], fill="black", width=W)
                    draw.line([(ox + 22, oy + 5), (ox + 22, oy + 25)], fill="black", width=W)
                else:
                    # Rectangle with vertical bisector and horizontal offset lines
                    draw.rectangle([ox + 5, oy + 5, ox + 40, oy + 45], outline="black", width=W)
                    draw.line([(ox + 22, oy + 5), (ox + 22, oy + 45)], fill="black", width=W)
                    draw.line([(ox + 5, oy + 15), (ox + 40, oy + 15)], fill="black", width=W)
                    draw.line([(ox + 5, oy + 35), (ox + 40, oy + 35)], fill="black", width=W)

        elif motif_type == 'arrow':
            if is_correct:
                # Rectangle containing right-angle corner with diagonal
                draw.rectangle([ox + 5, oy + 5, ox + 40, oy + 45], outline="black", width=W)
                draw.line([(ox + 5, oy + 45), (ox + 40, oy + 5)], fill="black", width=W)
                draw.line([(ox + 5, oy + 25), (ox + 22, oy + 45)], fill="black", width=W)
                draw.line([(ox + 22, oy + 5), (ox + 22, oy + 45)], fill="black", width=W)
            else:
                if opt_num == 1:
                    draw.rectangle([ox + 5, oy + 5, ox + 40, oy + 45], outline="black", width=W)
                    draw.line([(ox + 5, oy + 5), (ox + 40, oy + 45)], fill="black", width=W)
                    draw.line([(ox + 40, oy + 5), (ox + 5, oy + 45)], fill="black", width=W)
                elif opt_num == 2:
                    draw.rectangle([ox + 5, oy + 5, ox + 40, oy + 45], outline="black", width=W)
                    draw.line([(ox + 5, oy + 25), (ox + 40, oy + 25)], fill="black", width=W)
                    draw.line([(ox + 22, oy + 5), (ox + 22, oy + 45)], fill="black", width=W)
                else:
                    draw.rectangle([ox + 5, oy + 5, ox + 40, oy + 45], outline="black", width=W)
                    draw.line([(ox + 5, oy + 15), (ox + 40, oy + 35)], fill="black", width=W)
                    draw.line([(ox + 5, oy + 35), (ox + 40, oy + 15)], fill="black", width=W)

        elif motif_type == 'cross':
            if is_correct:
                draw.rectangle([ox + 3, oy + 3, ox + 42, oy + 47], outline="black", width=W)
                draw.line([(ox + 22, oy + 3), (ox + 22, oy + 47)], fill="black", width=W)
                draw.line([(ox + 8, oy + 25), (ox + 38, oy + 25)], fill="black", width=W)
                draw.line([(ox + 38, oy + 25), (ox + 38, oy + 11)], fill="black", width=W)
                draw.line([(ox + 22, oy + 11), (ox + 38, oy + 11)], fill="black", width=W)
            else:
                if opt_num == 1:
                    draw.rectangle([ox + 3, oy + 3, ox + 42, oy + 47], outline="black", width=W)
                    draw.line([(ox + 22, oy + 3), (ox + 22, oy + 47)], fill="black", width=W)
                    draw.line([(ox + 8, oy + 25), (ox + 38, oy + 25)], fill="black", width=W)
                elif opt_num == 2:
                    draw.rectangle([ox + 3, oy + 3, ox + 42, oy + 47], outline="black", width=W)
                    draw.line([(ox + 22, oy + 3), (ox + 22, oy + 47)], fill="black", width=W)
                    draw.line([(ox + 8, oy + 25), (ox + 38, oy + 25)], fill="black", width=W)
                    draw.line([(ox + 8, oy + 25), (ox + 8, oy + 11)], fill="black", width=W)
                else:
                    draw.rectangle([ox + 3, oy + 3, ox + 42, oy + 47], outline="black", width=W)
                    draw.line([(ox + 3, oy + 3), (ox + 42, oy + 47)], fill="black", width=W)
                    draw.line([(ox + 42, oy + 3), (ox + 3, oy + 47)], fill="black", width=W)

        else: # stair
            if is_correct:
                draw.rectangle([ox + 3, oy + 3, ox + 42, oy + 47], outline="black", width=W)
                draw.line([(ox + 3, oy + 37), (ox + 16, oy + 37)], fill="black", width=W)
                draw.line([(ox + 16, oy + 37), (ox + 16, oy + 25)], fill="black", width=W)
                draw.line([(ox + 16, oy + 25), (ox + 29, oy + 25)], fill="black", width=W)
                draw.line([(ox + 29, oy + 25), (ox + 29, oy + 13)], fill="black", width=W)
                draw.line([(ox + 29, oy + 13), (ox + 42, oy + 13)], fill="black", width=W)
            else:
                if opt_num == 1:
                    draw.rectangle([ox + 3, oy + 3, ox + 42, oy + 47], outline="black", width=W)
                    draw.line([(ox + 3, oy + 37), (ox + 16, oy + 15), (ox + 29, oy + 37), (ox + 42, oy + 15)], fill="black", width=W)
                elif opt_num == 2:
                    draw.rectangle([ox + 3, oy + 3, ox + 42, oy + 47], outline="black", width=W)
                    draw.line([(ox + 3, oy + 25), (ox + 22, oy + 25), (ox + 22, oy + 10)], fill="black", width=W)
                else:
                    draw.rectangle([ox + 3, oy + 3, ox + 42, oy + 47], outline="black", width=W)
                    draw.line([(ox + 3, oy + 18), (ox + 42, oy + 18)], fill="black", width=W)
                    draw.line([(ox + 3, oy + 32), (ox + 42, oy + 32)], fill="black", width=W)

    dist_counter = 1
    for i in range(4):
        bx = start_x + i * (bw + spacing)
        by = 12
        draw.rectangle([bx, by, bx + bw, by + 60], outline="black", width=W)
        draw_text_centered(draw, (bx + bw/2, by + 76), f"({i+1})", font_lbl)

        if i + 1 == correct_opt:
            draw_figure_for_option(bx, by, 0, is_correct=True)
        else:
            draw_figure_for_option(bx, by, dist_counter, is_correct=False)
            dist_counter += 1

    img.save(output_path, "PNG", dpi=(300, 300))
    return output_path

def create_figure_analogy_diagram(output_path: str, correct_opt: int, analogy_type: str = 'invert_dot'):
    """
    Renders non-verbal analogy:
    (A) : (B) :: (C) : (?)
    Options (1), (2), (3), (4)
    analogy_type: 'invert_dot', 'side_inc', 'rotate', 'swap', 'quarter_shading'
    """
    img_w, img_h = 360, 150
    img = Image.new("RGB", (img_w, img_h), "white")
    draw = ImageDraw.Draw(img)
    font_lbl = get_font(15)
    font_sym = get_font(20)

    bw = 48
    top_y = 10
    top_cy = top_y + bw / 2

    def draw_shape(cx, cy, s_type):
        if s_type == 'tri_up':
            draw.polygon([(cx, cy - 15), (cx - 15, cy + 14), (cx + 15, cy + 14)], outline="black", width=2)
        elif s_type == 'tri_down_dot':
            draw.polygon([(cx, cy + 15), (cx - 15, cy - 14), (cx + 15, cy - 14)], outline="black", width=2)
            draw.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill="black")
        elif s_type == 'sq':
            draw.rectangle([cx - 14, cy - 14, cx + 14, cy + 14], outline="black", width=2)
        elif s_type == 'sq_dot':
            draw.rectangle([cx - 14, cy - 14, cx + 14, cy + 14], outline="black", width=2)
            draw.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill="black")
        elif s_type == 'sq_corner_dot':
            draw.rectangle([cx - 14, cy - 14, cx + 14, cy + 14], outline="black", width=2)
            draw.ellipse([cx + 5, cy + 5, cx + 11, cy + 11], fill="black")
        elif s_type == 'sq_diag':
            draw.rectangle([cx - 14, cy - 14, cx + 14, cy + 14], outline="black", width=2)
            draw.line([(cx - 14, cy - 14), (cx + 14, cy + 14)], fill="black", width=2)
        elif s_type == 'pentagon':
            pts = [(cx + 15 * math.cos(-math.pi/2 + i * 2 * math.pi / 5), cy + 15 * math.sin(-math.pi/2 + i * 2 * math.pi / 5)) for i in range(5)]
            draw.polygon(pts, outline="black", width=2)
        elif s_type == 'hexagon':
            pts = [(cx + 15 * math.cos(i * math.pi / 3), cy + 15 * math.sin(i * math.pi / 3)) for i in range(6)]
            draw.polygon(pts, outline="black", width=2)
        elif s_type == 'heptagon':
            pts = [(cx + 15 * math.cos(-math.pi/2 + i * 2 * math.pi / 7), cy + 15 * math.sin(-math.pi/2 + i * 2 * math.pi / 7)) for i in range(7)]
            draw.polygon(pts, outline="black", width=2)
        elif s_type == 'arrow_up':
            draw.line([(cx, cy + 14), (cx, cy - 14)], fill="black", width=2)
            draw.line([(cx - 7, cy - 7), (cx, cy - 14), (cx + 7, cy - 7)], fill="black", width=2)
        elif s_type == 'arrow_right':
            draw.line([(cx - 14, cy), (cx + 14, cy)], fill="black", width=2)
            draw.line([(cx + 7, cy - 7), (cx + 14, cy), (cx + 7, cy + 7)], fill="black", width=2)
        elif s_type == 'arrow_down':
            draw.line([(cx, cy - 14), (cx, cy + 14)], fill="black", width=2)
            draw.line([(cx - 7, cy + 7), (cx, cy + 14), (cx + 7, cy + 7)], fill="black", width=2)
        elif s_type == 'arrow_left':
            draw.line([(cx + 14, cy), (cx - 14, cy)], fill="black", width=2)
            draw.line([(cx - 7, cy - 7), (cx - 14, cy), (cx - 7, cy + 7)], fill="black", width=2)
        elif s_type == 'circle_in_sq':
            draw.rectangle([cx - 14, cy - 14, cx + 14, cy + 14], outline="black", width=2)
            draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], outline="black", width=2)
        elif s_type == 'sq_in_circle':
            draw.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], outline="black", width=2)
            draw.rectangle([cx - 8, cy - 8, cx + 8, cy + 8], outline="black", width=2)
        elif s_type == 'tri_in_circle':
            draw.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], outline="black", width=2)
            draw.polygon([(cx, cy - 9), (cx - 8, cy + 7), (cx + 8, cy + 7)], outline="black", width=2)
        elif s_type == 'circle_in_tri':
            draw.polygon([(cx, cy - 14), (cx - 14, cy + 12), (cx + 14, cy + 12)], outline="black", width=2)
            draw.ellipse([cx - 6, cy - 3, cx + 6, cy + 9], outline="black", width=2)
        elif s_type == 'tri_in_tri':
            draw.polygon([(cx, cy - 15), (cx - 15, cy + 14), (cx + 15, cy + 14)], outline="black", width=2)
            draw.polygon([(cx, cy - 5), (cx - 7, cy + 10), (cx + 7, cy + 10)], outline="black", width=2)
        elif s_type == 'circle_in_circle':
            draw.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], outline="black", width=2)
            draw.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], outline="black", width=2)
        elif s_type == 'circle_sh_tr':
            draw.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], outline="black", width=2)
            draw.pieslice([cx - 14, cy - 14, cx + 14, cy + 14], 270, 360, fill="black")
        elif s_type == 'circle_sh_br':
            draw.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], outline="black", width=2)
            draw.pieslice([cx - 14, cy - 14, cx + 14, cy + 14], 0, 90, fill="black")
        elif s_type == 'sq_sh_tr':
            draw.rectangle([cx - 14, cy - 14, cx + 14, cy + 14], outline="black", width=2)
            draw.rectangle([cx, cy - 14, cx + 14, cy], fill="black")
        elif s_type == 'sq_sh_br':
            draw.rectangle([cx - 14, cy - 14, cx + 14, cy + 14], outline="black", width=2)
            draw.rectangle([cx, cy, cx + 14, cy + 14], fill="black")
        elif s_type == 'sq_sh_bl':
            draw.rectangle([cx - 14, cy - 14, cx + 14, cy + 14], outline="black", width=2)
            draw.rectangle([cx - 14, cy, cx, cy + 14], fill="black")
        elif s_type == 'sq_sh_tl':
            draw.rectangle([cx - 14, cy - 14, cx + 14, cy + 14], outline="black", width=2)
            draw.rectangle([cx - 14, cy - 14, cx, cy], fill="black")
        else:
            draw.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], outline="black", width=2)

    # Top boxes: A : B :: C : ?
    draw.rectangle([10, top_y, 10 + bw, top_y + bw], outline="black", width=2)
    draw_text_centered(draw, (10 + bw/2, top_y + bw + 12), "(A)", font_lbl)
    draw_text_centered(draw, (70, top_cy), ":", font_sym)

    draw.rectangle([82, top_y, 82 + bw, top_y + bw], outline="black", width=2)
    draw_text_centered(draw, (82 + bw/2, top_y + bw + 12), "(B)", font_lbl)
    draw_text_centered(draw, (144, top_cy), "::", font_sym)

    draw.rectangle([156, top_y, 156 + bw, top_y + bw], outline="black", width=2)
    draw_text_centered(draw, (156 + bw/2, top_y + bw + 12), "(C)", font_lbl)
    draw_text_centered(draw, (216, top_cy), ":", font_sym)

    draw.rectangle([228, top_y, 228 + bw, top_y + bw], outline="black", width=2)
    draw_text_centered(draw, (228 + bw/2, top_cy), "?", get_font(24))
    draw_text_centered(draw, (228 + bw/2, top_y + bw + 12), "(?)", font_lbl)

    if analogy_type == 'side_inc':
        draw_shape(10 + bw/2, top_cy, 'tri_up')
        draw_shape(82 + bw/2, top_cy, 'sq')
        draw_shape(156 + bw/2, top_cy, 'pentagon')
        correct_shape = 'hexagon'
        dist_shapes = ['pentagon', 'heptagon', 'sq']
    elif analogy_type == 'rotate':
        draw_shape(10 + bw/2, top_cy, 'arrow_up')
        draw_shape(82 + bw/2, top_cy, 'arrow_right')
        draw_shape(156 + bw/2, top_cy, 'arrow_down')
        correct_shape = 'arrow_left'
        dist_shapes = ['arrow_right', 'arrow_up', 'arrow_down']
    elif analogy_type == 'swap':
        draw_shape(10 + bw/2, top_cy, 'sq_in_circle')
        draw_shape(82 + bw/2, top_cy, 'circle_in_sq')
        draw_shape(156 + bw/2, top_cy, 'tri_in_circle')
        correct_shape = 'circle_in_tri'
        dist_shapes = ['tri_in_circle', 'tri_in_tri', 'circle_in_circle']
    elif analogy_type == 'quarter_shading':
        draw_shape(10 + bw/2, top_cy, 'circle_sh_tr')
        draw_shape(82 + bw/2, top_cy, 'circle_sh_br')
        draw_shape(156 + bw/2, top_cy, 'sq_sh_tr')
        correct_shape = 'sq_sh_br'
        dist_shapes = ['sq_sh_bl', 'sq_sh_tl', 'sq_sh_tr']
    else: # invert_dot
        draw_shape(10 + bw/2, top_cy, 'tri_up')
        draw_shape(82 + bw/2, top_cy, 'tri_down_dot')
        draw_shape(156 + bw/2, top_cy, 'sq')
        correct_shape = 'sq_dot'
        dist_shapes = ['sq', 'sq_corner_dot', 'sq_diag']

    options = list(dist_shapes)
    options.insert(correct_opt - 1, correct_shape)

    start_x = 35
    for i in range(4):
        bx = start_x + i * (bw + 20)
        by = 88
        draw.rectangle([bx, by, bx + bw, by + bw], outline="black", width=2)
        draw_text_centered(draw, (bx + bw/2, by + bw + 12), f"({i+1})", font_lbl)
        draw_shape(bx + bw/2, by + bw/2, options[i])

    img.save(output_path, "PNG", dpi=(300, 300))
    return output_path

