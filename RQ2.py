import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect("my_database.db")

# SQL query
query = """
SELECT 
    m."Year",
    m."Sex",
    t.total_telehealth_users,
    m.total_deaths,
    ROUND(m.total_deaths * 1000.0 / NULLIF(t.total_telehealth_users, 0), 2) AS deaths_per_1000_users
FROM (
    SELECT 
        "Year",
        "Sex",
        SUM("Deaths") AS total_deaths
    FROM mortality
    WHERE "Sex" IN ('Male', 'Female')
    GROUP BY "Year", "Sex"
) m
JOIN (
    SELECT 
        "Year",
        "Sex",
        SUM("Total_Telehealth_Users") AS total_telehealth_users
    FROM telehealth
    WHERE "Sex" IN ('Male', 'Female') AND "Age_Group" = 'All'
    GROUP BY "Year", "Sex"
) t
ON m."Year" = t."Year" AND m."Sex" = t."Sex"
WHERE m."Year" BETWEEN 2020 AND 2022
ORDER BY m."Year", m."Sex";
"""

# Load data
df = pd.read_sql_query(query, conn)
conn.close()

# Display the DataFrame
print("📊 RQ2: Impact of Digital Healthcare on Mortality (2020–2022)")
print(df)


years = df["Year"].unique()
male = df[df["Sex"] == "Male"]
female = df[df["Sex"] == "Female"]

bar_width = 0.35
index = range(len(years))

plt.figure(figsize=(10, 6))
plt.bar([i - bar_width/2 for i in index], female["deaths_per_1000_users"], 
        width=bar_width, label='Female')
plt.bar([i + bar_width/2 for i in index], male["deaths_per_1000_users"], 
        width=bar_width, label='Male')

plt.title("Deaths per 1000 Telehealth Users by Year and Sex (2020–2022)", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Deaths per 1000 Users", fontsize=14)
plt.xticks(index, years, fontsize=12)
plt.yticks(fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save and show plot
plt.savefig("deaths_per_1000_users_by_sex.png", dpi=300)
plt.show()