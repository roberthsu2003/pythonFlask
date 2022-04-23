import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print('連結資料庫發生錯誤')
        print(e)
        return conn

    create_table(conn)
    return conn


def create_table(conn):
    sql = '''
    CREATE TABLE IF NOT EXISTS lot(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        num1 INTEGER NOT NULL,
        num2 INTEGER NOT NULL,
        num3 INTEGER NOT NULL,
        num4 INTEGER NOT NULL,
        num5 INTEGER NOT NULL,
        num6 INTEGER NOT NULL,
        spec INTEGER NOT NULL,
        datetime TEXT
    );
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print('建立資料表出錯')
        print(e)
        return None

    print('資料表建立')


def insertData(conn, data_list):
    insertSQL = '''INSERT INTO lot (name,num1,num2,num3,num4,num5,num6,spec,datetime) 
VALUES (?,?,?,?,?,?,?,?,?);'''
    cursor = conn.cursor()
    cursor.execute(insertSQL, data_list)
    conn.commit()

def getlot(conn):
    lotSQL = '''
    SELECT *
    FROM lot
    ORDER BY datetime DESC
    LIMIT 10
    '''
    cursor = conn.cursor()
    cursor.execute(lotSQL)
    return cursor.fetchall()


