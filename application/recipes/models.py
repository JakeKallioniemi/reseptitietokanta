from application import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    instructions = db.Column(db.String, nullable=False)

    def __init__(self, name, duration, instructions):
        self.name = name
        self.duration = duration
        self.instructions = instructions
        