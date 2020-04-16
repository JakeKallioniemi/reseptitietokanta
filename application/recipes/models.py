from application import db
from sqlalchemy.sql import text

recipe_tag = db.Table('recipe_tag', 
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                            nullable=False)
    tags = db.relationship('Tag', secondary=recipe_tag)

    def __init__(self, name, duration, instructions):
        self.name = name
        self.duration = duration
        self.instructions = instructions
        
    
    @staticmethod
    def get_average_rating(recipe_id):
        stmt = text("SELECT ROUND(AVG(rating), 1) FROM Review"
                    " WHERE recipe_id = :recipe_id").params(recipe_id=recipe_id)
        res = db.engine.execute(stmt)
        return res.first()[0]

    @staticmethod
    def filter_by_rating(rating):
        stmt = text("SELECT Recipe.id, Recipe.name, Recipe.duration FROM Recipe "
                    " LEFT JOIN Review ON Review.recipe_id = Recipe.id"
                    " GROUP BY Recipe.id"
                    " HAVING AVG(Review.rating) >= :rating").params(rating=float(rating))
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "duration":row[2]})
        return response