from . import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from querySim import query_result


# --- Als we migreren naar mssql -----
# importeren van de nodige packages and driver installeren
# from flask_migrate import Migrate

# migrate = Migrate(app, db)
# ------------------------------------


# model voor het videomateriaal op sqlite
class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material_id = db.Column(db.String(32), nullable=False, unique=False)
    title = db.Column(db.String(60))
    material_type = db.Column(db.String(60))


# POPULATE DATABASE voorlopig met de querySym.py
def populate_db():
    from .models import Material

    for record in query_result:
        material = Material(
            material_id=record["MATERIAL ID"],
            title=record["TITLE"],
            material_type=record["MATERIAL TYPE"],
        )
        db.session.add(material)
    db.session.commit()
