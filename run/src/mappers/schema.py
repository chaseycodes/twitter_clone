import sqlite3

def run(dbname='mock_twitter.db'):

    CON = sqlite3.connect(dbname)
    CUR = CON.cursor()

    CUR.execute("""DROP TABLE IF EXISTS users;""")
    # create accounts table
    CUR.execute("""CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR,
        password VARCHAR,
        CONSTRAINT unique_username UNIQUE(username)
    );""")

    CUR.execute("""DROP TABLE IF EXISTS tweets;""")
    # create positions table
    CUR.execute("""CREATE TABLE tweets(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        post VARCHAR,
        time INTEGER,
        users_pk INTEGER,
        FOREIGN KEY(users_pk) REFERENCES users(pk)
    );""")

    # CUR.execute("""DROP TABLE IF EXISTS trades;""")

    # # create trades table
    # CUR.execute("""CREATE TABLE trades(
    #     pk INTEGER PRIMARY KEY AUTOINCREMENT,
    #     symbol VARCHAR,
    #     price FLOAT,
    #     shares INTEGER,
    #     time INTEGER,
    #     account_pk INTEGER,
    #     FOREIGN KEY(account_pk) REFERENCES accounts(pk)
    # );""")

    # # CUR.execute("""DROP TABLE IF EXISTS master;""")
    # # # create accounts table
    # # CUR.execute("""CREATE TABLE master(
    # #     pk INTEGER PRIMARY KEY AUTOINCREMENT,
    # #     username VARCHAR,
    # #     balance FLOAT,
    # #     pw_hash VARCHAR,
    # #     trade_pk INTEGER,
    # #     FOREIGN KEY(trade_pk) REFERENCES trades(pk)
    # # );""")

    # # CUR.execute("""DROP TABLE IF EXISTS master_sheet;""")
    # # # create accounts table
    # # CUR.execute("""CREATE TABLE master_sheet(
    # #     pk INTEGER PRIMARY KEY AUTOINCREMENT,
    # #     account_pk INTEGER,
    # #     symbol VARCHAR,
    # #     skim_amount FLOAT,
    # #     trade_pk INTEGER,
    # #     FOREIGN KEY(account_pk) REFERENCES accounts(pk),
    # #     FOREIGN KEY(trade_pk) REFERENCES trades(pk)
    # # );""")

    CON.commit()
    CUR.close()
    CON.close()

if __name__ == '__main__':
    run()