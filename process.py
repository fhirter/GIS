import pandas as pd
import sqlite3

# Define the path to the CSV file
csv_file_path = 'unlock.csv'

# Load the CSV data into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Define the SQLite database file (it will be created if it doesn't exist)
sqlite_file = 'identifier.sqlite'

# Establish a connection to the SQLite database
conn = sqlite3.connect(sqlite_file)

# Define the name of the table to store the data
table_name = 'raw_data'

# Load the data into the SQLite database table
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Close the connection to the SQLite database
conn.close()

print(f"Data successfully loaded into the '{table_name}' table in '{sqlite_file}' database.")