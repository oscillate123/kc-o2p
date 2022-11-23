from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    print(request.headers)
    return "hello app1"

@app.route('/app1')
def app1():
    print(request.headers)
    return "hello app1 - app1 route"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)