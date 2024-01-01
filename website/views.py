#    This is going to be a central of the routes 
#      Html
#      JS 
#      Json
# The architect blueprint 



# get a library flask and blurprint, and rendereing html templates #############

from flask import Blueprint, render_template
################################################################################
################################################################################
################################################################################

 # variable that will hold a lot of info to be across files. Calling it "views" for now. 
#views var will get info blueprint func which takes 2 arguments, var views and "__name__" not cleat yet. 
views  =   Blueprint( 'views', __name__)




###############################################################################################################################################################
########## DEFINE ROUTE. DEFINE ROUTE ### which movment from screen to another in the app. ########
################################################################################################################################################################

# @name of variable dot route parenthisis '/'    ::: this has to do URL control on the web. 

@views.route('/')
def home(): 
          # Let's get some html flowing.
 
     return render_template("home.html")  #template_render( " html file")  

#  this is on SCREEN:    How do you feel this morning?

#  last step is to register with __init.py__ (file name)#############################################



# this code will be the start of many files necessary I.E: authentification file, and others with small modifications. 


