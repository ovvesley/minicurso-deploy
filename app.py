from flask import Flask, render_template, jsonify, request
from repositories.serie_repository import SerieRepository
import socket


app = Flask(__name__)

def get_hostname_ipaddress():
    try:
        hostname = socket.gethostname()
        ipaddress = socket.gethostbyname(hostname)
    except Exception as e:
        hostname = 'unknown'
        ipaddress = 'unknown'

    return hostname, ipaddress


@app.route('/')
def index():
    
    hostname, ipaddress = get_hostname_ipaddress()
    return render_template('index.html', hostname=hostname, ipaddress=ipaddress)
    


@app.route('/api/series', methods=['GET'])
def list_series():
    serieRepository = SerieRepository()
    series = serieRepository.list_series() 
    return jsonify({
        'status': 'ok',
        'data': series
    })

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
