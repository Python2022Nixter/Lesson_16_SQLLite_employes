import csv
import pathlib
import sqlite3

CSV_FILE = "test_users.csv"
CSV_FOLDER = "CSV"
DB_FILE = "test.db"
DB_FOLDER = "database"
TABLE_NAME = "users_new"

"""
SQLite data types:
NULL
The value is a NULL value.
INTEGER
The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
REAL
The value is a floating point value, stored as an 8-byte IEEE floating point number.
TEXT
The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE)
BLOB
The value is a blob of data, stored exactly as it was input.

"""
PATH_TO_DB = pathlib.Path(__file__).parent.joinpath(DB_FOLDER, DB_FILE)
PATH_TO_CSV = pathlib.Path(__file__).parent.joinpath(CSV_FOLDER, CSV_FILE)

# Read from csv
headers = []
users = []
with open(PATH_TO_CSV) as f:
    # rdr = csv.reader(f)
    # for row in rdr:
    #     if row[0] == 'id': headers = row
    #     else: users.append(row[1:])
    headers = f.readline().strip().split(",")
    users_strings = f.readlines()
    pass

for next_user in users_strings:
    users.append(next_user.strip().split(",")[1:])
    pass

print(users[1])
SQL_CREATE_TABLE = F"""
CREATE TABLE IF NOT EXISTS '{TABLE_NAME}' (
    '{headers[0]}' INTEGER PRIMARY KEY AUTOINCREMENT,
    '{headers[1]}' TEXT,
    '{headers[2]}' TEXT,
    '{headers[3]}' TEXT,
    '{headers[4]}' TEXT,
    '{headers[5]}' TEXT
);
"""

print (SQL_CREATE_TABLE)

sql_add_users = F"""
    INSERT INTO '{TABLE_NAME}' 
    ('{headers[1]}', '{headers[2]}', '{headers[3]}', '{headers[4]}', '{headers[5]}') VALUES
    (?,?,?,?,?);
    
    """

with sqlite3.connect(PATH_TO_DB) as c:
    try:
        curs = c.cursor()
        curs.execute(SQL_CREATE_TABLE) # sqlite3.OperationalError: table 'users' already exists
        curs.executemany(sql_add_users, users)
         
        pass
    except sqlite3.OperationalError as e:
        print ("DataBase operation - ERROR: ", e)
        pass
    finally:
        print ("Finally ...")
        pass
    pass    

# print ("After WITH - statements")

