from flask import Flask, request, jsonify, make_response
from src.api import Api

api = Api()
app = Flask(__name__)

@app.route("/")
def get_generico():
    return "<h1>Starter Flask Apps</h1>"

@app.route("/users/create", methods=["POST"])
def create_user():
    data = request.get_json()
    message, code = api.write_user(data["user"], data["password"].encode())
    return jsonify({"messsage": message, "code": code})

@app.route("/token")
def get_token():
    data = request.get_json()
    client_secret = data["client_secret"]
    user = data["userName"]
    token = api.generate_token(client_secret, user)
    return jsonify({"token": token.decode("UTF-8")})

@app.route("/reports/<account_id>", methods=["GET"])
def get_report(account_id: str):
    payload = request.get_json()
    data, code = api.direct_query_report(payload["query_parameter"])
    return jsonify({"content": {"data": data}, "code": code})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)