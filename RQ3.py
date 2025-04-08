import pandas as pd
import sqlite3

# Load CSV files
df1 = pd.read_csv("mortality.csv")
df2 = pd.read_csv("telehealth.csv")

# Create or connect to SQLite database
conn = sqlite3.connect("my_database.db")

# Write dataframes to SQLite
df1.to_sql("mortality", conn, if_exists="replace", index=False)
df2.to_sql("telehealth", conn, if_exists="replace", index=False)

# --- SQL Query: Which groups used telehealth the most between age and race (2020–2024) ---
query = """
SELECT 
    "Age_Group",
    "Race",
    SUM("Total_Telehealth_Users") AS total_users
FROM telehealth
WHERE "Year" BETWEEN 2020 AND 2024
GROUP BY "Age_Group", "Race"
ORDER BY total_users DESC;
"""

results = pd.read_sql_query(query, conn)
print("🔹 Top digital healthcare users by Age Group and Race (2020–2024):")
print(results)

results.to_csv("top_telehealth_users_by_age_race_3RQ.csv", index=False)

conn.close()