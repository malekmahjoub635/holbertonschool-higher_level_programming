#!/usr/bin/python3
''' lists all cities from the database hbtn_0e_4_usa '''
if __name__ == "__main__":
    import MySQLdb
    import sys

    data = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           password=sys.argv[2], db=sys.argv[3])
    cur = data.cursor()
    cur.execute("SELECT c.id, c.name, s.name "
                "FROM cities AS c JOIN states AS s ON c.state_id = s.id "
                "ORDER BY c.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    data.close()
