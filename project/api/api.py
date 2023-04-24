import http
from flask import Flask, jsonify

# Method contain API endpoints
def init_app(app: Flask):
    @app.route('/courses', methods=['GET'])
    def get_courses():
        return jsonify({'message':'courses endpoint'}), http.HTTPStatus.OK

    @app.route('/rooms', methods=['GET'])
    def get_rooms():
        return jsonify({'message':'rooms endpoint'}), http.HTTPStatus.OK

    @app.route('/teachers', methods=['GET'])
    def get_teachers():
        return jsonify({'message':'teachers endpoint'}), http.HTTPStatus.OK