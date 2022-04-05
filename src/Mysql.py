import mysql.connector
from mysql.connector import errorcode


class MysqlDriver:

    def __init__(self, val):
        self.val = val
        try:
            self.cnx = mysql.connector.connect(user='felipearruda', password='felipejf34',
                                          host='mysql-twitch.cf7idmglqggw.sa-east-1.rds.amazonaws.com',
                                          database='twitch')
            self.cursor = self.cnx.cursor()
            print("Connected to Mysql.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                exit()
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                exit()
            else:
                print(err)
                exit()

    def query(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        return row