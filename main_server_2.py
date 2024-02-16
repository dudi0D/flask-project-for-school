from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    count = [str(i) for i in range(10, 0, -1)]
    count.append('Старт!')
    return '<br>'.join(count)


@app.route('/image_sample')
def image_sample():
    return f'''<img src="{url_for('static', filename='/image/cat.webp')}"
                alt="Это картинка кота" width=200 height=200>'''


@app.route('/sample_page')
def sample_page():
    return f'''<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="static/css/style.css">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<h1> Первая веб-страница на Flask
<body>
  
</body>
</html>'''


@app.route('/sample_bootstrap')
def sample_bootstrap():
    return f'''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
  A simple success alert-check it out!
  </body>
</html>'''


i = 0


@app.route('/i')
def show_i():
    global i
    i += 1
    return str(i)


@app.route('/sample_param/<username>')
def sample_param(username):
    return f'''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{username}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
  привет {username}!
  </body>
</html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''
    <!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Колонизация</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link href="static/css/style.css" rel="stylesheet">  
  </head>
  <body>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
  
  <h1>Жди нас, Марс!</h1>
  <img src="static/image/mars.jpg" width=20%>
<div class="alert alert-secondary" role="alert">
  Человечество вырастает из детства.
</div>
<div class="alert alert-success" role="alert">
  Человечеству мала одна планета.
</div>
<div class="alert alert-danger" role="alert">
  Мы сделаем обитаемыми безжизненные пока планеты.
</div>
<div class="alert alert-warning" role="alert">
  И начнем с Марса!
</div>
<div class="alert alert-info" role="alert">
  Присоединяйся!
</div>

    </body>
</html>
'''


@app.route('/promotion')
def promotion():
    return '''
        <!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Рекламная кампания</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link href="static/css/style.css" rel="stylesheet">  
  </head>
  <body>
  <h1> Тезисы </h1>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
  <ul class="list-group">
  <li class="list-group-item">Человечество вырастает из детства.</li>
  <li class="list-group-item">Человечеству мала одна планета.</li>
  <li class="list-group-item"> Мы сделаем обитаемыми безжизненные пока планеты.</li>
  <li class="list-group-item">И начнем с Марса!</li>
  <li class="list-group-item">Присоединяйся!</li>
</ul>
    '''

if __name__ == '__main__':
    print("http://127.0.0.1:8080/")
    print("http://127.0.0.1:8080/image_sample")
    print("http://127.0.0.1:8080/sample_page")
    print("http://127.0.0.1:8080/sample_bootstrap")
    print("http://127.0.0.1:8080/i")
    print("http://127.0.0.1:8080/sample_param")
    print("http://127.0.0.1:8080/promotion_image")
    print("http://127.0.0.1:8080/promotion")
    app.run(port=8080, host='127.0.0.1')
