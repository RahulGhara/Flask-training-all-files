from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/DatabaseRahul2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

enrollment = db.Table('enrollment',
                      db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
                      db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'), primary_key=True),
                      )


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    subject = db.relationship('Subject', secondary=enrollment, backref='student')

    # def __repr__(self):
    #     return f'<Student: {self.name}>'


class Subject(db.Model):
    __tablename__ = 'subject'
    id = db.Column(db.Integer, primary_key=True)
    sub_name = db.Column(db.String(30), nullable=False)

    # def __repr__(self):
    #     return f'<Subject: {self.name}>'
