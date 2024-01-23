import os

from flask import Flask, send_from_directory, url_for

app = Flask(__name__, root_path=os.path.join(os.getcwd()))


@app.route('/api')
def api():
    return 'Hello World!'


@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/ui/')
@app.route('/ui/<path:path>')
def serve_ui_app():
    return send_from_directory('static/ui', 'index.html')


if __name__ == '__main__':
    app.run()
