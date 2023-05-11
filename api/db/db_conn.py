import mysql.connector

# Database configuration
rootConfig = {
    'host': 'mysql',
    'user': 'root',
    'password': 'root',
    'database': 'db',
    'port': "3306"
}

# Dan sin config
# rootConfig = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': '',
#     'database': 'project_db7',
#     'port': "3307"
# }

rootConnection = mysql.connector.connect(**rootConfig)

print("DB connected")

