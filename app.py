from flask import Flask, render_template, jsonify
import random
from connector.database import connect_postgressql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/t/<username>')
def teacher(username):
    return render_template('teacher.html', username=username)

# api

@app.route('/api/t')
def list_teacher():
    
    # { status: 'ok', data: [ { username: 'xxx', name: 'xxx', avatar: 'xxx' } ] }
    return jsonify({
        'status': 'ok',
        'data': [
            {
                'username': 'xxx',
                'name': 'xxx',
                'avatar': 'xxx'
            }
        ]
    })


@app.route('/api/t/<username>')
def show_teacher(username):

    # { status: 'ok', data: { username: 'xxx', name: 'xxx', avatar: 'xxx' }, review_count: 123, reviews: [ { username: 'xxx', name: 'xxx', avatar: 'xxx', content: 'xxx', score: 5, created_at: 'xxx' } ] }, avg_score: 4.5 }

    return jsonify({
        'status': 'ok',
        'data': {
            'username': 'xxx',
            'name': 'xxx',
            'avatar': 'xxx'
        },
        'review_count': 123,
        'reviews': [
            {
                'username': 'xxx',
                'name': 'xxx',
                'avatar': 'xxx',
                'content': 'xxx',
                'score': 5,
                'created_at': 'xxx'
            }
        ],
        'avg_score': 4.5
    })


@app.route('/api/t/<username>/reviews')
def teacher_review():

    # { status: 'ok', message: 'xxx' }
    
    return jsonify({
        'status': 'ok',
        'message': 'xxx'
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)