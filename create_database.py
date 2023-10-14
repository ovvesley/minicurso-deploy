from connector.database import connect_postgressql
from dotenv import load_dotenv
import os
load_dotenv() 

def create_database():

    print ("Creating database...")

    if not os.getenv("DB_HOST") or not os.getenv("DB_NAME") or not os.getenv("DB_USER") or not os.getenv("DB_PASS") or not os.getenv("DB_PORT"):
        raise Exception("Environment variables not found")

    print ("DB_HOST: " + os.getenv("DB_HOST"))
    print ("DB_NAME: " + os.getenv("DB_NAME"))
    print ("DB_USER: " + os.getenv("DB_USER"))
    print ("DB_PASS: " + os.getenv("DB_PASS"))

    connection = connect_postgressql(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        port=os.getenv("DB_PORT")
    )
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS series (id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL, image_url VARCHAR(1000) NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS reviews (id SERIAL PRIMARY KEY, serie_id INTEGER NOT NULL, value INTEGER NOT NULL, FOREIGN KEY (serie_id) REFERENCES series (id))")
    connection.commit()
    cursor.close()
    connection.close()

create_database()