import pandas as pd

def generate_sql(csv_file, table_name, output_file):
    df = pd.read_csv(csv_file)

    with open(output_file, "w") as f:
        for _, row in df.iterrows():
            values = "', '".join(str(v) for v in row.tolist())  # Convert row to string values
            sql_statement = f"INSERT INTO {table_name} VALUES ('{values}');\n"
            f.write(sql_statement)

generate_sql("telehealth.csv", "telehealth", "insert_telehealth.sql")
generate_sql("mortality.csv", "mortality", "insert_mortality.sql")

print("✅ SQL files generated successfully!")