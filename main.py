from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')

def default():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Миссия Колонизация Марса</title>
                  </head>
                  <body>
                    <h1>Миссия Колонизация Марса</h1>
                  </body>
                </html>'''


@app.route('/index')
def index():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>И на Марсе будут яблони цвести!</title>
                  </head>
                  <body>
                    <h1>И на Марсе будут яблони цвести!</h1>
                  </body>
                </html>'''


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <p><img src={url_for('static', filename='images/mars.jpg')} width="500" height="500" alt="Нет фото"></p>
                        <p>Вот она, красная планета</p>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')