from app import db

class LifeGoals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    text = db.Column(db.String(120))
    status = db.Column(db.Boolean )
    end_date = db.Column(db.DateTime)

    def __init__(self, title, text, status, end_date):
        self.title = title
        self.text = text
        self.status = status
        self.end_date = end_date

    def __repr__(self):
        return '<User %r>' % (self.title)
