from datetime import datetime


def validateDatetime(dt):
    try:
        datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False