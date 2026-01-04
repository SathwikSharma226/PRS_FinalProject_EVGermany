# Electric Vehicle Charging Analysis - Bavaria

This is a Data Analysis and visualization project which explores distribution, density and dominance of Electric Vehicle charging stations across Germany, at present focused case study is on the city of Amberg, Bavaria.



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

##  Project Overview
As a part of the **Programming Starters Course** of the **MSc. Artificial Intelligence in Industrial Application Bridge Semester 2025–2026**, this project aims to offer **thorough and data-driven insights into Germany's Electric Vehicle Charging Infrastructure**.

This project primarily focuses on analyzing the **distribution, accessibility, and capacity of charging networks**, which can provide crucial information for the structuring of **urban planning** and support Germany’s transition toward a **cleaner mobility solution**.

The dataset used in this project is sourced from the **official network of the Federal Network Agency** (Bundesnetzagentur, [Click here for the dataset](https://d1269bxe5ubfat.cloudfront.net/bnetzalsr/data/ladestationFactTable.csv?v=1))

The project follows a **modular function-based approach**, allowing components to be reused in future analyses and ensuring **long-term usability**. Additionally, the project is designed to offer **flexibility**, enabling changes to the dataset with **minimal global modifications**.



##  Objectives

Analyze the geographical distribution of charging stations across 16 federal states of Germany.

Finding the states having maximum number and minimum density of stations.

Select the top medium sized cities excluding popular cities like Berlin, Munich, Hamburg and cologne.

Analayse about Amberg by examining total number of power stations, power output and location mapping.

Identifying the top 5 operators who are managing most of the charging points.

Visualizing data using Bar charts, and folium Interactive Maps.




##  Dataset

This Analaysis is based on the Dataset given below

* **File Name:** `ev_charging_germany.csv`
* **Source:** Public EV infrastructure data (e.g. Bundesland).
* **Format:** CSV (Semicolon `;` separated)
* **Encoding:** UTF-8


##  Key Variables

| Column Name | Description |
| :--- | :--- |
| `Bundesland` | German State (e.g., Bayern, Berlin) |
| `Ort` | City / Municipality |
| `Betreiber` | Charging Station Operator |
| `AnzahlLadepunkteNLL` | Number of Charging Points per Station |
| `InstallierteLadeleistungNLL` | Installed Charging Power (kW) |
| `Breitengrad` | Latitude (Geospatial) |
| `Laengengrad` | Longitude (Geospatial) |

---

##  Technologies Used

The project is built using **Python 3.x** and the following libraries:

* **Data Manipulation:** `pandas`,`numpy`
* **Visualization:** `matplotlib`,`seaborn`
* **Geospatial Analysis:** `geopandas`,`folium`


##  Project Structure

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
├── LICENSE
├── Markupfile.txt
├── PRS_Final_Project_v1.1.ipynb
└── Readme.md

```


##  Installation


```bash
1. Clone the git repository

    git clone https://github.com/SathwikSharma226/PRS_FinalProject_DataViz
    cd ev-charging-germany

2. Install Dependencies

    pip install pandas numpy matplotlib seaborn geopandas folium
    or 
    pip install -r requirements.txt

3. Run the Analysis

    python prs_german_charging_stations.py

    You can run the analysis via a Python script or Jupyter Notebook

```

##  Analysis & Workflow

    1. Data loading

    2. Data cleaning

    3. Reading CSV with specific encodings

    4. Handling missing values and data types



##  Authors
    Sathwik Nagasundara Sharma

    Alla Sai Surya (s.alla@oth-aw.de)

## License

    This project is purely for educational and academic purposes only and licensed under MIT-lICENSE.