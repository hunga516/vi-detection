from flask import Flask, jsonify, request
from flask_cors import CORS
CORS(app)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return(request.environ['REMOTE_ADDR'])
    else:
        return(request.environ['HTTP_X_FORWARDED_FOR'])

if __name__ == "__main__":
    app.run(debug=True)
