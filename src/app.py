import os

from flask import Flask, send_from_directory, url_for

app = Flask(__name__, static_url_path='/', root_path=os.path.join(os.getcwd()))


@app.route('/api')
def api():
    return 'Hello World!'


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run()
