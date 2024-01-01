
###############################################################################################################################################################
##########here will be the model for our data base .
####   a. User info.
####   b. Note taking capabilities. 
####
################################################################################################################################################################
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func




#### Note taking class and makes ########################################################
class Note(db.Model):
  id =     db.Column(db.Integer, primary_key=True)
  data =   db.Column(db.String(10000))

  date =   db.Column(db.DateTime(timezone=True), default=func.now())
  ## this idea  of Foreign Key is essential/.   
  user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 



### User classes that takes id, email, and password.##############################################################################################

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)

    password = db.Column(db.String(200))
    first_name = db.Column(db.String(200))

    SNotes = db.relationship('Note')

