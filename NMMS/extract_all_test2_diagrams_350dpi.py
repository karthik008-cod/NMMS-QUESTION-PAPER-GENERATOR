import os
import cv2
import numpy as np
import pymupdf

def clean_and_save(img_bgr, out_path, wipe_left_px=0, wipe_top_px=0, wipe_right_px=0, wipe_bot_px=0, min_area=35, pad=12):
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 205, 255, cv2.THRESH_BINARY)
    h, w = thresh.shape
    
    if wipe_left_px > 0:
        thresh[:, :wipe_left_px] = 255
    if wipe_top_px > 0:
        thresh[:wipe_top_px, :] = 255
    if wipe_right_px > 0:
        thresh[:, w - wipe_right_px:] = 255
    if wipe_bot_px > 0:
        thresh[h - wipe_bot_px:, :] = 255

    inv = 255 - thresh
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(inv, connectivity=8)

    cleaned = np.full_like(inv, 0)
    for i in range(1, num_labels):
        area = stats[i, cv2.CC_STAT_AREA]
        bw = stats[i, cv2.CC_STAT_WIDTH]
        bh = stats[i, cv2.CC_STAT_HEIGHT]
        # Keep components that are substantial
        if area >= min_area or (bw > 10 and bh > 2) or (bh > 10 and bw > 2):
            cleaned[labels == i] = 255

    result = 255 - cleaned

    coords = cv2.findNonZero(cleaned)
    if coords is not None:
        x, y, bw, bh = cv2.boundingRect(coords)
        x1 = max(0, x - pad)
        y1 = max(0, y - pad)
        x2 = min(w, x + bw + pad)
        y2 = min(h, y + bh + pad)
        result = result[y1:y2, x1:x2]

    cv2.imwrite(out_path, result)
    print(f"Saved: {out_path} ({result.shape[1]}x{result.shape[0]})")

def extract_all():
    out_dir = "NMMS/output/test2_diagrams"
    os.makedirs(out_dir, exist_ok=True)

    # 1. 2025 Paper
    doc_2025 = pymupdf.open("NMMS/2025 MENTAL ABILITY.pdf")
    
    # 2025 Q21 (Page 4, 0-indexed 3)
    p3_2025 = doc_2025[3].get_pixmap(dpi=350)
    img_p3_2025 = cv2.imdecode(np.frombuffer(p3_2025.tobytes(), np.uint8), cv2.IMREAD_COLOR)
    # 350 / 150 = 2.333
    # Q21: y 600..1150, x 100..1280
    clean_and_save(img_p3_2025[680:1150, 100:1280], f"{out_dir}/fig_circle_sectors_2025_q21.png", wipe_left_px=150, wipe_top_px=40, min_area=30)

    # 2025 Q26 (Page 4, 0-indexed 3, right column)
    # y 1000..1550, x 1350..2500
    clean_and_save(img_p3_2025[980:1550, 1320:2520], f"{out_dir}/fig_branch_trees_2025_q26.png", wipe_left_px=140, wipe_bot_px=80, min_area=30)

    # 2025 Q82 (Page 10, 0-indexed 9, right column)
    p9_2025 = doc_2025[9].get_pixmap(dpi=350)
    img_p9_2025 = cv2.imdecode(np.frombuffer(p9_2025.tobytes(), np.uint8), cv2.IMREAD_COLOR)
    # Q82: y 300..1150, x 1280..2450
    clean_and_save(img_p9_2025[300:1150, 1260:2480], f"{out_dir}/fig_loop_analogy_2025_q82.png", wipe_left_px=160, min_area=30)

    # 2025 Q83 (Page 10, 0-indexed 9, right column)
    # Q83: y 1250..2050, x 1280..2480
    clean_and_save(img_p9_2025[1280:2050, 1260:2480], f"{out_dir}/fig_diamond_analogy_2025_q83.png", wipe_left_px=160, min_area=30)

    # 2025 Q87 (Page 11, 0-indexed 10, left column)
    p10_2025 = doc_2025[10].get_pixmap(dpi=350)
    img_p10_2025 = cv2.imdecode(np.frombuffer(p10_2025.tobytes(), np.uint8), cv2.IMREAD_COLOR)
    # Q87: y 900..1950, x 100..1280
    clean_and_save(img_p10_2025[950:1950, 100:1280], f"{out_dir}/fig_shaded_analogy_2025_q87.png", wipe_left_px=140, wipe_top_px=30, min_area=30)

    # 2. 2024 Paper
    doc_2024 = pymupdf.open("NMMS/2024 MENTAL ABILITY.pdf")

    # 2024 Q70 (Page 5, 0-indexed 4, left column)
    p4_2024 = doc_2024[4].get_pixmap(dpi=350)
    img_p4_2024 = cv2.imdecode(np.frombuffer(p4_2024.tobytes(), np.uint8), cv2.IMREAD_COLOR)
    clean_and_save(img_p4_2024[650:1450, 120:980], f"{out_dir}/fig_spiral_circle_2024_q70.png", wipe_left_px=140, wipe_bot_px=100, min_area=30)

    # 2024 Q64 (Page 4, 0-indexed 3, right column)
    p3_2024 = doc_2024[3].get_pixmap(dpi=350)
    img_p3_2024 = cv2.imdecode(np.frombuffer(p3_2024.tobytes(), np.uint8), cv2.IMREAD_COLOR)
    clean_and_save(img_p3_2024[1220:1820, 1380:2600], f"{out_dir}/fig_h_blocks_2024_q64.png", wipe_left_px=140, wipe_bot_px=80, min_area=30)

    # 2024 Q67 (Page 4, 0-indexed 3, right column)
    clean_and_save(img_p3_2024[2600:3200, 1380:2600], f"{out_dir}/fig_cross_circle_2024_q67.png", wipe_left_px=140, wipe_bot_px=60, min_area=30)

    # 3. 2023 Paper
    doc_2023 = pymupdf.open("NMMS/2023 MENTAL ABILITY.pdf")

    # 2023 Q33 (Page 2, 0-indexed 1, left column)
    p1_2023 = doc_2023[1].get_pixmap(dpi=350)
    img_p1_2023 = cv2.imdecode(np.frombuffer(p1_2023.tobytes(), np.uint8), cv2.IMREAD_COLOR)
    clean_and_save(img_p1_2023[1750:2300, 150:1250], f"{out_dir}/fig_composite_cross_2023_q33.png", wipe_left_px=160, wipe_bot_px=80, min_area=30)

    # 2023 Q36 (Page 2, 0-indexed 1, left column)
    clean_and_save(img_p1_2023[2750:3300, 150:1250], f"{out_dir}/fig_cross_wing_2023_q36.png", wipe_left_px=160, wipe_bot_px=60, min_area=30)

    # 2023 Q51 (Page 3, 0-indexed 2, left column)
    p2_2023 = doc_2023[2].get_pixmap(dpi=350)
    img_p2_2023 = cv2.imdecode(np.frombuffer(p2_2023.tobytes(), np.uint8), cv2.IMREAD_COLOR)
    clean_and_save(img_p2_2023[550:1350, 150:1280], f"{out_dir}/fig_dot_box_series_2023_q51.png", wipe_left_px=160, min_area=30)

    # 2023 Q58 (Page 3, 0-indexed 2, right column)
    clean_and_save(img_p2_2023[1800:2600, 1380:2550], f"{out_dir}/fig_triangle_rot_series_2023_q58.png", wipe_left_px=160, min_area=30)

    # 4. Venn Diagrams:
    # Use existing spotless Venn 1 and Venn 2 from mega_180 output or re-clean if needed
    # In mega_180: fig_venn1.png, fig_venn2.png are already pristine HD spotless
    import shutil
    shutil.copy("NMMS/output/mega_180/fig_venn1.png", f"{out_dir}/fig_venn1_engineers.png")
    shutil.copy("NMMS/output/mega_180/fig_venn2.png", f"{out_dir}/fig_venn2_graduates.png")
    print("Copied spotless Venn diagrams.")

if __name__ == "__main__":
    extract_all()
