from flask_wtf import FlaskForm
from wtforms import IntegerField, validators

class ReviewForm(FlaskForm):
    rating = IntegerField("Rating (1-5)", [validators.NumberRange(1, 5)])
 
    class Meta:
        csrf = False