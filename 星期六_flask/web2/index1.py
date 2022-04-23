import pymysql.cursors
from pymysql import Error
def create_connection():
    connection = pymysql.connect(host='us-cdbr-east-05.cleardb.net',
                                 user='be8240e46ea8d8',
                                 password='',
                                 database='heroku_fe9f33d1b22e89f',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

def insert_project(conn, project):
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
    VALUES(%s, %s, %s)
    '''
    with conn.cursor() as cursor:
        cursor.execute(sql, project)
    conn.commit()
    return cursor.lastrowid

def insert_task(conn, task):
    #?符號要改為%s
    sql = ''' INSERT INTO task(name, priority, status_id, project_id,begin_date, end_date)
    VALUES(%s, %s, %s, %s, %s, %s)
    '''
    with conn.cursor() as cursor:
        cursor.execute(sql, task)
    conn.commit()

    return cursor.lastrowid

if __name__ == "__main__":
    conn = create_connection()
    if conn is not None:
        with conn:
            # 建新一個新的project
            project = ('Cool App with SQLite & Python', '2020-01-01', '2021-01-30')
            project_id = insert_project(conn, project)

            # 建立2個新的任務
            task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2020-01-01', '2020-01-02')
            task_2 = ('Confirm with user about top requirements', 1, 1, project_id, '2020-01-03', '2020-01-05')
            insert_task(conn, task_1)
            insert_task(conn, task_2)
