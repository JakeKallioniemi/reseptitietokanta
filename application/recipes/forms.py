from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DecimalField, BooleanField, SelectField, validators, ValidationError

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.InputRequired(), validators.Length(min=1, max=50)])
    duration = IntegerField("Time to make (in minutes)", [validators.InputRequired(), validators.NumberRange(min=1, max=10000)])
    instructions = TextAreaField("Instructions", [validators.InputRequired(), validators.Length(min=1, max=5000)])
    course = SelectField("Course", choices=[
        ('Appetizer', 'Appetizer'), ('Main course', 'Main course'), ('Dessert', 'Dessert'), 
        ('Snack', 'Snack'), ('Breakfast', 'Breakfast')
    ])
    dairy_free = BooleanField("Dairy-Free")
    gluten_free = BooleanField("Gluten-Free")
    vegan = BooleanField("Vegan")
 
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
    recipe_name = StringField("Name", [validators.Length(max=50)])
    tag_name = StringField("Tag", [validators.Length(max=50)])

    class Meta:
        csrf = False