import sqlite3
import time

def run(dbname='mock_twitter.db'):
    conn = sqlite3.connect(dbname)
    cur  = conn.cursor()

    SQL = """INSERT INTO users
        (username, password) 
        VALUES (?, ?); """

    cur.execute(SQL, ('chase', 'toor'))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    run()
