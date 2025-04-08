import pandas as pd
import sqlite3

df1 = pd.read_csv("mortality.csv")
df2 = pd.read_csv("telehealth.csv")

conn = sqlite3.connect("my_database.db")

df1.to_sql("mortality", conn, if_exists="replace", index=False)
df2.to_sql("telehealth", conn, if_exists="replace", index=False)

print("🔹 Column names in 'mortality':")
mortality_columns = pd.read_sql_query("SELECT * FROM mortality LIMIT 1;", conn).columns.tolist()
print(mortality_columns)

print("\n🔹 Column names in 'telehealth':")
telehealth_columns = pd.read_sql_query("SELECT * FROM telehealth LIMIT 1;", conn).columns.tolist()
print(telehealth_columns)

# --- Get schema for mortality
print("\n🔹 PRAGMA schema info for 'mortality':")
mortality_schema = pd.read_sql_query("PRAGMA table_info(mortality);", conn)
print(mortality_schema)

# --- Get schema for telehealth
print("\n🔹 PRAGMA schema info for 'telehealth':")
telehealth_schema = pd.read_sql_query("PRAGMA table_info(telehealth);", conn)
print(telehealth_schema)

print("\n🔹 CREATE TABLE SQL for 'mortality':")
mortality_create_sql = pd.read_sql_query(
    "SELECT sql FROM sqlite_master WHERE type='table' AND name='mortality';",
    conn
)
print(mortality_create_sql['sql'][0])

print("\n🔹 CREATE TABLE SQL for 'telehealth':")
telehealth_create_sql = pd.read_sql_query(
    "SELECT sql FROM sqlite_master WHERE type='table' AND name='telehealth';",
    conn
)
print(telehealth_create_sql['sql'][0])

conn.close()