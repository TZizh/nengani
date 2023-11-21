from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import qrcode


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30))
    price = db.Column(db.Integer())
    img_src = db.Column(db.String(length=2000))
    description = db.Column(db.String(length=100))
    bag_id = db.Column(db.Integer, db.ForeignKey('bag.id'))

    def __repr__(self):
        return f'Item {self.name}'

class Bag(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String(length=6))
    max_num_items = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    items = db.relationship('Item', backref='owned_user', lazy=True)

    def __repr__(self):
        return f'Item {self.name}'



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    bags = db.relationship('Bag', backref='owned_user', lazy=True)
#    budget = db.Column(db.Integer(), nullable=False, default=120)

