from api.db.db_conn import rootConnection


def get_teachers():
    cursor = rootConnection.cursor()
    cursor.execute('SELECT * FROM teacher')
    teachers = cursor.fetchall()

    return teachers
