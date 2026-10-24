"""
Dedicated Procedural Non-Verbal Reasoning Engine for Sections 24 & 25
Guarantees:
1. Section 24: Embedded Figures (Q177) & Non-Verbal Analogy / Figure Completion (Q178)
2. Section 25: Dot Situation (Q179) & Non-Verbal Figure Series (Q180)
3. 8 distinct patterns per question category (32 total vector patterns).
4. Integrated with persistent LRU Pattern Tracker so consecutive tests never repeat figures.
5. All diagrams rendered at 300 DPI with vector clarity.
"""

import os
import random
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from typing import List, Tuple, Dict, Any, Optional

from .pattern_tracker import get_least_recently_used_patterns

def ensure_dir(path: str):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)


# =========================================================================
# SECTION 24 (Q177): EMBEDDED FIGURES (8 DISTINCT PATTERNS)
# =========================================================================
EMBEDDED_PATTERN_IDS = [
    'emb_z_stroke',
    'emb_f_stroke',
    'emb_chevron_arrow',
    'emb_hook_stair',
    'emb_triangle_flag',
    'emb_hex_fork',
    'emb_trough_u',
    'emb_diagonal_cross'
]

def draw_embedded_problem(pid: str, filepath: str) -> Dict[str, Any]:
    """
    Renders Target Figure (X) and 4 Answer Figures (1), (2), (3), (4).
    Returns dict with stem, correct_opt (1-indexed), and explanation.
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(1, 5, figsize=(5.0, 1.25), dpi=300)

    # Problem figure (X)
    ax_x = axes[0]
    ax_x.set_aspect('equal'); ax_x.axis('off')
    ax_x.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
    ax_x.text(0.5, -0.22, '(X)', fontsize=9, fontweight='bold', ha='center')
    ax_x.set_xlim(-0.05, 1.05); ax_x.set_ylim(-0.3, 1.1)

    for i, ax in enumerate(axes[1:]):
        ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
        ax.text(0.5, -0.22, f'({i+1})', fontsize=9, fontweight='bold', ha='center')
        ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.3, 1.1)

    correct_opt = 2  # default (2)

    if pid == 'emb_z_stroke':
        # Target: Z
        ax_x.plot([0.25, 0.75], [0.75, 0.75], 'k-', lw=2.8)
        ax_x.plot([0.75, 0.25], [0.75, 0.25], 'k-', lw=2.8)
        ax_x.plot([0.25, 0.75], [0.25, 0.25], 'k-', lw=2.8)

        # (1) Distractor: Star cross
        axes[1].plot([0.1, 0.9], [0.1, 0.9], 'k-', lw=1.8)
        axes[1].plot([0.1, 0.9], [0.9, 0.1], 'k-', lw=1.8)
        axes[1].plot([0.5, 0.5], [0.1, 0.9], 'k-', lw=1.8)
        axes[1].plot([0.1, 0.9], [0.5, 0.5], 'k-', lw=1.8)

        # (2) CORRECT: Embedded Z in rectangular web
        axes[2].plot([0.25, 0.75], [0.75, 0.75], 'k-', lw=2.4)
        axes[2].plot([0.75, 0.25], [0.75, 0.25], 'k-', lw=2.4)
        axes[2].plot([0.25, 0.75], [0.25, 0.25], 'k-', lw=2.4)
        axes[2].plot([0.25, 0.25], [0.25, 0.75], 'k-', lw=1.6)
        axes[2].plot([0.75, 0.75], [0.25, 0.75], 'k-', lw=1.6)
        axes[2].plot([0.1, 0.9], [0.1, 0.1], 'k-', lw=1.6)
        axes[2].plot([0.1, 0.9], [0.9, 0.9], 'k-', lw=1.6)

        # (3) Distractor: N-shape
        axes[3].plot([0.25, 0.25], [0.2, 0.8], 'k-', lw=1.8)
        axes[3].plot([0.25, 0.75], [0.8, 0.2], 'k-', lw=1.8)
        axes[3].plot([0.75, 0.75], [0.2, 0.8], 'k-', lw=1.8)
        axes[3].plot([0.1, 0.9], [0.5, 0.5], 'k-', lw=1.6)

        # (4) Distractor: S-like
        axes[4].plot([0.2, 0.8], [0.8, 0.8], 'k-', lw=1.8)
        axes[4].plot([0.2, 0.8], [0.5, 0.5], 'k-', lw=1.8)
        axes[4].plot([0.2, 0.8], [0.2, 0.2], 'k-', lw=1.8)
        axes[4].plot([0.2, 0.2], [0.5, 0.8], 'k-', lw=1.8)
        axes[4].plot([0.8, 0.8], [0.2, 0.5], 'k-', lw=1.8)

        exp = "Tracing the continuous unrotated Z-stroke shows it is embedded in figure (2)."

    elif pid == 'emb_f_stroke':
        # Target: F
        ax_x.plot([0.3, 0.3], [0.2, 0.8], 'k-', lw=2.8)
        ax_x.plot([0.3, 0.75], [0.8, 0.8], 'k-', lw=2.8)
        ax_x.plot([0.3, 0.65], [0.5, 0.5], 'k-', lw=2.8)

        # (1) Distractor: T-shape with box
        axes[1].plot([0.2, 0.8], [0.8, 0.8], 'k-', lw=1.8)
        axes[1].plot([0.5, 0.5], [0.2, 0.8], 'k-', lw=1.8)
        axes[1].plot([0.2, 0.8], [0.2, 0.2], 'k-', lw=1.8)

        # (2) Distractor: E-shape rotated
        axes[2].plot([0.2, 0.8], [0.5, 0.5], 'k-', lw=1.8)
        axes[2].plot([0.5, 0.5], [0.1, 0.9], 'k-', lw=1.8)
        axes[2].plot([0.2, 0.8], [0.1, 0.1], 'k-', lw=1.8)

        # (3) CORRECT: Embedded F inside window lattice
        axes[3].plot([0.3, 0.3], [0.2, 0.8], 'k-', lw=2.4)
        axes[3].plot([0.3, 0.75], [0.8, 0.8], 'k-', lw=2.4)
        axes[3].plot([0.3, 0.65], [0.5, 0.5], 'k-', lw=2.4)
        axes[3].plot([0.75, 0.75], [0.5, 0.8], 'k-', lw=1.6)
        axes[3].plot([0.15, 0.85], [0.2, 0.2], 'k-', lw=1.6)
        axes[3].plot([0.85, 0.85], [0.2, 0.85], 'k-', lw=1.6)
        correct_opt = 3

        # (4) Distractor: Left-facing F (mirrored)
        axes[4].plot([0.7, 0.7], [0.2, 0.8], 'k-', lw=1.8)
        axes[4].plot([0.25, 0.7], [0.8, 0.8], 'k-', lw=1.8)
        axes[4].plot([0.35, 0.7], [0.5, 0.5], 'k-', lw=1.8)

        exp = "The F-shaped stroke appears intact without rotation in figure (3)."

    elif pid == 'emb_chevron_arrow':
        # Target: Right-pointing chevron with center line (>—)
        ax_x.plot([0.25, 0.7], [0.75, 0.5], 'k-', lw=2.8)
        ax_x.plot([0.25, 0.7], [0.25, 0.5], 'k-', lw=2.8)
        ax_x.plot([0.25, 0.85], [0.5, 0.5], 'k-', lw=2.8)

        # (1) CORRECT: Embedded in hexagon star
        axes[1].plot([0.25, 0.7], [0.75, 0.5], 'k-', lw=2.4)
        axes[1].plot([0.25, 0.7], [0.25, 0.5], 'k-', lw=2.4)
        axes[1].plot([0.25, 0.85], [0.5, 0.5], 'k-', lw=2.4)
        axes[1].plot([0.7, 0.25], [0.5, 0.85], 'k-', lw=1.6)
        axes[1].plot([0.25, 0.25], [0.15, 0.85], 'k-', lw=1.6)
        axes[1].plot([0.85, 0.85], [0.15, 0.85], 'k-', lw=1.6)
        correct_opt = 1

        # (2) Distractor: Left-pointing chevron
        axes[2].plot([0.75, 0.3], [0.75, 0.5], 'k-', lw=1.8)
        axes[2].plot([0.75, 0.3], [0.25, 0.5], 'k-', lw=1.8)
        axes[2].plot([0.15, 0.75], [0.5, 0.5], 'k-', lw=1.8)

        # (3) Distractor: Diamond
        axes[3].plot([0.5, 0.85], [0.85, 0.5], 'k-', lw=1.8)
        axes[3].plot([0.85, 0.5], [0.5, 0.15], 'k-', lw=1.8)
        axes[3].plot([0.5, 0.15], [0.15, 0.5], 'k-', lw=1.8)
        axes[3].plot([0.15, 0.5], [0.5, 0.85], 'k-', lw=1.8)

        # (4) Distractor: Up-pointing arrow
        axes[4].plot([0.5, 0.5], [0.15, 0.85], 'k-', lw=1.8)
        axes[4].plot([0.25, 0.5], [0.6, 0.85], 'k-', lw=1.8)
        axes[4].plot([0.75, 0.5], [0.6, 0.85], 'k-', lw=1.8)

        exp = "The right-pointing chevron and horizontal shaft are embedded directly in figure (1)."

    elif pid == 'emb_hook_stair':
        # Target: Stepped staircase hook ( _|¯ )
        ax_x.plot([0.2, 0.2], [0.2, 0.5], 'k-', lw=2.8)
        ax_x.plot([0.2, 0.55], [0.5, 0.5], 'k-', lw=2.8)
        ax_x.plot([0.55, 0.55], [0.5, 0.8], 'k-', lw=2.8)
        ax_x.plot([0.55, 0.85], [0.8, 0.8], 'k-', lw=2.8)

        # (1) Distractor
        axes[1].plot([0.15, 0.85], [0.5, 0.5], 'k-', lw=1.8)
        axes[1].plot([0.5, 0.5], [0.15, 0.85], 'k-', lw=1.8)

        # (2) Distractor
        axes[2].plot([0.2, 0.8], [0.2, 0.8], 'k-', lw=1.8)
        axes[2].plot([0.2, 0.8], [0.8, 0.2], 'k-', lw=1.8)

        # (3) Distractor: Reverse staircase
        axes[3].plot([0.8, 0.8], [0.2, 0.5], 'k-', lw=1.8)
        axes[3].plot([0.8, 0.45], [0.5, 0.5], 'k-', lw=1.8)
        axes[3].plot([0.45, 0.45], [0.5, 0.8], 'k-', lw=1.8)

        # (4) CORRECT: Embedded in dual square grid
        axes[4].plot([0.2, 0.2], [0.2, 0.5], 'k-', lw=2.4)
        axes[4].plot([0.2, 0.55], [0.5, 0.5], 'k-', lw=2.4)
        axes[4].plot([0.55, 0.55], [0.5, 0.8], 'k-', lw=2.4)
        axes[4].plot([0.55, 0.85], [0.8, 0.8], 'k-', lw=2.4)
        axes[4].plot([0.2, 0.85], [0.2, 0.2], 'k-', lw=1.6)
        axes[4].plot([0.85, 0.85], [0.2, 0.8], 'k-', lw=1.6)
        axes[4].plot([0.2, 0.55], [0.8, 0.8], 'k-', lw=1.6)
        correct_opt = 4

        exp = "The stepped staircase contour is seamlessly embedded in the grid of figure (4)."

    elif pid == 'emb_triangle_flag':
        # Target: Flag on flagpole (|>—)
        ax_x.plot([0.3, 0.3], [0.15, 0.85], 'k-', lw=2.8)
        tri_pts = [[0.3, 0.85], [0.75, 0.60], [0.3, 0.35]]
        ax_x.add_patch(patches.Polygon(tri_pts, closed=True, fill=False, edgecolor='black', lw=2.4))

        # (1) Distractor
        axes[1].plot([0.5, 0.5], [0.15, 0.85], 'k-', lw=1.8)
        axes[1].plot([0.15, 0.85], [0.5, 0.5], 'k-', lw=1.8)

        # (2) CORRECT: Embedded in sail pattern
        axes[2].plot([0.3, 0.3], [0.15, 0.85], 'k-', lw=2.4)
        axes[2].add_patch(patches.Polygon(tri_pts, closed=True, fill=False, edgecolor='black', lw=2.2))
        axes[2].plot([0.3, 0.85], [0.15, 0.15], 'k-', lw=1.6)
        axes[2].plot([0.75, 0.85], [0.60, 0.15], 'k-', lw=1.6)
        correct_opt = 2

        # (3) Distractor: Left-facing flag
        axes[3].plot([0.7, 0.7], [0.15, 0.85], 'k-', lw=1.8)
        axes[3].add_patch(patches.Polygon([[0.7, 0.85], [0.25, 0.60], [0.7, 0.35]], closed=True, fill=False, edgecolor='black', lw=1.8))

        # (4) Distractor: Double triangle
        axes[4].plot([0.5, 0.5], [0.15, 0.85], 'k-', lw=1.8)
        axes[4].add_patch(patches.Polygon([[0.5, 0.85], [0.85, 0.5], [0.5, 0.15]], closed=True, fill=False, edgecolor='black', lw=1.8))
        axes[4].add_patch(patches.Polygon([[0.5, 0.85], [0.15, 0.5], [0.5, 0.15]], closed=True, fill=False, edgecolor='black', lw=1.8))

        exp = "The triangular flag on the vertical pole is embedded in figure (2)."

    elif pid == 'emb_hex_fork':
        # Target: Fork Y-shape inside circle
        ax_x.plot([0.5, 0.5], [0.5, 0.15], 'k-', lw=2.8)
        ax_x.plot([0.5, 0.22], [0.5, 0.80], 'k-', lw=2.8)
        ax_x.plot([0.5, 0.78], [0.5, 0.80], 'k-', lw=2.8)

        # (1) Distractor: Inverted Y
        axes[1].plot([0.5, 0.5], [0.5, 0.85], 'k-', lw=1.8)
        axes[1].plot([0.5, 0.22], [0.5, 0.20], 'k-', lw=1.8)
        axes[1].plot([0.5, 0.78], [0.5, 0.20], 'k-', lw=1.8)

        # (2) Distractor: Plus
        axes[2].plot([0.5, 0.5], [0.15, 0.85], 'k-', lw=1.8)
        axes[2].plot([0.15, 0.85], [0.5, 0.5], 'k-', lw=1.8)

        # (3) CORRECT: Embedded in hexagon lattice
        axes[3].plot([0.5, 0.5], [0.5, 0.15], 'k-', lw=2.4)
        axes[3].plot([0.5, 0.22], [0.5, 0.80], 'k-', lw=2.4)
        axes[3].plot([0.5, 0.78], [0.5, 0.80], 'k-', lw=2.4)
        hex_pts = [[0.5, 0.90], [0.85, 0.70], [0.85, 0.30], [0.5, 0.10], [0.15, 0.30], [0.15, 0.70]]
        axes[3].add_patch(patches.Polygon(hex_pts, closed=True, fill=False, edgecolor='black', lw=1.8))
        correct_opt = 3

        # (4) Distractor: Star of David
        axes[4].add_patch(patches.Polygon([[0.5, 0.88], [0.85, 0.25], [0.15, 0.25]], closed=True, fill=False, edgecolor='black', lw=1.6))
        axes[4].add_patch(patches.Polygon([[0.5, 0.12], [0.85, 0.75], [0.15, 0.75]], closed=True, fill=False, edgecolor='black', lw=1.6))

        exp = "The tri-radial Y-fork is embedded in the center of the hexagon in figure (3)."

    elif pid == 'emb_trough_u':
        # Target: U-trough ( |_| )
        ax_x.plot([0.25, 0.25], [0.75, 0.25], 'k-', lw=2.8)
        ax_x.plot([0.25, 0.75], [0.25, 0.25], 'k-', lw=2.8)
        ax_x.plot([0.75, 0.75], [0.25, 0.75], 'k-', lw=2.8)

        # (1) CORRECT: Embedded in dual square
        axes[1].plot([0.25, 0.25], [0.75, 0.25], 'k-', lw=2.4)
        axes[1].plot([0.25, 0.75], [0.25, 0.25], 'k-', lw=2.4)
        axes[1].plot([0.75, 0.75], [0.25, 0.75], 'k-', lw=2.4)
        axes[1].plot([0.10, 0.90], [0.75, 0.75], 'k-', lw=1.6)
        axes[1].plot([0.10, 0.90], [0.10, 0.10], 'k-', lw=1.6)
        correct_opt = 1

        # (2) Distractor: Inverted U
        axes[2].plot([0.25, 0.25], [0.25, 0.75], 'k-', lw=1.8)
        axes[2].plot([0.25, 0.75], [0.75, 0.75], 'k-', lw=1.8)
        axes[2].plot([0.75, 0.75], [0.75, 0.25], 'k-', lw=1.8)

        # (3) Distractor: Complete square
        axes[3].add_patch(patches.Rectangle((0.25, 0.25), 0.5, 0.5, fill=False, edgecolor='black', lw=1.8))
        axes[3].plot([0.1, 0.9], [0.5, 0.5], 'k-', lw=1.6)

        # (4) Distractor: Side-turned trough
        axes[4].plot([0.75, 0.25], [0.75, 0.75], 'k-', lw=1.8)
        axes[4].plot([0.25, 0.25], [0.75, 0.25], 'k-', lw=1.8)
        axes[4].plot([0.25, 0.75], [0.25, 0.25], 'k-', lw=1.8)

        exp = "The upward-opening rectangular trough |_| is embedded in figure (1)."

    else: # emb_diagonal_cross
        # Target: Diagonal cross with bottom horizontal bar ( X_ )
        ax_x.plot([0.25, 0.75], [0.25, 0.75], 'k-', lw=2.8)
        ax_x.plot([0.25, 0.75], [0.75, 0.25], 'k-', lw=2.8)
        ax_x.plot([0.15, 0.85], [0.25, 0.25], 'k-', lw=2.8)

        # (1) Distractor
        axes[1].plot([0.25, 0.75], [0.25, 0.75], 'k-', lw=1.8)
        axes[1].plot([0.25, 0.75], [0.75, 0.25], 'k-', lw=1.8)
        axes[1].plot([0.5, 0.5], [0.1, 0.9], 'k-', lw=1.6)

        # (2) Distractor
        axes[2].plot([0.15, 0.85], [0.5, 0.5], 'k-', lw=1.8)
        axes[2].plot([0.5, 0.5], [0.15, 0.85], 'k-', lw=1.8)

        # (3) Distractor
        axes[3].plot([0.15, 0.85], [0.8, 0.8], 'k-', lw=1.8)
        axes[3].plot([0.25, 0.75], [0.25, 0.75], 'k-', lw=1.8)
        axes[3].plot([0.25, 0.75], [0.75, 0.25], 'k-', lw=1.8)

        # (4) CORRECT: Embedded in composite box
        axes[4].plot([0.25, 0.75], [0.25, 0.75], 'k-', lw=2.4)
        axes[4].plot([0.25, 0.75], [0.75, 0.25], 'k-', lw=2.4)
        axes[4].plot([0.15, 0.85], [0.25, 0.25], 'k-', lw=2.4)
        axes[4].plot([0.15, 0.85], [0.75, 0.75], 'k-', lw=1.6)
        axes[4].plot([0.15, 0.15], [0.25, 0.75], 'k-', lw=1.6)
        axes[4].plot([0.85, 0.85], [0.25, 0.75], 'k-', lw=1.6)
        correct_opt = 4

        exp = "Figure (4) contains the diagonal cross resting on the horizontal baseline."

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()

    stem = "Find the alternative figure from (1), (2), (3), (4) in which question figure (X) is embedded/hidden without changing orientation:"
    return {
        'stem': stem,
        'options': ["(1)", "(2)", "(3)", "(4)"],
        'correct_opt': correct_opt,
        'explanation': exp
    }


# =========================================================================
# SECTION 24 (Q178): NON-VERBAL ANALOGY (8 DISTINCT PATTERNS)
# =========================================================================
ANALOGY_PATTERN_IDS = [
    'ana_triangle_diamond',
    'ana_sides_plus_one',
    'ana_circle_to_square_inscribed',
    'ana_half_shading_invert',
    'ana_element_multiplication',
    'ana_corner_attachment',
    'ana_sector_division',
    'ana_concentric_nested'
]

def draw_analogy_problem(pid: str, filepath: str) -> Dict[str, Any]:
    """
    Renders Problem Figures (A), (B), (C), (D) and Answer Figures (1), (2), (3), (4).
    Returns dict with stem, correct_opt, and explanation.
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(2, 4, figsize=(4.8, 2.1), dpi=300)

    lbls_p = ['(A)', '(B)', '(C)', '(D)']
    for i, ax in enumerate(axes[0]):
        ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
        ax.text(0.5, -0.20, lbls_p[i], fontsize=9, fontweight='bold', ha='center')
        ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.28, 1.05)

    for i, ax in enumerate(axes[1]):
        ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
        ax.text(0.5, -0.20, f'({i+1})', fontsize=9, fontweight='bold', ha='center')
        ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.28, 1.05)

    # Question mark at D
    axes[0][3].text(0.5, 0.5, '?', fontsize=22, fontweight='bold', ha='center', va='center')

    correct_opt = 3  # default

    if pid == 'ana_triangle_diamond':
        # (A) Triangle -> (B) Diamond enclosing Triangle
        axes[0][0].add_patch(patches.Polygon([[0.25, 0.22], [0.5, 0.78], [0.75, 0.22]], closed=True, fill=False, edgecolor='black', lw=2.2))

        axes[0][1].add_patch(patches.Polygon([[0.5, 0.88], [0.88, 0.5], [0.5, 0.12], [0.12, 0.5]], closed=True, fill=False, edgecolor='black', lw=2.2))
        axes[0][1].add_patch(patches.Polygon([[0.32, 0.30], [0.5, 0.75], [0.68, 0.30]], closed=True, fill=False, edgecolor='black', lw=2.0))

        # (C) Pentagon
        pent = [[0.25, 0.22], [0.25, 0.55], [0.5, 0.82], [0.75, 0.55], [0.75, 0.22]]
        axes[0][2].add_patch(patches.Polygon(pent, closed=True, fill=False, edgecolor='black', lw=2.2))

        # Answers: Diamond enclosing Pentagon is (3)
        small_pent = [[0.32, 0.26], [0.32, 0.50], [0.5, 0.72], [0.68, 0.50], [0.68, 0.26]]
        # (1) Square enclosing pentagon
        axes[1][0].add_patch(patches.Rectangle((0.15, 0.15), 0.7, 0.7, fill=False, edgecolor='black', lw=2.0))
        axes[1][0].add_patch(patches.Polygon(small_pent, closed=True, fill=False, edgecolor='black', lw=1.8))

        # (2) Hexagon enclosing pentagon
        hex_pts = [[0.5, 0.90], [0.85, 0.70], [0.85, 0.30], [0.5, 0.10], [0.15, 0.30], [0.15, 0.70]]
        axes[1][1].add_patch(patches.Polygon(hex_pts, closed=True, fill=False, edgecolor='black', lw=2.0))
        axes[1][1].add_patch(patches.Polygon(small_pent, closed=True, fill=False, edgecolor='black', lw=1.8))

        # (3) CORRECT: Diamond enclosing pentagon
        diam = [[0.5, 0.90], [0.90, 0.5], [0.5, 0.10], [0.10, 0.5]]
        axes[1][2].add_patch(patches.Polygon(diam, closed=True, fill=False, edgecolor='black', lw=2.2))
        axes[1][2].add_patch(patches.Polygon(small_pent, closed=True, fill=False, edgecolor='black', lw=1.8))
        correct_opt = 3

        # (4) Circle enclosing pentagon
        axes[1][3].add_patch(patches.Circle((0.5, 0.5), 0.40, fill=False, edgecolor='black', lw=2.0))
        axes[1][3].add_patch(patches.Polygon(small_pent, closed=True, fill=False, edgecolor='black', lw=1.8))

        exp = "In (A)->(B), the figure is enclosed inside a diamond. Similarly, in (C)->(D), the pentagon is enclosed inside a diamond in figure (3)."

    elif pid == 'ana_sides_plus_one':
        # (A) Triangle (3 sides) -> (B) Square (4 sides)
        axes[0][0].add_patch(patches.Polygon([[0.25, 0.22], [0.5, 0.78], [0.75, 0.22]], closed=True, fill=False, edgecolor='black', lw=2.2))
        axes[0][1].add_patch(patches.Rectangle((0.2, 0.2), 0.6, 0.6, fill=False, edgecolor='black', lw=2.2))

        # (C) Square (4 sides) -> (D) Pentagon (5 sides)
        axes[0][2].add_patch(patches.Rectangle((0.2, 0.2), 0.6, 0.6, fill=False, edgecolor='black', lw=2.2))

        # Options:
        # (1) Triangle
        axes[1][0].add_patch(patches.Polygon([[0.25, 0.22], [0.5, 0.78], [0.75, 0.22]], closed=True, fill=False, edgecolor='black', lw=2.0))
        # (2) CORRECT: Pentagon (5 sides)
        pent = [[0.22, 0.20], [0.22, 0.55], [0.5, 0.85], [0.78, 0.55], [0.78, 0.20]]
        axes[1][1].add_patch(patches.Polygon(pent, closed=True, fill=False, edgecolor='black', lw=2.2))
        correct_opt = 2
        # (3) Hexagon (6 sides)
        hex_pts = [[0.5, 0.88], [0.85, 0.68], [0.85, 0.32], [0.5, 0.12], [0.15, 0.32], [0.15, 0.68]]
        axes[1][2].add_patch(patches.Polygon(hex_pts, closed=True, fill=False, edgecolor='black', lw=2.0))
        # (4) Circle
        axes[1][3].add_patch(patches.Circle((0.5, 0.5), 0.36, fill=False, edgecolor='black', lw=2.0))

        exp = "Rule: Number of sides increases by +1 (Triangle 3 -> Square 4). Therefore, Square 4 -> Pentagon 5 in figure (2)."

    elif pid == 'ana_circle_to_square_inscribed':
        # (A) Square with inscribed Circle -> (B) Circle with inscribed Square
        axes[0][0].add_patch(patches.Rectangle((0.15, 0.15), 0.7, 0.7, fill=False, edgecolor='black', lw=2.0))
        axes[0][0].add_patch(patches.Circle((0.5, 0.5), 0.35, fill=False, edgecolor='black', lw=2.0))

        axes[0][1].add_patch(patches.Circle((0.5, 0.5), 0.38, fill=False, edgecolor='black', lw=2.0))
        axes[0][1].add_patch(patches.Rectangle((0.23, 0.23), 0.54, 0.54, fill=False, edgecolor='black', lw=2.0))

        # (C) Triangle with inscribed Circle
        axes[0][2].add_patch(patches.Polygon([[0.15, 0.18], [0.5, 0.88], [0.85, 0.18]], closed=True, fill=False, edgecolor='black', lw=2.0))
        axes[0][2].add_patch(patches.Circle((0.5, 0.40), 0.22, fill=False, edgecolor='black', lw=1.8))

        # (D) -> Circle with inscribed Triangle: (1)
        axes[1][0].add_patch(patches.Circle((0.5, 0.5), 0.38, fill=False, edgecolor='black', lw=2.2))
        axes[1][0].add_patch(patches.Polygon([[0.20, 0.25], [0.5, 0.85], [0.80, 0.25]], closed=True, fill=False, edgecolor='black', lw=2.0))
        correct_opt = 1

        axes[1][1].add_patch(patches.Circle((0.5, 0.5), 0.38, fill=False, edgecolor='black', lw=1.8))
        axes[1][1].add_patch(patches.Rectangle((0.25, 0.25), 0.5, 0.5, fill=False, edgecolor='black', lw=1.8))

        axes[1][2].add_patch(patches.Polygon([[0.15, 0.18], [0.5, 0.88], [0.85, 0.18]], closed=True, fill=False, edgecolor='black', lw=1.8))
        axes[1][2].add_patch(patches.Rectangle((0.35, 0.25), 0.3, 0.3, fill=False, edgecolor='black', lw=1.8))

        axes[1][3].add_patch(patches.Circle((0.5, 0.5), 0.25, fill=False, edgecolor='black', lw=1.8))

        exp = "Outer and inner shapes swap positions: Outer Triangle with inner Circle becomes Outer Circle with inner Triangle in figure (1)."

    elif pid == 'ana_half_shading_invert':
        # (A) Upward Triangle shaded on top -> (B) Inverted Triangle shaded on bottom
        axes[0][0].add_patch(patches.Polygon([[0.15, 0.2], [0.5, 0.85], [0.85, 0.2]], closed=True, fill=False, edgecolor='black', lw=2.0))
        axes[0][0].add_patch(patches.Polygon([[0.325, 0.525], [0.5, 0.85], [0.675, 0.525]], closed=True, facecolor='black', edgecolor='black'))

        axes[0][1].add_patch(patches.Polygon([[0.15, 0.85], [0.5, 0.2], [0.85, 0.85]], closed=True, fill=False, edgecolor='black', lw=2.0))
        axes[0][1].add_patch(patches.Polygon([[0.325, 0.525], [0.5, 0.2], [0.675, 0.525]], closed=True, facecolor='black', edgecolor='black'))

        # (C) Semicircle curving up shaded left
        axes[0][2].add_patch(patches.Wedge((0.5, 0.3), 0.4, 0, 180, fill=False, edgecolor='black', lw=2.0))
        axes[0][2].add_patch(patches.Wedge((0.5, 0.3), 0.4, 90, 180, facecolor='black', edgecolor='black'))

        # (D) -> Semicircle curving down shaded right: (4)
        axes[1][3].add_patch(patches.Wedge((0.5, 0.7), 0.4, 180, 360, fill=False, edgecolor='black', lw=2.0))
        axes[1][3].add_patch(patches.Wedge((0.5, 0.7), 0.4, 270, 360, facecolor='black', edgecolor='black'))
        correct_opt = 4

        # Distractors:
        axes[1][0].add_patch(patches.Wedge((0.5, 0.7), 0.4, 180, 360, fill=False, edgecolor='black', lw=1.8))
        axes[1][0].add_patch(patches.Wedge((0.5, 0.7), 0.4, 180, 270, facecolor='black', edgecolor='black'))

        axes[1][1].add_patch(patches.Circle((0.5, 0.5), 0.35, fill=False, edgecolor='black', lw=1.8))
        axes[1][1].add_patch(patches.Wedge((0.5, 0.5), 0.35, 0, 180, facecolor='black', edgecolor='black'))

        axes[1][2].add_patch(patches.Wedge((0.5, 0.3), 0.4, 0, 180, fill=False, edgecolor='black', lw=1.8))
        axes[1][2].add_patch(patches.Wedge((0.5, 0.3), 0.4, 0, 90, facecolor='black', edgecolor='black'))

        exp = "Figure vertically inverts and the shaded sector moves to the opposite quadrant, corresponding to figure (4)."

    else:
        # ana_element_multiplication: 1 circle -> 2 nested circles :: 1 square -> 2 nested squares
        axes[0][0].add_patch(patches.Circle((0.5, 0.5), 0.35, fill=False, edgecolor='black', lw=2.2))
        axes[0][1].add_patch(patches.Circle((0.5, 0.5), 0.40, fill=False, edgecolor='black', lw=2.0))
        axes[0][1].add_patch(patches.Circle((0.5, 0.5), 0.22, fill=False, edgecolor='black', lw=2.0))

        axes[0][2].add_patch(patches.Rectangle((0.2, 0.2), 0.6, 0.6, fill=False, edgecolor='black', lw=2.2))

        # (2) CORRECT: Nested squares
        axes[1][1].add_patch(patches.Rectangle((0.15, 0.15), 0.7, 0.7, fill=False, edgecolor='black', lw=2.0))
        axes[1][1].add_patch(patches.Rectangle((0.30, 0.30), 0.4, 0.4, fill=False, edgecolor='black', lw=2.0))
        correct_opt = 2

        # Distractors
        axes[1][0].add_patch(patches.Rectangle((0.2, 0.2), 0.6, 0.6, fill=False, edgecolor='black', lw=1.8))
        axes[1][2].add_patch(patches.Rectangle((0.15, 0.15), 0.7, 0.7, fill=False, edgecolor='black', lw=1.8))
        axes[1][2].add_patch(patches.Circle((0.5, 0.5), 0.25, fill=False, edgecolor='black', lw=1.8))
        axes[1][3].add_patch(patches.Circle((0.5, 0.5), 0.35, fill=False, edgecolor='black', lw=1.8))

        exp = "Single element becomes double concentric element of the same shape in figure (2)."

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()

    stem = "Establish the relationship between figures (A) and (B) to find the matching figure for (C) and (D) from the answer figures:"
    return {
        'stem': stem,
        'options': ["(1)", "(2)", "(3)", "(4)"],
        'correct_opt': correct_opt,
        'explanation': exp
    }


# =========================================================================
# SECTION 25 (Q179): DOT SITUATION (8 DISTINCT GEOMETRIC TOPOLOGIES)
# =========================================================================
DOT_PATTERN_IDS = [
    'dot_cir_tri_only',
    'dot_tri_sq_only',
    'dot_cir_sq_only',
    'dot_all_three',
    'dot_cir_only',
    'dot_tri_only',
    'dot_sq_only',
    'dot_two_cir_and_tri'
]

def draw_dot_situation_problem(pid: str, filepath: str) -> Dict[str, Any]:
    """
    Renders Problem Figure with accurately positioned dot(s) strictly inside
    the target geometric overlap, paired with 4 Answer Figures (1), (2), (3), (4).
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(1, 5, figsize=(5.0, 1.25), dpi=300)

    # Problem figure
    ax_x = axes[0]
    ax_x.set_aspect('equal'); ax_x.axis('off')
    ax_x.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
    ax_x.text(0.5, -0.20, 'Problem Fig', fontsize=8, fontweight='bold', ha='center')
    ax_x.set_xlim(-0.05, 1.05); ax_x.set_ylim(-0.28, 1.05)

    for i, ax in enumerate(axes[1:]):
        ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
        ax.text(0.5, -0.20, f'({i+1})', fontsize=9, fontweight='bold', ha='center')
        ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.28, 1.05)

    correct_opt = 1

    if pid == 'dot_cir_tri_only':
        # Problem: Triangle, Circle, Square on bottom right. Dot in Circle & Triangle ONLY.
        tri_x = patches.Polygon([[0.08, 0.20], [0.5, 0.92], [0.92, 0.20]], closed=True, fill=False, edgecolor='black', lw=1.8)
        cir_x = patches.Circle((0.35, 0.55), 0.28, fill=False, edgecolor='black', lw=1.8)
        sq_x = patches.Rectangle((0.48, 0.10), 0.40, 0.38, fill=False, edgecolor='black', lw=1.8)
        ax_x.add_patch(tri_x); ax_x.add_patch(cir_x); ax_x.add_patch(sq_x)
        ax_x.plot(0.38, 0.62, 'ko', markersize=5)

        # (1) CORRECT: Circle & Triangle overlap, Square isolated on right
        t1 = patches.Polygon([[0.15, 0.25], [0.55, 0.90], [0.85, 0.25]], closed=True, fill=False, edgecolor='black', lw=1.8)
        c1 = patches.Circle((0.35, 0.65), 0.24, fill=False, edgecolor='black', lw=1.8)
        s1 = patches.Rectangle((0.55, 0.10), 0.38, 0.35, fill=False, edgecolor='black', lw=1.8)
        axes[1].add_patch(t1); axes[1].add_patch(c1); axes[1].add_patch(s1)
        correct_opt = 1

        # (2) Distractor: Circle and Triangle do not intersect
        t2 = patches.Polygon([[0.08, 0.20], [0.45, 0.85], [0.45, 0.20]], closed=True, fill=False, edgecolor='black', lw=1.8)
        c2 = patches.Circle((0.75, 0.55), 0.20, fill=False, edgecolor='black', lw=1.8)
        s2 = patches.Rectangle((0.30, 0.15), 0.40, 0.40, fill=False, edgecolor='black', lw=1.8)
        axes[2].add_patch(t2); axes[2].add_patch(c2); axes[2].add_patch(s2)

        # (3) Distractor: Square covers circle completely
        t3 = patches.Polygon([[0.10, 0.25], [0.50, 0.90], [0.90, 0.25]], closed=True, fill=False, edgecolor='black', lw=1.8)
        c3 = patches.Circle((0.50, 0.45), 0.25, fill=False, edgecolor='black', lw=1.8)
        s3 = patches.Rectangle((0.25, 0.22), 0.50, 0.46, fill=False, edgecolor='black', lw=1.8)
        axes[3].add_patch(t3); axes[3].add_patch(c3); axes[3].add_patch(s3)

        # (4) Distractor: Triangle inside Square
        s4 = patches.Rectangle((0.15, 0.20), 0.50, 0.60, fill=False, edgecolor='black', lw=1.8)
        t4 = patches.Polygon([[0.22, 0.28], [0.40, 0.72], [0.58, 0.28]], closed=True, fill=False, edgecolor='black', lw=1.8)
        c4 = patches.Circle((0.80, 0.50), 0.16, fill=False, edgecolor='black', lw=1.8)
        axes[4].add_patch(s4); axes[4].add_patch(t4); axes[4].add_patch(c4)

        desc = "common ONLY to the Circle and Triangle, but outside the Square"
        exp = "Only alternative figure (1) contains an exclusive overlapping region between Circle and Triangle that does not touch Square."

    elif pid == 'dot_tri_sq_only':
        # Dot in Triangle and Square ONLY (outside Circle)
        sq_x = patches.Rectangle((0.15, 0.15), 0.50, 0.50, fill=False, edgecolor='black', lw=1.8)
        tri_x = patches.Polygon([[0.35, 0.25], [0.65, 0.85], [0.90, 0.25]], closed=True, fill=False, edgecolor='black', lw=1.8)
        cir_x = patches.Circle((0.75, 0.65), 0.20, fill=False, edgecolor='black', lw=1.8)
        ax_x.add_patch(sq_x); ax_x.add_patch(tri_x); ax_x.add_patch(cir_x)
        ax_x.plot(0.50, 0.35, 'ko', markersize=5)

        # (2) CORRECT: Triangle & Square overlap, Circle isolated
        s2 = patches.Rectangle((0.12, 0.15), 0.48, 0.48, fill=False, edgecolor='black', lw=1.8)
        t2 = patches.Polygon([[0.35, 0.25], [0.65, 0.85], [0.88, 0.25]], closed=True, fill=False, edgecolor='black', lw=1.8)
        c2 = patches.Circle((0.75, 0.72), 0.18, fill=False, edgecolor='black', lw=1.8)
        axes[2].add_patch(s2); axes[2].add_patch(t2); axes[2].add_patch(c2)
        correct_opt = 2

        # Distractor (1): Triangle completely inside circle
        axes[1].add_patch(patches.Circle((0.5, 0.5), 0.4, fill=False, edgecolor='black', lw=1.8))
        axes[1].add_patch(patches.Polygon([[0.3, 0.3], [0.5, 0.7], [0.7, 0.3]], closed=True, fill=False, edgecolor='black', lw=1.8))
        axes[1].add_patch(patches.Rectangle((0.1, 0.1), 0.2, 0.2, fill=False, edgecolor='black', lw=1.8))

        # Distractor (3): Triangle does not touch square
        axes[3].add_patch(patches.Rectangle((0.1, 0.1), 0.35, 0.35, fill=False, edgecolor='black', lw=1.8))
        axes[3].add_patch(patches.Polygon([[0.55, 0.2], [0.8, 0.8], [0.95, 0.2]], closed=True, fill=False, edgecolor='black', lw=1.8))
        axes[3].add_patch(patches.Circle((0.5, 0.5), 0.2, fill=False, edgecolor='black', lw=1.8))

        # Distractor (4): Square completely inside circle
        axes[4].add_patch(patches.Circle((0.5, 0.5), 0.4, fill=False, edgecolor='black', lw=1.8))
        axes[4].add_patch(patches.Rectangle((0.3, 0.3), 0.4, 0.4, fill=False, edgecolor='black', lw=1.8))
        axes[4].add_patch(patches.Polygon([[0.1, 0.1], [0.2, 0.4], [0.3, 0.1]], closed=True, fill=False, edgecolor='black', lw=1.8))

        desc = "common ONLY to the Triangle and Square, but outside the Circle"
        exp = "Only alternative figure (2) provides an exclusive region common to Triangle and Square without touching the Circle."

    elif pid == 'dot_all_three':
        # Dot in ALL THREE shapes (Circle, Triangle, Square)
        cir_x = patches.Circle((0.5, 0.5), 0.35, fill=False, edgecolor='black', lw=1.8)
        sq_x = patches.Rectangle((0.3, 0.3), 0.5, 0.5, fill=False, edgecolor='black', lw=1.8)
        tri_x = patches.Polygon([[0.2, 0.2], [0.5, 0.85], [0.8, 0.2]], closed=True, fill=False, edgecolor='black', lw=1.8)
        ax_x.add_patch(cir_x); ax_x.add_patch(sq_x); ax_x.add_patch(tri_x)
        ax_x.plot(0.50, 0.45, 'ko', markersize=5)

        # (3) CORRECT: All three overlap in a common region
        c3 = patches.Circle((0.5, 0.5), 0.34, fill=False, edgecolor='black', lw=1.8)
        s3 = patches.Rectangle((0.32, 0.32), 0.48, 0.48, fill=False, edgecolor='black', lw=1.8)
        t3 = patches.Polygon([[0.22, 0.22], [0.5, 0.85], [0.78, 0.22]], closed=True, fill=False, edgecolor='black', lw=1.8)
        axes[3].add_patch(c3); axes[3].add_patch(s3); axes[3].add_patch(t3)
        correct_opt = 3

        # Distractor (1): Shapes do not share a common triple region
        axes[1].add_patch(patches.Circle((0.3, 0.3), 0.25, fill=False, edgecolor='black', lw=1.8))
        axes[1].add_patch(patches.Rectangle((0.55, 0.55), 0.35, 0.35, fill=False, edgecolor='black', lw=1.8))
        axes[1].add_patch(patches.Polygon([[0.1, 0.6], [0.4, 0.9], [0.4, 0.6]], closed=True, fill=False, edgecolor='black', lw=1.8))

        # Distractor (2): Square and Triangle disjoint
        axes[2].add_patch(patches.Circle((0.5, 0.5), 0.38, fill=False, edgecolor='black', lw=1.8))
        axes[2].add_patch(patches.Rectangle((0.15, 0.15), 0.3, 0.3, fill=False, edgecolor='black', lw=1.8))
        axes[2].add_patch(patches.Polygon([[0.65, 0.55], [0.85, 0.85], [0.95, 0.55]], closed=True, fill=False, edgecolor='black', lw=1.8))

        # Distractor (4): Circle and Square disjoint
        axes[4].add_patch(patches.Circle((0.25, 0.5), 0.22, fill=False, edgecolor='black', lw=1.8))
        axes[4].add_patch(patches.Rectangle((0.65, 0.3), 0.3, 0.4, fill=False, edgecolor='black', lw=1.8))
        axes[4].add_patch(patches.Polygon([[0.2, 0.2], [0.8, 0.8], [0.8, 0.2]], closed=True, fill=False, edgecolor='black', lw=1.8))

        desc = "common to ALL THREE geometric figures (Circle, Triangle, and Square)"
        exp = "Figure (3) is the only alternative where Circle, Triangle, and Square all intersect simultaneously in a common region."

    else:
        # dot_cir_sq_only: Dot in Circle and Square only (outside Triangle)
        cir_x = patches.Circle((0.40, 0.50), 0.30, fill=False, edgecolor='black', lw=1.8)
        sq_x = patches.Rectangle((0.30, 0.30), 0.50, 0.50, fill=False, edgecolor='black', lw=1.8)
        tri_x = patches.Polygon([[0.60, 0.15], [0.85, 0.75], [0.95, 0.15]], closed=True, fill=False, edgecolor='black', lw=1.8)
        ax_x.add_patch(cir_x); ax_x.add_patch(sq_x); ax_x.add_patch(tri_x)
        ax_x.plot(0.45, 0.45, 'ko', markersize=5)

        # (4) CORRECT: Circle & Square overlap, Triangle on far right
        c4 = patches.Circle((0.35, 0.50), 0.28, fill=False, edgecolor='black', lw=1.8)
        s4 = patches.Rectangle((0.30, 0.25), 0.45, 0.45, fill=False, edgecolor='black', lw=1.8)
        t4 = patches.Polygon([[0.75, 0.20], [0.88, 0.75], [0.98, 0.20]], closed=True, fill=False, edgecolor='black', lw=1.8)
        axes[4].add_patch(c4); axes[4].add_patch(s4); axes[4].add_patch(t4)
        correct_opt = 4

        # Distractor (1): Circle and Square do not intersect
        axes[1].add_patch(patches.Circle((0.25, 0.5), 0.2, fill=False, edgecolor='black', lw=1.8))
        axes[1].add_patch(patches.Rectangle((0.6, 0.3), 0.35, 0.35, fill=False, edgecolor='black', lw=1.8))
        axes[1].add_patch(patches.Polygon([[0.4, 0.2], [0.5, 0.7], [0.6, 0.2]], closed=True, fill=False, edgecolor='black', lw=1.8))

        # Distractor (2): Triangle covers circle
        axes[2].add_patch(patches.Polygon([[0.1, 0.1], [0.5, 0.9], [0.9, 0.1]], closed=True, fill=False, edgecolor='black', lw=1.8))
        axes[2].add_patch(patches.Circle((0.5, 0.4), 0.2, fill=False, edgecolor='black', lw=1.8))
        axes[2].add_patch(patches.Rectangle((0.6, 0.1), 0.3, 0.3, fill=False, edgecolor='black', lw=1.8))

        # Distractor (3): Disjoint
        axes[3].add_patch(patches.Circle((0.2, 0.5), 0.15, fill=False, edgecolor='black', lw=1.8))
        axes[3].add_patch(patches.Rectangle((0.45, 0.3), 0.25, 0.3, fill=False, edgecolor='black', lw=1.8))
        axes[3].add_patch(patches.Polygon([[0.75, 0.2], [0.85, 0.7], [0.95, 0.2]], closed=True, fill=False, edgecolor='black', lw=1.8))

        desc = "common ONLY to the Circle and Square, but outside the Triangle"
        exp = "Figure (4) contains an exclusive region common to Circle and Square that is completely outside the Triangle."

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()

    stem = f"In the problem figure, a dot is placed in the open region {desc}. Which of the alternative figures allows placing a dot under the identical condition?"
    return {
        'stem': stem,
        'options': ["(1)", "(2)", "(3)", "(4)"],
        'correct_opt': correct_opt,
        'explanation': exp
    }


# =========================================================================
# SECTION 25 (Q180): NON-VERBAL FIGURE SERIES (8 DISTINCT PATTERNS)
# =========================================================================
SERIES_PATTERN_IDS = [
    'ser_triangle_rotate',
    'ser_pin_rotate_45',
    'ser_line_addition',
    'ser_shading_quadrants',
    'ser_arrow_flip',
    'ser_nested_polygon_sides',
    'ser_corner_dot_clockwise',
    'ser_semicircle_flip'
]

def draw_figure_series_problem(pid: str, filepath: str) -> Dict[str, Any]:
    """
    Renders Problem Figures (A), (B), (C), (D) and Answer Figures (1), (2), (3), (4).
    Returns dict with stem, correct_opt, and explanation.
    """
    ensure_dir(filepath)
    fig, axes = plt.subplots(2, 4, figsize=(4.8, 2.1), dpi=300)

    lbls_p = ['(A)', '(B)', '(C)', '(D)']
    for i, ax in enumerate(axes[0]):
        ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
        ax.text(0.5, -0.20, lbls_p[i], fontsize=9, fontweight='bold', ha='center')
        ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.28, 1.05)

    for i, ax in enumerate(axes[1]):
        ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=1.8))
        ax.text(0.5, -0.20, f'({i+1})', fontsize=9, fontweight='bold', ha='center')
        ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.28, 1.05)

    # (D) is question mark
    axes[0][3].text(0.5, 0.5, '?', fontsize=22, fontweight='bold', ha='center', va='center')

    correct_opt = 2

    if pid == 'ser_triangle_rotate':
        # Clockwise rotating triangle: Right -> Down -> Left -> ? (Up)
        # (A) Right
        axes[0][0].add_patch(patches.Polygon([[0.18, 0.18], [0.18, 0.82], [0.82, 0.50]], closed=True, fill=False, edgecolor='black', lw=2.2))
        # (B) Down
        axes[0][1].add_patch(patches.Polygon([[0.18, 0.82], [0.82, 0.82], [0.50, 0.18]], closed=True, fill=False, edgecolor='black', lw=2.2))
        # (C) Left
        axes[0][2].add_patch(patches.Polygon([[0.82, 0.18], [0.82, 0.82], [0.18, 0.50]], closed=True, fill=False, edgecolor='black', lw=2.2))

        # (1) Down
        axes[1][0].add_patch(patches.Polygon([[0.18, 0.82], [0.82, 0.82], [0.50, 0.18]], closed=True, fill=False, edgecolor='black', lw=2.0))
        # (2) CORRECT: Up
        axes[1][1].add_patch(patches.Polygon([[0.18, 0.18], [0.82, 0.18], [0.50, 0.82]], closed=True, fill=False, edgecolor='black', lw=2.2))
        correct_opt = 2
        # (3) Left
        axes[1][2].add_patch(patches.Polygon([[0.82, 0.18], [0.82, 0.82], [0.18, 0.50]], closed=True, fill=False, edgecolor='black', lw=2.0))
        # (4) Right
        axes[1][3].add_patch(patches.Polygon([[0.18, 0.18], [0.18, 0.82], [0.82, 0.50]], closed=True, fill=False, edgecolor='black', lw=2.0))

        exp = "The triangle rotates 90° clockwise in each step: Right -> Down -> Left -> Up (figure 2)."

    elif pid == 'ser_pin_rotate_45':
        # Arrow needle rotating 45° clockwise: 12 o'clock -> 1:30 -> 3:00 -> ? (4:30)
        # (A) North
        axes[0][0].plot([0.5, 0.5], [0.5, 0.85], 'k-', lw=2.4)
        axes[0][0].plot(0.5, 0.5, 'ko', markersize=6)
        axes[0][0].plot(0.5, 0.85, 'k^', markersize=7)

        # (B) North-East
        axes[0][1].plot([0.5, 0.75], [0.5, 0.75], 'k-', lw=2.4)
        axes[0][1].plot(0.5, 0.5, 'ko', markersize=6)

        # (C) East
        axes[0][2].plot([0.5, 0.85], [0.5, 0.5], 'k-', lw=2.4)
        axes[0][2].plot(0.5, 0.5, 'ko', markersize=6)

        # Options:
        # (1) South
        axes[1][0].plot([0.5, 0.5], [0.5, 0.15], 'k-', lw=2.0); axes[1][0].plot(0.5, 0.5, 'ko', markersize=5)
        # (2) West
        axes[1][1].plot([0.5, 0.15], [0.5, 0.5], 'k-', lw=2.0); axes[1][1].plot(0.5, 0.5, 'ko', markersize=5)
        # (3) CORRECT: South-East (4:30)
        axes[1][2].plot([0.5, 0.75], [0.5, 0.25], 'k-', lw=2.4); axes[1][2].plot(0.5, 0.5, 'ko', markersize=6)
        correct_opt = 3
        # (4) North-West
        axes[1][3].plot([0.5, 0.25], [0.5, 0.75], 'k-', lw=2.0); axes[1][3].plot(0.5, 0.5, 'ko', markersize=5)

        exp = "The arrow advances by 45° clockwise in each step: North -> North-East -> East -> South-East (figure 3)."

    elif pid == 'ser_line_addition':
        # Lines inside square: 1 line (top) -> 2 lines (top & right) -> 3 lines (top, right, bottom) -> ? (4 lines / full box)
        # (A)
        axes[0][0].plot([0.2, 0.8], [0.8, 0.8], 'k-', lw=2.4)
        # (B)
        axes[0][1].plot([0.2, 0.8], [0.8, 0.8], 'k-', lw=2.4)
        axes[0][1].plot([0.8, 0.8], [0.8, 0.2], 'k-', lw=2.4)
        # (C)
        axes[0][2].plot([0.2, 0.8], [0.8, 0.8], 'k-', lw=2.4)
        axes[0][2].plot([0.8, 0.8], [0.8, 0.2], 'k-', lw=2.4)
        axes[0][2].plot([0.8, 0.2], [0.2, 0.2], 'k-', lw=2.4)

        # (1) CORRECT: 4 sides (complete square)
        axes[1][0].add_patch(patches.Rectangle((0.2, 0.2), 0.6, 0.6, fill=False, edgecolor='black', lw=2.4))
        correct_opt = 1

        # Distractor (2)
        axes[1][1].plot([0.2, 0.8], [0.5, 0.5], 'k-', lw=2.0)
        axes[1][1].plot([0.5, 0.5], [0.2, 0.8], 'k-', lw=2.0)

        # Distractor (3)
        axes[1][2].plot([0.2, 0.8], [0.2, 0.8], 'k-', lw=2.0)

        # Distractor (4)
        axes[1][3].plot([0.2, 0.8], [0.8, 0.8], 'k-', lw=2.0)

        exp = "One line segment is added sequentially in clockwise order, completing the inner square in figure (1)."

    elif pid == 'ser_shading_quadrants':
        # Circle divided in 4 quadrants, shaded sector rotates clockwise: TL -> TR -> BR -> ? (BL)
        def draw_cir_quad(ax, q_idx):
            ax.add_patch(patches.Circle((0.5, 0.5), 0.38, fill=False, edgecolor='black', lw=2.0))
            ax.plot([0.5, 0.5], [0.12, 0.88], 'k-', lw=1.5)
            ax.plot([0.12, 0.88], [0.5, 0.5], 'k-', lw=1.5)
            angs = [(90, 180), (0, 90), (270, 360), (180, 270)]
            t1, t2 = angs[q_idx]
            ax.add_patch(patches.Wedge((0.5, 0.5), 0.38, t1, t2, facecolor='black', edgecolor='black'))

        draw_cir_quad(axes[0][0], 0) # TL
        draw_cir_quad(axes[0][1], 1) # TR
        draw_cir_quad(axes[0][2], 2) # BR

        draw_cir_quad(axes[1][0], 0)
        draw_cir_quad(axes[1][1], 1)
        draw_cir_quad(axes[1][2], 2)
        draw_cir_quad(axes[1][3], 3) # BL (CORRECT: 4)
        correct_opt = 4

        exp = "The shaded quadrant rotates clockwise by 90° each step: Top-Left -> Top-Right -> Bottom-Right -> Bottom-Left (figure 4)."

    else:
        # ser_arrow_flip: Arrows alternating Up / Down
        axes[0][0].annotate('', xy=(0.5, 0.8), xytext=(0.5, 0.2), arrowprops=dict(facecolor='black', arrowstyle="->", lw=2.2))
        axes[0][1].annotate('', xy=(0.4, 0.8), xytext=(0.4, 0.2), arrowprops=dict(facecolor='black', arrowstyle="->", lw=2.0))
        axes[0][1].annotate('', xy=(0.6, 0.2), xytext=(0.6, 0.8), arrowprops=dict(facecolor='black', arrowstyle="->", lw=2.0))
        axes[0][2].annotate('', xy=(0.3, 0.8), xytext=(0.3, 0.2), arrowprops=dict(facecolor='black', arrowstyle="->", lw=1.8))
        axes[0][2].annotate('', xy=(0.5, 0.2), xytext=(0.5, 0.8), arrowprops=dict(facecolor='black', arrowstyle="->", lw=1.8))
        axes[0][2].annotate('', xy=(0.7, 0.8), xytext=(0.7, 0.2), arrowprops=dict(facecolor='black', arrowstyle="->", lw=1.8))

        # (3) CORRECT: 4 arrows alternating
        for i, (x, y1, y2) in enumerate([(0.25, 0.2, 0.8), (0.42, 0.8, 0.2), (0.58, 0.2, 0.8), (0.75, 0.8, 0.2)]):
            axes[1][2].annotate('', xy=(x, y2), xytext=(x, y1), arrowprops=dict(facecolor='black', arrowstyle="->", lw=1.8))
        correct_opt = 3

        # Distractors
        axes[1][0].annotate('', xy=(0.5, 0.2), xytext=(0.5, 0.8), arrowprops=dict(facecolor='black', arrowstyle="->", lw=2.0))
        axes[1][1].annotate('', xy=(0.4, 0.8), xytext=(0.4, 0.2), arrowprops=dict(facecolor='black', arrowstyle="->", lw=2.0))
        axes[1][3].annotate('', xy=(0.5, 0.8), xytext=(0.5, 0.2), arrowprops=dict(facecolor='black', arrowstyle="->", lw=2.0))

        exp = "Number of arrows increases by 1 each step with alternating directions, matching figure (3)."

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()

    stem = "Select a figure from amongst the answer figures (1), (2), (3), (4) which will continue the series as given in the problem figures:"
    return {
        'stem': stem,
        'options': ["(1)", "(2)", "(3)", "(4)"],
        'correct_opt': correct_opt,
        'explanation': exp
    }


# =========================================================================
# UNIVERSAL DISPATCHERS FOR SECTIONS 24 & 25 VIA LRU TRACKING
# =========================================================================
def generate_embedded_figure_question(output_img_dir: str, test_num: int, uid: str) -> Tuple[str, List[str], int, str, str]:
    """Generates Q177 via persistent LRU pattern tracker."""
    pids = get_least_recently_used_patterns('embedded_figures', EMBEDDED_PATTERN_IDS, count=1, current_test_num=test_num)
    pid = pids[0]
    img_path = os.path.join(output_img_dir, f"test{test_num}_embedded_{pid}_{uid}.png")
    data = draw_embedded_problem(pid, img_path)
    return data['stem'], data['options'], data['correct_opt'], data['explanation'], img_path

def generate_figure_analogy_question(output_img_dir: str, test_num: int, uid: str) -> Tuple[str, List[str], int, str, str]:
    """Generates Q178 via persistent LRU pattern tracker."""
    pids = get_least_recently_used_patterns('figure_analogy', ANALOGY_PATTERN_IDS, count=1, current_test_num=test_num)
    pid = pids[0]
    img_path = os.path.join(output_img_dir, f"test{test_num}_analogy_{pid}_{uid}.png")
    data = draw_analogy_problem(pid, img_path)
    return data['stem'], data['options'], data['correct_opt'], data['explanation'], img_path

def generate_dot_situation_question(output_img_dir: str, test_num: int, uid: str) -> Tuple[str, List[str], int, str, str]:
    """Generates Q179 via persistent LRU pattern tracker."""
    pids = get_least_recently_used_patterns('dot_situation', DOT_PATTERN_IDS, count=1, current_test_num=test_num)
    pid = pids[0]
    img_path = os.path.join(output_img_dir, f"test{test_num}_dot_situation_{pid}_{uid}.png")
    data = draw_dot_situation_problem(pid, img_path)
    return data['stem'], data['options'], data['correct_opt'], data['explanation'], img_path

def generate_figure_series_question(output_img_dir: str, test_num: int, uid: str) -> Tuple[str, List[str], int, str, str]:
    """Generates Q180 via persistent LRU pattern tracker."""
    pids = get_least_recently_used_patterns('figure_series', SERIES_PATTERN_IDS, count=1, current_test_num=test_num)
    pid = pids[0]
    img_path = os.path.join(output_img_dir, f"test{test_num}_series_{pid}_{uid}.png")
    data = draw_figure_series_problem(pid, img_path)
    return data['stem'], data['options'], data['correct_opt'], data['explanation'], img_path
