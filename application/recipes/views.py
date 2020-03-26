from application import app, db
from flask import redirect, render_template, request, url_for
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm

@app.route("/recipes/", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.all())

@app.route("/recipes/new/")
def recipes_form():
    return render_template("recipes/new.html", form = RecipeForm())

@app.route("/recipes/", methods=["POST"])
def recipes_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form = form)

    name = form.name.data
    duration = form.duration.data
    instructions = form.instructions.data
    recipe = Recipe(name, duration, instructions)

    db.session().add(recipe)
    db.session().commit()

    return redirect(url_for("recipes_index"))
