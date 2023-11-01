import mysql.connector
import uuid
import random
from datetime import datetime, timedelta

mysql_config = {
    "host": "localhost",
    "user": "root",
    "password": "pass",
    "database": "first_api"
}

def random_date(start_date, end_date):
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
    
    date_range = (end_datetime - start_datetime).days
    
    random_days = random.randint(0, date_range)
    
    result_date = start_datetime + timedelta(days=random_days)
    
    return result_date.strftime('%Y-%m-%d')

def generate_random_uuid():
    return str(uuid.uuid4())

connection = mysql.connector.connect(**mysql_config)
cursor = connection.cursor()

data = []
for _ in range(3):
    account = str(random.randint(714000000, 714999999))
    for _ in range(5):
        campaignID = generate_random_uuid()
        campaignName = f"Campaign_{account}_{campaignID}"
        for _ in range(10):
            adID = generate_random_uuid()
            adName = f"Ad_{account}_{campaignID}_{adID}"
            for _ in range(50):
                date = random_date("2023-01-01", "2023-10-28")
                impressions = random.randint(1000, 5000)
                clicks = random.randint(100, 1000)
                spend = random.uniform(100.0, 5000.0)
                insert_query = "INSERT INTO basic (accountId, day, campaignName, campaignID, adName, adID, impressions, clicks, spend) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                data = (account, date, campaignName, campaignID, adName, adID, impressions, clicks, spend)

                cursor.execute(insert_query, data)
connection.commit()
cursor.close()
connection.close()



