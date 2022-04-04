from flask import Flask
import os

app = Flask("Twitch Messages")



@app.route("/")
def hello_world():
    return "AWS 23"



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)