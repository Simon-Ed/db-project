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


# 12. Show a list of all teachers and the courses, they teach, including the room number and building
# name where each course is held.
def get_teachers_task12():
    query = "SELECT CONCAT(university_member.name,' ' , university_member.surname) AS name, MAX(course_semester.name), COUNT(course.id) AS num_courses, course_semester.semester FROM course INNER JOIN university_member ON course.teacher_id = university_member.id INNER JOIN course_semester ON course.id = course_semester.course_id GROUP BY university_member.id, course_semester.semester ORDER BY num_courses DESC, course_semester.semester;"
    return jsonify(queryExec(query))


# 13. Show a list of all teachers and the courses, they teach, including the room number and building
# name where each course is held.
def get_teachers_task13():
    query = "SELECT university_member.name AS firstName, university_member.surname, course.name AS course, room.room_number, building.building_name FROM course INNER JOIN teacher ON course.teacher_id = teacher.university_member INNER JOIN room ON room.id = teacher.office INNER JOIN building ON room.building_id = building.id INNER JOIN university_member ON teacher.university_member = university_member.id; "
    
    return jsonify(queryExec(query))


# 14. Show a list of all teachers and the total number of hours they teach each week.
def get_teachers_task14():
    query = "SELECT university_member.name, WEEK(room_booking.start_time) AS week, SUM(TIMESTAMPDIFF(hour, room_booking.start_time, room_booking.end_time)) AS totalweeklyhours FROM course INNER JOIN university_member ON course.teacher_id = university_member.id INNER JOIN lecture ON course.id = lecture.course_id INNER JOIN room_booking ON lecture.booking_id = room_booking.id GROUP BY university_member.id, WEEK(room_booking.start_time);"
    
    return jsonify(queryExec(query))


# 16. Show a list of all teachers and the average number of students in the courses they teach,
# sorted by the average number of students
def get_teachers_task16():
    query = "SELECT university_member.name AS firstName, university_member.surname, MIN(course_semester.name) AS course_name, COUNT(course.id) AS num_courses, course_semester.semester FROM course INNER JOIN university_member ON course.teacher_id = university_member.id INNER JOIN course_semester ON course.id = course_semester.course_id GROUP BY university_member.id, course_semester.semester ORDER BY num_courses DESC;"
    
    return jsonify(queryExec(query))