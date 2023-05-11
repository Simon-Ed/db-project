import mysql.connector

# Database configuration
rootConfig = {
    'host': 'mysql',
    'user': 'root',
    'password': 'root',
    'database': 'db',
    'port': "3306"
}

rootConnection = mysql.connector.connect(**rootConfig)

print("DB connected")

