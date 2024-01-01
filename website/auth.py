from flask import Blueprint, render_template, request, flash, redirect, url_for 
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
#import Modes, user, generate hash, database

 # variable that will hold a lot of info to be across files. Calling it "views" for now. 
    #views var will get info blueprint func which takes 2 arguments, var views and "__name__" not cleat yet. 
auth  =   Blueprint( 'auth', __name__)




###############################################################################################################################################################
########## DEFINE ROUTE. DEFINE ROUTE
#  ### which movment from screen to another in the app. ########
################################################################################################################################################################

# @name of variable dot route parenthisis '/'    ::: this has to do URL control on the web. 
# GET and POST requests are communication with the server. 
@auth.route('/login', methods=['GET', 'POST'])
def login(): 
      data = request.form
      # want to see the data from get and post on my VScode terminal
      print(data)
      # send, or return some text of HTML  # template_render()  
      return render_template("login.html", boolen=True)

@auth.route('/logout')
def logout(): 

    # send, or return some text of HTML
      return render_template("login.html")

@auth.route('/sign_up', methods=['GET', 'POST'])  # NOTE:: should be " join the family, not sign up. "
def sign_up(): 
      # if request method is 
      if request.method == 'POST': 
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('Password1')     
        password2 = request.form.get('Password2')

        #limitations for the user 
        if len(email) < 5: 
            flash('Your email must be bigger than 5 characters', category='error')
            
        elif len(first_name) < 3: 
            flash('Your First Name must be bigger than 3 characters', category='error')
   
        elif password1 != password2: 
            flash('Your Passwords don\'t match', category='error')

        elif len(password1) < 7: 
            flash('Password is too short', category='error')
        else: 
            flash('Account Created!', category='success')
                # add user information to database
            flash('Account Created. Welcome to Mingo', category='success')
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            ### to add a new element to the data base, 
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')
            return redirect(url_for('views.home'))    
        

                 # send, or return some text of HTML
      return render_template("sign_up.html")  # template_render()  will let eme render all kind of HTML mechanisms. 


# NOTE: Add elements on website here. 
#       any contact or a door to a page can be implemented using route. 
#@auth.route('/login')
#def home(): 

