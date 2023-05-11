from api.db.db_conn import rootConnection

def get_rooms():
    cursor = rootConnection.cursor()
    cursor.execute('SELECT * FROM room')
    rooms = cursor.fetchall()

    return rooms