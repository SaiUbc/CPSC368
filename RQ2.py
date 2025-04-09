import oracledb
import pandas as pd
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt

# Load environment variables from .env file
load_dotenv()

# Retrieve CWL and SNUM from environment variables
cwl = os.getenv('CWL')
snum = os.getenv('SNUM')

# Make Oracle SQLPlus connection
dsn = oracledb.makedsn("localhost", 1522, service_name="stu")
connection = oracledb.connect(user=f"ora_{cwl}", password=f"a{snum}", dsn=dsn)

cur = connection.cursor()

query = """
SELECT 
    M."YEAR",
    M."SEX",
    T.TOTAL_TELEHEALTH_USERS,
    M.TOTAL_DEATHS,
    ROUND(M.TOTAL_DEATHS * 1000.0 / NULLIF(T.TOTAL_TELEHEALTH_USERS, 0), 2) AS DEATHS_PER_1000_USERS
FROM (
    SELECT 
        "YEAR",
        "SEX",
        SUM("DEATHS") AS TOTAL_DEATHS
    FROM MORTALITY
    WHERE "SEX" IN ('Male', 'Female')
    GROUP BY "YEAR", "SEX"
) M
JOIN (
    SELECT 
        "YEAR",
        "SEX",
        SUM("TOTAL_TELEHEALTH_USERS") AS TOTAL_TELEHEALTH_USERS
    FROM TELEHEALTH
    WHERE "SEX" IN ('Male', 'Female') AND "AGE_GROUP" = 'All'
    GROUP BY "YEAR", "SEX"
) T
ON M."YEAR" = T."YEAR" AND M."SEX" = T."SEX"
WHERE M."YEAR" BETWEEN 2020 AND 2022
ORDER BY M."YEAR", M."SEX"
"""

cur.execute(query)

rows = cur.fetchall()
columns = [col[0] for col in cur.description]

df = pd.DataFrame(rows, columns=columns)

data_dir = "data/processed_data"
df.to_csv(os.path.join(data_dir, "research_question_2.csv"), index=False)

cur.close()

print(df)

years = df["YEAR"].unique()
male = df[df["SEX"] == "Male"]
female = df[df["SEX"] == "Female"]

bar_width = 0.35
index = range(len(years))

plt.figure(figsize=(10, 6))
plt.bar([i - bar_width/2 for i in index], female["DEATHS_PER_1000_USERS"], 
        width=bar_width, label='Female')
plt.bar([i + bar_width/2 for i in index], male["DEATHS_PER_1000_USERS"], 
        width=bar_width, label='Male')

plt.title("Deaths per 1000 Telehealth Users by Year and Sex (2020–2022)", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Deaths per 1000 Users", fontsize=14)
plt.xticks(index, years, fontsize=12)
plt.yticks(fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save and show plot
plt.savefig("pics/deaths_per_1000_users_by_sex.png", dpi=300)