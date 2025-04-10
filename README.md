# 🩺 CPSC368 – Digital Healthcare Analysis in the United States (2020–2024)

This project explores the **adoption** and **impact** of digital healthcare services (telehealth) in the United States from **2020 to 2024**. Using public datasets and SQL queries on a local SQLite database, we analyze trends in telehealth usage, demographic patterns, and potential relationships with health outcomes like hospital mortality.

---

## ❓ Research Questions

- **RQ1:** Has the adoption of digital healthcare in the United States increased from 2020 to 2024? 
- **RQ2:** Did the use of digital healthcare services have an impact on mortality rates during the years 2020-2022? 
- **RQ3:** Which groups of people used digital healthcare services the most between age and race in 2020 to 2024 in the United States?

---

## 🗂️ Project Structure

| File/Folder            | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `create_tables.sql`    | SQL script to create tables from CSV files                                  |
| `insert_sql.py`        | Python script to insert and process CSV data into SQLite database           |
| `RQ1.py`               | SQL + analysis for RQ1 (adoption trend: 2020–2024)                          |
| `RQ2.py`               | SQL + analysis for RQ2 (mortality impact of telehealth)                    |
| `RQ3.py`               | SQL + analysis for RQ3 (demographic usage by age & race)                   |
| `data/`                | Folder containing raw datasets (`mortality.csv`, `telehealth.csv`)         |
| `data/processed_data/` | Processed outputs used in answering RQs                                     |
| `notebooks/`           | Jupyter notebooks for exploratory data analysis                             |
| `pics/`                | Generated visualizations and graphs from the analysis                       |
| `my_database.db`       | SQLite database built from telehealth and mortality datasets                |
| `README.md`            | Project documentation and usage guide                                       |
| `LICENSE`              | MIT License                                                                 |

---

## 🧪 Datasets

This project uses two public datasets:

- **Mortality Data:** Contains year, sex, age group, and number of deaths.
- **Telehealth Data:** Contains demographic details (age, sex, race) and counts of users accessing telehealth services.

---

## 📄 Dataset Schema

### `telehealth.csv` → `telehealth` table

| Column                              | Type     | Description                                                |
|-------------------------------------|----------|------------------------------------------------------------|
| `ID`                                | NUMBER   | Unique identifier for each record                          |
| `Year`                              | NUMBER   | Year of observation (2020–2024)                            |
| `Age_Group`                         | VARCHAR  | Age category (e.g., 0–64, 65–74, 75–84, 85+)               |
| `State`                             | VARCHAR  | U.S. state abbreviation                                    |
| `Medicare_Medicaid_Status`          | VARCHAR  | Medicare/Medicaid eligibility category                     |
| `Race`                              | VARCHAR  | Race/Ethnicity group                                       |
| `Sex`                               | VARCHAR  | Sex (Male, Female)                                         |
| `Medicare_Enrollment_Status`        | VARCHAR  | Medicare enrollment type/status                            |
| `Age_Grouping`                      | VARCHAR  | Age category (e.g., 0–64, 65–74, 75–84, 85+)               |
| `Urban_Rural_Description`           | VARCHAR  | Urban or rural classification                              |
| `Total_Eligible_Users`              | NUMBER   | Total people eligible for digital health                   |
| `Total_Medicare_Enrollment`         | NUMBER   | Total Medicare enrollees                                   |
| `Total_Telehealth_Users`            | NUMBER   | Number of people who used telehealth services              |
| `Percentage_of_Medicare_Telehealth_Users` | NUMBER | Percent of Medicare enrollees who used telehealth      |

### `mortality.csv` → `mortality` table

| Column      | Type     | Description                            |
|-------------|----------|----------------------------------------|
| `ID`        | NUMBER   | Unique identifier for each record      |
| `Year`      | NUMBER   | Year of death report                   |
| `Sex`       | VARCHAR  | Sex (Male, Female)                     |
| `Age`       | NUMBER   | Age in years                           |
| `Deaths`    | NUMBER   | Number of recorded deaths              |
| `Age_Group` | VARCHAR  | Age category (e.g., 0–64, 65–74, etc.) |

---

## 📋 SQL Queries

### RQ1 – Has the adoption of digital healthcare increased from 2020 to 2024?

```sql
SELECT 
    "Year",
    SUM("Total_Telehealth_Users") AS total_users
FROM telehealth
WHERE "Year" BETWEEN 2020 AND 2024
GROUP BY "Year"
ORDER BY "Year";
```

### RQ2 – Did digital healthcare use impact mortality from 2020 to 2022?
```sql
SELECT 
    M."Year",
    M."Sex",
    T.Total_Telehealth_Users,
    M.Total_Deaths,
    ROUND(M.Total_Deaths * 1000.0 / NULLIF(T.Total_Telehealth_Users, 0), 2) AS Deaths_Per_1000_Users
FROM (
    SELECT 
        "Year",
        "Sex",
        SUM("Deaths") AS Total_Deaths
    FROM mortality
    WHERE "Sex" IN ('Male', 'Female')
    GROUP BY "Year", "Sex"
) M
JOIN (
    SELECT 
        "Year",
        "Sex",
        SUM("Total_Telehealth_Users") AS Total_Telehealth_Users
    FROM telehealth
    WHERE "Sex" IN ('Male', 'Female') AND "Age_Group" = 'All'
    GROUP BY "Year", "Sex"
) T
ON M."Year" = T."Year" AND M."Sex" = T."Sex"
WHERE M."Year" BETWEEN 2020 AND 2022
ORDER BY M."Year", M."Sex";
```

### RQ3 – Which age and race groups used telehealth the most from 2020 to 2024?
```sql
SELECT 
    "Age_Group",
    "Race",
    SUM("Total_Telehealth_Users") AS Total_Users
FROM telehealth
WHERE "Year" BETWEEN 2020 AND 2024
GROUP BY "Age_Group", "Race"
ORDER BY Total_Users DESC;
```



## 📊 Sample Visualizations

Below are a few sample plots generated from the analysis:

<img src="pics/total_telehealth_users_2020_2024.png" width="500"/>
<img src="pics/deaths_per_1000_users_by_sex.png" width="500"/>
<img src="pics/top_telehealth_users_by_age_race.png" width="500"/>

---

## ⚙️ Requirements

Ensure the following Python packages are installed:

```bash
pip install pandas sqlite3 matplotlib oracledb dotenv
```

## LICENSE

This project is licensed under the MIT License.
You are free to use, modify, and distribute this project for personal or academic purposes.

See the LICENSE file for more details.

## Acknowledgements

Developed by Sai Pusuluri, Elias Khan, Angus Lau as part of CPSC 368: Databases in Data Science at UBC.
Special thanks to instructors and data providers from CMS.gov.
