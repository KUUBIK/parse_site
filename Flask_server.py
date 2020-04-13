from flask import Flask, render_template, request
from BS4 import find_image, headers, parce, find_from_title_png
from flask_socketio import SocketIO, send, emit
import json

app = Flask(__name__)
socketio = SocketIO(app)


url = 'https://www.redbubble.com/shop/csgo+stickers?ref=search_box'
port = 8888
host = 'localhost'

@app.route('/')
def hello_world():
    return render_template('login.html')

@app.route('/', methods=['GET','POST'])
def my_form_post():
    text = request.form['name_of_sticker']
    print(text)
    global family_urls
    family_urls = "https://www.redbubble.com/shop/" + text + "?iaCode=all-stickers&ref=search_box&sortOrder=relevant"
    find_image(family_urls, headers)
    print("Это основная страница")
    print("----------------------")

    print(family_urls)
    print("Это подстраницы")
    print("----------------------")


    parsing_family_urls = find_from_title_png(family_urls, headers)
    print(parsing_family_urls)
    return render_template('login.html', data = parsing_family_urls)

@socketio.on('message', namespace='/')
def handle_message(message):
    print('received message: ' + message)


if __name__ == '__main__':
    app.run(host, port, debug=True)


