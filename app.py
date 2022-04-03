from flask import Flask
import os
import mysql.connector
from mysql.connector import errorcode




app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Mysql!</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)