# Data Analysis Projects

This repository showcases a collection of beginner-to-intermediate level data analysis and visualization projects using Python, Pandas, Matplotlib, Seaborn, and SciPy. Each project demonstrates different techniques in data cleaning, analysis, and visual storytelling.

---

## 📈 Page Views Time Series Analyzer

**Data Source:** `fcc-forum-pageviews.csv`  
**Libraries Used:** Pandas, Matplotlib, Seaborn, NumPy

This project visualizes daily page views on the freeCodeCamp Forum from May 2016 to December 2019.

**Features:**
- Cleans outliers using the 2.5th and 97.5th percentiles.
- Generates:
  - **Line Plot** showing daily trends over time.
  - **Bar Plot** showing monthly average page views per year.
  - **Box Plots** illustrating year-wise trends and month-wise seasonality.

**Output Files:**  
- `line_plot.png`  
- `bar_plot.png`  
- `box_plot.png`

---

## 🌊 Sea Level Predictor

**Data Source:** `epa-sea-level.csv`  
**Libraries Used:** Pandas, Matplotlib, SciPy

This project explores and predicts global sea level trends based on CSIRO adjusted historical data.

**Features:**
- Creates a scatter plot of sea level rise.
- Fits:
  - A **regression line** on all data points.
  - A **second regression line** on data from the year 2000 onward.
- Projects sea level rise through the year 2050.

**Output File:**  
- `sea_level_plot.png`

---

## 🩺 Medical Data Visualizer

**Data Source:** `medical_examination.csv`  
**Libraries Used:** Pandas, Seaborn, Matplotlib, NumPy

Analyzes cardiovascular data to produce visual summaries.

**Features:**
- Computes BMI and flags patients as overweight.
- Normalizes cholesterol and glucose levels.
- Generates:
  - **Categorical Plot** comparing features like smoking, alcohol use, activity, and medical indicators across cardiovascular disease presence.
  - **Heatmap** showing correlations between health indicators after cleaning the dataset.

**Output Files:**  
- `catplot.png`  
- `heatmap.png`

---

## 🧑‍🤝‍🧑 Demographic Data Analyzer

**Data Source:** `adult.data.csv`  
**Libraries Used:** Pandas

Processes U.S. Census data to compute demographic statistics.

**Features:**
- Calculates race distribution.
- Computes average age of men.
- Determines education and income relationships.
- Finds:
  - Percentage of rich among those with and without advanced degrees.
  - Minimum working hours and related income statistics.
  - Country with the highest percentage of high earners.
  - Top occupation in India among high earners.

**Output:**  
Returns a Python dictionary with key statistics and optionally prints them to the console.

---
