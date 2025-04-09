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
    "YEAR",
    SUM("TOTAL_TELEHEALTH_USERS") AS total_users
FROM telehealth
WHERE "YEAR" BETWEEN 2020 AND 2024
GROUP BY "YEAR"
ORDER BY "YEAR"
"""

cur.execute(query)

rows = cur.fetchall()
columns = [col[0] for col in cur.description]

df = pd.DataFrame(rows, columns=columns)

data_dir = "data/processed_data"
df.to_csv(os.path.join(data_dir, "research_question_1.csv"), index=False)


cur.close()

print(df)

plt.figure(figsize=(10, 6))
plt.bar(df["YEAR"], df["TOTAL_USERS"], color='skyblue')
plt.title("Total Telehealth Users (2020–2024)", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Total Users", fontsize=14)
plt.xticks(df["YEAR"], fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot as an image
plt.savefig("pics/total_telehealth_users_2020_2024.png", dpi=300)