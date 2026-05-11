from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():

    return "MIFL HELPER BOT IS WORKING"

def run_web():

    port = int(
        os.environ.get("PORT", 10000)
    )

    app.run(
        host="0.0.0.0",
        port=port
    )
