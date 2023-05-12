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

# 8. Show a list of all rooms available for a given date and time range.
def get_rooms_task8(start_datetime, end_datetime):
    query = "SELECT room.*, building.building_name, building.location FROM room LEFT JOIN building ON room.building_id = building.id WHERE room.id NOT IN ( SELECT room.id FROM room LEFT JOIN room_booking ON room.id = room_booking.id WHERE room_booking.start_time <= %s AND room_booking.end_time >= %s)"

    cursor = rootConnection.cursor()
    cursor.execute(query, (start_datetime, end_datetime))
    courses = cursor.fetchall()

    field_names = [desc[0] for desc in cursor.description]
    mapped_res = [dict(zip(field_names, course)) for course in courses]

    return jsonify(mapped_res)


# 9. Show a list of all reservations made by a specific user, along with the room number and building name for each
# reservation.
def get_rooms_task9(name, surname):
    query = "SELECT CONCAT(university_member.name, ' ', university_member.surname) AS name, room.*, room.room_number, building.building_name FROM room_booking INNER JOIN room ON room_booking.room_id = room.id INNER JOIN building ON room.building_id = building.id INNER JOIN university_member ON booker = university_member.id WHERE university_member.name IN (%s) AND university_member.surname IN (%s)"

    cursor = rootConnection.cursor()
    cursor.execute(query, (name, surname))
    courses = cursor.fetchall()

    field_names = [desc[0] for desc in cursor.description]
    mapped_res = [dict(zip(field_names, course)) for course in courses]

    return jsonify(mapped_res)


# 10. Show a list of all rooms and the reservations made for each room, including the name of the person who made
# each reservation
def get_rooms_task10():
    query = "SELECT room.*, room_booking.*, CONCAT(university_member.name, ' ', university_member.surname) AS name FROM room LEFT JOIN room_booking ON room.id = room_booking.room_id LEFT JOIN university_member ON booker = university_member.id"
    
    return jsonify(queryExec(query))


# 11. Show a list of all rooms, along with the number and type of reservations made for each room.
def get_rooms_task11():
    query = "SELECT room.*, room_booking.type, COUNT(*) AS num_of_booking_type FROM room LEFT JOIN room_booking ON room.id = room_booking.room_id GROUP BY room.id, room_booking.type"
    
    return jsonify(queryExec(query))

