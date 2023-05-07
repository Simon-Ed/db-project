from flask import Flask, jsonify
from endpoints.courses import get_courses
from endpoints.rooms import get_rooms
from endpoints.teachers import get_teachers

app = Flask(__name__)

@app.route('/courses', methods=['GET'])
def courses_endpoint():
    courses = get_courses()

    return jsonify(courses)


@app.route('/rooms', methods=['GET'])
def rooms_endpoint():
    rooms = get_rooms()

    return jsonify(rooms)


@app.route('/teachers', methods=['GET'])
def teachers_endpoint():
    teachers = get_teachers()

    return jsonify(teachers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
