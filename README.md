# 💡EconInsight & 🔮EconViz

## An Analysis of Global Digital Trade and Technology Adoption

*Exploring the key drivers and leaders of the digital service economy from 2010 to 2023.*

This repository contains the data, analysis notebooks, and Streamlit web application for the "Programming with Data" final project. The project investigates the landscape of global digital trade and examines the econometric relationship between technology adoption and digital service exports.

## ✨ Featured Visualization: Interactive 3D Data Cloud

To showcase the relationship between Internet Usage, GDP, and Digital Service Exports, we created a fully interactive 3D scatter plot using Plotly. The GIF below demonstrates the interactivity.


  ![Interactive 3D Plot Demo](app/data/output/3dplot_data_cloud.gif)


---

---

## 📋 Table of Contents

1.  [Key Research Questions](#-key-research-questions)
2.  [Data Overview](#-data-overview)
3.  [Technical Implementation](#️-technical-implementation)
4.  [Project Structure](#-project-structure)
5.  [Usage](#-usage)
6.  [Contributing](#-contributing)

---

## 🚀 Key Research Questions

This project answers two primary questions:

**1. 🌍 Global Digital Trade Landscape**
> *Which countries lead in digital service exports and how has this evolved?*
>
> **Takeaway:** A small group of developed nations, including Ireland, the United States, and Germany, consistently dominate the top ranks. However, the animated bar chart race reveals a dynamic mid-tier, with countries like China and India demonstrating significant upward momentum over the last decade.

[Barchart Race](app/data/barchart_race.gif)

**2. ⚙️ Technology Adoption & Trade**
> *Is there a relationship between internet adoption and digital service exports?*
>
> **Takeaway:** Yes, but the story is complex. While a strong positive visual correlation exists, our rigorous econometric analysis shows this simple relationship is misleading. After controlling for country-specific characteristics and global time-based shocks using a Two-Way Fixed Effects model, the direct impact of internet usage becomes statistically insignificant, highlighting the importance of advanced modeling to avoid false conclusions.

*(The final 2 questions are currently under development)*

---

## 📊 Data Overview

The analysis is based on a comprehensive panel dataset compiled from primary public sources.

| Variable | Description | Source |
| :--- | :--- | :--- |
| `Exports_Digital_Service` | Volume of digital service exports | World Bank / UNCTAD |
| `internet_usage_pct` | Percentage of population using the internet | World Bank |
| `gdp_per_capita` | Gross Domestic Product per capita | World Bank |
| `population` | Total population | World Bank |
| `is_developing` | Development status classification | World Bank |

The final dataset covers approximately 150 countries over a span from 2010 to 2023. I utilized the [`wbdata`](https://wbdata.readthedocs.io/en/stable/) Python library to systematically account for missing values in the main dataset.

**Primary Data Source:** [World Bank Data (UNCTAD_DE)](https://data.worldbank.org/ )

---

## 🛠️ Technical Implementation

The project was executed through a series of robust data processing and analysis steps:

**1. Data Cleaning & Harmonization**
- Raw CSV files from the OECD and World Bank were ingested using **Pandas**.
- Datasets were cleaned, harmonized, and merged into a single, tidy panel DataFrame (`final_panel_for_regression.csv`).

**2. Analysis & Modeling**
- **Baseline OLS:** Initial regression analysis performed using **Statsmodels**.
- **Panel Data Models:** Implementation of Fixed Effects and Two-Way Fixed Effects models using the **linearmodels** library to control for unobserved heterogeneity.

**3. Visualization & Dashboarding**
- **Interactive Web App:** Built with **Streamlit** to allow users to explore the data dynamically.
- **Advanced Charts:** Choropleth maps, animated bar charts, and 3D scatter plots created with **Plotly Express** and **Plotly Graph Objects**.
- **Custom Styling:** A polished dark theme and custom CSS (via `config.toml`) ensure a high-quality user experience.

---

## 📦 Project Structure

```
KLDR-Project/

│
├── 📁 app/                   # Core Streamlit application source code
│   ├── 📁 .streamlit/        # Streamlit configuration files (e.g., config.toml for themes)
│   ├── 📁 data/               # Data files used directly by the live application
│   │   ├── 📁 output/         # Processed data from notebooks, ready for visualization
│   │   │   ├── 📁 question1/
│   │   │   ├── 📁 question2_paneldata/
│   │   │   └── 📁 question3/
│   │   └── 📁 tables/         # Other miscellaneous data tables
│   ├── 📁 pages/              # Each .py file here is a separate page/tab in the Streamlit app
│   │   ├── 📄 data_assistant.py
│   │   ├── 📄 data_overview.py
│   │   ├── 📄 EconInsight.py
│   │   ├── 📄 EconViz.py
│   │   ├── 📄 homepage1.py
│   │   ├── 📄 homepage2.py
│   │   └── 📄 must-know.py
│   ├── 📁 utils/              # Utility scripts and helper functions
│   │   └── 📄 common_imports.py
│   └── 📄 app.py                # Main entry point to run the Streamlit application
│
├── 📁 drafts/                  # Folder for draft scripts or old code versions
├── 📁 scripts/                 # Standalone helper scripts for tasks
│
├── 📄 .gitignore               # Specifies files and folders for Git to ignore
├── 📄 README.md                # This project documentation file
├── 📄 requirements.txt         # List of Python libraries required for the project
├── 📄 test.ipynb               # A Jupyter notebook for testing and experimentation
└── 📄 test.txt                 # A simple text file for notes or tests

```





---

## 💻 Usage

To run the dashboard locally:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/kldr-project.git
    cd kldr-project
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit app:**
    ```bash
    streamlit run app/app.py
    ```

---

<sub>Built with ❤️ by Kevin for Data Analysis with Python Course of University of Zurich</sub>
</p>
