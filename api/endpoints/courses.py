from api.db.db_conn import rootConnection


def get_courses():
    cursor = rootConnection.cursor()
    cursor.execute('SELECT * FROM course')
    courses = cursor.fetchall()

    return courses
