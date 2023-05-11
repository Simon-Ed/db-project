from flask import jsonify

from api.db.db_conn import rootConnection


# 8. Show a list of all rooms available for a given date and time range.
def get_rooms_available_givendate_timerange():
    with rootConnection.cursor() as cursor:
        query = "SELECT room.* " \
                "FROM room" \
                "WHERE room.room_id NOT IN (" \
                "SELECT room.room_id " \
                "FROM room " \
                "LEFT JOIN room_booking ON room.room_id = room_booking.id" \
                "WHERE room_booking.start_time <= '2023-06-08 09:00:00' AND room_booking.end_time >= '2023-06-08 11:00:00')"
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response


# 9. Show a list of all reservations made by a specific user, along with the room number and building name for each
# reservation.
def get_reservations_specificuser_roomnr_buildingname():
    with rootConnection.cursor() as cursor:
        query = "SELECT room.booking.*, room.room_number, room.building_name " \
                "FROM room_booking " \
                "INNER JOIN room ON room_booking.room.id = room.room.id " \
                "INNER JOIN university_member ON booker = university_member.id " \
                "WHERE university_member.name IN ('John') AND university_member.surname IN ('Doe')"
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response


# 10. Show a list of all rooms and the reservations made for each room, including the name of the person who made
# each reservation
def get_room_and_reservations_booker():
    with rootConnection.cursor() as cursor:
        query = "SELECT room.*, room_booking.*, university_member.name, university_member.surname " \
                "FROM room " \
                "LEFT JOIN room_booking ON room.room.id = room_booking.room.id " \
                "LEFT JOIN university_member ON booker = university_member.id "
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response


# 11. Show a list of all rooms, along with the number and type of reservations made for each room.
def get_rooms_nrOfreservation_reservationType():
    with rootConnection.cursor() as cursor:
        query = "SELECT room.*, room_booking.type, COUNT() " \
                "FROM room " \
                "LEFT JOIN room_booking ON room.room.id = room_booking.room.id " \
                "GROUP BY room.room_id, room_booking.type"
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response


# 12. Show a list of all teachers and the number of courses they are teaching in each semester, sorted by the number
# of courses.
def get_rooms_nrOfreservation_reservationType():
    with rootConnection.cursor() as cursor:
        query = "SELECT room.*, room_booking.type, COUNT() " \
                "FROM room " \
                "LEFT JOIN room_booking ON room.room.id = room_booking.room.id " \
                "GROUP BY room.room_id, room_booking.type"
        cursor.execute(query)
        courses = cursor.fetchall()
        response = jsonify(courses)
    return response
