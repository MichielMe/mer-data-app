from flask import Blueprint, render_template, Flask, request
from flask_wtf import FlaskForm
from wtforms import FileField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed
from . import db
import openpyxl

# merdata = Blueprint("merdata", __name__)


class UploadForm(FlaskForm):
    file = FileField(
        "Upload bestand met WP-nummers",
        validators=[
            FileRequired(),
            FileAllowed(["xlsx", "xls"], "Enkel Excel bestanden!"),
        ],
    )
    suffix = StringField(
        "Wat wil je toevoegen aan de titel?", validators=[DataRequired()]
    )
    material_type = SelectField(
        "Material Type",
        choices=[
            ("COMMERCIAL", "COMMERCIAL"),
            ("JUNCTION", "JUNCTION"),
            ("PROGRAMME", "PROGRAMME"),
            ("LIVE RECORD", "LIVE RECORD"),
        ],
        validators=[DataRequired()],
    )
    submit = SubmitField("GO")
