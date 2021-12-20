#!/usr/bin/python3
''' lists all states with a name starting with N from the database '''
if __name__ == "__main__":
    import MySQLdb
    import sys

    data = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           password=sys.argv[2], db=sys.argv[3])
    cur = data.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name LIKE BINARY 'N%'\
                ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    data.close()
