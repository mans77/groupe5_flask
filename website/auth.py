from crypt import methods
from unicodedata import category
from flask import Blueprint,render_template, request,flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import  login_user, login_required,logout_user, current_user
# from . import db
from .models import *
from .models import db
import folium
from requests import  get
from werkzeug.security import generate_password_hash, check_password_hash
db.init_app(app)

app.config['SECRET_KEY'] = "groupe5"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:groupe5@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# db = SQLAlchemy()

auth = Blueprint('auth', __name__)

def selectposts(end, nbr):
    vide = Posts.query.all()
    api = get("https://jsonplaceholder.typicode.com/" + end)
    data = api.json()
    if len(vide) == 0:
        if nbr > len(data):
            ecart = len(data)
        else:
            ecart = nbr
                
        for i in range(ecart):
            posts = Posts(title = data[i].get("title"),
            body = data[i].get("body"),
            userId = data[i].get("userId"))
        
            try:
                db.session.add(posts)
                db.session.commit()
            except:
                db.session.rollback()
                return "error"
    else:
        id_user = Posts.query.all()
        id_list = {0}
        for i in range(len(id_user)):
           id_list.add(id_user[i].id)
        nextStep = len(Posts.query.all())
        if nbr  >  nextStep:
            if nextStep + nbr < len(data):
                endIndex = nextStep + nbr
            else:
                endIndex = len(data)
            for i in range(nextStep, endIndex):
                if data[i].get('id') not in id_list:
                    posts = Posts(title = data[i].get("title"),
                    body = data[i].get("body"),
                    userId = data[i].get("userId"))
                try:
                    db.session.add(posts)
                    db.session.commit()
                except:
                    db.session.rollback()
                    return "error"





def selectalbums(end, nbr):
    vide = Albums.query.all()
    api = get("https://jsonplaceholder.typicode.com/" + end)
    data = api.json()
    if len(vide) == 0:
        if nbr > len(data):
            ecart = len(data)
        else:
            ecart = nbr
            
        for i in range(ecart):
            albums = Albums(title = data[i].get("title"),
            userId = data[i].get("userId"))
            try:
                db.session.add(albums)
                db.session.commit()
            except:
                db.session.rollback()
                return "error"
    else:
        id_user = Albums.query.all()
        id_list = {0}
        for i in range(len(id_user)):
           id_list.add(id_user[i].id)
        nextStep = len(Albums.query.all())
        if nbr  >  nextStep:
            if nextStep + nbr < len(data):
                endIndex = nextStep + nbr
            else:
                endIndex = len(data)
            for i in range(nextStep, endIndex):
                if data[i].get('id') not in id_list:
                     albums = Albums(title = data[i].get("title"),
                     userId = data[i].get("userId"))
                try:
                    db.session.add(albums)
                    db.session.commit()
                except:
                    db.session.rollback()
                    return "error"




def selectphotos(end, nbr):
    vide = Photos.query.all()
    api = get("https://jsonplaceholder.typicode.com/" + end)
    data = api.json()
    if len(vide) == 0:
        if nbr > len(data):
            ecart = len(data)
        else:
            ecart = nbr
            
        for i in range(ecart):
            photos = Photos(albumId = data[i].get("albumId"), title = data[i].get("title"),
            url = data[i].get("url"),thumbnailUrl = data[i].get("thumbnailUrl"))
            try:
                db.session.add(photos)
                db.session.commit()
            except:
                db.session.rollback()
                return "error"
    else:
        id_user = Photos.query.all()
        id_list = {0}
        for i in range(len(id_user)):
           id_list.add(id_user[i].id)
        nextStep = len(Photos.query.all())
        if nbr  >  nextStep:
            if nextStep + nbr < len(data):
                endIndex = nextStep + nbr
            else:
                endIndex = len(data)
            for i in range(nextStep, endIndex):
                if data[i].get('id') not in id_list:
                     photos = Photos(albumId = data[i].get("albumId"), title = data[i].get("title"),
                     url = data[i].get("url"),thumbnailUrl = data[i].get("thumbnailUrl"))
                try:
                    db.session.add(photos)
                    db.session.commit()
                except:
                    db.session.rollback()
                    return "error"





def selectcomments(end, nbr):
    vide = Comments.query.all()
    api = get("https://jsonplaceholder.typicode.com/" + end)
    data = api.json()
    if len(vide) == 0:
        if nbr > len(data):
            ecart = len(data)
        else:
            ecart = nbr
            
        for i in range(ecart):
            comments = Comments(postId = data[i].get("postId"), name = data[i].get("name"),
            email = data[i].get("name"), body = data[i].get("body"))
            try:
                db.session.add(comments)
                db.session.commit()
            except:
                db.session.rollback()
                return "error"
    else:
        id_user = Comments.query.all()
        id_list = {0}
        for i in range(len(id_user)):
           id_list.add(id_user[i].id)
        nextStep = len(Comments.query.all())
        if nbr  >  nextStep:
            if nextStep + nbr < len(data):
                endIndex = nextStep + nbr
            else:
                endIndex = len(data)
            for i in range(nextStep, endIndex):
                if data[i].get('id') not in id_list:
                    comments = Comments(postId = data[i].get("postId"), name = data[i].get("name"),
                    email = data[i].get("name"), body = data[i].get("body"))
                try:
                    db.session.add(comments)
                    db.session.commit()
                except:
                    db.session.rollback()
                    return "error"




def selectodos(end, nbr):
    vide = Todos.query.all()
    api = get("https://jsonplaceholder.typicode.com/" + end)
    data = api.json()
    if len(vide) == 0:
        if nbr > len(data):
            ecart = len(data)
        else:
            ecart = nbr
            
        for i in range(ecart):
            todos = Todos(userId = data[i].get("userId"), title = data[i].get("title"),
            completed = data[i].get("completed"))
            try:
                db.session.add(todos)
                db.session.commit()
            except:
                db.session.rollback()
                return "error"
    else:
        id_user = Todos.query.all()
        id_list = {0}
        for i in range(len(id_user)):
           id_list.add(id_user[i].id)
        nextStep = len(Todos.query.all())
        if nbr  >  nextStep:
            if nextStep + nbr < len(data):
                endIndex = nextStep + nbr
            else:
                endIndex = len(data)
            for i in range(nextStep, endIndex):
                if data[i].get('id') not in id_list:
                     todos = Todos(userId = data[i].get("userId"), title = data[i].get("title"),
                     completed = data[i].get("completed"))
                try:
                    db.session.add(todos)
                    db.session.commit()
                except:
                    db.session.rollback()
                    return "error"





def selectapi(endpoint,nbr):
    vide = Users.query.all()
    api = get("https://jsonplaceholder.typicode.com/" + endpoint)
    data = api.json()
    password = "groupe5"
    if len(vide) == 0:
        if nbr > len(data):
            ecart = len(data)
        else:
            ecart = nbr
            
        for i in range(ecart):
            perso = Users(name = data[i].get("name"), 
                          username = data[i].get("username"), email = data[i].get("email"), password = password,
                          phone = data[i].get("phone"),
                          website = data[i].get("website"), street = data[i]["address"]["street"],
                          suite = data[i]["address"]["suite"], 
                          city = data[i]["address"]["city"],zipcode = data[i]["address"]["zipcode"],
                          lng = data[i]["address"]["geo"]["lat"], lat = data[i]["address"]["geo"]["lat"],
                          name_company = data[i]["company"]["name"], catchPrase = data[i]["company"]["catchPhrase"],
                          bs = data[i]["company"]["bs"])
            try:
                db.session.add(perso)
                db.session.commit()
            except:
                db.session.rollback()
                return "error"
    else:
        id_user = Users.query.all()
        id_list = {0}
        for i in range(len(id_user)):
           id_list.add(id_user[i].id)
        nextStep = len(Users.query.all())
        if nbr  >  nextStep:
            if nextStep + nbr < len(data):
                endIndex = nextStep + nbr
            else:
                endIndex = len(data)
            for i in range(nextStep, endIndex):
                if data[i].get('id') not in id_list:
                   perso = Users(name = data[i].get("name"), 
                          username = data[i].get("username"), email = data[i].get("email"), password = password,
                          phone = data[i].get("phone"),
                          website = data[i].get("website"), street = data[i]["address"]["street"],
                          suite = data[i]["address"]["suite"], 
                          city = data[i]["address"]["city"],zipcode = data[i]["address"]["zipcode"],
                          lng = data[i]["address"]["geo"]["lng"], lat = data[i]["address"]["geo"]["lat"],
                          name_company = data[i]["company"]["name"], catchPrase = data[i]["company"]["catchPhrase"],
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
          title = request.form.get('title')
          body = request.form.get('body')   
                
          add_posts = Posts(title = title, body = body)
          db.session.add(add_posts)
          db.session.commit()
          flash("posts added ", category="success")

          nbpost= request.form.get('nbpost')
          return redirect(url_for("auth.loadpost", nbpost = nbpost))

     return render_template('posts.html')





@auth.route("/albums", methods = ["GET","POST"])
def albums():
    if  request.method == "POST":
          title = request.form.get('title')
          add_album = Albums(title = title)
          db.session.add(add_album)
          db.session.commit()
          flash("album added ", category="success")
          nbralbum = request.form.get("nbralbum")  
          return redirect(url_for("auth.loadalbum",  nbralbum = nbralbum))
    return render_template("albums.html")






@auth.route("/todos")
def todos():


    if  request.method == "POST":
          title = request.form.get('title')
          completed = request.form.get('completed')
          
               
           
          add_album = Todos(title = title, completed = completed)
          db.session.add(add_album)
          db.session.commit()
          flash("added ", category="success")
          

    return render_template("todos.html")




@auth.route("/infos", methods = ["GET","POST"])
def infos():
      
    return redirect(url_for("auth.infousers"))




def maper(lng, lat):
    start_coords = (lat, lng)
    folium_map = folium.Map(
        location=start_coords, 
        zoom_start=17
    )
    folium.Marker(start_coords,
            popup='Some Other Location',
            icon=folium.Icon(color='red',icon='info-sign')
            ).add_to(folium_map)
    folium_map
    
    folium_map.save('website/templates/map.html')



    
@auth.route("/infousers", methods = ["GET"])
def infousers():
    if 'email' in session:
       users = Users.query.filter_by(email=session['email'])
       for user in users:
           maper(user.lat, user.lng)
           
    return render_template("infousers.html", users = users)
    




@auth.route('/map')
def map():
    return render_template('map.html')





@auth.route("/photos", methods = ["GET", "POST"])
def photos():
    init = 0
    nbr = 6
    selectphotos("photos", nbr)
    photos = Photos.query.all()[init:nbr]
   
    return render_template("infos.html", photos = photos)



@auth.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = Users.query.filter_by(email = email).first()
        # print(email)
        
        if user.email == email: 
            session['email'] = email
            # print(email)
            flash("logged in succesfully", category="succes")
        return redirect(url_for("auth.posts"))
    return render_template("coonexion.html")





@auth.route("/newuser", methods = ["GET", "POST"])
def newuser():
    if  request.method == "POST":
          print('this action occured ')
          #   id = request.form.get('id')
          name  = request.form.get('name')
          username = request.form.get('Username')
          email = request.form.get('email')
          password = request.form.get('password')
          phone = request.form.get('phone')
          website = request.form.get('website')
          street = request.form.get('street')
          suite = request.form.get('suite')
          city = request.form.get('city')
          zipcode = request.form.get('zipcode')
          lng = request.form.get('lng')
          lat = request.form.get('lat')
          name_company = request.form.get('compname')
          catchPhrase = request.form.get('catchPhrase')
          bs = request.form.get('bs')

         
          user_add = Users(name = name, username = username, email = email, 
                           password = password,
                           phone = phone, website = website, street = street,
                           suite = suite, city = city, zipcode = zipcode, 
                           lng = lng, lat = lat, name_company = name_company,
                           catchPrase = catchPhrase, bs = bs)
          
          print(user_add)
          db.session.add(user_add)
          
          try:
             db.session.commit()
          except:
             db.session.rollback()
             flash("added ", category="success")
    return render_template("newuser.html")




@auth.route("/load", methods = ["POST","GET"])
def load():
    nnr = 0
    nbr = request.args.get("nbr")
    selectapi("users", int(nbr))
    users = Users.query.all()[nnr:int(nbr)]
    
    # for user in users:

    #     id  = user.id
    #     name = user.name
    #     username  = user.username
    #     email  = user.email
    #     phone  = user.phone
    #     website  = user.phone
    #     selectapi('users',nombre)
   
    return render_template("load.html", users=users)




@auth.route('/loadpost', methods = ["GET","POST"])
def loadpost():
    init = 0
    nbpost = request.args.get("nbpost")
    selectposts("posts", int(nbpost))
    posts = Posts.query.all()[init:int(nbpost)]
    print(posts)
    return render_template("loadpost.html", posts = posts)




@auth.route('/newpost', methods=["GET", "POST"])
def newpost():
    if  request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        post_add = Posts(title = title, body = body)
        db.session.add(post_add)
          
        try:
            db.session.commit()
        except:
            db.session.rollback()
            flash("added ", category="success")
    return render_template("newpost.html")




@auth.route('/newtodos')
def newtodos():
    
    return render_template("triplepost.html")




@auth.route('/addtodos', methods = ["GET","POST"])
def addtodos():
    title = request.form.get("title")
    completed = request.form.get("completed")
    add_todos = Todos(title = title, completed = completed)
    db.session.add(add_todos)  
    try:
        db.session.commit()
    except:
        db.session.rollback()
        flash("added ", category="success")
    
    return render_template("add_todos.html")


@auth.route('/addalbum', methods=["GET","POST"])
def addalbum():
    if  request.method == "POST":
        title = request.form.get("title")
        userid = request.form.get("userid")
        add_album = Albums(title = title, userId = userid)
        db.session.add(add_album)
          
        try:
            db.session.commit()
        except:
            db.session.rollback()
            flash("added ", category="success")
    
    return render_template("newalbum.html")

@auth.route('/loadalbum')
def loadalbum():
    init = 0
    nbr = request.args.get("nbralbum")
    print(nbr)
    selectalbums("albums", int(nbr))
    albums = Albums.query.all()[init:int(nbr)]

    return render_template("multicolor.html", albums = albums)



