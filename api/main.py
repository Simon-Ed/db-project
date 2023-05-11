from flask import Flask, jsonify
from endpoints.courses import get_courses_task1, get_courses_task2, get_courses_task3, get_courses_task4, get_courses_task5
#from endpoints.rooms import get_rooms_available_givendate_timerange
#from endpoints.teachers import get_teachers_nrOfcourses_eachSem_sotredBynr

app = Flask(__name__)

# Endpoint for testing the 16 queries in the task.
@app.route('/query-test/<int:endpoint>', methods=['GET'])
def query_test_endpoint(endpoint):
    tasks = {
        1: get_courses_task1,
        2: lambda: None,  # Replace None with the appropriate function for endpoint 2
        3: get_courses_task3,
        4: get_courses_task4,
        5: get_courses_task5
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
