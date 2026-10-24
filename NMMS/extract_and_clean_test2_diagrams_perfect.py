import os
import cv2
import numpy as np
import pymupdf

def clean_diagram(gray_img, thresh_val=205, min_area=25, pad=10):
    # Pure white background thresholding
    _, thresh = cv2.threshold(gray_img, thresh_val, 255, cv2.THRESH_BINARY)
    h, w = thresh.shape
    inv = 255 - thresh
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(inv, connectivity=8)

    cleaned = np.full_like(inv, 0)
    for i in range(1, num_labels):
        area = stats[i, cv2.CC_STAT_AREA]
        bw = stats[i, cv2.CC_STAT_WIDTH]
        bh = stats[i, cv2.CC_STAT_HEIGHT]
        # Keep significant components (strokes, dots, letters, numbers)
        if area >= min_area or (bw >= 5 and bh >= 5) or (bw > 10 and bh > 2) or (bh > 10 and bw > 2):
            cleaned[labels == i] = 255

    result = 255 - cleaned

    # Crop neatly with padding
    coords = cv2.findNonZero(cleaned)
    if coords is not None:
        x, y, bw, bh = cv2.boundingRect(coords)
        x1 = max(0, x - pad)
        y1 = max(0, y - pad)
        x2 = min(w, x + bw + pad)
        y2 = min(h, y + bh + pad)
        result = result[y1:y2, x1:x2]

    return result

def main():
    out_dir = "NMMS/output/test2_diagrams"
    os.makedirs(out_dir, exist_ok=True)

    doc_2025 = pymupdf.open("NMMS/2025 MENTAL ABILITY.pdf")
    doc_2024 = pymupdf.open("NMMS/2024 MENTAL ABILITY.pdf")
    doc_2023 = pymupdf.open("NMMS/2023 MENTAL ABILITY.pdf")

    # 1. 2025 Q21: Circle sectors (page 2)
    # y: 800..1150, x: 350..1280 (cut out "21." at left, cut out options below)
    pix25_p2 = doc_2025[2].get_pixmap(dpi=350)
    img25_p2 = cv2.imdecode(np.frombuffer(pix25_p2.tobytes(), np.uint8), cv2.IMREAD_GRAYSCALE)
    crop_q21 = img25_p2[800:1150, 350:1280]
    res_q21 = clean_diagram(crop_q21, thresh_val=205, min_area=25, pad=12)
    cv2.imwrite(f"{out_dir}/fig_circle_sectors_2025_q21.png", res_q21)
    print("Saved fig_circle_sectors_2025_q21.png", res_q21.shape)

    # 2. 2025 Q26: Branch trees (page 2, right col)
    # y: 1005..1410, x: 1530..2510 (all 3 trees, no "26.", no options below)
    crop_q26 = img25_p2[1005:1410, 1530:2510]
    res_q26 = clean_diagram(crop_q26, thresh_val=205, min_area=25, pad=12)
    cv2.imwrite(f"{out_dir}/fig_branch_trees_2025_q26.png", res_q26)
    print("Saved fig_branch_trees_2025_q26.png", res_q26.shape)

    # 3. 2024 Q70: Spiral circle (page 4, left col)
    pix24_p4 = doc_2024[4].get_pixmap(dpi=350)
    img24_p4 = cv2.imdecode(np.frombuffer(pix24_p4.tobytes(), np.uint8), cv2.IMREAD_GRAYSCALE)
    # y: 660..1055, x: 260..760 (only the spiral circle, no options, no directions below)
    crop_q70 = img24_p4[660:1055, 260:760]
    res_q70 = clean_diagram(crop_q70, thresh_val=205, min_area=25, pad=12)
    cv2.imwrite(f"{out_dir}/fig_spiral_circle_2024_q70.png", res_q70)
    print("Saved fig_spiral_circle_2024_q70.png", res_q70.shape)

    # 4. 2024 Q64: H blocks (page 3, right col)
    pix24_p3 = doc_2024[3].get_pixmap(dpi=350)
    img24_p3 = cv2.imdecode(np.frombuffer(pix24_p3.tobytes(), np.uint8), cv2.IMREAD_GRAYSCALE)
    # y: 1010..1545, x: 1540..2320 (all 3 H blocks, boxes 15,5,2,6,80; 9,4,7,6,65; 13,11,16,8,?, no "64.", no options below)
    crop_q64 = img24_p3[1010:1545, 1540:2320]
    res_q64 = clean_diagram(crop_q64, thresh_val=205, min_area=25, pad=12)
    cv2.imwrite(f"{out_dir}/fig_h_blocks_2024_q64.png", res_q64)
    print("Saved fig_h_blocks_2024_q64.png", res_q64.shape)

    # 5. 2024 Q67: Cross circle (page 3, right col)
    # y: 2600..2915, x: 1550..2440 (all 3 cross-circles, top numbers 5,9,8 and bottom 3,3,3, left 7, right 4)
    crop_q67 = img24_p3[2600:2915, 1550:2440]
    res_q67 = clean_diagram(crop_q67, thresh_val=205, min_area=25, pad=12)
    cv2.imwrite(f"{out_dir}/fig_cross_circle_2024_q67.png", res_q67)
    print("Saved fig_cross_circle_2024_q67.png", res_q67.shape)

    # 6. 2023 Q33: Composite double cross (page 1, left col)
    pix23_p1 = doc_2023[1].get_pixmap(dpi=350)
    img23_p1 = cv2.imdecode(np.frombuffer(pix23_p1.tobytes(), np.uint8), cv2.IMREAD_GRAYSCALE)
    # y: 1625..1870, x: 330..880 (both cross figures, [58] and [?], no "33.", no options)
    crop_q33 = img23_p1[1625:1870, 330:880]
    res_q33 = clean_diagram(crop_q33, thresh_val=205, min_area=25, pad=12)
    cv2.imwrite(f"{out_dir}/fig_composite_cross_2023_q33.png", res_q33)
    print("Saved fig_composite_cross_2023_q33.png", res_q33.shape)

    # 7. 2023 Q36: 4-wing propeller (page 1, left col)
    # y: 2800..3005, x: 300..1120 (all 3 wings, no "36.", no options below)
    crop_q36 = img23_p1[2800:3005, 300:1120]
    res_q36 = clean_diagram(crop_q36, thresh_val=205, min_area=25, pad=12)
    cv2.imwrite(f"{out_dir}/fig_cross_wing_2023_q36.png", res_q36)
    print("Saved fig_cross_wing_2023_q36.png", res_q36.shape)

    # 8. 2025 Q82: Loop petals analogy (page 9, right col)
    pix25_p9 = doc_2025[9].get_pixmap(dpi=350)
    img25_p9 = cv2.imdecode(np.frombuffer(pix25_p9.tobytes(), np.uint8), cv2.IMREAD_GRAYSCALE)
    # y: 320..1030, x: 1420..2480 (includes full (A)-(D) and (1)-(4))
    crop_q82 = img25_p9[320:1030, 1420:2480]
    res_q82 = clean_diagram(crop_q82, thresh_val=205, min_area=25, pad=12)
    cv2.imwrite(f"{out_dir}/fig_loop_analogy_2025_q82.png", res_q82)
    print("Saved fig_loop_analogy_2025_q82.png", res_q82.shape)

    # 9. 2025 Q83: Diamond analogy (page 9, right col)
    # y: 1120..1920, x: 1420..2480
    crop_q83 = img25_p9[1120:1920, 1420:2480]
    res_q83 = clean_diagram(crop_q83, thresh_val=205, min_area=25, pad=12)
    cv2.imwrite(f"{out_dir}/fig_diamond_analogy_2025_q83.png", res_q83)
    print("Saved fig_diamond_analogy_2025_q83.png", res_q83.shape)

    # 10. 2025 Q87: Shaded chevron analogy (page 10, left col)
    pix25_p10 = doc_2025[10].get_pixmap(dpi=350)
    img25_p10 = cv2.imdecode(np.frombuffer(pix25_p10.tobytes(), np.uint8), cv2.IMREAD_GRAYSCALE)
    # y: 1100..2020, x: 260..1250
    crop_q87 = img25_p10[1100:2020, 260:1250]
    res_q87 = clean_diagram(crop_q87, thresh_val=205, min_area=25, pad=12)
    cv2.imwrite(f"{out_dir}/fig_shaded_analogy_2025_q87.png", res_q87)
    print("Saved fig_shaded_analogy_2025_q87.png", res_q87.shape)

    # 11. 2023 Q51: Dot box series (page 2, left col)
    pix23_p2 = doc_2023[2].get_pixmap(dpi=350)
    img23_p2 = cv2.imdecode(np.frombuffer(pix23_p2.tobytes(), np.uint8), cv2.IMREAD_GRAYSCALE)
    # y: 610..1140, x: 290..1010
    crop_q51 = img23_p2[610:1140, 290:1010]
    res_q51 = clean_diagram(crop_q51, thresh_val=205, min_area=15, pad=12)
    cv2.imwrite(f"{out_dir}/fig_dot_box_series_2023_q51.png", res_q51)
    print("Saved fig_dot_box_series_2023_q51.png", res_q51.shape)

    # 12. 2023 Q58: Triangle rot series (page 2, right col)
    # y: 1485..1965, x: 1470..2200 (problem figures A,B,C,D + answer figures 1,2,3,4 full labels, no stray text)
    crop_q58 = img23_p2[1485:1965, 1470:2200]
    res_q58 = clean_diagram(crop_q58, thresh_val=205, min_area=25, pad=12)
    cv2.imwrite(f"{out_dir}/fig_triangle_rot_series_2023_q58.png", res_q58)
    print("Saved fig_triangle_rot_series_2023_q58.png", res_q58.shape)

    # 13. Venn 2: Graduates survey
    v2_raw = cv2.imread("NMMS/output/mega_180/venn_female_graduates.png", cv2.IMREAD_GRAYSCALE)
    v2_crop = v2_raw[70:386, 10:550]
    res_v2 = clean_diagram(v2_crop, thresh_val=210, min_area=30, pad=12)
    cv2.imwrite(f"{out_dir}/fig_venn2_graduates.png", res_v2)
    print("Saved fig_venn2_graduates.png", res_v2.shape)

    # 14. Venn 1: Engineers
    v1_raw = cv2.imread("NMMS/output/mega_180/fig_venn1.png", cv2.IMREAD_GRAYSCALE)
    res_v1 = clean_diagram(v1_raw, thresh_val=210, min_area=25, pad=12)
    cv2.imwrite(f"{out_dir}/fig_venn1_engineers.png", res_v1)
    print("Saved fig_venn1_engineers.png", res_v1.shape)

    print("ALL 14 DIAGRAMS EXTRACTED AND CLEANED TO HD SPOTLESS!")

if __name__ == "__main__":
    main()
