from flask import Flask, jsonify
from endpoints.courses import *
from endpoints.rooms import *
#from endpoints.teachers import get_teachers_nrOfcourses_eachSem_sotredBynr

app = Flask(__name__)

# Endpoint for testing the 16 queries in the task.
@app.route('/query-test/<int:endpoint>', methods=['GET'])
def query_test_endpoint(endpoint):
    tasks = {
        1: get_courses_task1,
        2: get_courses_task2,  # Replace None with the appropriate function for endpoint 2
        3: get_courses_task3,
        4: get_courses_task4,
        5: get_courses_task5,
        6: get_courses_task6,
        7: get_courses_task7,
        8: get_rooms_task8,
        9: get_rooms_task9,
        10: get_rooms_task10,
        11: get_rooms_task11
    }
    return tasks.get(endpoint, lambda: None)()


@app.route('/rooms', methods=['GET'])
def rooms_endpoint():
    rooms = get_courses_task1()

    return jsonify(rooms)


@app.route('/teachers', methods=['GET'])
def teachers_endpoint():
    teachers = get_courses_task1()

    return jsonify(teachers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
