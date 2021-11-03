import sqlite3


def database_creation(name):
    con = sqlite3.connect(name)

    cur = con.cursor()

    result = cur.execute("""CREATE TABLE IF NOT EXISTS record (
        id INTEGER PRIMARY KEY,
	    note TEXT,
	    time INTEGER
    )""")

    con.close()


def database_insert(name, elem):
    con = sqlite3.connect(name)

    cur = con.cursor()

    print(elem)

    sqlite_insert_query = f"""INSERT INTO record
    (note,time)
    VALUES
    {elem}"""

    result = cur.execute(sqlite_insert_query)
    con.commit()

    cur.close()