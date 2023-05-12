from datetime import datetime
from db.db_conn import rootConnection


def sortRes(cursor, res):
    field_names = [desc[0] for desc in cursor.description]
    return [dict(zip(field_names, course)) for course in res]


def queryExec(query):
    cursor = rootConnection.cursor()
    cursor.execute(query)
    courses = cursor.fetchall()

    # Map column names to custom field names
    field_names = [desc[0] for desc in cursor.description]
    mapped_res = [dict(zip(field_names, course)) for course in courses]
    
    return mapped_res