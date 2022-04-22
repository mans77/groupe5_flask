from flask import Blueprint,render_template, request,flash, redirect, url_for


auth = Blueprint('auth', __name__)


@auth.route('/posts')
def posts():
    
    return render_template("posts.html")

@auth.route("/albums")
def albums():
   
    return render_template("albums.html")

@auth.route("/todos")
def todos():
   
    return  render_template("todos.html")

@auth.route("/infos")
def infos():
   
    return render_template("infos.html")
