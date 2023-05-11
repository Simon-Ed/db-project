from flask import Flask, jsonify, request
from endpoints.courses import *
from endpoints.rooms import *
from endpoints.teachers import *

app = Flask(__name__)

# Endpoint for testing the 16 queries in the task.
@app.route('/query-test/<int:endpoint>', methods=['GET'])
def query_test_endpoint(endpoint):
    tasks = {
        1: get_courses_task1,
        2: get_courses_task2,
        3: get_courses_task3,
        4: get_courses_task4,
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


@app.route('/rooms', methods=['GET'])
def rooms_endpoint():
    rooms = get_courses_task1()

    return jsonify(rooms)


@app.route('/teachers', methods=['GET'])
def teachers_endpoint():
    teachers = get_courses_task1()

    return jsonify(teachers)
#
# # TODO: Move logic into own modules
# @app.route('/testGeneralPublic', methods=['GET'])
# def test_general_public_permissions_UPDATE():  #
#     with publicConnection.cursor() as cursor:
#         query = "UPDATE course SET name = 'Databaser 3', teacher_id = '1234567890'" \
#                 " WHERE course_id = 'IDATG2001' AND semester_id = '2' LIMIT 1"
#         cursor.execute(query)
#         publicConnection.commit()
#         data = cursor.fetchall()
#         response = jsonify(data)
#     return response
#
# @app.route('/testStudent1', methods=['GET'])
# def test_student_permissions_UPDATE():  #
#     with studentConnection.cursor() as cursor:
#         query = "UPDATE course SET name = 'Databaser 3', teacher_id = '1234567890'" \
#                 " WHERE course_id = 'IDATG2001' AND semester_id = '2' LIMIT 1"
#         cursor.execute(query)
#         publicConnection.commit()
#         data = cursor.fetchall()
#         response = jsonify(data)
#     return response
#
# @app.route('/testStudent2', methods=['GET'])
# def test_student_update_booking():
#     booking_id = request.args.get('booking_id')
#     start_time = request.args.get('start_time')
#     end_time = request.args.get('end_time')
#     type_update = request.args.get('type')
#     room_id = request.args.get('room_id')
#     booker = request.args.get('booker')
#
#     with studentConnection.cursor() as cursor:
#         query = "UPDATE room_booking \
#                     SET start_time = %s, end_time = %s, type = %s, room_id = %s, booker = %s \
#                     WHERE booking_id = %s"
#         values = (start_time, end_time, type_update, room_id, booker, booking_id)
#         cursor.execute(query, values)
#         studentConnection.commit()
#
#     return "Booking with ID {} was successfully updated".format(booking_id)
#
# @app.route('/testLecturer1', methods=['GET'])
# def test_lecturer_permissions_UPDATE_1():
#     with lecturerConnection.cursor() as cursor:
#         query = "UPDATE course SET name = CASE WHEN name = 'Databaser 1' THEN 'Databaser 3' WHEN name = 'Databaser 3' THEN 'Databaser 1' ELSE name " \
#                 "END WHERE course_id = 'IDATG2001' AND semester_id = 2 LIMIT 1;"
#         cursor.execute(query)
#         lecturerConnection.commit()
#         data = cursor.fetchall()
#         response = jsonify(data)
#     return response
#
# @app.route('/testLecturer2', methods=['GET'])
# def test_lecturer_permissions_UPDATE_2():
#     with lecturerConnection.cursor() as cursor:
#         query = "UPDATE teacher SET title = CASE WHEN title = 'Professor' THEN 'rosseforP' ELSE 'Professor' " \
#                 "END WHERE personal_id = '0123456789' LIMIT 1;"
#         cursor.execute(query)
#         lecturerConnection.commit()
#         data = cursor.fetchall()
#         response = jsonify(data)
#     return response
#
#
# @app.route('/testAdmin', methods=['GET'])
# def test_admin_permissions_UPDATE():
#     with adminConnection.cursor() as cursor:
#         query = "UPDATE teacher SET title = CASE WHEN title = 'Professor' THEN 'rosseforP' ELSE 'Professor' " \
#                 "END WHERE personal_id = '0123456789' LIMIT 1;"
#         cursor.execute(query)
#         adminConnection.commit()
#         data = cursor.fetchall()
#         response = jsonify(data)
#     return response
#

# add course to time schedule 
@app.route('/add-to-schedule')
def add_course_to_time_schedule():
    user = request.args.get('user', default='', type=int)
    course = request.args.get('course', default='', type=int)
    with rootConnection.cursor() as cursor:
        query = "INSERT INTO user_schedule( user_schedule.user_id, user_schedule.course_id) VALUES(%s, %s);"
        cursor.execute(query, (user,course,))
        rootConnection.commit()
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response

# view personal time schedule 
@app.route('/view-schedule')
def view_time_schedule():
    user = request.args.get('user', default='', type=int)
    with rootConnection.cursor() as cursor:
        query = "SELECT * FROM user_time_schedule WHERE user_time_schedule.user_id=%s;" 
        cursor.execute(query, (user,))
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
