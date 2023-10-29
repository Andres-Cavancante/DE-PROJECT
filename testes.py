# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import hashlib
import requests
import json


# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://data-engineer:pass@172.19.0.3:3306/database"
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)

# new_user = User(id="23423424")
# db.session.add(new_user)
# db.session.commit()

mydb = mysql.connector.connect(
  host="172.21.0.2",
  user="data-engineer",
  password="pass"
)


# response = requests.post("http://localhost:5000/users/create", json={"user": "samsumg", "password": "samsung2023@Global"})

# print(response)