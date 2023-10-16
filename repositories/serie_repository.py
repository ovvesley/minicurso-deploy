from connector.database import connect_postgressql
from dotenv import load_dotenv
import os
load_dotenv() 

class SerieRepository:
    def __init__(self):
        self.connection = connect_postgressql(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            port=os.getenv("DB_PORT")
        )

    def list_series(self) -> list:
        cursor = self.connection.cursor()
        cursor.execute("SELECT series.*, AVG(reviews.value) as reviews_avg, COUNT(reviews.id) as reviews_count FROM series LEFT JOIN reviews ON series.id = reviews.serie_id GROUP BY series.id")
        series = cursor.fetchall()

        series = [{
            'id': serie[0],
            'title': serie[1],
            'image_url': serie[2],
            'reviews_avg': serie[3] or 0,
            'reviews_count': serie[4] or 0
        } for serie in series]


        cursor.close()
        return series
    
    def insert_review(self, serie_id: int, value: int) -> None:
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO reviews (serie_id, value) VALUES (%s, %s)", (serie_id, value))
        self.connection.commit()
        cursor.close()

    def create_series(self, title: str, image_url: str) -> dict:
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO series (title, image_url) VALUES (%s, %s) RETURNING id", (title, image_url))
        self.connection.commit()
        serie_id = cursor.fetchone()[0]
        cursor.close()
        return {
            'id': serie_id,
            'title': title,
            'image_url': image_url
        }

        