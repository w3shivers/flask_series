from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page!</h1>"

if __name__ == '__main__':
    app.run(
        host=os.getenv('FLASK_HOST'),
        port=os.getenv('FLASK_PORT'),
        debug=os.getenv('FLASK_DEBUG_MODE')
    )