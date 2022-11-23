from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    print(request.headers)
    return "hello app2"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)