import http
from flask import Flask, jsonify
import pymysql.cursors

# Database configuration
adminConfig = {
    'host': 'localhost',
    'user': 'admin',
    'password': '',
    'db': 'project_db',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

publicConfig = {
    'host': 'localhost',
    'user': 'general_public',
    'password': '',
    'db': 'project_db',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

studentConfig = {
    'host': 'localhost',
    'user': 'Student',
    'password': '',
    'db': 'project_db',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

adminConnection = pymysql.connect(**adminConfig)
publicConnection = pymysql.connect(**publicConfig)
studentConnection = pymysql.connect(**studentConfig)


# Method contain API endpoints
def init_app(app: Flask):
    @app.route('/courses', methods=['GET'])
    def get_courses():
        return jsonify({'message': 'courses endpoint'}), http.HTTPStatus.OK

    @app.route('/rooms', methods=['GET'])
    def get_rooms():
        return jsonify({'message': 'rooms endpoint'}), http.HTTPStatus.OK

    @app.route('/teachers', methods=['GET'])
    def get_teachers():
        return jsonify({'message': 'teachers endpoint'}), http.HTTPStatus.OK

    @app.route('/test', methods=['GET'])
    def test_user_permissions_SELECT():  #
        with publicConnection.cursor() as cursor:
            query = "UPDATE course SET name = 'Databaser 3', teacher_id = '1234567890'" \
                    " WHERE course_id = 'IDATG2001' AND semester_id = '2' LIMIT 1"
            cursor.execute(query)
            publicConnection.commit()
            data = cursor.fetchall()
            response = jsonify(data)
        return response

    """"@app.route('/test', methods=['GET'])
    def test_USER_permissions_BOOKROOM():  # Is supposed to fail, because general public can not book rooms.
        with publicConnection.cursor() as cursor:
            # query = "SELECT * FROM course;"
            query = "INSERT INTO institute (institute ,faculty) VALUES ('sa', 'b');"
            cursor.execute(query)
            # https://stackoverflow.com/questions/6027271/python-mysql-insert-not-working
            publicConnection.commit()
            data = cursor.fetchall()
            response = jsonify(data)
        return response

    @app.route('/test', methods=['GET'])
    def test_ADMIN_permissions():
        with adminConnection.cursor() as adminCursor:
            # query = ----
            cursor.execute(query)
            adminConnection.commit()
            data = cursor.fetchall()
            response = jsonify(data)
        return response

    @app.route('/test', methods=['GET'])
    def test_STUDENT_permissions():
        with studentConnection.cursor() as studentCursor:
            # query = ----
            cursor.execute(query)
            studentConnection.commit()
            data = cursor.fetchall()
            response = jsonify(data)
        return response"""
