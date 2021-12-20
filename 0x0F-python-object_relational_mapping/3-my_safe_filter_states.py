#!/usr/bin/python3
''' a script that takes in an argument and displays
    all values in the states table of hbtn_0e_0_usa'''
if __name__ == "__main__":
    import MySQLdb
    import sys

    data = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           password=sys.argv[2], db=sys.argv[3])
    cur = data.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name='{}'\
                ORDER BY id ASC".format(sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    data.close()
