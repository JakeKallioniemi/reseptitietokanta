from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired(), validators.Length(max=50)])
    password = PasswordField("Password", [validators.InputRequired(), validators.Length(max=144)])
  
    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired(), validators.Length(min=2, max=50)])
    password = PasswordField("Password", [validators.InputRequired(), validators.Length(min=6, max=144)])
    confirm = PasswordField("Confirm password", [
        validators.InputRequired(),
        validators.EqualTo("password", message="Passwords must match")
    ])
  
    class Meta:
        csrf = False