from flask import Flask, render_template, jsonify, request
from connector.database import connect_postgressql
from repositories.serie_repository import SerieRepository

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/series')
def list_series():
    serieRepository = SerieRepository()
    series = serieRepository.list_series() 

    series.append({
        'id': 1,
        'title': 'Serie 1',
        'image_url': 'https://picsum.photos/200/300',
        'reviews_avg': 4,
        'reviews_count': 10
    })   
    return jsonify({
        'status': 'ok',
        'data': series
    })


@app.route('/api/series/<int:series_id>/review', methods=['POST'])
def series_review(series_id: int):
    serieRepository = SerieRepository()
    serieRepository.insert_review(
        serie_id=series_id,
        value=request.json['value']
    )
    return jsonify({
        'status': 'ok',
        'message': 'Review inserted'
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)