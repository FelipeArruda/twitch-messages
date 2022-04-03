from flask import Flask
import os
import mysql.connector
from mysql.connector import errorcode




app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>AWS!</p>"

    try:
        cnx = mysql.connector.connect(user='felipearruda', password='felipejf34',
                                      host='mysql-twitch.cf7idmglqggw.sa-east-1.rds.amazonaws.com',
                                      database='twitch')
        print("Conectado")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)