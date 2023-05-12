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
    'database': 'project_db',
    'port': "3306"
}

publicConfig = {
    'host': 'localhost',
    'user': 'general_public',
    'password': '',
    'database': 'project_db',
    'port': "3306"
}

studentConfig = {
    'host': 'localhost',
    'user': 'student',
    'password': '',
    'database': 'project_db',
    'port': "3306"
}

lecturerConfig = {
    'host': 'localhost',
    'user': 'lecturer',
    'password': '',
    'database': 'project_db',
    'port': "3306"
}

rootConnection = mysql.connector.connect(**rootConfig)
publicConnection = mysql.connector.connect(**publicConfig)
studentConnection = mysql.connector.connect(**studentConfig)
lecturerConnect = mysql.connector.connect(**lecturerConfig)
adminConnect = mysql.connector.connect(**adminConfig)

print("DB connected")

