import sqlite3

def train_sql():
    dbname = "TEST.db"
    conn = sqlite3.connect(dbname)

    cur = conn.cursor()

    # cur.execute(
    # "create table persons(id integer primary key autoincrement, name string)")

    # cur.execute('insert into persons(name) values("TARO")')

    cur.execute('select * from persons')

    print(cur.fetchall())

    # conn.commit()
    cur.close()
    conn.close()
