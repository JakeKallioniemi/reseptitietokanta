from application import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'),
                            nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                            nullable=False)

    def __init__(self, rating):
        self.rating = rating
        