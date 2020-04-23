from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
  
    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
    confirm = PasswordField("Confirm password", [
        validators.InputRequired(),
        validators.EqualTo("password", message="Passwords must match")
    ])
  
    class Meta:
        csrf = False