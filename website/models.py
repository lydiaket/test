from . import db # importing db obj from current package (website folder) 
from flask_login import UserMixin # helps log users in
from sqlalchemy.sql import func # don't need to specify date

# all notes need to look like this
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True) # id automatically added by db
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # current date/time
    # associating different info with different users:
    # setting up relationship between note obj and user obj
    
    
    # storing the id of the user who created this note 
    # foreign key- must pass valid id of an existing user to this column('one to many'- one user, many notes)
    # storing a foreign key on a child obj that refrences the parent obj
    # can figure out which user created each note by looking at the key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# setting up user model
# all users have to conform to below
class User(db.Model, UserMixin):
    # defining columns in table (schema/layout) 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # max length 150
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # tell flask/sql to add relationship b/w each note and user
    


