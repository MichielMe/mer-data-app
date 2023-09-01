from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import Material, populate_db
from .merdata import UploadForm
import pandas as pd

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def index():
    form = UploadForm()
    material_ids_to_display = []
    if form.validate_on_submit():
        # 1. Read the uploaded Excel file
        file = form.file.data
        df = pd.read_excel(file)
        material_ids = df.iloc[
            :, 0
        ].values.tolist()  # Als de ID's in de eerste column staan.
     
        # 2. Filter the database based on MATERIAL IDs
        materials_to_update = Material.query.filter(
            Material.material_id.in_(material_ids)
        ).all()
        
        # Populate the list of material_ids to be displayed on the web page
        material_ids_to_display = [material.material_id for material in materials_to_update]

        # 3. Modify the title and material type columns
        replace_text = form.replace_text.data
        suffix = form.suffix.data
        material_type = form.material_type.data

        for material in materials_to_update:
            if replace_text:
                material.title = material.title.replace(replace_text, suffix)
            else:
                material.title += " " + suffix

            material.material_type = material_type
        
        # 4. Commit changes to the database
        db.session.commit()

        flash("Database updated successfully!", "success")
        return redirect(url_for("views.index"))

    return render_template("index.html", form=form, material_ids=material_ids_to_display)






@views.route("/datasim")
def datasim():
    materials = Material.query.all()

    return render_template("datasim.html", materials=materials)


@views.route("/populate-db", methods=["POST"])
def populate_database():
    Material.query.delete()
    populate_db()
    flash("Database succesful reset!", "success")
    return redirect(url_for("views.datasim"))

