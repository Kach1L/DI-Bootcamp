import requests
import psycopg2
import random

# Connect to your PostgreSQL database
connection = psycopg2.connect(
    database="Menu_Base",
    user="postgres",
    password="Kachikwulu1",
    host="localhost",
    port="5432"
)

# Number of random countries to populate
num_countries = 10

# Fetch random countries from the REST Countries API
response = requests.get(f"https://restcountries.com/v3.1/all")
countries_data = response.json()

# Create a cursor to execute SQL commands
cursor = connection.cursor()

# Iterate over random countries and insert their data into the database
for _ in range(num_countries):
    random_country = random.choice(countries_data)
    name = random_country["name"]["common"]
    capital = random_country.get("capital", "N/A")
    flag = random_country.get("flags", ["N/A"])
    subregion = random_country.get("subregion", "N/A")
    population = random_country.get("population", 0)
    
    # Insert data into the table
    insert_query = "INSERT INTO countries (name, capital, flag, subregion, population) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (name, capital, flag, subregion, population))
    connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print(f"{num_countries} random countries inserted into the database.")
