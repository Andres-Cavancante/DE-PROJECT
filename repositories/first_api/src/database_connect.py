import mysql.connector
import os

class database:
    def __init__(self):
        self.config = {
            "host": os.getenv("DB_HOST", "localhost"),
            "user": os.getenv("DB_USER", "root"),
            "password": os.getenv("DB_PASS", "pass"),
            "port": int(os.getenv("DB_PORT", 3306))
        }
        self.database = os.getenv("DB_database", "first_api")

    def interact(self, method: str, query: str, data: str = None):
        status = "Error"
        response = None

        try:
            connection = mysql.connector.connect(**self.config)
            cursor = connection.cursor(buffered=True)
        except:
            return status, f"An error ocurred trying to stablish connection to the database"
        
        try:
            cursor.execute(f"USE {self.database};")
            cursor.execute(query) if not data else cursor.execute(query, data) 
        except:
            return status, f"An error ocurred trying to interact with the database"

        status = "Success"

        if method == "GET":
            response = cursor.fetchall()
        if method == "SET":
            connection.commit()
        cursor.close()
        connection.close()
        return status, response if method == "GET" else status