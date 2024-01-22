from flask import Flask

app = Flask(__name__, static_url_path='/')


@app.route('/api')
def main():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
