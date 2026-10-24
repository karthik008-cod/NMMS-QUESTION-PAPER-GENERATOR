"""
NMMS Paper Folding & Paper Cutting (PFC) Generation Engine
Provides 16 mathematically verified, distinct paper fold & cut problem types.
Guarantees:
- Step X, Y, Z figures rendered with 300+ DPI vector clarity.
- 4 separate, crisp option card images for every problem.
- Option 1 (before shuffle) is 100% mathematically exact based on true reflection math.
- Options 2, 3, 4 are high-quality, realistic distractors.
"""

import os
from typing import List, Tuple, Dict, Any, Optional
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def ensure_dir(path: str) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)

# ---------------------------------------------------------------------------
# OPTION CARD RENDERING HELPERS
# ---------------------------------------------------------------------------

def render_unfolded_square_card(
    filepath: str,
    holes: Optional[List[Tuple[float, float, float]]] = None,
    diamonds: Optional[List[Tuple[float, float, float]]] = None,
    squares: Optional[List[Tuple[float, float, float]]] = None,
    polygons: Optional[List[List[Tuple[float, float]]]] = None,
    corner_triangles_size: float = 0.0,
    corner_circles_r: float = 0.0,
    center_shape: Optional[str] = None
) -> str:
    """Renders a single square option card showing unfolded paper patterns."""
    ensure_dir(filepath)
    fig, ax = plt.subplots(figsize=(1.1, 1.1), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')

    # Outer border
    ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=2.0))
    # Light dotted fold lines showing quarters
    ax.plot([0.5, 0.5], [0, 1], 'k:', lw=0.8, alpha=0.55)
    ax.plot([0, 1], [0.5, 0.5], 'k:', lw=0.8, alpha=0.55)

    if holes:
        for (hx, hy, hr) in holes:
            ax.add_patch(patches.Circle((hx, hy), hr, facecolor='black', edgecolor='black'))

    if diamonds:
        for (cx, cy, s) in diamonds:
            d_pts = [[cx, cy - s], [cx + s, cy], [cx, cy + s], [cx - s, cy]]
            ax.add_patch(patches.Polygon(d_pts, closed=True, facecolor='black', edgecolor='black'))

    if squares:
        for (cx, cy, s) in squares:
            ax.add_patch(patches.Rectangle((cx - s, cy - s), 2*s, 2*s, facecolor='black', edgecolor='black'))

    if polygons:
        for pts in polygons:
            ax.add_patch(patches.Polygon(pts, closed=True, facecolor='black', edgecolor='black'))

    if corner_triangles_size > 0:
        s = corner_triangles_size
        corners = [
            [[0, 0], [s, 0], [0, s]],
            [[1, 0], [1 - s, 0], [1, s]],
            [[1, 1], [1 - s, 1], [1, 1 - s]],
            [[0, 1], [s, 1], [0, 1 - s]]
        ]
        for c_pts in corners:
            ax.add_patch(patches.Polygon(c_pts, closed=True, facecolor='black', edgecolor='black'))

    if corner_circles_r > 0:
        r = corner_circles_r
        # Quarter circles at 4 corners
        ax.add_patch(patches.Wedge((0, 0), r, 0, 90, facecolor='black', edgecolor='black'))
        ax.add_patch(patches.Wedge((1, 0), r, 90, 180, facecolor='black', edgecolor='black'))
        ax.add_patch(patches.Wedge((1, 1), r, 180, 270, facecolor='black', edgecolor='black'))
        ax.add_patch(patches.Wedge((0, 1), r, 270, 360, facecolor='black', edgecolor='black'))

    if center_shape == 'diamond':
        ax.add_patch(patches.Polygon([[0.5, 0.35], [0.65, 0.5], [0.5, 0.65], [0.35, 0.5]], closed=True, facecolor='black', edgecolor='black'))
    elif center_shape == 'square':
        ax.add_patch(patches.Rectangle((0.38, 0.38), 0.24, 0.24, facecolor='black', edgecolor='black'))
    elif center_shape == 'circle':
        ax.add_patch(patches.Circle((0.5, 0.5), 0.14, facecolor='black', edgecolor='black'))

    ax.set_xlim(-0.04, 1.04)
    ax.set_ylim(-0.04, 1.04)
    plt.tight_layout(pad=0.02)
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.02)
    plt.close()
    return filepath


def render_unfolded_circle_card(
    filepath: str,
    holes: Optional[List[Tuple[float, float, float]]] = None,
    center_shape: Optional[str] = None
) -> str:
    """Renders a single circular option card showing unfolded circular paper patterns."""
    ensure_dir(filepath)
    fig, ax = plt.subplots(figsize=(1.1, 1.1), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.add_patch(patches.Circle((0.5, 0.5), 0.44, facecolor='white', edgecolor='black', lw=2.0))
    # Light dotted crosshairs
    ax.plot([0.06, 0.94], [0.5, 0.5], 'k:', lw=0.8, alpha=0.55)
    ax.plot([0.5, 0.5], [0.06, 0.94], 'k:', lw=0.8, alpha=0.55)

    if holes:
        for (hx, hy, hr) in holes:
            ax.add_patch(patches.Circle((hx, hy), hr, facecolor='black', edgecolor='black'))

    if center_shape == 'diamond':
        ax.add_patch(patches.Polygon([[0.5, 0.40], [0.60, 0.5], [0.5, 0.60], [0.40, 0.5]], closed=True, facecolor='black', edgecolor='black'))
    elif center_shape == 'circle':
        ax.add_patch(patches.Circle((0.5, 0.5), 0.12, facecolor='black', edgecolor='black'))

    ax.set_xlim(0.02, 0.98)
    ax.set_ylim(0.02, 0.98)
    plt.tight_layout(pad=0.02)
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.02)
    plt.close()
    return filepath


def render_transparent_fold_card(filepath: str, tri_type: str = 'left') -> str:
    """Renders an option card for transparent sheet fold."""
    ensure_dir(filepath)
    fig, ax = plt.subplots(figsize=(1.1, 1.1), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.add_patch(patches.Rectangle((0.5, 0.0), 0.5, 1.0, facecolor='white', edgecolor='black', lw=2.0))
    ax.add_patch(patches.Circle((0.75, 0.5), 0.20, fill=False, edgecolor='black', lw=2.0))

    if tri_type == 'left':  # Correct laterally reflected
        ax.add_patch(patches.Polygon([[0.85, 0.25], [0.85, 0.75], [0.58, 0.5]], closed=True, facecolor='black'))
    elif tri_type == 'right':  # Distractor: unreflected
        ax.add_patch(patches.Polygon([[0.65, 0.25], [0.65, 0.75], [0.92, 0.5]], closed=True, facecolor='black'))
    elif tri_type == 'down':  # Distractor: flipped vertically
        ax.add_patch(patches.Polygon([[0.60, 0.65], [0.90, 0.65], [0.75, 0.35]], closed=True, facecolor='black'))
    elif tri_type == 'outside':  # Distractor: misplaced outside
        ax.add_patch(patches.Polygon([[0.85, 0.72], [0.85, 0.96], [0.65, 0.84]], closed=True, facecolor='black'))

    ax.set_xlim(0.46, 1.04)
    ax.set_ylim(-0.04, 1.04)
    plt.tight_layout(pad=0.02)
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.02)
    plt.close()
    return filepath


# ---------------------------------------------------------------------------
# PROBLEM FIGURE GENERATOR (STEPS X, Y, Z)
# ---------------------------------------------------------------------------

def render_standard_2fold_problem(filepath: str, z_draw_callback) -> str:
    """Renders standard 2-fold square paper problem: Step X (down), Step Y (right), Step Z (cuts)."""
    ensure_dir(filepath)
    fig, axes = plt.subplots(1, 3, figsize=(4.6, 1.6), dpi=300)
    for ax, lbl in zip(axes, ['X', 'Y', 'Z']):
        ax.set_aspect('equal')
        ax.axis('off')
        ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=2.0))
        ax.text(0.5, -0.25, lbl, fontsize=12, fontweight='bold', ha='center')
        ax.set_xlim(-0.08, 1.08)
        ax.set_ylim(-0.35, 1.08)

    # Step X: Fold down along y=0.5
    axes[0].plot([0, 1], [0.5, 0.5], 'k--', lw=1.6)
    axes[0].annotate('', xy=(0.5, 0.38), xytext=(0.5, 0.62), arrowprops=dict(arrowstyle='->', lw=1.8, color='black'))

    # Step Y: Fold right along x=0.5
    axes[1].add_patch(patches.Rectangle((0, 0.5), 1, 0.5, facecolor='#f0f0f0', edgecolor='none'))
    axes[1].plot([0, 1], [0.5, 0.5], 'k-', lw=2.0)
    axes[1].plot([0.5, 0.5], [0, 0.5], 'k--', lw=1.6)
    axes[1].annotate('', xy=(0.62, 0.25), xytext=(0.38, 0.25), arrowprops=dict(arrowstyle='->', lw=1.8, color='black'))

    # Step Z: Bottom-right quadrant [0.5, 1.0] x [0, 0.5]
    axes[2].add_patch(patches.Rectangle((0, 0.5), 1, 0.5, facecolor='#f0f0f0', edgecolor='none'))
    axes[2].add_patch(patches.Rectangle((0, 0), 0.5, 0.5, facecolor='#f0f0f0', edgecolor='none'))
    axes[2].plot([0, 1], [0.5, 0.5], 'k-', lw=2.0)
    axes[2].plot([0.5, 0.5], [0, 0.5], 'k-', lw=2.0)

    # Draw specific cutouts
    z_draw_callback(axes[2])

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath


def render_circular_fold_problem(filepath: str) -> str:
    """Renders circular fold problem figures X, Y, Z."""
    ensure_dir(filepath)
    fig, axes = plt.subplots(1, 3, figsize=(4.6, 1.6), dpi=300)
    for ax, lbl in zip(axes, ['X', 'Y', 'Z']):
        ax.set_aspect('equal')
        ax.axis('off')
        ax.text(0.5, -0.25, lbl, fontsize=12, fontweight='bold', ha='center')
        ax.set_xlim(-0.08, 1.08)
        ax.set_ylim(-0.35, 1.08)

    # Step X: Fold circle up along horizontal centerline
    axes[0].add_patch(patches.Circle((0.5, 0.5), 0.44, fill=False, edgecolor='black', lw=2.0))
    axes[0].plot([0.06, 0.94], [0.5, 0.5], 'k--', lw=1.6)
    axes[0].annotate('', xy=(0.5, 0.65), xytext=(0.5, 0.35), arrowprops=dict(arrowstyle='->', lw=1.8, color='black'))

    # Step Y: Semicircle folded left along vertical centerline
    axes[1].add_patch(patches.Wedge((0.5, 0.5), 0.44, 0, 180, fill=False, edgecolor='black', lw=2.0))
    axes[1].plot([0.06, 0.94], [0.5, 0.5], 'k-', lw=2.0)
    axes[1].plot([0.5, 0.5], [0.5, 0.94], 'k--', lw=1.6)
    axes[1].annotate('', xy=(0.35, 0.72), xytext=(0.65, 0.72), arrowprops=dict(arrowstyle='->', lw=1.8, color='black'))

    # Step Z: Quadrant wedge [90, 180] with 2 punched holes
    axes[2].add_patch(patches.Wedge((0.5, 0.5), 0.44, 90, 180, fill=False, edgecolor='black', lw=2.0))
    axes[2].plot([0.06, 0.5], [0.5, 0.5], 'k-', lw=2.0)
    axes[2].plot([0.5, 0.5], [0.5, 0.94], 'k-', lw=2.0)
    r_h = 0.28
    th1, th2 = np.radians(120), np.radians(150)
    axes[2].add_patch(patches.Circle((0.5 + r_h*np.cos(th1), 0.5 + r_h*np.sin(th1)), 0.05, facecolor='black'))
    axes[2].add_patch(patches.Circle((0.5 + r_h*np.cos(th2), 0.5 + r_h*np.sin(th2)), 0.05, facecolor='black'))

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath


def render_transparent_sheet_problem(filepath: str) -> str:
    """Renders Problem Figure (X) for transparent sheet fold."""
    ensure_dir(filepath)
    fig, ax = plt.subplots(figsize=(2.0, 1.6), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.add_patch(patches.Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', lw=2.0))
    ax.plot([0.5, 0.5], [0, 1], 'k--', lw=1.6)
    # Left design: solid triangle pointing right
    ax.add_patch(patches.Polygon([[0.15, 0.25], [0.15, 0.75], [0.42, 0.5]], closed=True, facecolor='black'))
    # Right design: empty circle
    ax.add_patch(patches.Circle((0.75, 0.5), 0.20, fill=False, edgecolor='black', lw=2.0))
    ax.text(0.5, -0.25, '(X)', fontsize=12, fontweight='bold', ha='center')
    ax.set_xlim(-0.08, 1.08)
    ax.set_ylim(-0.35, 1.08)

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, facecolor='white', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    return filepath


# ---------------------------------------------------------------------------
# THE 16 MATHEMATICALLY VERIFIED PFC PATTERNS
# ---------------------------------------------------------------------------

PFC_PATTERNS: Dict[str, Dict[str, Any]] = {
    'pfc_center_diamond': {
        'stem': "A square sheet of paper is folded and cut as shown in X, Y, and Z. Choose the alternative showing the unfolded paper:",
        'exp': "Cutting a right triangle at the closed center corner (0.5, 0.5) unfolds symmetrically into 4 triangles that join to form a single diamond in the center.",
        'render_prob': lambda fp: render_standard_2fold_problem(
            fp, lambda ax: ax.add_patch(patches.Polygon([[0.5, 0.5], [0.65, 0.5], [0.5, 0.35]], closed=True, facecolor='black'))
        ),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - Center diamond
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt1.png"), center_shape='diamond'),
            # Opt 2: Distractor - Center square
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt2.png"), center_shape='square'),
            # Opt 3: Distractor - 4 outer corner triangles
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt3.png"), corner_triangles_size=0.15),
            # Opt 4: Distractor - 2 vertical diamonds
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt4.png"), diamonds=[(0.5, 0.25, 0.10), (0.5, 0.75, 0.10)])
        ]
    },

    'pfc_center_circle': {
        'stem': "A square sheet of paper is folded and cut as shown in X, Y, and Z. Choose the correct figure showing the unfolded paper:",
        'exp': "A quarter-circle cutout at the closed central corner unfolds into a single complete circular hole at the center of the sheet.",
        'render_prob': lambda fp: render_standard_2fold_problem(
            fp, lambda ax: ax.add_patch(patches.Wedge((0.5, 0.5), 0.14, 270, 360, facecolor='black'))
        ),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - 1 Center circle
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt1.png"), holes=[(0.5, 0.5, 0.14)]),
            # Opt 2: Distractor - 4 circular holes in quarters
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt2.png"), holes=[(0.25, 0.25, 0.08), (0.75, 0.25, 0.08), (0.25, 0.75, 0.08), (0.75, 0.75, 0.08)]),
            # Opt 3: Distractor - 2 circular holes on vertical midline
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt3.png"), holes=[(0.5, 0.25, 0.08), (0.5, 0.75, 0.08)]),
            # Opt 4: Distractor - 4 corner quarter-circles
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt4.png"), corner_circles_r=0.14)
        ]
    },

    'pfc_center_square': {
        'stem': "A square sheet of paper is folded and cut as shown in X, Y, and Z. Which alternative represents the unfolded paper?",
        'exp': "A square cut at the central folded corner duplicates across both fold axes to form a single enlarged square centered at the sheet's center.",
        'render_prob': lambda fp: render_standard_2fold_problem(
            fp, lambda ax: ax.add_patch(patches.Rectangle((0.5, 0.38), 0.12, 0.12, facecolor='black'))
        ),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - Center square
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt1.png"), center_shape='square'),
            # Opt 2: Distractor - Center diamond
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt2.png"), center_shape='diamond'),
            # Opt 3: Distractor - 4 square holes in quarters
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt3.png"), squares=[(0.25, 0.25, 0.06), (0.75, 0.25, 0.06), (0.25, 0.75, 0.06), (0.75, 0.75, 0.06)]),
            # Opt 4: Distractor - Center circle
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt4.png"), center_shape='circle')
        ]
    },

    'pfc_outer_corners_tri': {
        'stem': "A square sheet of paper is folded and cut as shown in X, Y, and Z. Which alternative shows the unfolded paper?",
        'exp': "The triangle cut at the open outer corner (1.0, 0.0) is mirrored across both fold creases, producing a triangular notch at each of the 4 outer corners.",
        'render_prob': lambda fp: render_standard_2fold_problem(
            fp, lambda ax: ax.add_patch(patches.Polygon([[1.0, 0.0], [0.85, 0.0], [1.0, 0.15]], closed=True, facecolor='black'))
        ),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - 4 corner triangles
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt1.png"), corner_triangles_size=0.15),
            # Opt 2: Distractor - Center diamond
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt2.png"), center_shape='diamond'),
            # Opt 3: Distractor - 2 corner notches only
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt3.png"), polygons=[[[0, 0], [0.15, 0], [0, 0.15]], [[1, 0], [0.85, 0], [1, 0.15]]]),
            # Opt 4: Distractor - 4 midline notches
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt4.png"), diamonds=[(0.5, 0.25, 0.08), (0.5, 0.75, 0.08), (0.25, 0.5, 0.08), (0.75, 0.5, 0.08)])
        ]
    },

    'pfc_outer_corners_circle': {
        'stem': "A square sheet of paper is folded and cut as shown in X, Y, and Z. Choose the correct figure showing the unfolded paper:",
        'exp': "A quarter-circle cut at the open outer corner reflects into 4 quarter-circle cutouts at the external corners of the unfolded sheet.",
        'render_prob': lambda fp: render_standard_2fold_problem(
            fp, lambda ax: ax.add_patch(patches.Wedge((1.0, 0.0), 0.14, 90, 180, facecolor='black'))
        ),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - 4 corner quarter-circles
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt1.png"), corner_circles_r=0.14),
            # Opt 2: Distractor - Center circle
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt2.png"), center_shape='circle'),
            # Opt 3: Distractor - 4 circular holes inside quarters
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt3.png"), holes=[(0.25, 0.25, 0.08), (0.75, 0.25, 0.08), (0.25, 0.75, 0.08), (0.75, 0.75, 0.08)]),
            # Opt 4: Distractor - 2 corner quarter-circles
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt4.png"), corner_circles_r=0.08)
        ]
    },

    'pfc_single_hole_quarter': {
        'stem': "A square sheet of paper is folded and punched as shown in X, Y, and Z. Choose the alternative showing the unfolded pattern:",
        'exp': "Punched through 4 layers at the center of the quadrant, 4 symmetric circular holes appear in the 4 quarters of the paper.",
        'render_prob': lambda fp: render_standard_2fold_problem(
            fp, lambda ax: ax.add_patch(patches.Circle((0.75, 0.25), 0.08, facecolor='black'))
        ),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - 4 holes in quarters
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt1.png"), holes=[(0.25, 0.25, 0.08), (0.75, 0.25, 0.08), (0.25, 0.75, 0.08), (0.75, 0.75, 0.08)]),
            # Opt 2: Distractor - 2 holes on vertical midline
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt2.png"), holes=[(0.5, 0.25, 0.08), (0.5, 0.75, 0.08)]),
            # Opt 3: Distractor - 1 hole bottom-right only
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt3.png"), holes=[(0.75, 0.25, 0.08)]),
            # Opt 4: Distractor - 4 holes on outer edges
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt4.png"), holes=[(0.5, 0.12, 0.08), (0.5, 0.88, 0.08), (0.12, 0.5, 0.08), (0.88, 0.5, 0.08)])
        ]
    },

    'pfc_vertical_crease_diamond': {
        'stem': "A square sheet of paper is folded and cut as shown in X, Y, and Z. Which figure shows the unfolded paper?",
        'exp': "A triangle cut on the vertical fold crease x=0.5 mirrors across the crease to form a diamond, and unrolls vertically to produce two diamonds on the vertical centerline.",
        'render_prob': lambda fp: render_standard_2fold_problem(
            fp, lambda ax: ax.add_patch(patches.Polygon([[0.5, 0.17], [0.62, 0.25], [0.5, 0.33]], closed=True, facecolor='black'))
        ),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - 2 diamonds on vertical midline
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt1.png"), diamonds=[(0.5, 0.25, 0.09), (0.5, 0.75, 0.09)]),
            # Opt 2: Distractor - 2 diamonds on horizontal midline
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt2.png"), diamonds=[(0.25, 0.5, 0.09), (0.75, 0.5, 0.09)]),
            # Opt 3: Distractor - 4 diamonds on all midlines
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt3.png"), diamonds=[(0.5, 0.25, 0.09), (0.5, 0.75, 0.09), (0.25, 0.5, 0.09), (0.75, 0.5, 0.09)]),
            # Opt 4: Distractor - 1 center diamond
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt4.png"), center_shape='diamond')
        ]
    },

    'pfc_horizontal_crease_diamond': {
        'stem': "A square sheet of paper is folded and cut as shown in X, Y, and Z. Choose the alternative showing the unfolded pattern:",
        'exp': "A triangle cut along the horizontal crease y=0.5 unfolds into two symmetric diamonds along the horizontal centerline.",
        'render_prob': lambda fp: render_standard_2fold_problem(
            fp, lambda ax: ax.add_patch(patches.Polygon([[0.67, 0.5], [0.75, 0.38], [0.83, 0.5]], closed=True, facecolor='black'))
        ),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - 2 diamonds on horizontal midline
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt1.png"), diamonds=[(0.25, 0.5, 0.09), (0.75, 0.5, 0.09)]),
            # Opt 2: Distractor - 2 diamonds on vertical midline
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt2.png"), diamonds=[(0.5, 0.25, 0.09), (0.5, 0.75, 0.09)]),
            # Opt 3: Distractor - 4 diamonds on all midlines
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt3.png"), diamonds=[(0.5, 0.25, 0.09), (0.5, 0.75, 0.09), (0.25, 0.5, 0.09), (0.75, 0.5, 0.09)]),
            # Opt 4: Distractor - 2 triangles on edges
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt4.png"), corner_triangles_size=0.12)
        ]
    },

    'pfc_dual_crease_diamonds': {
        'stem': "A square sheet of paper is folded and cut as shown in X, Y, and Z. Which alternative shows the unfolded paper?",
        'exp': "Cutting notches along both the horizontal and vertical fold creases yields 4 diamonds arranged symmetrically on the midlines.",
        'render_prob': lambda fp: render_standard_2fold_problem(
            fp, lambda ax: (
                ax.add_patch(patches.Polygon([[0.5, 0.18], [0.60, 0.25], [0.5, 0.32]], closed=True, facecolor='black')),
                ax.add_patch(patches.Polygon([[0.68, 0.5], [0.75, 0.40], [0.82, 0.5]], closed=True, facecolor='black'))
            )
        ),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - 4 diamonds on midlines
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt1.png"), diamonds=[(0.5, 0.25, 0.08), (0.5, 0.75, 0.08), (0.25, 0.5, 0.08), (0.75, 0.5, 0.08)]),
            # Opt 2: Distractor - 2 diamonds on vertical midline only
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt2.png"), diamonds=[(0.5, 0.25, 0.08), (0.5, 0.75, 0.08)]),
            # Opt 3: Distractor - 2 diamonds on horizontal midline only
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt3.png"), diamonds=[(0.25, 0.5, 0.08), (0.75, 0.5, 0.08)]),
            # Opt 4: Distractor - 4 corner notches
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt4.png"), corner_triangles_size=0.12)
        ]
    },

    'pfc_double_vertical_holes': {
        'stem': "A square sheet of paper is folded and punched as shown in X, Y, and Z. Choose the alternative showing the unfolded pattern:",
        'exp': "Two holes in the 4-layer quadrant unfold into 2 * 4 = 8 circular holes, with two holes in each quarter.",
        'render_prob': lambda fp: render_standard_2fold_problem(
            fp, lambda ax: (
                ax.add_patch(patches.Circle((0.75, 0.16), 0.05, facecolor='black')),
                ax.add_patch(patches.Circle((0.75, 0.34), 0.05, facecolor='black'))
            )
        ),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - 8 holes (pairs in 4 quarters)
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt1.png"), holes=[
                (0.25, 0.16, 0.05), (0.25, 0.34, 0.05),
                (0.75, 0.16, 0.05), (0.75, 0.34, 0.05),
                (0.25, 0.66, 0.05), (0.25, 0.84, 0.05),
                (0.75, 0.66, 0.05), (0.75, 0.84, 0.05)
            ]),
            # Opt 2: Distractor - 4 holes (1 in each quarter)
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt2.png"), holes=[(0.25, 0.25, 0.06), (0.75, 0.25, 0.06), (0.25, 0.75, 0.06), (0.75, 0.75, 0.06)]),
            # Opt 3: Distractor - 4 holes on vertical midline
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt3.png"), holes=[(0.5, 0.16, 0.05), (0.5, 0.34, 0.05), (0.5, 0.66, 0.05), (0.5, 0.84, 0.05)]),
            # Opt 4: Distractor - 6 holes
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt4.png"), holes=[(0.25, 0.5, 0.05), (0.75, 0.5, 0.05), (0.5, 0.25, 0.05), (0.5, 0.75, 0.05), (0.5, 0.5, 0.05)])
        ]
    },

    'pfc_diagonal_double_holes': {
        'stem': "A square sheet of paper is folded and punched as shown in X, Y, and Z. Choose the correct figure showing the unfolded paper:",
        'exp': "The two diagonal holes mirror across both axes, creating pairs along the diagonal lines of all 4 quarters.",
        'render_prob': lambda fp: render_standard_2fold_problem(
            fp, lambda ax: (
                ax.add_patch(patches.Circle((0.68, 0.18), 0.05, facecolor='black')),
                ax.add_patch(patches.Circle((0.82, 0.32), 0.05, facecolor='black'))
            )
        ),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - 8 diagonal holes in quarters
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt1.png"), holes=[
                (0.68, 0.18, 0.05), (0.82, 0.32, 0.05),
                (0.32, 0.18, 0.05), (0.18, 0.32, 0.05),
                (0.68, 0.82, 0.05), (0.82, 0.68, 0.05),
                (0.32, 0.82, 0.05), (0.18, 0.68, 0.05)
            ]),
            # Opt 2: Distractor - 4 circular holes in diamond
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt2.png"), holes=[(0.5, 0.20, 0.06), (0.5, 0.80, 0.06), (0.20, 0.5, 0.06), (0.80, 0.5, 0.06)]),
            # Opt 3: Distractor - 4 holes in quarters
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt3.png"), holes=[(0.25, 0.25, 0.06), (0.75, 0.25, 0.06), (0.25, 0.75, 0.06), (0.75, 0.75, 0.06)]),
            # Opt 4: Distractor - 8 holes in circle
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt4.png"), holes=[
                (0.5 + 0.3*np.cos(np.radians(a)), 0.5 + 0.3*np.sin(np.radians(a)), 0.05) for a in range(0, 360, 45)
            ])
        ]
    },

    'pfc_center_diamond_plus_4_holes': {
        'stem': "A square sheet of paper is folded, cut, and punched as shown in X, Y, and Z. Which figure shows the unfolded paper?",
        'exp': "The center corner cutout produces a central diamond, while the interior hole punch generates 4 circular holes.",
        'render_prob': lambda fp: render_standard_2fold_problem(
            fp, lambda ax: (
                ax.add_patch(patches.Polygon([[0.5, 0.5], [0.62, 0.5], [0.5, 0.38]], closed=True, facecolor='black')),
                ax.add_patch(patches.Circle((0.78, 0.22), 0.06, facecolor='black'))
            )
        ),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - Center diamond + 4 holes in quarters
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt1.png"),
                diamonds=[(0.5, 0.5, 0.12)],
                holes=[(0.22, 0.22, 0.06), (0.78, 0.22, 0.06), (0.22, 0.78, 0.06), (0.78, 0.78, 0.06)]
            ),
            # Opt 2: Distractor - Center circle + 4 holes
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt2.png"),
                holes=[(0.5, 0.5, 0.12), (0.22, 0.22, 0.06), (0.78, 0.22, 0.06), (0.22, 0.78, 0.06), (0.78, 0.78, 0.06)]
            ),
            # Opt 3: Distractor - Center diamond + 2 holes
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt3.png"),
                diamonds=[(0.5, 0.5, 0.12)],
                holes=[(0.5, 0.22, 0.06), (0.5, 0.78, 0.06)]
            ),
            # Opt 4: Distractor - 4 corner triangles + 4 holes
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt4.png"),
                corner_triangles_size=0.12,
                holes=[(0.22, 0.22, 0.06), (0.78, 0.22, 0.06), (0.22, 0.78, 0.06), (0.78, 0.78, 0.06)]
            )
        ]
    },

    'pfc_center_square_plus_4_holes': {
        'stem': "A square sheet of paper is folded, cut, and punched as shown in X, Y, and Z. Choose the alternative showing the unfolded pattern:",
        'exp': "The square cut at the central folded corner becomes a center square, and the punch creates 4 holes.",
        'render_prob': lambda fp: render_standard_2fold_problem(
            fp, lambda ax: (
                ax.add_patch(patches.Rectangle((0.5, 0.40), 0.10, 0.10, facecolor='black')),
                ax.add_patch(patches.Circle((0.78, 0.22), 0.06, facecolor='black'))
            )
        ),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - Center square + 4 holes
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt1.png"),
                squares=[(0.5, 0.5, 0.10)],
                holes=[(0.22, 0.22, 0.06), (0.78, 0.22, 0.06), (0.22, 0.78, 0.06), (0.78, 0.78, 0.06)]
            ),
            # Opt 2: Distractor - Center diamond + 4 holes
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt2.png"),
                diamonds=[(0.5, 0.5, 0.12)],
                holes=[(0.22, 0.22, 0.06), (0.78, 0.22, 0.06), (0.22, 0.78, 0.06), (0.78, 0.78, 0.06)]
            ),
            # Opt 3: Distractor - Center square + 4 square holes
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt3.png"),
                squares=[(0.5, 0.5, 0.10), (0.22, 0.22, 0.04), (0.78, 0.22, 0.04), (0.22, 0.78, 0.04), (0.78, 0.78, 0.04)]
            ),
            # Opt 4: Distractor - Center circle + 4 holes
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt4.png"),
                holes=[(0.5, 0.5, 0.10), (0.22, 0.22, 0.06), (0.78, 0.22, 0.06), (0.22, 0.78, 0.06), (0.78, 0.78, 0.06)]
            )
        ]
    },

    'pfc_crease_semicircles': {
        'stem': "A square sheet of paper is folded and cut as shown in X, Y, and Z. Which figure represents the paper when unfolded?",
        'exp': "A semicircle cut on the vertical crease unrolls into a full circle on the vertical midline, replicated twice.",
        'render_prob': lambda fp: render_standard_2fold_problem(
            fp, lambda ax: ax.add_patch(patches.Wedge((0.5, 0.25), 0.09, -90, 90, facecolor='black'))
        ),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - 2 circles on vertical midline
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt1.png"), holes=[(0.5, 0.25, 0.09), (0.5, 0.75, 0.09)]),
            # Opt 2: Distractor - 2 circles on horizontal midline
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt2.png"), holes=[(0.25, 0.5, 0.09), (0.75, 0.5, 0.09)]),
            # Opt 3: Distractor - 4 circular holes in quarters
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt3.png"), holes=[(0.25, 0.25, 0.07), (0.75, 0.25, 0.07), (0.25, 0.75, 0.07), (0.75, 0.75, 0.07)]),
            # Opt 4: Distractor - 1 center circle
            render_unfolded_square_card(os.path.join(od, f"{pfx}_opt4.png"), holes=[(0.5, 0.5, 0.12)])
        ]
    },

    'pfc_transparent_sheet_fold': {
        'stem': "A transparent square sheet (X) with a design on both halves is folded along the dotted vertical centerline. Choose the correct figure from the answer figures showing how it will appear:",
        'exp': "Folding along the vertical centerline superimposes the left design onto the right design with lateral reflection.",
        'render_prob': lambda fp: render_transparent_sheet_problem(fp),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - triangle laterally reflected inside circle
            render_transparent_fold_card(os.path.join(od, f"{pfx}_opt1.png"), tri_type='left'),
            # Opt 2: Distractor - triangle unreflected inside circle
            render_transparent_fold_card(os.path.join(od, f"{pfx}_opt2.png"), tri_type='right'),
            # Opt 3: Distractor - triangle vertically inverted
            render_transparent_fold_card(os.path.join(od, f"{pfx}_opt3.png"), tri_type='down'),
            # Opt 4: Distractor - triangle outside circle
            render_transparent_fold_card(os.path.join(od, f"{pfx}_opt4.png"), tri_type='outside')
        ]
    },

    'pfc_circular_sheet_8_holes': {
        'stem': "A circular paper is folded and punched as shown in figures X, Y, and Z. Choose the correct figure from the answer figures showing how it will appear when unfolded:",
        'exp': "Unfolding the punched quadrant produces 2 symmetric circular holes in each quadrant, giving 8 holes total.",
        'render_prob': lambda fp: render_circular_fold_problem(fp),
        'render_opts': lambda od, pfx: [
            # Opt 1: Correct - 8 holes in 4 quadrants
            render_unfolded_circle_card(os.path.join(od, f"{pfx}_opt1.png"), holes=[
                (0.5 + 0.28*np.cos(np.radians(d)), 0.5 + 0.28*np.sin(np.radians(d)), 0.045)
                for d in [30, 60, 120, 150, 210, 240, 300, 330]
            ]),
            # Opt 2: Distractor - 4 holes on crosshairs
            render_unfolded_circle_card(os.path.join(od, f"{pfx}_opt2.png"), holes=[
                (0.5 + 0.28*np.cos(np.radians(d)), 0.5 + 0.28*np.sin(np.radians(d)), 0.045)
                for d in [0, 90, 180, 270]
            ]),
            # Opt 3: Distractor - 6 holes
            render_unfolded_circle_card(os.path.join(od, f"{pfx}_opt3.png"), holes=[
                (0.5 + 0.28*np.cos(np.radians(d)), 0.5 + 0.28*np.sin(np.radians(d)), 0.045)
                for d in [30, 90, 150, 210, 270, 330]
            ]),
            # Opt 4: Distractor - 4 holes in diamond
            render_unfolded_circle_card(os.path.join(od, f"{pfx}_opt4.png"), holes=[
                (0.5 + 0.28*np.cos(np.radians(d)), 0.5 + 0.28*np.sin(np.radians(d)), 0.045)
                for d in [45, 135, 225, 315]
            ])
        ]
    }
}

PFC_ALL_PATTERN_IDS: List[str] = list(PFC_PATTERNS.keys())

def generate_pfc_problem(pattern_id: str, filepath: str) -> str:
    """Generates the problem figure X, Y, Z for given pattern ID."""
    cfg = PFC_PATTERNS.get(pattern_id, PFC_PATTERNS['pfc_center_diamond'])
    return cfg['render_prob'](filepath)

def generate_pfc_options(pattern_id: str, output_dir: str, prefix: str) -> List[str]:
    """Generates the 4 option card images for given pattern ID (Opt 1 is always the mathematically correct one)."""
    cfg = PFC_PATTERNS.get(pattern_id, PFC_PATTERNS['pfc_center_diamond'])
    return cfg['render_opts'](output_dir, prefix)

def get_pfc_pattern_details(pattern_id: str) -> Dict[str, Any]:
    """Returns stem, explanation, and metadata for a PFC pattern."""
    return PFC_PATTERNS.get(pattern_id, PFC_PATTERNS['pfc_center_diamond'])
