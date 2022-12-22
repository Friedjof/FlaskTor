import os

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT', 5000)
    app.run("0.0.0.0", port=port)