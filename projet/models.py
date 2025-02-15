from datetime import datetime
from projet import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Définition de la classe Cuisine en premier
class Cuisine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    icon = db.Column(db.String(20), nullable=False, default="default.jpg")
    recettes = db.relationship('recette', backref='cuisine', lazy=True)  # Change backref ici pour 'cuisine'
    
    def __repr__(self):
        return f"Cuisine('{self.title}','{self.icon}','{self.description}')"

# Définition de la classe User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(125), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    recettes = db.relationship('recette', backref='author', lazy=True)  # Backref pour User avec 'author'

    def __repr__(self):
        return f"User('{self.fname}','{self.lname}','{self.username}', '{self.email}', '{self.image_file}')"

# Définition de la classe Recette
class recette(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    thumbnail = db.Column(db.String(20), nullable=False, default="default.jpg")
    slug = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Relier Recette à User
    Cuisine_id = db.Column(db.Integer, db.ForeignKey('cuisine.id'), nullable=False)  # Relier Recette à Cuisine

    def __repr__(self):
            return f"recette('{self.title}','{self.date_posted}','{self.thumbnail}')"
