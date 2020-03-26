from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, validators

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.InputRequired()])
    duration = IntegerField("Time to make", [validators.InputRequired()])
    instructions = TextAreaField("Instructions", [validators.InputRequired()])
 
    class Meta:
        csrf = False