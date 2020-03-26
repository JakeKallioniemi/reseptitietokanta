from application import db

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
        