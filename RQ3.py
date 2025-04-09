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
    "AGE_GROUP",
    "RACE",
    SUM("TOTAL_TELEHEALTH_USERS") AS TOTAL_USERS
FROM TELEHEALTH
WHERE "YEAR" BETWEEN 2020 AND 2024
GROUP BY "AGE_GROUP", "RACE"
ORDER BY TOTAL_USERS DESC
"""

cur.execute(query)

rows = cur.fetchall()
columns = [col[0] for col in cur.description]

df = pd.DataFrame(rows, columns=columns)

# Save the DataFrame to a CSV file in the data directory
data_dir = "data/processed_data"
df.to_csv(os.path.join(data_dir, "research_question_3.csv"), index=False)

print(df)

df["LABEL"] = df["AGE_GROUP"] + " - " + df["RACE"]

# Plot the top N combinations (e.g., top 15 for clarity)
# top_n = 15
# top_data = df.head(top_n)

# Create horizontal bar chart
plt.figure(figsize=(12, 8))
plt.barh(df["LABEL"], df["TOTAL_USERS"], color="teal")
plt.xlabel("Total Telehealth Users", fontsize=14)
plt.ylabel("Age Group - Race", fontsize=14)
plt.title("Top Digital Healthcare Users by Age Group and Race (2020–2024)", fontsize=16)
plt.gca().invert_yaxis()  # Highest value at top
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

# Save and display the figure
plt.savefig("pics/top_telehealth_users_by_age_race.png", dpi=300)