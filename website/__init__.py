# mingo
# what can you help with here? 
# 1.  I need to understand the structure of the files.
# This function is responsible for creating and configuring the Flask application.

# remember: the file organization system is still not aceptable. 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
## comunicartions to Operating System  'from os'
# We need the the path module to verify if the path to our app already exists. 
from os import path
 ### register other files here#####

 

# Naming the data base, and what to do is a fundamental part of this.
########################################################################################################
########## DEFINE Data Base.  ###The users will tranfer informartion into this list. ########
########################################################################################################
db = SQLAlchemy()
DB_NAME = "database.db"
  
# here i will put flask work, dependencies  


 





# Func taking input from various files which are writen in Html, js, bootstrap, jinga

def creating_app(): 
    applic = Flask(__name__)   # __name__    ?  # note: d you have flask in your machine? 
    applic.config['SECRET_KEY'] = 'pneumonoultramicroscopicsilicovolcanoconiosis'
    applic.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  ## the 'f' makes it possible to write python inside squigly brackets. 
    db.init_app(applic)

    ### register other files here#####
    from .views import views
    from .auth  import auth
 
    ### import the rest of the files: authentification, and so on. 

    # How to access the URL's we have in our system?   
    applic.register_blueprint(views, url_prefix= '/')
    applic.register_blueprint(auth, url_prefix= '/')
    # applic.register_blueprint(another file... or var, url_prefix= '/authentification ')
    # applic.register_blueprint(another file... or var, url_prefix= '/ page_2')   
    # we are doing no prefix just forward slash.

    from .models import User, Note 

    with applic.app_context():
            create_database()

    return applic

    return applic


def create_database():
  if not path.exists('website/' + DB_NAME):  ## if it does not exist 
      db.create_all()              ##  create the db for this application. 
      print(" the data base is done.")