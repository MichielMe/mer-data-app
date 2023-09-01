from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from querySim import query_result
from flask_bootstrap import Bootstrap

boostrap = Bootstrap()


# database met sqlite als 'dummy'-database
db = SQLAlchemy()
DB_NAME = "database.db"
basedir = os.path.abspath(os.path.dirname(__file__))

# db_test = SQLAlchemy()                                            #todo TEST DATABASE, setup sqlalchemy db connection

# DATABASE URL als variable. Zo kan ik later de url aanpassen naar een microsoft sql
DATABASE_URL = os.environ.get("DATABASE_URL") or f"sqlite:///{basedir}/{DB_NAME}"
#DATABASE_TEST_URL =                                             #todo TEST DATABASE

# maken van de app, deze wordt opgeroepen in de main.py file in de directory MER-data-app
def create_app():
    app = Flask(__name__)
    boostrap.init_app(app)
    app.config["SECRET_KEY"] = "MerdataAppMichiel"
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    # app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL          #todo TEST DATABASE
    db.init_app(app)

    from .views import views

    # from .merdata import merdata

    app.register_blueprint(views, url_prefix="/")
    # app.register_blueprint(merdata, url_prefix="/")

    from .models import Material
    # from .models import Material_test                             #todo TEST DATABASE

    with app.app_context():
        db.create_all()
        # populate_db()

    return app
