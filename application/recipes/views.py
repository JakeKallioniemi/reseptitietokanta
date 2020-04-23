from flask import redirect, render_template, request, url_for, abort
from flask_login import login_required, current_user

from application import app, db
from application.recipes.models import Recipe, Tag
from application.reviews.models import Review
from application.recipes.forms import RecipeForm, SearchForm
from application.reviews.forms import ReviewForm

@app.route("/recipes/", methods=["GET"])
def recipes_index():
    form = SearchForm()
    form.min_rating.data = request.args.get("min_rating")

    if not form.validate():
        return redirect(url_for("recipes_index"))

    min_rating = form.min_rating.data
    recipes = None

    if not min_rating:
        recipes = Recipe.query.all()
    else:
        recipes = Recipe.filter_by_rating(min_rating)

    return render_template("recipes/list.html", recipes = recipes, form = SearchForm())

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
    recipe.tags = get_tags(form)

    db.session().add(recipe)
    db.session().commit()

    return redirect(url_for("recipes_index"))

@app.route("/recipes/<recipe_id>", methods=["GET"])
def recipe_view(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if not recipe:
        return redirect(url_for("recipes_index"))

    review = None
    if current_user.is_authenticated:
        review = Review.query.filter_by(account_id=current_user.id, recipe_id=recipe_id).first()

    form = ReviewForm()

    if review:
        form.rating.data = review.rating

    rating = Recipe.get_average_rating(recipe_id)

    return render_template("recipes/view.html", recipe = recipe, form = form, rating = rating)

@app.route("/recipes/<recipe_id>/edit", methods=["GET"])
@login_required
def recipe_edit_form(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if recipe.account_id != current_user.id: 
        abort(403)

    form = RecipeForm()
    form.name.data = recipe.name
    form.duration.data = recipe.duration
    form.instructions.data = recipe.instructions
    form.course.data = next(tag for tag in recipe.tags if tag.category == "course").name
    form.dairy_free.data = any(tag.name == "Dairy-Free" for tag in recipe.tags)
    form.gluten_free.data = any(tag.name == "Gluten-Free" for tag in recipe.tags)
    form.vegan.data = any(tag.name == "Vegan" for tag in recipe.tags)

    return render_template("recipes/edit.html", form = form, recipe_id = recipe_id)

@app.route("/recipes/<recipe_id>/edit", methods=["POST"])
@login_required
def recipe_edit(recipe_id):
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/edit.html", form = form, recipe_id = recipe_id)

    recipe = Recipe.query.get(recipe_id)

    if recipe.account_id != current_user.id: 
        abort(403)

    recipe.name = form.name.data
    recipe.duration = form.duration.data
    recipe.instructions = form.instructions.data
    recipe.tags = get_tags(form)

    db.session().add(recipe)
    db.session().commit()

    return redirect(url_for("recipe_view", recipe_id = recipe.id))

@app.route("/recipes/<recipe_id>/delete", methods=["POST"])
@login_required
def recipe_delete(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if recipe.account_id != current_user.id: 
        abort(403)

    db.session().delete(recipe)
    db.session().commit()

    return redirect(url_for("recipes_index"))

def get_tags(form):
    tag_names = []
    if form.dairy_free.data:
        tag_names.append("Dairy-Free")
    if form.gluten_free.data:
        tag_names.append("Gluten-Free")
    if form.vegan.data:
        tag_names.append("Vegan")
    tag_names.append(form.course.data)

    return Tag.query.filter(Tag.name.in_(tag_names)).all()
