from flask import jsonify

from api.db.db_conn import rootConnection


def get_courses_roomnr_buildingname_noTeacher():
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
