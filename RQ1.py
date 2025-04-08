import pandas as pd
import sqlite3

conn = sqlite3.connect("my_database.db")

# --- Query 1: Total Telehealth Users Per Year ---
query_total_users = """
SELECT 
    "Year",
    SUM("Total_Telehealth_Users") AS total_users
FROM telehealth
WHERE "Year" BETWEEN 2020 AND 2024
GROUP BY "Year"
ORDER BY "Year";
"""

total_users = pd.read_sql_query(query_total_users, conn)
print("📊 Total Telehealth Users (2020–2024):")
print(total_users)

# --- Query 2: Average % of Medicare Telehealth Users Per Year ---
query_avg_percentage = """
SELECT 
    "Year",
    AVG("Percentage_of_Medicare_Telehealth_Users") AS avg_percentage
FROM telehealth
WHERE "Year" BETWEEN 2020 AND 2024
GROUP BY "Year"
ORDER BY "Year";
"""

avg_percentage = pd.read_sql_query(query_avg_percentage, conn)
print("\n📊 Average % of Medicare Telehealth Users (2020–2024):")
print(avg_percentage)

total_users.to_csv("total_telehealth_users_by_year_1RQ.csv", index=False)
avg_percentage.to_csv("average_percentage_medicare_users_by_year_1RQ.csv", index=False)

# --- Optional: Plot (Uncomment to use) ---
# import matplotlib.pyplot as plt
# fig, ax1 = plt.subplots()
# ax2 = ax1.twinx()
# 
# ax1.plot(total_users["Year"], total_users["total_users"], 'g-', label='Total Users')
# ax2.plot(avg_percentage["Year"], avg_percentage["avg_percentage"], 'b-', label='Avg % Medicare Users')
# 
# ax1.set_xlabel('Year')
# ax1.set_ylabel('Total Users', color='g')
# ax2.set_ylabel('Avg % Medicare Users', color='b')
# 
# plt.title("Digital Healthcare Adoption in the US (2020–2024)")
# plt.show()

conn.close()