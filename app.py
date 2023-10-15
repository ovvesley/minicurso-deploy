from flask import Flask, render_template, jsonify, request
from repositories.serie_repository import SerieRepository

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/series', methods=['GET'])
def list_series():
    serieRepository = SerieRepository()
    series = serieRepository.list_series() 
    return jsonify({
        'status': 'ok',
        'data': series
    })

# @app.route('/api/series', methods=['POST'])
# def create_series():
#     serieRepository = SerieRepository()
#     series = serieRepository.create_series(
#         title=request.json['title'],
#         image_url=request.json['image_url']
#     )
#     return jsonify({
#         'status': 'ok',
#         'data': series
#     })


@app.route('/api/series/<int:series_id>/review', methods=['POST'])
def series_review(series_id: int):
    serieRepository = SerieRepository()
    serieRepository.insert_review(
        serie_id=series_id,
        value=request.json['rating']
    )
    return jsonify({
        'status': 'ok',
        'message': 'Review inserted'
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)