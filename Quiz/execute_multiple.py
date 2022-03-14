import pathlib
import sqlite3
import csv

CSV_FILE = "test_users.csv"
CSV_FOLDER = "CSV"
DB_FILE = "test.db"
DB_FOLDER = "database"
TABLE_NAME = "users_new"

PATH_TO_DB = pathlib.Path(__file__).parent.joinpath(DB_FOLDER, DB_FILE)
PATH_TO_CSV = pathlib.Path(__file__).parent.joinpath(CSV_FOLDER, CSV_FILE)

# Read CSV file
headers = []
users = []

with open(PATH_TO_CSV, "r") as f:
    rdr = csv.reader(f, delimiter=",")
    for row in rdr:
        if row[0] == "id":
            headers = row
            continue
        else:
            users.append(row[1:])

            pass
        pass
    #csv_data = f.readlines()
    pass

SQL_QUERY = F"""
CREATE TABLE IF NOT EXIST '{TABLE_NAME}' (
    '{headers[0]}' INTEGER PRIMARY KEY AUTOINCREMENT,
    '{headers[1]}' TEXT,
    '{headers[2]}' TEXT,
    '{headers[3]}' TEXT,
    '{headers[4]}' TEXT,
    '{headers[5]}' TEXT
)

"""

sql_add_users = F"""
    INSERT INTO '{TABLE_NAME}' 
    ('{headers[1]}', '{headers[2]}', '{headers[3]}', '{headers[4]}', '{headers[5]}') VALUES
    ('?, ?, ?, ?, ?')');
    """



with sqlite3.connect(PATH_TO_DB) as c:
    try:
        curs = c.cursor()
        curs.execute(SQL_QUERY)
        curs.executemany(sql_add_users, users)
        pass
    except sqlite3.OperationalError as e:
        print("DataBase operation - ERROR: ", e)
        pass
    finally:
        print("Finally ...")
        pass
    pass

print("After WITH - statements")
