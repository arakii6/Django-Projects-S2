# Step 1: Import msql connector to connect to MySQL
import mysql.connector

# Step 2: Create a dictionary to store all arguments as keys-value pairs
db_config = {
    'user': 'root',
    'password': 'admin',
    'host': 'localhost',
}

# Step 3: Create a variable to hold the connection object established using mysql.connector.connect().
db_connection = mysql.connector.connect(**db_config)

# Step 4: Print the connection id, to show that the connection has been established
print(db_connection.connection_id)

# Step 5: Create a Cursor object to execute SQL statements via python code
db_cur = db_connection.cursor()