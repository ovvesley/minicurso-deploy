from connector.database import connect_postgressql
import os
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
        cursor.execute("SELECT AVG(reviews.value) as reviews_avg, COUNT(reviews.id) as reviews_count FROM series INNER JOIN reviews ON series.id = reviews.serie_id GROUP BY series.id")
        series = cursor.fetchall()
        cursor.close()
        return series
    
    def insert_review(self, serie_id: int, value: int) -> None:
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO reviews (serie_id, value) VALUES (%s, %s)", (serie_id, value))
        self.connection.commit()
        cursor.close()

        