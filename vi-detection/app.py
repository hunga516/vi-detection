from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        print(request.environ['REMOTE_ADDR'])
    else:
        print(request.environ['HTTP_X_FORWARDED_FOR'])
    return jsonify(success=True)
