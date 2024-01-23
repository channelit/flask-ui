import json
import os
from flask import Flask, send_from_directory, request

from api import Api

app = Flask(__name__)

ui_folder = './ui'
print(ui_folder)
search_api = Api()


@app.route('/api', methods=['POST'])
def api():
    user_input = request.get_json()
    search_text = user_input['search_text']
    return search_api.get_results(search_text)


@app.route('/ui/<path:path>', methods=['GET'])
def static_proxy(path):
    if path.endswith(".js"):
        return send_from_directory(ui_folder, path, mimetype="application/javascript")
    elif path.endswith(".css"):
        return send_from_directory(ui_folder, path, mimetype="text/css")
    else:
        return send_from_directory(ui_folder, path)


@app.route('/ui')
def root():
    return send_from_directory(ui_folder, 'index.html')


@app.errorhandler(404)
def not_found(e):
    return send_from_directory(ui_folder, 'index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
