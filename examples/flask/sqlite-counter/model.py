from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Counter(db.Model):
    name = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)
    count = db.Column(db.Integer, unique=False, nullable=False, default=0)
