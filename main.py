# https://github.com/1ffedor/web_yandex/blob/problem6

from flask import Flask, url_for, render_template
import json

app = Flask(__name__)


@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')