import mysql.connector
import mysql.connector.pooling
from database.db_config import dbconfig


class database:
    def __init__(self):
        # restarted every battle?
        self.pool = mysql.connector.pooling.MySQLConnectionPool(pool_reset_session=True,
                                                                pool_name="mypool", pool_size=10, **dbconfig)

    def get_con(self):
        return self.pool.get_connection()

    # NOT GENERIC QUERY, select and delete
    def query(self, query):
        print(query)
        con = self.get_con()
        cursor = con.cursor()
        cursor.execute(query)
        try:
            result = cursor.fetchall()
        except:
            result = None

        cursor.close()
        con.close()

        return result

    def insert(self, query, values):
        #query = "INSERT INTO players (uid, rank, username)"
        if len(query) <= 0 and len(values) <= 0:
            return None
        con = self.get_con()
        cursor = con.cursor()

        sql = f"{query} VALUES (%s, %s, %s)"
        print(sql)
        cursor.executemany(sql, values)
        con.commit()

        cursor.close()
        con.close()


#db = database()
# db.insert("INSERT INTO players (uid, permission, username)",
# [(1033556742, 9, "Starcatcher")])

#print(db.select_or_delete('select_or_delete * from players'))
# con.close()
