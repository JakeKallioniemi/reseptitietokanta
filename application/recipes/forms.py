from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DecimalField, validators, ValidationError

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.InputRequired()])
    duration = IntegerField("Time to make (in minutes)", [validators.InputRequired()])
    instructions = TextAreaField("Instructions", [validators.InputRequired()])
 
    class Meta:
        csrf = False

def validate_rating(form, field):
    if field.data:
        try:
            float(field.data)
        except ValueError:
            raise ValidationError("rating must be a number")

class SearchForm(FlaskForm):
    min_rating = DecimalField("Rating", [validate_rating])

    class Meta:
        csrf = False