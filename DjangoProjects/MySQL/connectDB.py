# Step 1: Import msql connector to connect to MySQL
import mysql.connector

# Step 2: Create a dictionary to store all arguments as keys-value pairs
db_config = {
    'user': 'DJ_arakii6',
    'password': 'django',
    'host': 'localhost',
    'database': 'Django_Projects'
}

# Step 3: Create a variable to hold the connection object established using mysql.connector.connect().
db_connection = mysql.connector.connect(**db_config)