import http
from flask import Flask, jsonify
import pymysql.cursors


publicConfig = {
    'host': 'localhost',
    # 'user': 'root',
    'user': 'general_public',
    'password': '',
    'db': 'project_db',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

publicConnection = pymysql.connect(**publicConfig)

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

    @app.route('/admin/test', methods=['GET'])
    def test_user_permissions():
        with publicConnection.cursor() as cursor:
            # query = "SELECT * FROM course;"
            query = "INSERT INTO institute (institute ,faculty) VALUES ('sa', 'b');"
            cursor.execute(query)
            # https://stackoverflow.com/questions/6027271/python-mysql-insert-not-working
            publicConnection.commit()
            data = cursor.fetchall()
            response = jsonify(data)
        return response
