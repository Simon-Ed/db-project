import mysql.connector

# Database configuration
rootConfig = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'project_db',
    'port': "3306"
}

adminConfig = {
    'host': 'localhost',
    'user': 'admin',
    'password': '',
    'db': 'project_db',
    'port': "3306"
}

publicConfig = {
    'host': 'localhost',
    'user': 'general_public',
    'password': '',
    'db': 'project_db',
    'port': "3306"
}

studentConfig = {
    'host': 'localhost',
    'user': 'Student',
    'password': '',
    'db': 'project_db',
    'port': "3306"
}

lecturerConfig = {
    'host': 'localhost',
    'user': 'lecturer',
    'password': '',
    'db': 'project_db',
    'port': "3306"
}

rootConnection = mysql.connector.connect(**rootConfig)
adminConnection = mysql.connector.connect(**adminConfig)
publicConnection = mysql.connector.connect(**publicConfig)
studentConnection = mysql.connector.connect(**studentConfig)
lecturerConnection = mysql.connector.connect(**lecturerConfig)

print("DB connected")