from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Bem vindo!</p>"



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='https://twitch-message.herokuapp.com/', port=port)