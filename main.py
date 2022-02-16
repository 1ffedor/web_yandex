# https://github.com/1ffedor/web_yandex/blob/WEB.2.problem1

from flask import Flask, url_for, render_template
import json

app = Flask(__name__)


@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')