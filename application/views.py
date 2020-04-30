from flask import render_template
from application import app

from application.recipes.models import Recipe

@app.route("/")
def index():
    count = Recipe.get_count()
    return render_template("index.html", count = count)
