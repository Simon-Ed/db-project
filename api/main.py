import http
from utility.query_format import validateDatetime
from flask import Flask, jsonify, render_template, request
from endpoints.courses import *
from endpoints.rooms import *
from endpoints.teachers import *

app = Flask(__name__)
API_URL = "http://localhost:5000"

# Endpoint for testing the 16 queries in the task.
@app.route('/query-test/<int:endpoint>', methods=['GET'])
def query_test_endpoint(endpoint):
    # Get potential query parameters 
    id = request.args.get('id')
    name = request.args.get('name')
    surname = request.args.get('surname')
    semester = request.args.get('semester')
    starttime = request.args.get('starttime', default='', type=str)
    endtime = request.args.get('endtime', default='', type=str)

    if starttime:
        if not validateDatetime(starttime):
            return jsonify({'error': 'Invalid datetime format'}), http.HTTPStatus.BAD_REQUEST
        
    if endtime:
        if not validateDatetime(endtime):
            return jsonify({'error': 'Invalid datetime format'}), http.HTTPStatus.BAD_REQUEST

    # List of the different endpoints
    tasks = {
        1: get_courses_task1,
        2: lambda: get_courses_task2(name, semester),
        3: lambda: get_courses_task3(id, starttime, endtime),
        4: lambda: get_courses_task4(starttime, id),
        5: get_courses_task5,
        6: lambda: get_courses_task6(name, surname),
        7: lambda: get_courses_task7(name, surname),
        8: lambda: get_rooms_task8(starttime, endtime),
        9: lambda: get_rooms_task9(name, surname),
        10: get_rooms_task10,
        11: get_rooms_task11,
        12: get_teachers_task12,
        13: get_teachers_task13,
        14: get_teachers_task14,
        15: lambda: get_courses_task15(id),
        16: get_teachers_task16
    }

    # Handle the request
    return tasks.get(endpoint, lambda: None)()

# Endpoint for rendering the html table with urls to different endpoints
@app.route('/')
def default_path():
    return render_template('index.html', URL=API_URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
