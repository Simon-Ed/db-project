import http
from flask import Flask, jsonify
import pymysql.cursors

# Database configuration
adminConfig = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'db': 'project_db',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

adminConnection = pymysql.connect(**adminConfig)

def init_admin_app(app: Flask):
    @app.route('/admin/test', methods=['GET'])
    def test_admin():
        with adminConfig.cursor() as cursor:
            # query = "SELECT * FROM course;"
            query = "INSERT INTO institute (institute ,faculty) VALUES ('sa', 'b');"
            cursor.execute(query)
            # https://stackoverflow.com/questions/6027271/python-mysql-insert-not-working
            adminConfig.commit()
            data = cursor.fetchall()
            response = jsonify(data)
        return response ,http.HTTPStatus.OK
