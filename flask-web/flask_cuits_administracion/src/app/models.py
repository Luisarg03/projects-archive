from datetime import datetime
from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    user = db.Column(db.String(50), unique=False, nullable=False)
    name2 = db.Column(db.String(50), unique=False, nullable=False)

    email = db.Column(db.String(90), unique=True, nullable=False)

    cuit = db.Column(db.String(93), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now())

    def __str__(self):
        return str(self.id)

    @classmethod
    def create_element(cls, user, name2, email, cuit):
        username = User(user=user, name2=name2, email=email, cuit=cuit)

        db.session.add(username)
        db.session.commit()

        return username


    @classmethod
    def get_user(cls, user):
        return User.query.filter_by(user=user).first()
    
    @classmethod
    def get_user_name2(cls, name2):
        return User.query.filter_by(name2=name2).first()

    @classmethod
    def get_email(cls, email):
        return User.query.filter_by(email=email).first()
    
    @classmethod
    def get_cuit(cls, cuit):
        return User.query.filter_by(cuit=cuit).first()

    @classmethod
    def get_by_id(cls, id):
        return User.query.filter_by(id=id).first()