from flask import Flask, request, jsonify, make_response
from src.api import Api
from functools import wraps

api = Api()
app = Flask(__name__)

def require_token(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return {"message": "Token is missing!"}
        
        secret = api.check_token(token)
    
        return f(secret=secret, *args, **kwargs)
    return wrapper


@app.route("/")
def get_generico():
    return "<h1>Starter Flask Apps</h1>"

@app.route("/users/create", methods=["POST"])
def create_user():
    data = request.get_json()
    message, code = api.write_user(data["user"], data["password"].encode())
    return jsonify({"messsage": message, "code": code})

@app.route("/token", methods=["GET"])
def get_token():
    data = request.get_json()
    password = data["password"]
    user = data["app_id"]
    token = api.generate_token(user, password)
    return jsonify({"token": token})

@app.route("/reports/<account_id>", methods=["GET"])
@require_token
def get_report(account_id: str, secret: str):
    payload = request.get_json()
    # if request.headers.get("Authorization", None):

    data, code = api.direct_query_report(secret, payload)
    return jsonify({"content": {"data": data}, "code": code})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)