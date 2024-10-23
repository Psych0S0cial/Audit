
from datetime import datetime
from flask import Flask, request, jsonify, make_response, render_template
from FlaskWebProject6 import app

# 1. Роут для GET-запросов
@app.route('/get-root', methods=['GET'])
def handle_get():
    if request.method == 'GET':
        a = 1 # заглушка
    else:
        return make_response("Method Not Allowed", 405)

# 2. Роут для POST-запросов
@app.route('/post-root', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        a = 1 # заглушка
    else:
        return make_response("Method Not Allowed", 405)

# 3. Роут для HEAD-запросов
@app.route('/head-root', methods=['HEAD'])
def handle_head():
    if request.method == 'HEAD':
        response = make_response('', 200)
        return response
    else:
        return make_response("Method Not Allowed", 405)

# 4. Роут для OPTIONS-запросов
@app.route('/options-root', methods=['OPTIONS'])
def handle_options():
    if request.method == 'OPTIONS':
        response = make_response('', 204)
        return response
    else:
        return make_response("Method Not Allowed", 405)

# Главная страница с ссылками на все роуты
@app.route('/')
def index():
    return render_template('index.html')
