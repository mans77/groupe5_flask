from flask import Blueprint, render_template, request,flash, redirect, url_for
from .models import Users
from  .auth import selectapi

views = Blueprint("views", __name__)


    
    

@views.route("/", methods=["GET","POST"])
def home():
    
     if request.method == "POST":
          nbr = request.form.get("nbre")  
          selectapi("users", int(nbr))
          #users = Users.query.all()[nnr:int(nbr)]
          #print(users)
          return redirect(url_for('auth.load', nbr=nbr))
          
     return render_template('home.html')



