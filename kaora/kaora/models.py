from datetime import datetime
from kaora import db


class User(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    birthday = db.Column(db.DateTime)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    address = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    collection = db.Column(db.String(20), unique=True, nullable=False)
    category = db.Column(db.String(20), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    is_available = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.String(10), default=datetime.utcnow)
    product_img = db.Column(default='default.jpg')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"
