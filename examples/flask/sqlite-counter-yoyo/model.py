from flask_sqlalchemy import SQLAlchemy
from yoyo import read_migrations
from yoyo import get_backend
from sqlalchemy.ext.automap import automap_base

def apply_db_migrations(db_uri):
    backend = get_backend(db_uri)
    migrations = read_migrations('./migrations')
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))


def setup_db(app):
    db = SQLAlchemy()
    db.init_app(app)
    return db

def create_classes(db):
    Base = automap_base()
    Base.prepare(db.engine, reflect=True)
    Counter = Base.classes.counter
    return Counter

