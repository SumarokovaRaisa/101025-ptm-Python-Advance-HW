from app.extensions import db


class Question(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    responses = db.relationship('Response', backref='question', lazy=True)

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=True)

    def __repr__(self):
        return f'Question: {self.text}'

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    questions = db.relationship("Question", backref="category", lazy=True)


    def __repr__(self):
        return f'Category: {self.name}'


class Statistic(db.Model):
    __tablename__ = 'statistic'

    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    agree_count = db.Column(db.Integer, nullable=False, default=0)
    disagree_count = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return ('<Statistic for Question %r: %r agree, %r disagree>' %
                (self.question_id, self.agree_count,
                self.disagree_count))