from flask import Flask, jsonify, request

from api.db.db_conn import publicConnection, studentConnection, lecturerConnection, adminConnection
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


@app.route('/testGeneralPublic', methods=['GET'])
def test_general_public_permissions_UPDATE():  #
    with publicConnection.cursor() as cursor:
        query = """
        UPDATE course SET name = 
        CASE 
        WHEN name = 'Database Systems' THEN 'Database Systems 2'
        WHEN name = 'Database Systems 2' THEN 'Database Systems'
        END
        WHERE code = 'IT2201' AND id = '1' LIMIT 1
        """
        cursor.execute(query)
        publicConnection.commit()
        data = cursor.fetchall()
        response = jsonify(data)
    return response


@app.route('/testStudent1', methods=['GET'])
def test_student_permissions_UPDATE():  #
    with studentConnection.cursor() as cursor:
        query = """
            UPDATE course SET name = 
                CASE 
                    WHEN name = 'Database Systems' THEN 'Database Systems 2'
                    WHEN name = 'Database Systems 2' THEN 'Database Systems'
                END
            WHERE code = 'IT2201' AND id = '1' LIMIT 1
        """
        cursor.execute(query)
        studentConnection.commit()
        data = cursor.fetchall()
        response = jsonify(data)
    return response


@app.route('/testStudent2', methods=['GET'])
def test_student_insert_booking():
    with studentConnection.cursor() as cursor:
        query = "INSERT INTO room_booking (id, start_time, end_time, type, room_id, booker) \
                 VALUES (54, '2024-05-14 15:30:00', '2024-05-14 17:00:00','Meeting', 16, 4)"
        cursor.execute(query)
        studentConnection.commit()
        data = cursor.fetchall()
        response = jsonify(data)
    return response



@app.route('/testLecturer1', methods=['GET'])
def test_lecturer_permissions_UPDATE_1():
    with lecturerConnection.cursor() as cursor:
        query = """
        UPDATE course SET name = 
        CASE 
        WHEN name = 'Database Systems' THEN 'Database Systems 2'
        WHEN name = 'Database Systems 2' THEN 'Database Systems'
        END
        WHERE code = 'IT2201' AND id = '1' LIMIT 1
        """
        cursor.execute(query)
        lecturerConnection.commit()
        data = cursor.fetchall()
        response = jsonify(data)
    return response


@app.route('/testLecturer2', methods=['GET'])
def test_lecturer_permissions_UPDATE_2():
    with lecturerConnection.cursor() as cursor:
        query = "UPDATE teacher SET title = CASE WHEN title = 'Prof.' THEN '.forP' ELSE 'Prof.' " \
                "END WHERE university_member = '12' LIMIT 1;"
        cursor.execute(query)
        lecturerConnection.commit()
        data = cursor.fetchall()
        response = jsonify(data)
    return response


@app.route('/testAdmin', methods=['GET'])
def test_admin_permissions_UPDATE():
    with adminConnection.cursor() as cursor:
        query = "UPDATE teacher SET title = CASE WHEN title = 'Prof.' THEN '.forP' ELSE 'Prof.' " \
                "END WHERE university_member = '12' LIMIT 1;"
        cursor.execute(query)
        adminConnection.commit()
        data = cursor.fetchall()
        response = jsonify(data)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
