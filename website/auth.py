from flask import Blueprint,render_template, request,flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from . import db
from .models import *
import folium
from requests import  get
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
DB_NAME = "flask"

auth = Blueprint('auth', __name__)

def selectapi(endpoint,nbr):
    api = get("https://jsonplaceholder.typicode.com/" + endpoint)
    data = api.json()
    vide = Users.query.all()
    if len(vide) == 0:
        if nbr > len(data):
            ecart = len(data)
        else:
            ecart = nbr
        for i in range(ecart):
            perso = Users(id = data[i].get("id"), name = data[i].get("name"), 
                          username = data[i].get("username"), email = data[i].get("email"), 
                          phone = data[i].get("phone"),
                          website = data[i].get("website"), street = data[i]["address"]["street"],
                          suite = data[i]["address"]["suite"], 
                          city = data[i]["address"]["city"],zipcode = data[i]["address"]["zipcode"],
                          lng = data[i]["address"]["geo"]["zipcode"], lat = data[i]["address"]["zipcode"],
                          name_company = data[i]["company"]["name"], catchPhrase = data[i]["company"]["catchPhrase"],
                          bs = data[i]["company"]["bs"])
            try:
                db.session.add(perso)
                db.session.commit()
            except:
                db.session.rollback()
                return "error"
    else:
        userOfId = Users.query.all()
        listOfId = {0}
        for i in range(len(userOfId)):
            listOfId.add(userOfId[i].id)
        nextStep = len(Users.query.all())
        if nbr  >  nextStep:
            if nextStep + nbr < len(data):
                endIndex = nextStep + nbr
            else:
                endIndex = len(data)
            for i in range(nextStep, endIndex):
                if data[i].get('id') not in listOfId:
                   perso = Users(id = data[i].get("id"), name = data[i].get("name"), 
                          username = data[i].get("username"), email = data[i].get("email"), 
                          phone = data[i].get("phone"),
                          website = data[i].get("website"), street = data[i]["address"]["street"],
                          suite = data[i]["address"]["suite"], 
                          city = data[i]["address"]["city"],zipcode = data[i]["address"]["zipcode"],
                          lng = data[i]["address"]["geo"]["zipcode"], lat = data[i]["address"]["zipcode"],
                          name_company = data[i]["company"]["name"], catchPhrase = data[i]["company"]["catchPhrase"],
                          bs = data[i]["company"]["bs"])
                try:
                    db.session.add(perso)
                    db.session.commit()
                except:
                    db.session.rollback()
                    return "error"
            
            

@auth.route('/posts', methods = ["GET","POST"])
def posts():
     if  request.method == "POST":
          id = request.form.get('id')
          title = request.form.get('title')
          body = request.form.get('body')   
                
          add_posts = Posts(title = title, body = body)
          db.session.add(add_posts)
          db.session.commit()
          flash("posts added ", category="success")

     return render_template('posts.html')

@auth.route("/albums", methods = ["GET","POST"])
def albums():
    if  request.method == "POST":
          title = request.form.get('title')
               
           
          add_album = Albums(title = title)
          db.session.add(add_album)
          db.session.commit()
          flash("album added ", category="success")
    return render_template("album.html")

@auth.route("/todos")
def todos():
    if  request.method == "POST":
          title = request.form.get('title')
          completed = request.form.get('completed')
          
               
           
          add_album = Todos(title = title, completed = completed)
          db.session.add(add_album)
          db.session.commit()
          flash("album added ", category="success")
          
    return render_template("album.html")



@auth.route("/infos", methods = ["GET"])
def infos():
    
   
    return render_template("infos.html")



@auth.route("/infousers", methods = ["GET"])
def infosusers():
    users = Users.query.all()
    start_coords = (14.7012975,-17.4671398)
    folium_map = folium.Map(
        location=start_coords, 
        zoom_start=17
    )
    folium_map.save('map.html')
    return render_template("infousers.html", users = users)
    
@auth.route('/map')
def map():
    return render_template('map.html')
@auth.route("/photos", methods = ["GET", "POST"])
def photos():
   
    return render_template("infos.html")



@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = Users.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("logged in succesfully", category="succes")
                login_user(user, remember = True)
                return redirect(url_for("posts.html"))
            else:
                flash("incorrect password try again", category = "error")

        else:
            flash("email does not exist.", category="error")

    return render_template("coonexion.html")

@auth.route("/newuser", methods = ["GET", "POST"])
def newuser():
   
    return render_template("newuser.html")


@auth.route("/load", methods = ["GET", "POST"])
def load():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
    users = Users.query.all()
    # for user in users:

    #     id  = user.id
    #     name = user.name
    #     username  = user.username
    #     email  = user.email
    #     phone  = user.phone
    #     website  = user.phone
    #     selectapi('users',nombre)
   
    return render_template("load.html", users = users)



