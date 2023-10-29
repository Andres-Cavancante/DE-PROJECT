from flask import Flask, request, jsonify, make_response
from src.database_connect import database
import uuid
import hashlib

db = database()
app = Flask(__name__)

@app.route("/")
def get_generico():
    return "<h1>Starter Flask Apps</h1>"

@app.route("/users/create", methods=["POST"])
def create_user():
    data = request.get_json()
    hs_pass = hashlib.sha256(data["password"].encode()).hexdigest()
    user_name = data["user"]
    message, code = db.write_user(str(uuid.uuid4()), user_name, hs_pass)
    return jsonify({"messsage": message, "code": code})

@app.route("/reports/<account_id>", methods=["GET"])
def get_report(account_id: str):
    payload = request.get_json()
    data, code = db.direct_query_report(payload["query_parameter"])
    return jsonify({"content": {"data": data}, "code": code})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)