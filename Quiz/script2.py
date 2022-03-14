import pathlib
import sqlite3

DB_FILE = "test.db"
DB_FOLDER = "database"
TABLE_NAME = "users"

PATH_TO_DB = pathlib.Path(__file__).parent.joinpath(DB_FOLDER, DB_FILE)

SQL_QUERY = F"""
CREATE TABLE '{TABLE_NAME}' (
    'user_id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'user_name' TEXT,
    'user_mail' TEXT
)

"""
sql_multiple_queries = ""
for i in range(100, 200):
    sql_multiple_queries += F"""
    INSERT INTO '{TABLE_NAME}' 
    ('user_name', 'user_mail') VALUES
    ('user_{i}', 'user_{i}@gmail.com');
    
    """
    pass

with sqlite3.connect(PATH_TO_DB) as c:
    try:
        curs = c.cursor()
        # sqlite3.OperationalError: table 'users' already exists
        curs.execute(SQL_QUERY)
        curs.executescript(sql_multiple_queries)
        pass
    except sqlite3.OperationalError as e:
        print("DataBase operation - ERROR: ", e)
        pass
    finally:
        print("Finally ...")
        pass
    pass

print("After WITH - statements")
