from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db
from application.auth.models import User
from application.recipes.models import Recipe
from application.auth.forms import LoginForm, SignupForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))  

@app.route("/auth/signup", methods = ["GET", "POST"])
def auth_signup():
    if request.method == "GET":
        return render_template("auth/signupform.html", form = SignupForm())

    form = SignupForm(request.form)

    if not form.validate():
        return render_template("auth/signupform.html", form = form)

    username = form.username.data
    password = form.password.data

    user = User.query.filter_by(username=username).first()

    if user:
        return render_template("auth/signupform.html", form = form,
                            error = "Username already taken")

    user = User(username, password)

    db.session().add(user)
    db.session().commit()

    login_user(user)
    return redirect(url_for("index"))

@app.route("/profile", methods = ["GET"])
@login_required
def profile():
    username = User.query.get(current_user.id).username
    avg_rating = Recipe.get_avg_rating_of_users_recipes(current_user.id)
    return render_template("auth/profile.html", username = username, avg_rating = avg_rating)
