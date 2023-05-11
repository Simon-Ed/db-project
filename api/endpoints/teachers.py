from flask import jsonify

from db.db_conn import rootConnection


# 12. Show a list of all teachers and the number of courses they are teaching in each semester, sorted by the number
# of courses.
def get_teachers_nrOfcourses_eachSem_sotredBynr():
    with rootConnection.cursor() as cursor:
        query = "SELECT teacher.*, semester.name , COUNT(DISTINCT course.course_id) AS num_courses " \
                "FROM teacher " \
                "LEFT JOIN course ON course.teacher_id = teacher.persona_.id " \
                "LEFT JOIN semester ON course.semester_id = semester.semester_id " \
                "GROUP BY teacher.personal_id, semester.semester_id " \
                "ORDER BY num_courses DESC ON semester.semester_id "
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response


# 13. Show a list of all teachers and the courses they teach, including the room number and building
# name where each course is held.
def get_teachers_courses_they_teach_roomnr_buildingname():
    with rootConnection.cursor() as cursor:
        query = "SELECT university_member.name, course.name , room.room_number, room.building_name " \
                "FROM course " \
                "LEFT JOIN teacher ON course.teacher_id = teacher.personal.id " \
                "LEFT JOIN room ON room.room_id = teacher.office " \
                "LEFT JOIN room_booking ON room_booking.room_id = room.room_id " \
                "LEFT JOIN univserity_member ON teacher.university_member = university_member.id"
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response


# 14. Show a list of all teachers and the total number of hours they teach each week.
def get_teachers_and_total_workhours():
    with rootConnection.cursor() as cursor:
        query = "SELECT university_member.name, WEEK(room_booking.start_time) AS week, SUM(TIMESTAMPDIFF(hour, room_booking.start_time, room_booking.end_time)) AS total weeklyhours " \
                "FROM teacher " \
                "LEFT JOIN course ON teacher.personal_id = course.teacher_id " \
                "LEFT JOIN lecture ON course.course_id = lecture.course_id " \
                "LEFT JOIN room_booking ON lecture.booking_id = room_booking.booking_id " \
                "LEFT JOIN univserity_member ON teacher.university_member = university_member.id " \
                "GROUP BY teacher.personal_id, WEEK(room_booking.start-time)"
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response

# 16. Show a list of all teachers and the average number of students in the courses they teach,
# sorted by the average number of students.
def get_teacher_avg_number_of_students_sorted_by_avgnr():
    with rootConnection.cursor() as cursor:
        query = "SELECT university_member.name, AVG(course.number_of_students) AS average_number_of_students " \
                "FROM course " \
                "LEFT JOIN teacher ON course.teacher_id = teacher.personal_id " \
                "LEFT JOIN university_member ON university_member.id = teacher.university_member " \
                "GROUP BY room_booking ON lecture.booking_id = room_booking.booking_id " \
                "LEFT JOIN university_member.name " \
                "ORDER BY average_number_of_students ASC"
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response
