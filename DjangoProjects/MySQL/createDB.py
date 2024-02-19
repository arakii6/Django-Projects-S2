#createDB.py
from config import db_connection, db_cur

# Step 1: Create Database
db_cur.execute("CREATE DATABASE IF NOT EXISTS Django_Projects")

# Step 2: Create and Grant all privileges to user
db_cur.execute("CREATE USER 'DJ_arakii6'@'localhost' IDENTIFIED BY 'django'")
db_cur.execute("GRANT ALL PRIVILEGES ON Django_Projects.* TO 'DJ_arakii6'@'localhost'")
db_cur.execute("FLUSH PRIVILEGES")

# Step 3: Close the cursor and connection
db_cur.close()
db_connection.close()
