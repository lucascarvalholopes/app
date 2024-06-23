from flask import request, jsonify, render_template
from models import db, Movie, Actor, MovieActor, Client, Dependent, History
from datetime import datetime

def setup_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/clients', methods=['GET', 'POST'])
    def clients():
        if request.method == 'POST':
            data = request.json
            client = Client(name=data['name'])
            db.session.add(client)
            db.session.commit()
            return jsonify({'id': client.id}), 201
        clients = Client.query.all()
        return render_template('client.html', clients=clients)

    @app.route('/actors', methods=['GET'])
    def actors():
        actors = Actor.query.all()
        return render_template('actor.html', actors=actors)

    @app.route('/movies', methods=['GET'])
    def movies():
        movies = Movie.query.all()
        return jsonify([{'id': movie.id, 'title': movie.title, 'category': movie.category} for movie in movies])

    @app.route('/history', methods=['POST'])
    def add_history():
        data = request.json
        history = History(
            client_id=data['client_id'],
            movie_id=data['movie_id'],
            watch_date=datetime.strptime(data['watch_date'], '%Y-%m-%d')
        )
        db.session.add(history)
        db.session.commit()
        return jsonify({'id': history.id}), 201

    @app.route('/history/<int:client_id>', methods=['GET'])
    def get_history(client_id):
        history = History.query.filter_by(client_id=client_id).all()
        return jsonify([{'movie_id': h.movie_id, 'watch_date': h.watch_date} for h in history])