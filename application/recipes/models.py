from application import db
from sqlalchemy.sql import text

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                            nullable=False)

    def __init__(self, name, duration, instructions):
        self.name = name
        self.duration = duration
        self.instructions = instructions
        
    
    @staticmethod
    def get_average_rating(recipe_id):
        stmt = text("select round(avg(rating), 1) from review where recipe_id = :recipe_id").params(recipe_id=recipe_id)
        res = db.engine.execute(stmt)
        return res.first()[0]