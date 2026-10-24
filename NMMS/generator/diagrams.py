"""
NMMS High-Definition Spotless Diagram Generator
Generates publication-quality, 300+ DPI vector-crisp diagrams with pure #FFFFFF backgrounds,
solid black lines, and zero cutoff/distortion for:
- Dice (2-view, 3-view, unfolded nets)
- 3D Cubes (painted face analysis)
- Clocks (analog dials with precise hand angles)
- Mirror Images (words, codes, geometric figures)
- Water Images (words, codes, geometric figures)
- Paper Folding & Cutting (X, Y, Z fold steps and answer grids)
- Embedded Figures (target X and option figures)
- Dot Situations (overlapping geometric sets with constraint dots)
- Venn Diagrams (Euler-Venn 3-set and 4-set survey diagrams)
- Number Puzzles (circles, spokes, trees, crosses, spirals)
"""

import os
from typing import List, Optional, Tuple, Dict, Any
from PIL import Image
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def ensure_dir(path):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)

# -------------------------------------------------------------
# 1. DICE & NET DIAGRAMS
# -------------------------------------------------------------
def generate_two_dice(d1_faces, d2_faces, filepath, labels=('(i)', '(ii)')):
    """
    Renders two isometric dice side by side.
    d1_faces: [top, front, right]
    d2_faces: [top, front, right]
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(1, 2, figsize=(3.8, 1.9), dpi=300)
    for ax, faces, lbl in zip(axes, [d1_faces, d2_faces], labels):
        ax.set_aspect('equal')
        ax.axis('off')
        
        top = patches.Polygon([[-0.866, 0.5], [0, 1.0], [0.866, 0.5], [0, 0.0]], closed=True, facecolor='white', edgecolor='black', lw=2.2)
        front = patches.Polygon([[-0.866, 0.5], [0, 0.0], [0, -1.0], [-0.866, -0.5]], closed=True, facecolor='white', edgecolor='black', lw=2.2)
        right = patches.Polygon([[0, 0.0], [0.866, 0.5], [0.866, -0.5], [0, -1.0]], closed=True, facecolor='white', edgecolor='black', lw=2.2)
        ax.add_patch(top); ax.add_patch(front); ax.add_patch(right)
        
        ax.text(0, 0.5, str(faces[0]), fontsize=15, fontweight='bold', ha='center', va='center')
        ax.text(-0.433, -0.25, str(faces[1]), fontsize=15, fontweight='bold', ha='center', va='center')
        ax.text(0.433, -0.25, str(faces[2]), fontsize=15, fontweight='bold', ha='center', va='center')
        ax.text(0, -1.25, lbl, fontsize=11, fontweight='bold', ha='center', va='center')
        ax.set_xlim(-1.15, 1.15)
        ax.set_ylim(-1.45, 1.2)
        
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.04)
    plt.close()
    return filepath

def generate_three_dice(d1, d2, d3, filepath, labels=('(i)', '(ii)', '(iii)')):
    """Renders three isometric dice side by side."""
    ensure_dir(filepath)
    fig, axes = plt.subplots(1, 3, figsize=(5.2, 1.8), dpi=300)
    for ax, faces, lbl in zip(axes, [d1, d2, d3], labels):
        ax.set_aspect('equal')
        ax.axis('off')
        
        top = patches.Polygon([[-0.866, 0.5], [0, 1.0], [0.866, 0.5], [0, 0.0]], closed=True, facecolor='white', edgecolor='black', lw=2.0)
        front = patches.Polygon([[-0.866, 0.5], [0, 0.0], [0, -1.0], [-0.866, -0.5]], closed=True, facecolor='white', edgecolor='black', lw=2.0)
        right = patches.Polygon([[0, 0.0], [0.866, 0.5], [0.866, -0.5], [0, -1.0]], closed=True, facecolor='white', edgecolor='black', lw=2.0)
        ax.add_patch(top); ax.add_patch(front); ax.add_patch(right)
        
        ax.text(0, 0.5, str(faces[0]), fontsize=14, fontweight='bold', ha='center', va='center')
        ax.text(-0.433, -0.25, str(faces[1]), fontsize=14, fontweight='bold', ha='center', va='center')
        ax.text(0.433, -0.25, str(faces[2]), fontsize=14, fontweight='bold', ha='center', va='center')
        ax.text(0, -1.25, lbl, fontsize=11, fontweight='bold', ha='center', va='center')
        ax.set_xlim(-1.15, 1.15)
        ax.set_ylim(-1.45, 1.2)
        
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.04)
    plt.close()
    return filepath

def generate_dice_net(grid_layout, filepath):
    """
    grid_layout: dict of (row, col) -> label
    Standard unfolded dice layout.
    """
    ensure_dir(filepath)
    fig, ax = plt.subplots(figsize=(2.8, 2.8), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')
    
    for (r, c), val in grid_layout.items():
        sq = patches.Rectangle((c, -r), 1, 1, facecolor='white', edgecolor='black', lw=2.2)
        ax.add_patch(sq)
        ax.text(c + 0.5, -r + 0.5, str(val), fontsize=15, fontweight='bold', ha='center', va='center')
        
    ax.autoscale_view()
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.05)
    plt.close()
    return filepath

# -------------------------------------------------------------
# 2. 3D CUBE DIAGRAMS (PAINTED FACES)
# -------------------------------------------------------------
def generate_3d_cube(n, filepath):
    """
    Renders an isometric view of an n x n x n cube with visible grid lines.
    """
    ensure_dir(filepath)
    fig, ax = plt.subplots(figsize=(2.5, 2.5), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')
    
    top_pts = np.array([[0, 0.5], [0.866, 1.0], [0, 1.5], [-0.866, 1.0]])
    front_pts = np.array([[-0.866, 1.0], [0, 0.5], [0, -0.5], [-0.866, 0.0]])
    right_pts = np.array([[0, 0.5], [0.866, 1.0], [0.866, 0.0], [0, -0.5]])
    
    ax.add_patch(patches.Polygon(top_pts, closed=True, facecolor='white', edgecolor='black', lw=2.2))
    ax.add_patch(patches.Polygon(front_pts, closed=True, facecolor='white', edgecolor='black', lw=2.2))
    ax.add_patch(patches.Polygon(right_pts, closed=True, facecolor='white', edgecolor='black', lw=2.2))
    
    # Internal division lines
    for step in range(1, n):
        f = step / n
        # Top
        p1 = (1-f)*top_pts[0] + f*top_pts[1]
        p2 = (1-f)*top_pts[3] + f*top_pts[2]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-', lw=1.3)
        p3 = (1-f)*top_pts[0] + f*top_pts[3]
        p4 = (1-f)*top_pts[1] + f*top_pts[2]
        ax.plot([p3[0], p4[0]], [p3[1], p4[1]], 'k-', lw=1.3)
        
        # Front
        p1 = (1-f)*front_pts[0] + f*front_pts[1]
        p2 = (1-f)*front_pts[3] + f*front_pts[2]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-', lw=1.3)
        p3 = (1-f)*front_pts[0] + f*front_pts[3]
        p4 = (1-f)*front_pts[1] + f*front_pts[2]
        ax.plot([p3[0], p4[0]], [p3[1], p4[1]], 'k-', lw=1.3)
        
        # Right
        p1 = (1-f)*right_pts[0] + f*right_pts[1]
        p2 = (1-f)*right_pts[3] + f*right_pts[2]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-', lw=1.3)
        p3 = (1-f)*right_pts[0] + f*right_pts[3]
        p4 = (1-f)*right_pts[1] + f*right_pts[2]
        ax.plot([p3[0], p4[0]], [p3[1], p4[1]], 'k-', lw=1.3)
        
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-0.7, 1.7)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.04)
    plt.close()
    return filepath

# -------------------------------------------------------------
# 3. ANALOG CLOCK DIAGRAMS
# -------------------------------------------------------------
def generate_clock_face(hour, minute, filepath):
    """
    Renders an analog clock face showing the exact specified hour and minute.
    """
    ensure_dir(filepath)
    fig, ax = plt.subplots(figsize=(2.2, 2.2), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')
    
    circle = patches.Circle((0, 0), 1.0, facecolor='white', edgecolor='black', lw=2.5)
    ax.add_patch(circle)
    ax.plot(0, 0, 'ko', markersize=5)
    
    for i in range(1, 13):
        ang = np.pi/2 - i * (2*np.pi/12)
        x = 0.82 * np.cos(ang)
        y = 0.82 * np.sin(ang)
        ax.text(x, y, str(i), fontsize=10, fontweight='bold', ha='center', va='center')
        
    # Hands
    ang_min = np.pi/2 - (minute / 60) * (2*np.pi)
    total_hr = (hour % 12) + minute / 60
    ang_hr = np.pi/2 - (total_hr / 12) * (2*np.pi)
    
    ax.annotate('', xy=(0.72*np.cos(ang_min), 0.72*np.sin(ang_min)), xytext=(0,0),
                arrowprops=dict(arrowstyle='->', lw=2.2, color='black'))
    ax.annotate('', xy=(0.48*np.cos(ang_hr), 0.48*np.sin(ang_hr)), xytext=(0,0),
                arrowprops=dict(arrowstyle='->', lw=3.2, color='black'))
                
    ax.set_xlim(-1.12, 1.12)
    ax.set_ylim(-1.12, 1.12)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.04)
    plt.close()
    return filepath

# -------------------------------------------------------------
# 4. MIRROR & WATER IMAGE DIAGRAMS
# -------------------------------------------------------------
def generate_mirror_problem(text, filepath, mirror_label=('M', 'N')):
    """Renders text or symbol with vertical mirror line MN on right."""
    ensure_dir(filepath)
    fig, ax = plt.subplots(figsize=(3.4, 1.3), dpi=300)
    ax.axis('off')
    
    ax.text(0.32, 0.5, text, fontsize=18, fontweight='bold', fontfamily='sans-serif', ha='center', va='center')
    
    # Mirror line
    ax.plot([0.68, 0.68], [0.12, 0.88], 'k-', lw=2.4)
    ax.text(0.68, 0.96, mirror_label[0], fontsize=11, fontweight='bold', ha='center')
    ax.text(0.68, 0.02, mirror_label[1], fontsize=11, fontweight='bold', ha='center')
    
    for y in np.linspace(0.14, 0.86, 12):
        ax.plot([0.68, 0.74], [y, y + 0.04], 'k-', lw=1.2)
        
    ax.set_xlim(0, 0.95)
    ax.set_ylim(-0.1, 1.1)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.04)
    plt.close()
    return filepath

def generate_water_problem(text, filepath, water_label=('M', 'N')):
    """Renders text or symbol with horizontal water reflection line MN on bottom."""
    ensure_dir(filepath)
    fig, ax = plt.subplots(figsize=(3.4, 1.5), dpi=300)
    ax.axis('off')
    
    ax.text(0.5, 0.68, text, fontsize=18, fontweight='bold', fontfamily='sans-serif', ha='center', va='center')
    
    # Water line
    ax.plot([0.1, 0.9], [0.36, 0.36], 'k-', lw=2.4)
    ax.text(0.04, 0.36, water_label[0], fontsize=11, fontweight='bold', va='center')
    ax.text(0.96, 0.36, water_label[1], fontsize=11, fontweight='bold', va='center')
    
    for x in np.linspace(0.12, 0.88, 16):
        ax.plot([x, x - 0.03], [0.36, 0.22], 'k-', lw=1.2)
        
    ax.set_xlim(0, 1.0)
    ax.set_ylim(0.1, 0.95)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.04)
    plt.close()
    return filepath


def generate_text_card(text: str, filepath: str, flip_mode: Optional[str] = None) -> str:
    """Renders a single compact text card, optionally applying a reflection."""
    ensure_dir(filepath)
    fig, ax = plt.subplots(figsize=(2.2, 0.45), dpi=300)
    ax.axis('off')
    ax.text(0.5, 0.5, text, fontsize=15, fontweight='bold', fontfamily='sans-serif',
            ha='center', va='center')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout(pad=0.08)
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.02)
    plt.close()

    if flip_mode:
        im = Image.open(filepath)
        if flip_mode == 'FLIP_LR':
            im = im.transpose(Image.FLIP_LEFT_RIGHT)
        elif flip_mode == 'FLIP_TB':
            im = im.transpose(Image.FLIP_TOP_BOTTOM)
        elif flip_mode == 'ROTATE_180':
            im = im.transpose(Image.ROTATE_180)
        im.save(filepath)
    return filepath


def generate_mirror_options(text: str, output_dir: str, prefix: str) -> List[str]:
    """
    Generates 4 distinct HD vector option images for a mirror image problem:
    - Option 1 (Correct): Exact horizontal reflection (FLIP_LR).
    - Option 2 (Distractor): Reversed letter order in standard upright font.
    - Option 3 (Distractor): Vertical flip (Water reflection).
    - Option 4 (Distractor): 180° rotation (Rotated inverted).
    Returns list of 4 filepaths [opt1, opt2, opt3, opt4].
    """
    ensure_dir(output_dir)
    p1 = os.path.join(output_dir, f"{prefix}_opt1_mirror_corr.png")
    p2 = os.path.join(output_dir, f"{prefix}_opt2_rev_text.png")
    p3 = os.path.join(output_dir, f"{prefix}_opt3_water_flip.png")
    p4 = os.path.join(output_dir, f"{prefix}_opt4_rot180.png")

    generate_text_card(text, p1, flip_mode='FLIP_LR')
    generate_text_card(text[::-1], p2, flip_mode=None)
    generate_text_card(text, p3, flip_mode='FLIP_TB')
    generate_text_card(text, p4, flip_mode='ROTATE_180')

    return [p1, p2, p3, p4]


def generate_water_options(text: str, output_dir: str, prefix: str) -> List[str]:
    """
    Generates 4 distinct HD vector option images for a water image problem:
    - Option 1 (Correct): Exact vertical reflection (FLIP_TB).
    - Option 2 (Distractor): Horizontal reflection (Mirror image).
    - Option 3 (Distractor): Reversed letter order vertically flipped.
    - Option 4 (Distractor): 180° rotation (Rotated inverted).
    Returns list of 4 filepaths [opt1, opt2, opt3, opt4].
    """
    ensure_dir(output_dir)
    p1 = os.path.join(output_dir, f"{prefix}_opt1_water_corr.png")
    p2 = os.path.join(output_dir, f"{prefix}_opt2_mirror_flip.png")
    p3 = os.path.join(output_dir, f"{prefix}_opt3_rev_water.png")
    p4 = os.path.join(output_dir, f"{prefix}_opt4_rot180.png")

    generate_text_card(text, p1, flip_mode='FLIP_TB')
    generate_text_card(text, p2, flip_mode='FLIP_LR')
    generate_text_card(text[::-1], p3, flip_mode='FLIP_TB')
    generate_text_card(text, p4, flip_mode='ROTATE_180')

    return [p1, p2, p3, p4]


# -------------------------------------------------------------
# 5. SURVEY & GEOMETRIC VENN DIAGRAMS (Q131 - Q138)
# -------------------------------------------------------------
VENN_4SHAPE_CENTROIDS = {
    (1, 0, 0, 0): (0.461, 0.813),  # T only (Triangle apex)
    (0, 1, 0, 0): (0.257, 0.680),  # S only (Square upper-left)
    (0, 0, 1, 0): (0.119, 0.329),  # R only (Rectangle far-left)
    (0, 0, 0, 1): (0.830, 0.346),  # C only (Circle far-right)
    (1, 1, 0, 0): (0.434, 0.675),  # T + S (Triangle + Square, upper)
    (1, 1, 1, 0): (0.278, 0.382),  # T + S + R (Triangle + Square + Rectangle)
    (1, 1, 1, 1): (0.465, 0.429),  # All 4 shapes (Dead center)
    (1, 0, 1, 1): (0.687, 0.292),  # T + R + C (Triangle + Rectangle + Circle, lower right)
    (0, 0, 1, 1): (0.718, 0.497),  # R + C (Rectangle + Circle, upper right)
}

def generate_four_shape_venn_diagram(filepath, regions):
    """
    Renders vector-crisp 4-shape geometric Venn Diagram with
    Square, Triangle, Rectangle, and Circle with mathematically calculated centroids.
    Every number is placed at the exact maximum clearance point from all borders.
    """
    ensure_dir(filepath)
    fig, ax = plt.subplots(figsize=(4.6, 3.7), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')

    tri_pts = np.array([[0.10, 0.14], [0.46, 0.94], [0.84, 0.14]])
    tri = patches.Polygon(tri_pts, closed=True, fill=False, edgecolor='black', lw=2.4)
    sq = patches.Rectangle((0.18, 0.32), 0.44, 0.44, fill=False, edgecolor='black', lw=2.4)
    rect = patches.Rectangle((0.06, 0.22), 0.70, 0.32, fill=False, edgecolor='black', lw=2.4)
    circ = patches.Circle((0.62, 0.36), 0.28, fill=False, edgecolor='black', lw=2.4)

    ax.add_patch(tri)
    ax.add_patch(sq)
    ax.add_patch(rect)
    ax.add_patch(circ)

    for key, txt in regions.items():
        if key in VENN_4SHAPE_CENTROIDS:
            pos = VENN_4SHAPE_CENTROIDS[key]
        elif isinstance(key, (tuple, list)) and len(key) == 2:
            # Map legacy (x, y) float coordinate to nearest safe centroid
            kx, ky = key
            best_k = min(VENN_4SHAPE_CENTROIDS.keys(), key=lambda k: (VENN_4SHAPE_CENTROIDS[k][0]-kx)**2 + (VENN_4SHAPE_CENTROIDS[k][1]-ky)**2)
            pos = VENN_4SHAPE_CENTROIDS[best_k]
        else:
            pos = (0.5, 0.5)

        ax.text(pos[0], pos[1], str(txt), fontsize=14, fontweight='bold', ha='center', va='center')

    ax.set_xlim(-0.02, 0.96)
    ax.set_ylim(0.06, 0.98)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath


def generate_survey_venn_graduates(filepath, nums=None):
    """
    Renders 100% closed, vector-crisp survey Venn diagram with Triangle,
    Circle, and Rectangle.
    Numbers are positioned at mathematically verified centroids with generous clearance from all lines.
    """
    if nums is None:
        nums = {'T': 4, 'C': 1, 'TC': 7, 'ALL': 5, 'TR': 8, 'CR': 6, 'R': 3}
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

    # Verified safe centroids with maximum distance from all borders:
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

# -------------------------------------------------------------
# 6. PAPER FOLDING & CUTTING
# -------------------------------------------------------------
def generate_paper_fold_cut_problem(step_type, filepath):
    """
    Renders 3-step paper folding and hole punching (X, Y, Z).
    step_type: 'circle_corner' or 'triangle_edge'
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(1, 3, figsize=(4.6, 1.6), dpi=300)
    for ax, lbl in zip(axes, ['X', 'Y', 'Z']):
        ax.set_aspect('equal')
        ax.axis('off')
        ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=2))
        ax.text(0.5, -0.25, lbl, fontsize=12, fontweight='bold', ha='center')
        ax.set_xlim(-0.1, 1.1)
        ax.set_ylim(-0.35, 1.1)
        
    # Step X: fold down
    axes[0].plot([0, 1], [0.5, 0.5], 'k--', lw=1.6)
    axes[0].annotate('', xy=(0.5, 0.4), xytext=(0.5, 0.6), arrowprops=dict(arrowstyle='->', lw=1.8, color='black'))
    
    # Step Y: fold right
    axes[1].add_patch(patches.Rectangle((0, 0.5), 1, 0.5, facecolor='#f0f0f0', edgecolor='none'))
    axes[1].plot([0, 1], [0.5, 0.5], 'k-', lw=2)
    axes[1].plot([0.5, 0.5], [0, 0.5], 'k--', lw=1.6)
    axes[1].annotate('', xy=(0.6, 0.25), xytext=(0.4, 0.25), arrowprops=dict(arrowstyle='->', lw=1.8, color='black'))
    
    # Step Z: cutout
    axes[2].add_patch(patches.Rectangle((0, 0.5), 1, 0.5, facecolor='#f0f0f0', edgecolor='none'))
    axes[2].add_patch(patches.Rectangle((0, 0), 0.5, 0.5, facecolor='#f0f0f0', edgecolor='none'))
    axes[2].plot([0, 1], [0.5, 0.5], 'k-', lw=2)
    axes[2].plot([0.5, 0.5], [0, 0.5], 'k-', lw=2)
    
    if step_type == 'circle_corner':
        axes[2].add_patch(patches.Circle((0.75, 0.25), 0.1, facecolor='black', edgecolor='black'))
    else:
        tri = patches.Polygon([[1.0, 0.2], [0.85, 0.25], [1.0, 0.3]], closed=True, facecolor='black', edgecolor='black')
        axes[2].add_patch(tri)
        
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.04)
    plt.close()
    return filepath


def generate_unfolded_square_card(holes=None, notches=None, center_shape=None, filepath='test.png'):
    """Renders a single square option card showing unfolded paper patterns."""
    ensure_dir(filepath)
    fig, ax = plt.subplots(figsize=(1.0, 1.0), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Outer square
    ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=2))
    # Light dotted fold lines to show quarters
    ax.plot([0.5, 0.5], [0, 1], 'k:', lw=0.8, alpha=0.6)
    ax.plot([0, 1], [0.5, 0.5], 'k:', lw=0.8, alpha=0.6)
    
    if holes:
        for (hx, hy, r) in holes:
            ax.add_patch(patches.Circle((hx, hy), r, facecolor='black', edgecolor='black'))
            
    if notches:
        for poly_pts in notches:
            ax.add_patch(patches.Polygon(poly_pts, closed=True, facecolor='black', edgecolor='black'))
            
    if center_shape == 'diamond':
        ax.add_patch(patches.Polygon([[0.5, 0.3], [0.7, 0.5], [0.5, 0.7], [0.3, 0.5]], closed=True, facecolor='black', edgecolor='black'))
    elif center_shape == 'square':
        ax.add_patch(patches.Rectangle((0.35, 0.35), 0.3, 0.3, facecolor='black', edgecolor='black'))

    ax.set_xlim(-0.04, 1.04)
    ax.set_ylim(-0.04, 1.04)
    plt.tight_layout(pad=0.03)
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.02)
    plt.close()
    return filepath


def generate_paper_fold_options(step_type: str, output_dir: str, prefix: str) -> List[str]:
    """
    Generates 4 publication-quality vector option images for paper fold problems:
    - Option 1 (Correct): The exact unfolded pattern.
    - Options 2, 3, 4 (Distractors): Plausible unfolded patterns (notches/holes mispositioned).
    """
    ensure_dir(output_dir)
    p1 = os.path.join(output_dir, f"{prefix}_opt1.png")
    p2 = os.path.join(output_dir, f"{prefix}_opt2.png")
    p3 = os.path.join(output_dir, f"{prefix}_opt3.png")
    p4 = os.path.join(output_dir, f"{prefix}_opt4.png")

    if step_type == 'circle_corner':
        # (1) Correct: 4 holes in quarters
        generate_unfolded_square_card(holes=[(0.25, 0.25, 0.08), (0.75, 0.25, 0.08), (0.25, 0.75, 0.08), (0.75, 0.75, 0.08)], filepath=p1)
        # (2) Distractor: 2 holes vertical
        generate_unfolded_square_card(holes=[(0.5, 0.25, 0.08), (0.5, 0.75, 0.08)], filepath=p2)
        # (3) Distractor: 1 hole bottom-right
        generate_unfolded_square_card(holes=[(0.75, 0.25, 0.08)], filepath=p3)
        # (4) Distractor: 4 holes on edges
        generate_unfolded_square_card(holes=[(0.5, 0.15, 0.08), (0.5, 0.85, 0.08), (0.15, 0.5, 0.08), (0.85, 0.5, 0.08)], filepath=p4)
    else:  # triangle_edge
        notches_4 = [
            [[1.0, 0.42], [0.85, 0.5], [1.0, 0.58]],
            [[0.0, 0.42], [0.15, 0.5], [0.0, 0.58]],
            [[0.42, 1.0], [0.5, 0.85], [0.58, 1.0]],
            [[0.42, 0.0], [0.5, 0.15], [0.58, 0.0]],
        ]
        notches_2 = [
            [[1.0, 0.42], [0.85, 0.5], [1.0, 0.58]],
            [[0.0, 0.42], [0.15, 0.5], [0.0, 0.58]]
        ]
        # (1) Correct: 4 triangular notches
        generate_unfolded_square_card(notches=notches_4, filepath=p1)
        # (2) Distractor: 2 notches left/right
        generate_unfolded_square_card(notches=notches_2, filepath=p2)
        # (3) Distractor: Center diamond
        generate_unfolded_square_card(center_shape='diamond', filepath=p3)
        # (4) Distractor: Center square
        generate_unfolded_square_card(center_shape='square', filepath=p4)

    return [p1, p2, p3, p4]

def generate_transparent_fold_problem(filepath):
    """
    Renders Problem Figure (X) and 4 Answer Figures (1), (2), (3), (4)
    for transparent sheet folding along dotted vertical centerline.
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(1, 5, figsize=(5.0, 1.22), dpi=300)
    
    # Fig 0: Problem Figure (X)
    ax_x = axes[0]
    ax_x.set_aspect('equal')
    ax_x.axis('off')
    ax_x.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
    ax_x.plot([0.5, 0.5], [0, 1], 'k--', lw=1.5)
    # Left pattern: solid triangle pointing right
    ax_x.add_patch(patches.Polygon([[0.15, 0.25], [0.15, 0.75], [0.42, 0.5]], closed=True, facecolor='black'))
    # Right pattern: circle
    ax_x.add_patch(patches.Circle((0.75, 0.5), 0.2, fill=False, edgecolor='black', lw=1.8))
    ax_x.text(0.5, -0.22, '(X)', fontsize=9, fontweight='bold', ha='center')
    ax_x.set_xlim(-0.05, 1.05); ax_x.set_ylim(-0.3, 1.1)

    # 4 Answer figures: (1), (2), (3), (4)
    configs = [
        {'tri_dir': 'left'},        # (1) Correct: reflected left triangle pointing left inside circle
        {'tri_dir': 'right'},       # (2) Distractor: translated without reflection
        {'tri_dir': 'down'},        # (3) Distractor: upside down
        {'tri_dir': 'separated'}    # (4) Distractor: misplaced outside
    ]
    for idx, (ax_ans, cfg) in enumerate(zip(axes[1:], configs)):
        ax_ans.set_aspect('equal')
        ax_ans.axis('off')
        ax_ans.add_patch(patches.Rectangle((0.5, 0), 0.5, 1, facecolor='white', edgecolor='black', lw=1.8))
        ax_ans.add_patch(patches.Circle((0.75, 0.5), 0.2, fill=False, edgecolor='black', lw=1.8))
        
        td = cfg['tri_dir']
        if td == 'left':
            ax_ans.add_patch(patches.Polygon([[0.85, 0.25], [0.85, 0.75], [0.58, 0.5]], closed=True, facecolor='black'))
        elif td == 'right':
            ax_ans.add_patch(patches.Polygon([[0.65, 0.25], [0.65, 0.75], [0.92, 0.5]], closed=True, facecolor='black'))
        elif td == 'down':
            ax_ans.add_patch(patches.Polygon([[0.60, 0.65], [0.90, 0.65], [0.75, 0.35]], closed=True, facecolor='black'))
        else:
            ax_ans.add_patch(patches.Polygon([[0.85, 0.65], [0.85, 0.95], [0.65, 0.8]], closed=True, facecolor='black'))

        ax_ans.text(0.75, -0.22, f'({idx+1})', fontsize=9, fontweight='bold', ha='center')
        ax_ans.set_xlim(0.45, 1.05); ax_ans.set_ylim(-0.3, 1.1)

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath

def generate_circular_fold_cut_problem(filepath):
    """
    Renders Problem Figures X, Y, Z (circular fold and cut)
    and 4 Answer Figures (1), (2), (3), (4). Correct option is (3).
    """
    ensure_dir(filepath)
    fig = plt.figure(figsize=(4.8, 2.1), dpi=300)
    gs = fig.add_gridspec(2, 4, height_ratios=[1, 1], hspace=0.35, wspace=0.15)
    
    # Step X
    ax_x = fig.add_subplot(gs[0, 0])
    ax_x.set_aspect('equal'); ax_x.axis('off')
    ax_x.add_patch(patches.Circle((0.5, 0.5), 0.44, fill=False, edgecolor='black', lw=1.8))
    ax_x.plot([0.06, 0.94], [0.5, 0.5], 'k--', lw=1.4)
    ax_x.annotate('', xy=(0.5, 0.65), xytext=(0.5, 0.35), arrowprops=dict(arrowstyle='->', lw=1.4, color='black'))
    ax_x.text(0.5, -0.15, 'X', fontsize=9, fontweight='bold', ha='center')
    ax_x.set_xlim(0, 1); ax_x.set_ylim(-0.2, 1.05)

    # Step Y
    ax_y = fig.add_subplot(gs[0, 1])
    ax_y.set_aspect('equal'); ax_y.axis('off')
    wedge_y = patches.Wedge((0.5, 0.5), 0.44, 0, 180, fill=False, edgecolor='black', lw=1.8)
    ax_y.add_patch(wedge_y)
    ax_y.plot([0.06, 0.94], [0.5, 0.5], 'k-', lw=1.8)
    ax_y.plot([0.5, 0.5], [0.5, 0.94], 'k--', lw=1.4)
    ax_y.annotate('', xy=(0.35, 0.72), xytext=(0.65, 0.72), arrowprops=dict(arrowstyle='->', lw=1.4, color='black'))
    ax_y.text(0.5, -0.15, 'Y', fontsize=9, fontweight='bold', ha='center')
    ax_y.set_xlim(0, 1); ax_y.set_ylim(-0.2, 1.05)

    # Step Z
    ax_z = fig.add_subplot(gs[0, 2])
    ax_z.set_aspect('equal'); ax_z.axis('off')
    wedge_z = patches.Wedge((0.5, 0.5), 0.44, 90, 180, fill=False, edgecolor='black', lw=1.8)
    ax_z.add_patch(wedge_z)
    ax_z.plot([0.06, 0.5], [0.5, 0.5], 'k-', lw=1.8)
    ax_z.plot([0.5, 0.5], [0.5, 0.94], 'k-', lw=1.8)
    r_h = 0.28
    th1, th2 = np.radians(120), np.radians(150)
    ax_z.add_patch(patches.Circle((0.5 + r_h*np.cos(th1), 0.5 + r_h*np.sin(th1)), 0.05, facecolor='black'))
    ax_z.add_patch(patches.Circle((0.5 + r_h*np.cos(th2), 0.5 + r_h*np.sin(th2)), 0.05, facecolor='black'))
    ax_z.text(0.5, -0.15, 'Z', fontsize=9, fontweight='bold', ha='center')
    ax_z.set_xlim(0, 1); ax_z.set_ylim(-0.2, 1.05)

    ax_x.text(1.7, 1.15, 'Problem Figures', fontsize=9, fontweight='bold', ha='center')

    # Bottom Row: 4 Answer Figures (1), (2), (3), (4)
    ans_axes = [fig.add_subplot(gs[1, i]) for i in range(4)]
    ans_axes[0].text(2.2, 1.15, 'Answer Figures', fontsize=9, fontweight='bold', ha='center')
    
    for i, aax in enumerate(ans_axes):
        aax.set_aspect('equal'); aax.axis('off')
        aax.add_patch(patches.Circle((0.5, 0.5), 0.44, fill=False, edgecolor='black', lw=1.8))
        aax.text(0.5, -0.15, f'({i+1})', fontsize=9, fontweight='bold', ha='center')
        aax.set_xlim(0, 1); aax.set_ylim(-0.2, 1.05)
        
        if i == 0:
            for deg in [45, 135, 225, 315]:
                rad = np.radians(deg)
                aax.add_patch(patches.Circle((0.5 + 0.28*np.cos(rad), 0.5 + 0.28*np.sin(rad)), 0.05, facecolor='black'))
        elif i == 1:
            for deg in [30, 90, 150, 210, 270, 330]:
                rad = np.radians(deg)
                aax.add_patch(patches.Circle((0.5 + 0.28*np.cos(rad), 0.5 + 0.28*np.sin(rad)), 0.05, facecolor='black'))
        elif i == 2: # Correct: 8 holes symmetrically in 4 quadrants
            for deg in [30, 60, 120, 150, 210, 240, 300, 330]:
                rad = np.radians(deg)
                aax.add_patch(patches.Circle((0.5 + 0.28*np.cos(rad), 0.5 + 0.28*np.sin(rad)), 0.05, facecolor='black'))
        else:
            for deg in [0, 45, 90, 135, 180, 225, 270, 315]:
                rad = np.radians(deg)
                aax.add_patch(patches.Circle((0.5 + 0.40*np.cos(rad), 0.5 + 0.40*np.sin(rad)), 0.05, facecolor='black'))

    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath

# -------------------------------------------------------------
# 7. EMBEDDED FIGURES
# -------------------------------------------------------------
def generate_embedded_figure_problem(filepath):
    """
    Renders Target Figure (X) and 4 Answer Figures (1), (2), (3), (4).
    Correct option is (2).
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(1, 5, figsize=(5.0, 1.22), dpi=300)
    
    # Ax 0: Problem Figure (X)
    ax_x = axes[0]
    ax_x.set_aspect('equal'); ax_x.axis('off')
    ax_x.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
    # Target figure: Z-shape
    ax_x.plot([0.25, 0.75], [0.75, 0.75], 'k-', lw=3)
    ax_x.plot([0.75, 0.25], [0.75, 0.25], 'k-', lw=3)
    ax_x.plot([0.25, 0.75], [0.25, 0.25], 'k-', lw=3)
    ax_x.text(0.5, -0.22, '(X)', fontsize=9, fontweight='bold', ha='center')
    ax_x.set_xlim(-0.05, 1.05); ax_x.set_ylim(-0.3, 1.1)
    
    # 4 Answer figures: (1), (2), (3), (4)
    for i, ax in enumerate(axes[1:]):
        ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
        ax.text(0.5, -0.22, f'({i+1})', fontsize=9, fontweight='bold', ha='center')
        ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.3, 1.1)
        
        if i == 0:
            ax.plot([0.1, 0.9], [0.1, 0.9], 'k-', lw=1.8)
            ax.plot([0.1, 0.9], [0.9, 0.1], 'k-', lw=1.8)
            ax.plot([0.5, 0.5], [0.1, 0.9], 'k-', lw=1.8)
            ax.plot([0.1, 0.9], [0.5, 0.5], 'k-', lw=1.8)
        elif i == 1:
            # (2) CORRECT: Contains the exact Z-stroke embedded in a geometric web
            ax.plot([0.25, 0.75], [0.75, 0.75], 'k-', lw=2.2)
            ax.plot([0.75, 0.25], [0.75, 0.25], 'k-', lw=2.2)
            ax.plot([0.25, 0.75], [0.25, 0.25], 'k-', lw=2.2)
            ax.plot([0.25, 0.25], [0.25, 0.75], 'k-', lw=1.8)
            ax.plot([0.75, 0.75], [0.25, 0.75], 'k-', lw=1.8)
            ax.plot([0.1, 0.9], [0.1, 0.1], 'k-', lw=1.8)
            ax.plot([0.1, 0.9], [0.9, 0.9], 'k-', lw=1.8)
            ax.plot([0.5, 0.5], [0.25, 0.75], 'k-', lw=1.8)
        elif i == 2:
            ax.plot([0.25, 0.25], [0.25, 0.75], 'k-', lw=1.8)
            ax.plot([0.25, 0.75], [0.75, 0.25], 'k-', lw=1.8)
            ax.plot([0.75, 0.75], [0.25, 0.75], 'k-', lw=1.8)
            ax.plot([0.1, 0.9], [0.5, 0.5], 'k-', lw=1.8)
        else:
            ax.plot([0.25, 0.75], [0.75, 0.75], 'k-', lw=1.8)
            ax.plot([0.25, 0.75], [0.75, 0.25], 'k-', lw=1.8)
            ax.plot([0.25, 0.75], [0.25, 0.25], 'k-', lw=1.8)
            ax.plot([0.5, 0.5], [0.1, 0.9], 'k-', lw=1.8)

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath

# -------------------------------------------------------------
# 8. NON-VERBAL ANALOGY & SERIES
# -------------------------------------------------------------
def generate_analogy_problem(filepath):
    """
    Renders Problem Figures (A), (B), (C), (D) and Answer Figures (1), (2), (3), (4).
    Correct option is (3).
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(2, 4, figsize=(4.8, 2.1), dpi=300)
    
    lbls_p = ['(A)', '(B)', '(C)', '(D)']
    for i, ax in enumerate(axes[0]):
        ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
        ax.text(0.5, -0.20, lbls_p[i], fontsize=9, fontweight='bold', ha='center')
        ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.28, 1.05)
        
        if i == 0:
            tri = patches.Polygon([[0.25, 0.22], [0.5, 0.78], [0.75, 0.22]], closed=True, fill=False, edgecolor='black', lw=2.2)
            ax.add_patch(tri)
        elif i == 1:
            diam = patches.Polygon([[0.5, 0.88], [0.88, 0.5], [0.5, 0.12], [0.12, 0.5]], closed=True, fill=False, edgecolor='black', lw=2.2)
            tri = patches.Polygon([[0.32, 0.30], [0.5, 0.75], [0.68, 0.30]], closed=True, fill=False, edgecolor='black', lw=2.0)
            ax.add_patch(diam); ax.add_patch(tri)
        elif i == 2:
            pent = patches.Polygon([[0.25, 0.22], [0.25, 0.55], [0.5, 0.82], [0.75, 0.55], [0.75, 0.22]], closed=True, fill=False, edgecolor='black', lw=2.2)
            ax.add_patch(pent)
        else:
            ax.text(0.5, 0.5, '?', fontsize=22, fontweight='bold', ha='center', va='center')

    for i, ax in enumerate(axes[1]):
        ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
        ax.text(0.5, -0.20, f'({i+1})', fontsize=9, fontweight='bold', ha='center')
        ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.28, 1.05)
        
        pent = patches.Polygon([[0.32, 0.26], [0.32, 0.50], [0.5, 0.72], [0.68, 0.50], [0.68, 0.26]], closed=True, fill=False, edgecolor='black', lw=1.8)
        
        if i == 0:
            sq = patches.Rectangle((0.15, 0.15), 0.7, 0.7, fill=False, edgecolor='black', lw=2.0)
            ax.add_patch(sq); ax.add_patch(pent)
        elif i == 1:
            hex_pts = [[0.5, 0.90], [0.85, 0.70], [0.85, 0.30], [0.5, 0.10], [0.15, 0.30], [0.15, 0.70]]
            hx = patches.Polygon(hex_pts, closed=True, fill=False, edgecolor='black', lw=2.0)
            ax.add_patch(hx); ax.add_patch(pent)
        elif i == 2: # Correct: (3) Diamond containing Pentagon
            diam = patches.Polygon([[0.5, 0.90], [0.90, 0.5], [0.5, 0.10], [0.10, 0.5]], closed=True, fill=False, edgecolor='black', lw=2.2)
            ax.add_patch(diam); ax.add_patch(pent)
        else:
            cir = patches.Circle((0.5, 0.5), 0.40, fill=False, edgecolor='black', lw=2.0)
            ax.add_patch(cir); ax.add_patch(pent)

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath

def generate_series_problem(filepath):
    """
    Renders Problem Figures (A), (B), (C), (D) and Answer Figures (1), (2), (3), (4).
    Clockwise rotating triangle series. Correct option is (2).
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(2, 4, figsize=(4.8, 2.1), dpi=300)
    
    lbls_p = ['(A)', '(B)', '(C)', '(D)']
    for i, ax in enumerate(axes[0]):
        ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
        ax.text(0.5, -0.20, lbls_p[i], fontsize=9, fontweight='bold', ha='center')
        ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.28, 1.05)
        
        if i == 0:
            tri = patches.Polygon([[0.18, 0.18], [0.18, 0.82], [0.82, 0.50]], closed=True, fill=False, edgecolor='black', lw=2.2)
            ax.add_patch(tri)
        elif i == 1:
            tri = patches.Polygon([[0.18, 0.82], [0.82, 0.82], [0.50, 0.18]], closed=True, fill=False, edgecolor='black', lw=2.2)
            ax.add_patch(tri)
        elif i == 2:
            tri = patches.Polygon([[0.82, 0.18], [0.82, 0.82], [0.18, 0.50]], closed=True, fill=False, edgecolor='black', lw=2.2)
            ax.add_patch(tri)
        else:
            ax.text(0.5, 0.5, '?', fontsize=22, fontweight='bold', ha='center', va='center')

    for i, ax in enumerate(axes[1]):
        ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
        ax.text(0.5, -0.20, f'({i+1})', fontsize=9, fontweight='bold', ha='center')
        ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.28, 1.05)
        
        if i == 0:
            tri = patches.Polygon([[0.18, 0.82], [0.82, 0.82], [0.50, 0.18]], closed=True, fill=False, edgecolor='black', lw=2.2)
        elif i == 1: # Correct: (2) pointing Up
            tri = patches.Polygon([[0.18, 0.18], [0.82, 0.18], [0.50, 0.82]], closed=True, fill=False, edgecolor='black', lw=2.2)
        elif i == 2:
            tri = patches.Polygon([[0.82, 0.18], [0.82, 0.82], [0.18, 0.50]], closed=True, fill=False, edgecolor='black', lw=2.2)
        else:
            tri = patches.Polygon([[0.18, 0.18], [0.18, 0.82], [0.82, 0.50]], closed=True, fill=False, edgecolor='black', lw=2.2)
        ax.add_patch(tri)

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath

# -------------------------------------------------------------
# 9. DOT SITUATION (Q179)
# -------------------------------------------------------------
def generate_dot_situation(placement, filepath):
    """
    Renders Problem Figure with the dot placed strictly inside the open interior region
    (Circle & Triangle only, well outside Square, zero contact with any border),
    along with 4 Answer Figures (1), (2), (3), (4). Correct option is (1).
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(1, 5, figsize=(5.0, 1.22), dpi=300)
    
    # Ax 0: Problem Figure
    ax_x = axes[0]
    ax_x.set_aspect('equal'); ax_x.axis('off')
    ax_x.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
    
    tri_x = patches.Polygon([[0.08, 0.20], [0.5, 0.92], [0.92, 0.20]], closed=True, fill=False, edgecolor='black', lw=1.8)
    cir_x = patches.Circle((0.35, 0.55), 0.28, fill=False, edgecolor='black', lw=1.8)
    sq_x = patches.Rectangle((0.48, 0.10), 0.40, 0.38, fill=False, edgecolor='black', lw=1.8)
    
    ax_x.add_patch(tri_x); ax_x.add_patch(cir_x); ax_x.add_patch(sq_x)
    # Dot at (0.38, 0.62) -> strictly inside open space between borders
    ax_x.plot(0.38, 0.62, 'ko', markersize=5)
    ax_x.text(0.5, -0.20, 'Problem Fig', fontsize=8, fontweight='bold', ha='center')
    ax_x.set_xlim(-0.05, 1.05); ax_x.set_ylim(-0.28, 1.05)
    
    # 4 Answer figures:
    # (1) CORRECT: Circle & Triangle overlap in open space, Square is on the right
    ax1 = axes[1]
    ax1.set_aspect('equal'); ax1.axis('off')
    ax1.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
    t1 = patches.Polygon([[0.15, 0.25], [0.55, 0.90], [0.85, 0.25]], closed=True, fill=False, edgecolor='black', lw=1.8)
    c1 = patches.Circle((0.35, 0.65), 0.24, fill=False, edgecolor='black', lw=1.8)
    s1 = patches.Rectangle((0.55, 0.10), 0.38, 0.35, fill=False, edgecolor='black', lw=1.8)
    ax1.add_patch(t1); ax1.add_patch(c1); ax1.add_patch(s1)
    ax1.text(0.5, -0.20, '(1)', fontsize=9, fontweight='bold', ha='center')
    ax1.set_xlim(-0.05, 1.05); ax1.set_ylim(-0.28, 1.05)
    
    # (2) Distractor: Circle and Triangle do not intersect
    ax2 = axes[2]
    ax2.set_aspect('equal'); ax2.axis('off')
    ax2.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
    t2 = patches.Polygon([[0.08, 0.20], [0.45, 0.85], [0.45, 0.20]], closed=True, fill=False, edgecolor='black', lw=1.8)
    c2 = patches.Circle((0.75, 0.55), 0.20, fill=False, edgecolor='black', lw=1.8)
    s2 = patches.Rectangle((0.30, 0.15), 0.40, 0.40, fill=False, edgecolor='black', lw=1.8)
    ax2.add_patch(t2); ax2.add_patch(c2); ax2.add_patch(s2)
    ax2.text(0.5, -0.20, '(2)', fontsize=9, fontweight='bold', ha='center')
    ax2.set_xlim(-0.05, 1.05); ax2.set_ylim(-0.28, 1.05)
    
    # (3) Distractor: Square covers the entire circle interior
    ax3 = axes[3]
    ax3.set_aspect('equal'); ax3.axis('off')
    ax3.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
    t3 = patches.Polygon([[0.10, 0.25], [0.50, 0.90], [0.90, 0.25]], closed=True, fill=False, edgecolor='black', lw=1.8)
    c3 = patches.Circle((0.50, 0.45), 0.25, fill=False, edgecolor='black', lw=1.8)
    s3 = patches.Rectangle((0.25, 0.22), 0.50, 0.46, fill=False, edgecolor='black', lw=1.8)
    ax3.add_patch(t3); ax3.add_patch(c3); ax3.add_patch(s3)
    ax3.text(0.5, -0.20, '(3)', fontsize=9, fontweight='bold', ha='center')
    ax3.set_xlim(-0.05, 1.05); ax3.set_ylim(-0.28, 1.05)
    
    # (4) Distractor: Triangle is inside Square, Circle only touches Square
    ax4 = axes[4]
    ax4.set_aspect('equal'); ax4.axis('off')
    ax4.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
    s4 = patches.Rectangle((0.15, 0.20), 0.50, 0.60, fill=False, edgecolor='black', lw=1.8)
    t4 = patches.Polygon([[0.22, 0.28], [0.40, 0.72], [0.58, 0.28]], closed=True, fill=False, edgecolor='black', lw=1.8)
    c4 = patches.Circle((0.80, 0.50), 0.16, fill=False, edgecolor='black', lw=1.8)
    ax4.add_patch(s4); ax4.add_patch(t4); ax4.add_patch(c4)
    ax4.text(0.5, -0.20, '(4)', fontsize=9, fontweight='bold', ha='center')
    ax4.set_xlim(-0.05, 1.05); ax4.set_ylim(-0.28, 1.05)

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath

# -------------------------------------------------------------
# 10. SPOTLESS HD GEOMETRIC NUMBER PUZZLES (SECTION 18)
# -------------------------------------------------------------
def generate_satellite_circle_puzzle(center_val, pairs, filepath):
    """
    Renders HD vector spiral/satellite circle puzzle.
    center_val: central multiplier or base (e.g. 5)
    pairs: list of 5 (angle, value) tuples around the center.
    """
    ensure_dir(filepath)
    fig, ax = plt.subplots(figsize=(2.8, 2.8), dpi=300)
    ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(patches.Circle((0.5, 0.5), 0.22, facecolor='white', edgecolor='black', lw=2.4))
    ax.text(0.5, 0.5, str(center_val), fontsize=18, fontweight='bold', ha='center', va='center')

    r_sat = 0.15
    r_orb = 0.38
    for ang, val in pairs:
        rad = np.radians(ang)
        cx = 0.5 + r_orb * np.cos(rad)
        cy = 0.5 + r_orb * np.sin(rad)
        ax.add_patch(patches.Circle((cx, cy), r_sat, facecolor='white', edgecolor='black', lw=2.2))
        ax.text(cx, cy, str(val), fontsize=14, fontweight='bold', ha='center', va='center')

    ax.set_xlim(-0.06, 1.06); ax.set_ylim(-0.06, 1.06)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath


def generate_circle_quad_puzzle(data, filepath):
    """
    Renders 3 HD circles side by side with Top, Left, Bottom, Right, and Center numbers.
    data: list of 3 tuples (top, left, bottom, right, center)
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(1, len(data), figsize=(4.8, 1.8), dpi=300)
    if len(data) == 1:
        axes = [axes]
    for ax, (top, left, bot, right, center) in zip(axes, data):
        ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(patches.Circle((0.5, 0.5), 0.32, facecolor='white', edgecolor='black', lw=2.2))
        ax.text(0.5, 0.5, str(center), fontsize=15, fontweight='bold', ha='center', va='center')
        ax.text(0.5, 0.94, str(top), fontsize=14, fontweight='bold', ha='center', va='center')
        ax.text(0.5, 0.06, str(bot), fontsize=14, fontweight='bold', ha='center', va='center')
        ax.text(0.06, 0.5, str(left), fontsize=14, fontweight='bold', ha='center', va='center')
        ax.text(0.94, 0.5, str(right), fontsize=14, fontweight='bold', ha='center', va='center')
        ax.set_xlim(-0.08, 1.08); ax.set_ylim(-0.08, 1.08)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath


def generate_y_trees_puzzle(data, filepath):
    """
    Renders 3 HD Y-branch trees side by side with Left, Right, and Trunk numbers.
    data: list of 3 tuples (left, right, trunk)
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(1, len(data), figsize=(4.8, 2.0), dpi=300)
    if len(data) == 1:
        axes = [axes]
    for ax, (left, right, trunk) in zip(axes, data):
        ax.set_aspect('equal'); ax.axis('off')
        # Trunk stem and branches
        ax.plot([0.5, 0.5], [0.18, 0.55], 'k-', lw=2.4, zorder=1)
        ax.plot([0.5, 0.24], [0.55, 0.78], 'k-', lw=2.4, zorder=1)
        ax.plot([0.5, 0.76], [0.55, 0.78], 'k-', lw=2.4, zorder=1)
        
        r = 0.16
        ax.add_patch(patches.Circle((0.24, 0.78), r, facecolor='white', edgecolor='black', lw=2.2, zorder=2))
        ax.text(0.24, 0.78, str(left), fontsize=14, fontweight='bold', ha='center', va='center', zorder=3)
        
        ax.add_patch(patches.Circle((0.76, 0.78), r, facecolor='white', edgecolor='black', lw=2.2, zorder=2))
        ax.text(0.76, 0.78, str(right), fontsize=14, fontweight='bold', ha='center', va='center', zorder=3)
        
        ax.add_patch(patches.Circle((0.5, 0.18), r, facecolor='white', edgecolor='black', lw=2.2, zorder=2))
        ax.text(0.5, 0.18, str(trunk), fontsize=14, fontweight='bold', ha='center', va='center', zorder=3)
        
        ax.set_xlim(-0.02, 1.02); ax.set_ylim(-0.05, 1.02)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath


def generate_cross_boxed_puzzle(data, filepath):
    """
    Renders HD cross figures with Top, Bottom, Left, Right numbers and Center square box.
    data: list of tuples (top, bot, left, right, center)
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(1, len(data), figsize=(3.8, 1.8), dpi=300)
    if len(data) == 1:
        axes = [axes]
    for ax, (top, bot, left, right, center) in zip(axes, data):
        ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(patches.Rectangle((0.32, 0.32), 0.36, 0.36, facecolor='white', edgecolor='black', lw=2.2))
        ax.text(0.5, 0.5, str(center), fontsize=16, fontweight='bold', ha='center', va='center')
        ax.text(0.5, 0.88, str(top), fontsize=15, fontweight='bold', ha='center', va='center')
        ax.text(0.5, 0.12, str(bot), fontsize=15, fontweight='bold', ha='center', va='center')
        ax.text(0.12, 0.5, str(left), fontsize=15, fontweight='bold', ha='center', va='center')
        ax.text(0.88, 0.5, str(right), fontsize=15, fontweight='bold', ha='center', va='center')
        ax.set_xlim(-0.02, 1.02); ax.set_ylim(-0.02, 1.02)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath


def generate_cross_wing_puzzle(data, filepath):
    """
    Renders 3 HD X-wing figures with TL, TR, BL, BR circle petals and center diamond.
    data: list of tuples (tl, tr, bl, br, center)
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(1, len(data), figsize=(4.8, 1.8), dpi=300)
    if len(data) == 1:
        axes = [axes]
    for ax, (tl, tr, bl, br, center) in zip(axes, data):
        ax.set_aspect('equal'); ax.axis('off')
        # Center diamond
        diam = patches.Polygon([[0.5, 0.70], [0.70, 0.5], [0.5, 0.30], [0.30, 0.5]], closed=True, facecolor='white', edgecolor='black', lw=2.2, zorder=2)
        ax.add_patch(diam)
        ax.text(0.5, 0.5, str(center), fontsize=14, fontweight='bold', ha='center', va='center', zorder=3)
        
        # Diagonal bars
        ax.plot([0.24, 0.76], [0.24, 0.76], 'k-', lw=2.2, zorder=1)
        ax.plot([0.24, 0.76], [0.76, 0.24], 'k-', lw=2.2, zorder=1)
        
        r = 0.15
        pts = [(0.24, 0.76, tl), (0.76, 0.76, tr), (0.24, 0.24, bl), (0.76, 0.24, br)]
        for cx, cy, val in pts:
            ax.add_patch(patches.Circle((cx, cy), r, facecolor='white', edgecolor='black', lw=2.2, zorder=2))
            ax.text(cx, cy, str(val), fontsize=13, fontweight='bold', ha='center', va='center', zorder=3)
            
        ax.set_xlim(0.02, 0.98); ax.set_ylim(0.02, 0.98)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath


def generate_h_blocks_puzzle(data, filepath):
    """
    Renders 3 HD H-blocks with TL, BL, TR, BR corner boxes and central connector.
    data: list of tuples (tl, bl, tr, br, center)
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(1, len(data), figsize=(4.8, 1.8), dpi=300)
    if len(data) == 1:
        axes = [axes]
    for ax, (tl, bl, tr, br, center) in zip(axes, data):
        ax.set_aspect('equal'); ax.axis('off')
        # Center connector
        ax.add_patch(patches.Rectangle((0.30, 0.35), 0.40, 0.30, facecolor='white', edgecolor='black', lw=2.2, zorder=2))
        ax.text(0.5, 0.5, str(center), fontsize=14, fontweight='bold', ha='center', va='center', zorder=3)
        
        # Connecting vertical lines
        ax.plot([0.30, 0.30], [0.15, 0.85], 'k-', lw=2.4, zorder=1)
        ax.plot([0.70, 0.70], [0.15, 0.85], 'k-', lw=2.4, zorder=1)
        
        bw, bh = 0.28, 0.22
        boxes = [(0.06, 0.74, tl), (0.06, 0.04, bl), (0.66, 0.74, tr), (0.66, 0.04, br)]
        for bx, by, val in boxes:
            ax.add_patch(patches.Rectangle((bx, by), bw, bh, facecolor='white', edgecolor='black', lw=2.0, zorder=2))
            ax.text(bx + bw/2, by + bh/2, str(val), fontsize=13, fontweight='bold', ha='center', va='center', zorder=3)
            
        ax.set_xlim(0.0, 1.0); ax.set_ylim(-0.02, 1.02)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath

# Aliases for backward compatibility
generate_embedded_problem = generate_embedded_figure_problem
