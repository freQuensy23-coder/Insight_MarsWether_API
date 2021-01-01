import pymysql
from contextlib import closing

# connection =
with closing(pymysql.connect(host = "mametejs.beget.tech", user = "mametejs_test", password = "Alex-12345", db = "mametejs_test")) as connection:
    q = """INSERT INTO data(sol, data) VALUES (%s, %s)"""
    test_data = 12314, "123"
    cursor = connection.cursor()
    cursor.execute(q, test_data)
    
    # if cursor.lastrowid:
    #     print('last insert id', cursor.lastrowid)
    # else:
    #     print('last insert id not found')

    connection.commit()
