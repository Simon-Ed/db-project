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
    query = "SELECT course.code, course.name, CONCAT(university_member.name, ' ', university_member.surname) AS name, course_semester.semester, course_semester.start_date, course_semester.end_date FROM teacher LEFT JOIN university_member ON teacher.university_member = university_member.id LEFT JOIN course ON teacher.university_member = course.teacher_id LEFT JOIN course_semester ON course.id = course_semester.course_id WHERE university_member.name = 'Emily' AND course_semester.semester COLLATE utf8mb4_unicode_ci = 'Vår 2023';"

    return jsonify(queryExec(query))


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
def get_courses_task6():
    query = "SELECT course.code, course.name, CONCAT(university_member.name, ' ', university_member.surname) AS name, institute.institute, institute.faculty FROM teacher LEFT JOIN institute ON institute.institute = teacher.institute LEFT JOIN course ON course.teacher_id = teacher.university_member LEFT JOIN university_member ON university_member.id = teacher.university_member WHERE university_member.name = 'Robert' AND university_member.surname='Johnson'"

    return jsonify(queryExec(query))


# 7.Show a list of all courses taught by a specific lecturer, along with the room number and building name where each
# course is held.
def get_courses_task7():
    query = "SELECT course.code, course.name, CONCAT(university_member.name, ' ', university_member.surname) AS name, room.room_number, building.building_name FROM teacher LEFT JOIN university_member ON university_member.id = teacher.university_member LEFT JOIN course ON course.teacher_id = teacher.university_member LEFT JOIN lecture ON lecture.course_id = course.id LEFT JOIN room_booking ON lecture.booking_id =room_booking.id LEFT JOIN room ON room_booking.room_id = room.id LEFT JOIN building ON room.building_id = building.id WHERE university_member.name = 'Robert' AND university_member.surname='Johnson'"

    return jsonify(queryExec(query))


# 12. Show a list of all teachers and the courses, they teach, including the room number and building
# name where each course is held.
def get_courses_task12():
    query = "SELECT university_member.name AS firstName, university_member.surname, course_semester.name, COUNT(course.id) AS num_courses, course_semester.semester FROM course INNER JOIN university_member ON course.teacher_id = university_member.id INNER JOIN course_semester ON course.id = course_semester.course_id GROUP BY university_member.id, course_semester.semester ORDER BY `num_courses` DESC;"
    return jsonify(queryExec(query))


# 13. Show a list of all teachers and the courses, they teach, including the room number and building
# name where each course is held.
def get_courses_task13():
    query = "SELECT university_member.name AS firstName, university_member.surname, course.name AS course, room.room_number, building.building_name FROM course INNER JOIN teacher ON course.teacher_id = teacher.university_member INNER JOIN room ON room.id = teacher.office INNER JOIN building ON room.building_id = building.id INNER JOIN university_member ON teacher.university_member = university_member.id; "
    
    return jsonify(queryExec(query))


# 14. Show a list of all teachers and the total number of hours they teach each week.
def get_courses_task14():
    query = "SELECT university_member.name, WEEK(room_booking.start_time) AS week, SUM(TIMESTAMPDIFF(hour, room_booking.start_time, room_booking.end_time)) AS totalweeklyhours FROM course INNER JOIN university_member ON course.teacher_id = university_member.id INNER JOIN lecture ON course.id = lecture.course_id INNER JOIN room_booking ON lecture.booking_id = room_booking.id GROUP BY university_member.id, WEEK(room_booking.start_time);"
    
    return jsonify(queryExec(query))


# 15. Show a list of all courses, along with the name and email of the teacher teaching each course.
def get_courses_task15():
    query = "SELECT lecture.activity, course.name, room_booking.start_time, university_member.name, contact_info.email FROM course INNER JOIN lecture ON course.id = lecture.course_id INNER JOIN teacher ON course.teacher_id = teacher.university_member INNER JOIN room_booking ON lecture.booking_id = room_booking.id INNER JOIN university_member ON university_member.id = teacher.university_member INNER JOIN contact_info ON contact_info.university_member = university_member.id WHERE WEEKDAY(room_booking.start_time) = 0;"
    
    return jsonify(queryExec(query))


# 16. Show a list of all teachers and the average number of students in the courses they teach,
# sorted by the average number of students
def get_courses_task16():
    query = "SELECT university_member.name, AVG(course.number_of_students) AS average_number_of_students FROM course INNER JOIN university_member ON university_member.id = course.teacher_id GROUP BY university_member.name ORDER BY average_number_of_students ASC;"
    
    return jsonify(queryExec(query))

