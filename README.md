# EconInsight: An Analysis of Global Digital Trade and Technology Adoption

**A project exploring the key drivers and leaders of the digital service economy from 2005 to 2020.**

This repository contains the data, analysis notebooks, and Streamlit web application for the "Programming with Data" final project. The project investigates the landscape of global digital trade and examines the econometric relationship between technology adoption and digital service exports.

---

## Key Research Questions and Takeaways

This project answers two primary questions:

*   **🌍 Question 1: Global Digital Trade**
    *   **Which countries lead in digital service exports and how has this evolved?**
    *   **Takeaway:** A small group of developed nations, including Ireland, the United States, and Germany, consistently dominate the top ranks. However, the animated bar chart race reveals a dynamic mid-tier, with countries like China and India demonstrating significant upward momentum over the last decade.

*   **⚙️ Question 2: Technology Adoption & Trade**
    *   **Is there a relationship between internet adoption and digital service exports?**
    *   **Takeaway:** Yes, but the story is complex. While a strong positive visual correlation exists, our rigorous econometric analysis shows this simple relationship is misleading. After controlling for country-specific characteristics and global time-based shocks using a Two-Way Fixed Effects model, the direct impact of internet usage becomes statistically insignificant, highlighting the importance of advanced modeling to avoid false conclusions.

***the final 2 questions have yet to come**
---

## Data Overview

The analysis is based on a comprehensive panel dataset compiled from two primary public sources:

1.  **The World Bank:** Provided core economic indicators such as GDP per capita, population, and country development status.
2.  **The OECD:** Served as the source for key technology and trade variables, including internet usage percentage, and detailed import/export data for digital services.

The final dataset covers approximately 150 countries over a span from 2005 to 2020. The key variables used include `Exports_Digital_Service`, `internet_usage_pct`, `gdp_per_capita`, `population`, and `is_developing`.

*   **Data Source Link (OECD Stats):** [https://stats.oecd.org/](https://stats.oecd.org/ )

---

## Key Technical Steps

The project was executed through a series of data processing and analysis steps, leveraging several key Python libraries.

1.  **Data Cleaning & Merging:**
    *   Raw CSV files from the OECD and World Bank were loaded using **Pandas**.
    *   The datasets were cleaned, harmonized, and merged into a single, tidy panel DataFrame (`final_panel_for_regression.csv`) used for all analyses.

2.  **Analysis & Modeling:**
    *   A baseline Ordinary Least Squares (OLS) regression was performed using **Statsmodels**.
    *   Advanced **Panel Data Regressions** (Fixed Effects and Two-Way Fixed Effects models) were implemented using the **linearmodels** library to control for unobserved heterogeneity.

3.  **Visualization & Dashboarding:**
    *   An interactive web application was built using **Streamlit**.
    *   All data visualizations (choropleth maps, animated charts, 3D scatter plots) were created using **Plotly Express** and **Plotly Graph Objects**.
    *   The dashboard features interactive widgets and a custom dark theme (via `config.toml`) to create a polished, user-driven experience.

