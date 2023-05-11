from flask import Flask, jsonify
from endpoints.courses import get_courses_task1, get_courses_task2, get_courses_task3, get_courses_task4
#from endpoints.rooms import get_rooms_available_givendate_timerange
#from endpoints.teachers import get_teachers_nrOfcourses_eachSem_sotredBynr

app = Flask(__name__)


@app.route('/courses/1', methods=['GET'])
def courses_endpoint1():
    return get_courses_task1()


@app.route('/courses/2', methods=['GET'])
def courses_endpoint2():
    return ()


@app.route('/courses/3', methods=['GET'])
def courses_endpoint3():
    return get_courses_task3()

@app.route('/courses/4', methods=['GET'])
def courses_endpoint4():
    return get_courses_task4()


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
