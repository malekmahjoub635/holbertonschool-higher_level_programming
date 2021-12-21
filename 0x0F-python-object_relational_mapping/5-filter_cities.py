#!/usr/bin/python3
''' takes in an argument and displays '''
if __name__ == "__main__":
    import MySQLdb
    import sys

    data = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           password=sys.argv[2], db=sys.argv[3])
    cur = data.cursor()
    cur.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (sys.argv[4],))
    query = cur.fetchall()
    print(", ".join([row[0] for row in query]))
    cur.close()
    data.close()
