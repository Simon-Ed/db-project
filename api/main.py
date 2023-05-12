from datetime import datetime
import http
from flask import Flask, jsonify, render_template, request
from endpoints.courses import *
from endpoints.rooms import *
from endpoints.teachers import *

app = Flask(__name__)

# Endpoint for testing the 16 queries in the task.
@app.route('/query-test/<int:endpoint>', methods=['GET'])
def query_test_endpoint(endpoint):
    id = request.args.get('id')
    name = request.args.get('name')
    surname = request.args.get('surname')
    semester = request.args.get('semester')
    starttime = request.args.get('starttime', default='', type=str)
    endtime = request.args.get('endtime', default='', type=str)

    # Check if the date is formatted correctly
    if starttime:
        try:
            datetime.strptime(starttime, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return jsonify({'error': 'Invalid date format'}), http.HTTPStatus.BAD_REQUEST
        
    if endtime:
        try:
            datetime.strptime(endtime, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return jsonify({'error': 'Invalid date format'}), http.HTTPStatus.BAD_REQUEST

    tasks = {
        1: get_courses_task1,
        2: lambda: get_courses_task2(name, semester),
        3: lambda: get_courses_task3(id, starttime, endtime),
        4: lambda: get_courses_task4(starttime, id),
        5: get_courses_task5,
        6: get_courses_task6,
        7: get_courses_task7,
        8: get_rooms_task8,
        9: get_rooms_task9,
        10: get_rooms_task10,
        11: get_rooms_task11,
        12: get_teachers_task12,
        13: get_teachers_task13,
        14: get_teachers_task14,
        15: get_courses_task15,
        16: get_teachers_task16
    }
    return tasks.get(endpoint, lambda: None)()

@app.route('/')
def default_path():
    URL = "http://localhost:5000"
    return render_template('index.html', URL=URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
