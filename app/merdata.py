from flask_wtf import FlaskForm
from wtforms import FileField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed


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
    replace_text = StringField("Te vervangen tekst: (laat leeg als je alleen iets wilt toevoegen aan de tekst.)")  # New field
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
