from flask_sqlalchemy import SQLAlchemy
from yoyo import read_migrations
from yoyo import get_backend
from sqlalchemy.ext.automap import automap_base

class base():
    pass

def apply_db_migrations(db_uri):
    backend = get_backend(db_uri)
    migrations = read_migrations('./migrations')
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))

    Base = automap_base()
    Base.prepare(db.engine, reflect=True)
    global base
    base.Counter = Base.classes.counter

db = SQLAlchemy()
