from database import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    real_name = db.Column(db.String(100), nullable=False)
    bibliography = db.Column(db.Text, nullable=True)
    birth_date = db.Column(db.Date, nullable=True)

class MovieActor(db.Model):
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'), primary_key=True)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Dependent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    watch_date = db.Column(db.Date, nullable=False)