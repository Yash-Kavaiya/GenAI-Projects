import sqlite3
import pandas as pd
import random
from faker import Faker
import time

# Initialize Faker for generating dummy data
fake = Faker('en_IN')

# Create a new SQLite database (or connect to an existing one)
conn = sqlite3.connect('employee_kpi.db')
cursor = conn.cursor()

# Create a new table for employee data
cursor.execute('''
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    department TEXT,
    salary REAL,
    performance_score INTEGER,
    years_of_experience INTEGER,
    last_promotion_year INTEGER,
    location TEXT
)
''')

# Generate dummy data
departments = ['HR', 'Finance', 'IT', 'Sales', 'Marketing']
locations = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai']

start_time = time.time()  # Start time for execution

num_entries = 5000  # Number of entries to insert
for _ in range(num_entries):
    name = fake.name()
    age = random.randint(22, 60)
    department = random.choice(departments)
    salary = round(random.uniform(300000, 1500000), 2)
    performance_score = random.randint(1, 10)
    years_of_experience = random.randint(1, 35)
    last_promotion_year = random.randint(2015, 2023)
    location = random.choice(locations)
    
    cursor.execute('''
    INSERT INTO employee (name, age, department, salary, performance_score, years_of_experience, last_promotion_year, location)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, age, department, salary, performance_score, years_of_experience, last_promotion_year, location))

# Commit the transaction and close the connection
conn.commit()
conn.close()

# Calculate execution time
end_time = time.time()
execution_time = end_time - start_time

# Verify the data by loading it into a pandas DataFrame
conn = sqlite3.connect('employee_kpi.db')
df = pd.read_sql_query('SELECT * FROM employee', conn)
conn.close()

# Save DataFrame to CSV
csv_file_path = 'employee_kpi.csv'
df.to_csv(csv_file_path, index=False)

# Print the DataFrame and execution details
print(df)
print(f"Total entries inserted: {num_entries}")
print(f"Execution time: {execution_time:.2f} seconds")
print(f"Data saved to CSV file at: {csv_file_path}")
