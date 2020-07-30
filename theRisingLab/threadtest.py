"""
import time
import threading


def sing():
    for i in range(1, 5):
        print("singing")
        time.sleep(1)


def dance():
    print("dancing")
    time.sleep(1)


def run():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()


run()
"""

import MySQLdb
import datetime
import time


def insert(io):
    while True:
        time_now = datetime.datetime.now()
        print(io,time_now)
        conn = MySQLdb.connect(host="10.26.31.128",
                               port=3306,
                               user="fuxingyu",
                               password="syylfml1685",
                               db="risingdata",
                               charset='utf8mb4')
        cur = conn.cursor()
        sql = "insert into table_%s values ('%s','%s');"
        cur.execute(sql % (io, io, time_now))
        cur.close()
        conn.commit()
        time.sleep(5)


if __name__ == "__main__":
    import threading
    t = threading.Thread(target=insert, args=('in',))
    t.start()
    t = threading.Thread(target=insert, args=('out',))
    t.start()
    t.join()
