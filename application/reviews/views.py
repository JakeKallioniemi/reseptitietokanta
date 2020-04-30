from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.reviews.models import Review
from application.reviews.forms import ReviewForm

@app.route("/recipes/<recipe_id>/review", methods=["POST"])
@login_required
def review_create(recipe_id):
    form = ReviewForm(request.form)

    if not form.validate():
        return redirect(url_for("recipe_view", recipe_id=recipe_id))

    review = Review.query.filter_by(account_id=current_user.id, recipe_id=recipe_id).first()
    if not review:
        review = Review(form.rating.data)
        review.recipe_id = recipe_id
        review.account_id = current_user.id
        db.session().add(review)
        db.session().commit()
    else:
        review.rating = form.rating.data
        db.session().commit()

    return redirect(url_for("recipe_view", recipe_id=recipe_id))

@app.route("/recipes/<recipe_id>/review/delete", methods=["POST"])
@login_required
def review_delete(recipe_id):
    Review.query.filter_by(account_id=current_user.id, recipe_id=recipe_id).delete()
    db.session().commit()

    return redirect(url_for("recipe_view", recipe_id=recipe_id))