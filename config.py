import pymysql

def get_conection():
    conection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='fakestore',
        cursorclass=pymysql.cursors.DictCursor
    )

    return conection