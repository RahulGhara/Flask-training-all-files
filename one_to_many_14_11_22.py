from flask import Flask
# from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/Relationships"
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    address = db.relationship('Address', backref='person', lazy=True)


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(35), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
