from flask import Flask
import os
import mysql.connector
from mysql.connector import errorcode




app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>AWS! 001</p>"

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

    def pushEventMessage(data_event_message):
        add_event_message = ("INSERT INTO twitch.event_message "
                             "(user, channel, message, date, created_at) "
                             "VALUES (%s, %s, %s, %s, %s)")
        # user = usuario que mandou a msg,
        # channel = canal em que foi mandado a msg,
        # message = mensagem,
        # date = data/hora do servidor da twitch,
        # created_at = data/hora da insercao no BD

        cursor = cnx.cursor()
        cursor.execute(add_event_message, data_event_message)
        cnx.commit()
        cursor.close()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)