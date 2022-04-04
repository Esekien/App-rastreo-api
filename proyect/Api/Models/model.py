from flask_sqlalchemy import SQLAlchemy

import sys
sys.path.append(".")
from proyect import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    full_name = db.Column(db.Text, nullable=False)
    vehiculo = db.relationship('Behiculo', backref='user', lazy=True)

class Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plates = db.Column(db.Text, nullable=False, unique=True)
    last_position = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)


db.create_all()