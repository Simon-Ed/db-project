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

rootConnection = mysql.connector.connect(**rootConfig)
'''adminConnection = mysql.connector.connect(**adminConfig)
publicConnection = mysql.connector.connect(**publicConfig)
studentConnection = mysql.connector.connect(**studentConfig)
lecturerConnection = mysql.connector.connect(**lecturerConfig)'''

print("DB connected")