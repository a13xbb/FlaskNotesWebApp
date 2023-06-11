from . import db # type: ignore
from flask_login import UserMixin # type: ignore
from sqlalchemy.sql import func # type: ignore

class User(db.Model, UserMixin): # type: ignore
    id = db.Column(db.Integer, primary_key=True) # type: ignore
    email = db.Column(db.String(150), unique=True) # type: ignore
    password = db.Column(db.String(150)) # type: ignore
    first_name = db.Column(db.String(150)) # type: ignore
    notes = db.relationship('Note') # type: ignore
    
class Note(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True) # type: ignore
    data = db.Column(db.String(10000)) # type: ignore
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # type: ignore
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # type: ignore
