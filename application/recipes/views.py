from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm

@app.route("/recipes/", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.all())

@app.route("/recipes/new/")
@login_required
def recipes_form():
    return render_template("recipes/new.html", form = RecipeForm())

@app.route("/recipes/", methods=["POST"])
@login_required
def recipes_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form = form)

    name = form.name.data
    duration = form.duration.data
    instructions = form.instructions.data
    recipe = Recipe(name, duration, instructions)
    recipe.account_id = current_user.id

    db.session().add(recipe)
    db.session().commit()

    return redirect(url_for("recipes_index"))

@app.route("/recipes/<recipe_id>", methods=["GET"])
def recipe_view(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if not recipe:
        return redirect(url_for("recipes_index"))

    return render_template("recipes/view.html", recipe = recipe)

@app.route("/recipes/<recipe_id>/edit", methods=["GET"])
@login_required
def recipe_edit_form(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    form = RecipeForm()
    form.name.data = recipe.name
    form.duration.data = recipe.duration
    form.instructions.data = recipe.instructions

    return render_template("recipes/edit.html", form = form, recipe_id = recipe.id)

@app.route("/recipes/<recipe_id>/edit", methods=["POST"])
@login_required
def recipe_edit(recipe_id):
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/edit.html", form = form)

    recipe = Recipe.query.get(recipe_id)
    recipe.name = form.name.data
    recipe.duration = form.duration.data
    recipe.instructions = form.instructions.data

    db.session().add(recipe)
    db.session().commit()

    return redirect(url_for("recipe_view", recipe_id = recipe.id))

@app.route("/recipes/<recipe_id>/delete", methods=["POST"])
@login_required
def recipe_delete(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    db.session().delete(recipe)
    db.session().commit()

    return redirect(url_for("recipes_index"))