from sqlalchemy import ForeignKey
from sqlalchemy. orm import relationship
from calendar import week
from operator import index
from mijnproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# De user_loader decorator zorgt voor de flask-login voor de huidige gebruiker
# en haalt zijn/haar id op.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    # Maak een tabel aan in de database
    __tablename__ = 'Gasten'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Type(db.Model):
    __tablename__ = 'Types'

    id = db.Column(db.Integer, primary_key=True)
    a_personen = db.Column(db.Integer)
    weekprijs = db.Column(db.Integer)

    def __init__(self, id, a_personen, weekprijs):
        self.id = id
        self.a_personen = a_personen
        self.weekprijs = weekprijs

class Bungalow(db.Model):
    __tablename__ = 'Bungalows'

    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(64), unique=True, index=True)
    type = db.Column(db.String(64), ForeignKey(Type.id))

    def __init__(self, id, naam, type):
        self.id = id
        self.naam = naam
        self.type = type 

class Boeking(db.Model):
    __tablename__ = 'Boekingen'

    id = db.Column(db.Integer, primary_key=True)
    gast = db.Column(db.Integer, ForeignKey(User.id))
    bungalow = db.Column(db.Integer, ForeignKey(Bungalow.id))
    weeknummer = db.Column(db.Integer)
    prijs = db.Column(db.Integer)

    def __init__(self, id, gast, bungalow, weeknummer, prijs):
        self.id = id
        self.gast = gast
        self.bungalow = bungalow
        self.weeknummer = weeknummer
        self.prijs = prijs

db.create_all()
