import http
from flask import Flask, jsonify, request
import pymysql.cursors

# Database configuration
adminConfig = {
    'host': 'localhost',
    'user': 'admin',
    'password': '',
    'db': 'project_db',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

publicConfig = {
    'host': 'localhost',
    'user': 'general_public',
    'password': '',
    'db': 'project_db',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

studentConfig = {
    'host': 'localhost',
    'user': 'Student',
    'password': '',
    'db': 'project_db',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

lecturerConfig = {
    'host': 'localhost',
    'user': 'lecturer',
    'password': '',
    'db': 'project_db',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}


adminConnection = pymysql.connect(**adminConfig)
publicConnection = pymysql.connect(**publicConfig)
studentConnection = pymysql.connect(**studentConfig)
lecturerConnection = pymysql.connect(**lecturerConfig)



# Method contain API endpoints
def init_app(app: Flask):
    @app.route('/courses', methods=['GET'])
    def get_courses():
        return jsonify({'message': 'courses endpoint'}), http.HTTPStatus.OK

    @app.route('/rooms', methods=['GET'])
    def get_rooms():
        return jsonify({'message': 'rooms endpoint'}), http.HTTPStatus.OK

    @app.route('/teachers', methods=['GET'])
    def get_teachers():
        return jsonify({'message': 'teachers endpoint'}), http.HTTPStatus.OK

    @app.route('/testGeneralPublic', methods=['GET'])
    def test_general_public_permissions_UPDATE():  #
        with publicConnection.cursor() as cursor:
            query = "UPDATE course SET name = 'Databaser 3', teacher_id = '1234567890'" \
                    " WHERE course_id = 'IDATG2001' AND semester_id = '2' LIMIT 1"
            cursor.execute(query)
            publicConnection.commit()
            data = cursor.fetchall()
            response = jsonify(data)
        return response

    @app.route('/testStudent1', methods=['GET'])
    def test_student_permissions_UPDATE():  #
        with studentConnection.cursor() as cursor:
            query = "UPDATE course SET name = 'Databaser 3', teacher_id = '1234567890'" \
                    " WHERE course_id = 'IDATG2001' AND semester_id = '2' LIMIT 1"
            cursor.execute(query)
            publicConnection.commit()
            data = cursor.fetchall()
            response = jsonify(data)
        return response

    @app.route('/testStudent2', methods=['GET'])
    def test_student_update_booking():
        booking_id = request.args.get('booking_id')
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')
        type_update = request.args.get('type')
        room_id = request.args.get('room_id')
        booker = request.args.get('booker')

        with studentConnection.cursor() as cursor:
            query = "UPDATE room_booking \
                     SET start_time = %s, end_time = %s, type = %s, room_id = %s, booker = %s \
                     WHERE booking_id = %s"
            values = (start_time, end_time, type_update, room_id, booker, booking_id)
            cursor.execute(query, values)
            studentConnection.commit()

        return "Booking with ID {} was successfully updated".format(booking_id)

    @app.route('/testLecturer1', methods=['GET'])
    def test_lecturer_permissions_UPDATE_1():
        with lecturerConnection.cursor() as cursor:
            query = "UPDATE course SET name = CASE WHEN name = 'Databaser 1' THEN 'Databaser 3' WHEN name = 'Databaser 3' THEN 'Databaser 1' ELSE name " \
                    "END WHERE course_id = 'IDATG2001' AND semester_id = 2 LIMIT 1;"
            cursor.execute(query)
            lecturerConnection.commit()
            data = cursor.fetchall()
            response = jsonify(data)
        return response

    @app.route('/testLecturer2', methods=['GET'])
    def test_lecturer_permissions_UPDATE_2():
        with lecturerConnection.cursor() as cursor:
            query = "UPDATE teacher SET title = CASE WHEN title = 'Professor' THEN 'rosseforP' ELSE 'Professor' " \
                    "END WHERE personal_id = '0123456789' LIMIT 1;"
            cursor.execute(query)
            lecturerConnection.commit()
            data = cursor.fetchall()
            response = jsonify(data)
        return response


    @app.route('/testAdmin', methods=['GET'])
    def test_admin_permissions_UPDATE():
        with adminConnection.cursor() as cursor:
            query = "UPDATE teacher SET title = CASE WHEN title = 'Professor' THEN 'rosseforP' ELSE 'Professor' " \
                    "END WHERE personal_id = '0123456789' LIMIT 1;"
            cursor.execute(query)
            adminConnection.commit()
            data = cursor.fetchall()
            response = jsonify(data)
        return response





