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

def create_table(conn,create_table_sql):
    with conn.cursor() as cursor:
        cursor.execute(create_table_sql)
    conn.commit()

if __name__ == "__main__":
    #MYSQL AUTO_INCREMENT要有
    sql_create_projects_table = """
            CREATE TABLE IF NOT EXISTS projects(
    		id integer PRIMARY KEY AUTO_INCREMENT,
    		name text NOT NULL,
    		begin_date text,
    		end_date text
        );
       """

    sql_create_tasks_table = """
        CREATE TABLE IF NOT EXISTS task(
    	id integer PRIMARY KEY AUTO_INCREMENT,
    	name text NOT NULL,
    	priority integer,
    	project_id integer NOT NULL,
    	status_id integer NOT NULL,
    	begin_date text NOT NULL,
    	end_date text NOT NULL,
    	FOREIGN KEY(project_id) REFERENCES projects(id)
        );
        """

    conn = create_connection()
    if conn is not None:
        #with conn要使用在這裏,呼叫2次create_table後才可以close()
        with conn:
            create_table(conn,sql_create_projects_table)
            create_table(conn,sql_create_tasks_table)

    else:
        print("無法建立資料連線")
