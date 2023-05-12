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
# show courses 
@app.route('/view-courses')
def view_courses():
    with publicConnection.cursor() as cursor:
        query = "SELECT * FROM course;" 
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response

# bookable rooms 
@app.route('/bookable-rooms')
def view_bookable_rooms():
    with publicConnection.cursor() as cursor:
        query = "SELECT * FROM bookable_rooms;" 
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response


# view staff(teacher) without contact info
@app.route('/staff')
def view_teachers():
    with publicConnection.cursor() as cursor:
        query = "SELECT university_member.id, teacher.title, university_member.name, university_member.surname, teacher.institute FROM teacher LEFT JOIN university_member ON teacher.university_member = university_member.id;" 
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response


# student user

# booking a room
@app.route('/book-room')
def book_room():
    user = request.args.get('user', default='', type=int) 
    start_time = request.args.get('start_time', default='', type=str) 
    end_time = request.args.get('end_time', default='', type=str) 
    roomType = request.args.get('room_type', default='', type=str) 
    roomId = request.args.get('room_id', default='', type=int) 

    with studentConnection.cursor() as cursor:
        query = "SELECT `university_member`.`id` FROM university_member WHERE university_member.id=%s;"
        cursor.execute(query , (user, ))
        valid = cursor.fetchone()
        if valid is None:
            return jsonify("user does not have permission to do this")

    with studentConnection.cursor() as cursor:
        query = "INSERT INTO room_booking( id ,start_time, end_time, room_id, booker, TYPE) VALUES(NULL , %s,  %s,%s,%s, %s);" 
        cursor.execute(query, (start_time, end_time, roomId,user,roomType))
        studentConnection.commit()
        response = jsonify("successfully added room booking")
    return response

# retrieves contact info of teachers
@app.route('/contact-staff')
def view_contact_info():
    user = request.args.get('user', default='', type=int) 

    with studentConnection.cursor() as cursor:
        query = "SELECT `university_member`.`id` FROM university_member WHERE university_member.id=%s;"
        cursor.execute(query , (user, ))
        valid = cursor.fetchone()
        if valid is None:
            return jsonify("user does not have permission to do this")

    with studentConnection.cursor() as cursor:
        query = "SELECT * FROM `staff_contact`;" 
        cursor.execute(query)
        staff_contact = cursor.fetchall()
        response = jsonify(staff_contact)
    return response

# lecturer

# change course name
@app.route('/change-course-name')
def changer_course_name():
    user = request.args.get('user', default='', type=int) 
    course_id = request.args.get('course_id', default='', type=int) 
    new_course_name = request.args.get('new_course_name', default='', type=str) 

    with lecturerConnect.cursor() as cursor:
        query = "SELECT teacher.university_member FROM teacher WHERE teacher.university_member=%s;"
        cursor.execute(query , (user, ))
        valid = cursor.fetchone()
        if valid is None:
            return jsonify("user does not have permission to do this")

    with lecturerConnect.cursor() as cursor:
        query = "UPDATE course SET course.name=%s WHERE course.id=%s;" 
        cursor.execute(query, (new_course_name, course_id,))
        rootConnection.commit()
        response = jsonify("successfully changed name of course")
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)