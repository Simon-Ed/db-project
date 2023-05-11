from flask import jsonify

from api.db.db_conn import rootConnection


def get_courses_roomnr_buildingname_noteacher():
    with rootConnection.cursor() as cursor:
        query = "SELECT course.name, Room.room_number, Room.building_name " \
                "FROM course" \
                "LEFT JOIN teacher ON course.teacher_id = teacher.personal_id" \
                "LEFT JOIN lecture ON course.course_id = lecture.course_id" \
                "LEFT JOIN Room_booking ON lecture.booking_id = Room_booking.booking_id" \
                "LEFT JOIN Room ON Room_booking.room_id = Room.room_id" \
                "WHERE teacher_id = NULL;"
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response


def get_course_in_given_sem_specific_teacher():
    with rootConnection.cursor() as cursor:
        query = "SELECT course.name, university_member.name, semester.name, semester.start_time " \
                "FROM teacher " \
                "LEFT JOIN university_member ON teacher.university_member = university_member.id" \
                "LEFT JOIN course ON teacher.personal_id = course.teacher_id " \
                "LEFT JOIN semester ON course.semester_id = semester.semester_id " \
                "WHERE university_member.name = 'Emily' AND semester.name = 'SPRING2023' AND semester.start_time = '2023-01-01 00:00:00'"
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response


# 3. Show a list of all courses taught in a specific room on a given date and a specific time range.
def get_course_in_given_room_given_date_specific_time_range():
    with rootConnection.cursor() as cursor:
        query = "SELECT lecture.activity, room.room_number, room_booking.start_time, room_booking.end_time " \
                "FROM lecture " \
                "LEFT JOIN room_booking ON lecture.booking_id = room_booking.booking_id " \
                "LEFT JOIN room ON room_booking.room_id = room.room_id " \
                "WHERE room_booking.start_time " \
                "BETWEEN '2023-06-08 09:00:00' AND ('2023-06-08 13:15:00') " \
                "ORDER BY room_booking.start_time ASC, room_booking.end_time ASC"
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response


# 4. Show a list of all courses taught in a specific room on a given date and at a specific time.
def get_course_in_given_room_given_date_specific_time():
    with rootConnection.cursor() as cursor:
        query = "SELECT lecture.activity, room.room_number, room_booking.start_time, room_booking.end_time " \
                "FROM lecture " \
                "LEFT JOIN room_booking ON lecture.booking_id = room_booking.booking_id " \
                "LEFT JOIN room ON room_booking.room_id = room.room_id " \
                "WHERE room_booking.start_time = 'start_time' AND room_booking.end_time = 'end_time'"
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response


# 5. Show a list of all courses, along with the name and email of the teacher teaching each course.
def get_course_teachername_teacheremail():
    with rootConnection.cursor() as cursor:
        query = "SELECT university_member.name, university_member.surname, university_member.email, course.* " \
                "FROM course " \
                "LEFT JOIN (teacher JOIN university_member ON university_member.id = teacher.universtiy_member)" \
                "ON teacher.personal_id = course.teacher.id"
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response


# 6. Show a list of all courses taught by a specific teacher, along with the institute and faculty where each course
# belongs.
def get_course_specific_teacher_institue_faculty():
    with rootConnection.cursor() as cursor:
        query = "SELECT course.*, institue.* " \
                "FROM teacher " \
                "LEFT JOIN institute ON institute.institute = teacher.institute " \
                "LEFT JOIN course ON course.teacher_id = teacher.personal_id " \
                "WHERE teacher.personal_id = 8901234567"
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response


# 7.Show a list of all courses taught by a specific lecturer, along with the room number and building name where each
# course is held.
def get_course_specific_teacher_roomnr_buildingname():
    with rootConnection.cursor() as cursor:
        query = "SELECT course.*, room.room_number, room.building_name " \
                "FROM teacher " \
                "LEFT JOIN course ON course.teacher_id = teacher.personal_id " \
                "LEFT JOIN lecture ON lecture.course_id = course.course_id " \
                "LEFT JOIN room_booking ON lecture.booking_id =room_booking.booking.id " \
                "LEFT JOIN room ON room_booking.room.id = room.room_id " \
                "WHERE teacher.personal_id = 8901234567"
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response

# 15. Show a list of all courses that are taught on Mondays, along with the name and email of the
# teachers teaching each course.
def get_courses_on_Mondays_and_teachers_name_email():
    with rootConnection.cursor() as cursor:
        query = "SELECT course.name, room_booking.start_time, university_member.name, university_member.email " \
                "FROM course " \
                "LEFT JOIN lecture ON course.courses_id = lecture.course_id " \
                "LEFT JOIN teacher ON course.teacher_id = teacher.personal_id " \
                "LEFT JOIN room_booking ON lecture.booking_id = room_booking.booking_id " \
                "LEFT JOIN univserity_member ON university_member.id = teacher.university_member " \
                "WHERE WEEKDAY(room_booking.start-time) = 0"
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response
