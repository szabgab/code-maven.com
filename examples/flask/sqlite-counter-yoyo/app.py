from flask import Flask, render_template, request, abort
import logging
import os
from model import apply_db_migrations, db, base

def create_app():
    app = Flask(__name__)
    app.logger.setLevel(logging.INFO)

    with app.app_context():
        db_file = os.environ.get('COUNT_DB') or 'counter.db'
        db_uri = 'sqlite:///' + db_file
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
        apply_db_migrations(db_uri)

        @app.route('/')
        @app.route('/<name>')
        def counter(name = None):
            if name:
                if name == 'favicon.ico':
                    return abort(404)
                app.logger.info("name %s", name)
                cntr = db.session.query(base.Counter).filter_by(name=name).first()
                app.logger.info(cntr)
                if not cntr:
                    cntr = base.Counter(name=name, count=1)
                    db.session.add(cntr)
                else:
                    cntr.count += 1
                db.session.commit()
                app.logger.info(cntr)

                return render_template('counter.html', name = name, counter = cntr.count)
            else:
                counters = [ {"name": counter.name, "count" : counter.count} for counter in db.session.query(base.Counter).all()]
                app.logger.info(counters)
                return render_template('counter.html', counters = counters)



    return app
