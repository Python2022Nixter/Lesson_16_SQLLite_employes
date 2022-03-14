import sqlite3 as sql
import pathlib


DB_FILE = "test.db"
DB_FOLDER = "database"
TABLE_NAME = "users"
# """
# user_id autoincrement
# user_name
# user_mail
# """

path_to_DB = pathlib.Path(__file__).parent.joinpath(DB_FOLDER, DB_FILE)
with sql.connect(path_to_DB) as conn:
    c = conn.cursor()
    c.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            user_mail TEXT
        )
    """)

    sql_multiple_queries = f""
    for i in range(10):
        sql_multiple_queries += f"""
        INSERT INTO {TABLE_NAME} (user_name, user_mail) VALUES ("user_{i}", "user_{i}@.gmail.com");
        """
        pass

    c.executescript(sql_multiple_queries)
