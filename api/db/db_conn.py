import mysql.connector

# Database configuration
rootConfig = {
    'host': 'mysql',
    'user': 'root',
    'password': 'root',
    'database': 'db',
    'port': "3306"
}

adminConfig = {
    'host': 'mysql',
    'user': 'admin',
    'password': '',
    'database': 'db',
    'port': "3306"
}

publicConfig = {
    'host': 'mysql',
    'user': 'general_public',
    'password': '',
    'database': 'db',
    'port': "3306"
}

studentConfig = {
    'host': 'mysql',
    'user': 'Student',
    'password': '',
    'database': 'db',
    'port': "3306"
}

lecturerConfig = {
    'host': 'mysql',
    'user': 'lecturer',
    'password': '',
    'database': 'db',
    'port': "3306"
}

# Dan's config 
rootConfig = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'project_db7',
    'port': "3307"
}

rootConnection = mysql.connector.connect(**rootConfig)

print("DB connected")

