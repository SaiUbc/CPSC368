import oracledb
import pandas as pd
from dotenv import load_dotenv
import os

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
cur.close()

print(df)