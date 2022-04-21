from flask import Blueprint,render_template, request,flash, redirect, url_for


auth = Blueprint('auth', __name__)


@auth.route('/posts')
def posts():
    
    return render_template("multicolor.html")

@auth.route("/albums")
def albums():
   
    return render_template("triplepost.html")

@auth.route("/todos")
def todos():
   
    return  render_template("post_title.html")

@auth.route("/infos")
def infos():
   
    return render_template("infos.html")
