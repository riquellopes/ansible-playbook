# coding: utf-8
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello worlds!"

app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run(host='0.0.0.0')
