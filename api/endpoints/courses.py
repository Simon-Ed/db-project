from flask import jsonify

from db.db_conn import rootConnection

def queryExec(query):
    cursor = rootConnection.cursor()
    cursor.execute(query)
    courses = cursor.fetchall()

    # Map column names to custom field names
    field_names = [desc[0] for desc in cursor.description]
    mapped_res = [dict(zip(field_names, course)) for course in courses]
    
    return mapped_res

# Show a list of all courses that have not been assigned a lecturer, along with the room number
# and building name where each course is held.
def get_courses_task1():
    query = "SELECT course.name AS course_name, room.room_number, building.building_name FROM course LEFT JOIN teacher ON course.teacher_id = teacher.university_member LEFT JOIN lecture ON course.id = lecture.course_id LEFT JOIN room_booking ON lecture.booking_id = room_booking.id LEFT JOIN room ON room_booking.room_id = room.id LEFT JOIN building ON room.building_id = building.id WHERE course.teacher_id IS NULL;"
    
    return jsonify(queryExec(query))


#2. Show a list of all courses taught by a specific teacher in a given semester.
def get_courses_task2():
    cursor = rootConnection.cursor()
    query = ''
    cursor.execute(query)
    courses = cursor.fetchall()
    response = jsonify(courses)
    return response


# 3. Show a list of all courses taught in a specific room on a given date and a specific time range.
def get_courses_task3():
    query = "SELECT lecture.activity, room.room_number, room_booking.start_time, room_booking.end_time FROM lecture LEFT JOIN room_booking ON lecture.booking_id = room_booking.id LEFT JOIN room ON room_booking.room_id = room.id WHERE room_booking.start_time BETWEEN '2023-05-08 09:00:00' AND '2023-06-08 13:15:00' AND room.room_number='R101' ORDER BY room_booking.start_time ASC, room_booking.end_time ASC"
    
    return jsonify(queryExec(query))


# 4. Show a list of all courses taught in a specific room on a given date and at a specific time.
def get_courses_task4():
    query = "SELECT lecture.activity, room.room_number, room_booking.start_time, room_booking.end_time FROM lecture LEFT JOIN room_booking ON lecture.booking_id = room_booking.id LEFT JOIN room ON room_booking.room_id = room.id WHERE room_booking.start_time = '2023-05-12 09:00:00' AND room.room_number='R101'"
    
    return jsonify(queryExec(query))


# 5. Show a list of all courses, along with the name and email of the teacher teaching each course.
def get_courses_task5():
    query = "SELECT university_member.name, university_member.surname, contact_info.email, course.* FROM course LEFT JOIN teacher ON course.teacher_id = teacher.university_member INNER JOIN university_member ON university_member.id = teacher.university_member LEFT JOIN contact_info ON university_member.id = contact_info.university_member ORDER BY course.code ASC;"
     
    return jsonify(queryExec(query))


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
