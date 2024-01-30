
from website import creating_app
from flask import Flask, render_template


import os



# why is flask not accessible?  
# why is os not accessible? 
# why is render_template not accessible? 
#


# important point of contact inter files. 
applic = creating_app()    
 # Can we make more personilized names and not messe with 
 # the architecture of the code??   


# conditionals that update and reload. 
# only when I run this file directly, you can update the webserver. 


if __name__ == '__main__': 
 applic.run(debug=True)    # everytime I make a change. You run the server for me.
                           #    True result? 




##NOTE: We still have to use JINJA templates and HTML templates. 
#  This will make the webapp something that can work with buttons and lists. 
#  Templates need to be understood and used effectively.  
     #  Jinja is a template engine for Python. 
#  It allows us to create HTML pages that contain minimal display logic. 
#  Jinja allows us to create re-usable templates. 
#  Jinja is a web template engine for the Python programming language. 
#  It is licensed under a BSD License and is based on the Mako, 
#  and Django template languages.

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

# This line leads nowhere, need to figure out what this does and why is it here.
# from board.database import get_db

bp = Blueprint("posts", __name__)

@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form["author"] or "Anonymous"
        message = request.form["message"]

        if message:
            db = get_db()
            db.execute(
                "INSERT INTO post (author, message) VALUES (?, ?)",
                (author, message),
            )
            db.commit()
            flash(f"Thanks for posting, {author}!", category="success")
            return redirect(url_for("posts.posts"))
        else:
            flash("You need to post a message.", category="error")

    return render_template("posts/create.html")

# ...