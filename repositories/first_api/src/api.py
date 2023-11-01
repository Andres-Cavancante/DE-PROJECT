import uuid
import hashlib
import jwt
import datetime
from src.database_connect import database


db = database()

class Api():
    def write_user(self, user_name: str, password: str):
            query = f"INSERT INTO users (userID, userName, userPassword) VALUES (%s, %s, %s);"
            hs_pass = hashlib.sha256(password).hexdigest()
            client_secret = str(uuid.uuid4())
            hashed_secret = hashlib.sha256(client_secret.encode()).hexdigest()
            data = (user_name, hs_pass, hashed_secret)
            status, res = db.interact("SET", query, data)
            if status == "Success":
                 return f"User {user_name} succesfully created. Client secret: {client_secret}", 200
            else:
                 return res, 500
    
    def direct_query_report(self, query: str):
        dict_data = []
        code, data = db.interact("GET", query)
        for item in data:
            dict_data.append({
               "accountId": item[0],
               "day": item[1],
               "campaignName": item[2],
               "campaignID": item[3],
               "adName": item[4],
               "adID": item[5],
               "impressions": item[6],
               "clicks": item[7],
               "spend": item[8]
            })
        return dict_data, code
    
    def generate_token(self, secret: str, user: str):
        return jwt.encode({"user": user, "exp": datetime.datetime.now()+datetime.timedelta(minutes=15)}, secret)
         