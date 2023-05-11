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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
