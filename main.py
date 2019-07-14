from flask import Flask

app = Flask(__name__)

@app.route("/get", methods=["GET"])
def get():
    return "get"

@app.route("/post", methods=["POST"])
def post():
    return "post"

if __name__ == '__main__':
    app.run()