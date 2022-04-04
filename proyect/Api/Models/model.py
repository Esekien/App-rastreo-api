from flask_sqlalchemy import SQLAlchemy

import sys
sys.path.append(".")
from proyect import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    full_name = db.Column(db.Text, nullable=False)
    vehiculo = db.relationship('Vehiculo', backref='user', lazy=True)

class Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plates = db.Column(db.String(20), nullable=False)
    lat = db.Column(db.String(20), nullable=False)
    lon = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)

    def __init__(self, plates, lat, lon, user_id):
        self.plates = plates
        self.lat = lat
        self.lon = lon
        self.user_id = user_id


db.create_all()