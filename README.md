# NMMS Mental Ability Test (MAT) Question Paper Generator

A comprehensive, production-ready web application and algorithmic question paper generation engine for the **National Means-cum-Merit Scholarship (NMMS) Examination**.

---

## Features

- **180 Questions across 25 MAT Categories:**
  - Complete coverage of the NMMS MAT blueprint: Number Series, Letter Series, Coding-Decoding, Analogies, Classifications, Direction Sense, Calendar & Clock, Arithmetic Reasoning, Mathematical Operators, Matrix Puzzles, Geometric Puzzles, Dice & Open Dice, Cubes & Painted Faces, Mirror Images, Water Images, Paper Folding & Cutting, Embedded Figures, Dot Situation, and Figure Series.
- **Dynamic Procedural Generation & Entropy:**
  - Numbers and problems are mathematically calculated and dynamically randomized based on date, time, and entropy so consecutive papers never repeat values.
  - 100% verified answer keys and step-by-step mathematical explanations.
- **Persistent Least-Recently-Used (LRU) Pattern Tracking:**
  - Diagram patterns (Paper Folding, Mirror/Water Images, Geometric Venn, Survey Venn, Dot Situation, Embedded Figures, Figure Series, Analogies) cycle through pattern libraries without repeating on consecutive tests.
- **300 DPI High-Definition Vector Diagrams:**
  - Clean, publication-quality vector diagrams rendered with Matplotlib and Pillow.
- **Strict 7-Page Budget:**
  - Full Question Paper PDF is mathematically formatted to fit within an exact 7-page budget with zero overflow.
- **Interactive Web Application:**
  - Live preview and real-time editing of question stems, options, and explanations.
  - Single-question and full-section regeneration with connected group synchronization (e.g. Venn diagrams and Cubes).
  - One-click PDF finalization: Generates Question Paper (QP), Key & Solutions, and Complete Master PDF.

---

## Local Setup

### 1. Prerequisites
- Python 3.10+
- `pip`

### 2. Installation
```bash
git clone https://github.com/karthik008-cod/NMMS-QUESTION-PAPER-GENERATOR.git
cd NMMS-QUESTION-PAPER-GENERATOR
pip install -r requirements.txt
```

### 3. Running the Web Application
```bash
python nmms_webapp.py
```
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

### 4. Running CLI Generation
```bash
python generate_nmms_paper.py --test-num 8
```

---

## Deployment on Render

This repository includes `render.yaml` and `Procfile` ready for zero-configuration deployment on [Render](https://render.com).

### Render Web Service Settings:
- **Environment:** `Python`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn nmms_webapp:app --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 120`
- **Plan:** Free or Starter

---

## License
MIT License. Created for ZPHS Kistapur NMMS Training.
