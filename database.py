import psycopg2
from types import SimpleNamespace

conf = SimpleNamespace(
    DB_HOST = 'localhost',
    DB_NAME = 'postgres',
    DB_USER = 'postgres',
    DB_PASSWORD = ''
)


"""
Setup db conn
"""
def get_db_conn():
    conn = psycopg2.connect(
        host=conf.DB_HOST,
        database=conf.DB_NAME,
        user=conf.DB_USER,
        password=conf.DB_PASSWORD
    )
    return conn


"""

    @ Create tables

"""
def create_tables():
    tables = """create table users(
	user_id SERIAL primary key,
	user_name varchar(255),
	balance int
);

create table stations(
	station_id SERIAL primary key,
	station_name varchar(255),
	longitude double,
	latitude double,
);


create table trains(
	train_id SERIAL primary key,
	train_name varchar(255),
	capacity int,
);


create table train_stops(
    id SERIAL primary key,
    train_id int REFERENCES trains(train_id),
    station_id int REFERENCES stations(station_id)
);"""

    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute(tables)
    conn.commit()

    if conn:
        cursor.close()
        conn.close()




"""
Queries
"""

def view_all(query):
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data



# insert into db
def insert_into_db(query, params):
    try:
        conn = get_db_conn()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return True
    except:
        raise Exception("Error Inserting data")