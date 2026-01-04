# Electric Vehicle Charging Analysis - Bavaria

## Table of Contents

- [ Project Overview](#-project-overview)
- [ Objectives](#-objectives)
- [ Dataset](#-dataset)
- [ Technologies Used](#-technologies-used)
- [ Project Structure](#-project-structure)
- [ Installation & Setup](#-installation--setup)
- [ Analysis & Workflow](#-analysis--workflow)
- [ Key Insights](#-key-insights)
- [ Author](#-author)
- [ License](#-license)

## Project Overview

As a part of the **Programming Starters Course** of the **MSc. Artificial Intelligence in Industrial Application Bridge Semester 2025–2026**, this project aims to offer **thorough and data-driven insights into Germany's Electric Vehicle Charging Infrastructure**.

This project primarily focuses on analyzing the **distribution, accessibility, and capacity of charging networks**, which can provide crucial information for the structuring of **urban planning** and support Germany’s transition toward a **cleaner mobility solution**.

The dataset used in this project is sourced from the **official network of the Federal Network Agency** (Bundesnetzagentur, [Click here for the dataset](https://d1269bxe5ubfat.cloudfront.net/bnetzalsr/data/ladestationFactTable.csv?v=1))

The project follows a **modular function-based approach**, allowing components to be reused in future analyses and ensuring **long-term usability**. Additionally, the project is designed to offer **flexibility**, enabling changes to the dataset with **minimal global modifications**.

## Objectives

This analysis is structured to provide empirical and data-driven answers to the following key research questions:

1. Charging Station Distribution Across German States
   Which of the german states has the most charging stations? (highest/lowest density of charging stations per region - suggested framework: scikit-learn) Prove it with meaningful visualization(s).
2. City-Level Charging Infrastructure Analysis
   Which city has the most charging stations in Germany (besides Berlin, Hamburg, Munich and Cologne)? In total, how many charging stations does the city of Amberg have and how much energy can be charged at max?
3. Charging Station Operators in Germany
   What are the 5 most prominent charging station operators in Germany and how many electric vehicles can each of them charge at once?

## Dataset

This Analaysis is based on the Dataset given below

- **File Name:** `ev_charging_germany.csv`
- **Source:** Public EV infrastructure data (e.g. Bundesland).
- **Format:** CSV (Semicolon `;` separated)
- **Encoding:** UTF-8

## Key Variables

| Column Name                   | Description                           |
| :---------------------------- | :------------------------------------ |
| `Bundesland`                  | German State (e.g., Bayern, Berlin)   |
| `Ort`                         | City / Municipality                   |
| `Betreiber`                   | Charging Station Operator             |
| `AnzahlLadepunkteNLL`         | Number of Charging Points per Station |
| `InstallierteLadeleistungNLL` | Installed Charging Power (kW)         |
| `Breitengrad`                 | Latitude (Geospatial)                 |
| `Laengengrad`                 | Longitude (Geospatial)                |

---

## Technologies Used

The project is built using **Python 3.x** and the following libraries:

- **Data Manipulation:** `pandas`,`numpy`
- **Visualization:** `matplotlib`,`seaborn`
- **Geospatial Analysis:** `geopandas`,`folium`

## Project Structure

```text
my-data-analysis-project/
│
├── data/
│   ├── data_source_description.txt
│   └── ev_charging_germany.csv
│
├── src/
│   └── analysis_functions.py
│
├── requirements.txt
├── AI_Usage_Declaration.txt
├── PRS_Presentation_EVGermany.pptx
├── PRS_Final_Project_v1.1.ipynb
├── References.docx
└── Readme.md

```

## Installation

```bash
1. Clone the git repository

    git clone https://github.com/SathwikSharma226/PRS_FinalProject_DataViz

2. Install Dependencies

    pip install pandas numpy matplotlib seaborn geopandas folium
    or
    pip install -r requirements.txt

3. Run the Analysis

    You can run the analysis via Jupyter Notebook or you can use the functions that are present in analysis_functions.py file and build upon this project.

```

## Analysis & Workflow

    1. Data loading

    2. Data cleaning

    3. Reading CSV with specific encodings

    4. Handling missing values and data types

## Authors

    Sathwik Nagasundara Sharma

    Alla Sai Surya (s.alla@oth-aw.de)

## License

    This project is purely for educational and academic purposes only and no license is required.
