import mysql.connector
import os

class database:
    def __init__(self):
        self.user = os.getenv("DB_USER", "root")
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = int(os.getenv("DB_PORT", 3306))
        self.password = os.getenv("DB_PASS", "pass")
        self.database = os.getenv("DB_database", "first_api")

    def __interact(self, method, query: str):
        try:
            connection = mysql.connector.connect(user=self.user, host=self.host, port=self.port, password=self.password)
            cursor = connection.cursor(buffered=True)
        except:
            return f"An error ocurred trying to stablish connection to the database", 502
        
        try:
            cursor.execute(f"USE {self.database};")
            cursor.execute(query)
        except:
            return f"An error ocurred trying to interact with the database", 502

        response = "Success"

        if method == "GET":
            response = cursor.fetchall()
        if method == "SET":
            connection.commit()
        cursor.close()
        connection.close()
        return response

    def write_user(self, userID: str, userName: str, userPassword: str):
        query = f"INSERT INTO users (userID, userName, userPassword) VALUES ('{userID}', '{userName}', '{userPassword}');"
        db_response = self.__interact("SET", query)
        if db_response == "Success": 
            return  f"User {userName} created", 200 
        else:
            return db_response, 500
        
    def direct_query_report(self, query: str):
        db_response = self.__interact("GET", query)
        return db_response, 200
