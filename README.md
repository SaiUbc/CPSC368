# CPSC368# 🏥 Digital Healthcare Analysis in the United States (2020–2024)

This project explores the adoption and impact of digital healthcare services (telehealth) in the United States between 2020 and 2024. Using SQL queries on SQLite databases created from public datasets, we answer three key research questions (RQs) around trends in adoption, demographic usage, and potential effects on hospital readmissions.

---

## 📌 Research Questions

**RQ1:** Has the adoption of digital healthcare in the United States increased from 2020 to 2024?

**RQ2:** Did the use of digital healthcare services have an impact on the amount of hospital readmissions that occurred from 2020 to 2022 in the United States? *(Coming soon)*

**RQ3:** Which groups of people used digital healthcare services the most between age and race in 2020 to 2024 in the United States?

---

## 🗂 Project Structure

| File | Description |
|------|-------------|
| `sqlite3.py` | Creates a SQLite `.db` from `mortality.csv` and `telehealth.csv` |
| `RQ1.py` | SQL analysis for RQ1 – adoption trend (2020–2024) |
| `RQ3.py` | SQL analysis for RQ3 – demographic usage by age group and race |
| `mortality.csv` | Mortality dataset with year, age group, sex, and death counts |
| `telehealth.csv` | Telehealth dataset with demographic + digital healthcare usage info |
| `my_database.db` | Auto-generated SQLite database built from both CSVs |
| `LICENSE` | Open source license |
| `README.md` | Project overview and usage instructions |

---

## 📦 Requirements

Make sure you have the following Python packages installed:

```bash
pip install pandas sqlite3 matplotlib
