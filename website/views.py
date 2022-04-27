from flask import Blueprint, render_template, request,flash
from .models import Users

views = Blueprint("views", __name__)

@views.route("/", methods=["GET","POST"])
def home():
     
     if  request.method == "POST":
          id = request.form.get('id')
          name  = request.form.get('name')
          username = request.form.get('Username')
          email = request.form.get('email')
          phone = request.form.get('phone')
          website = request.form.get('website')
          street = request.form.get('street')
          suite = request.form.get('suite')
          city = request.form.get('city')
          zipcode = request.form.get('zipcode')
          lng = request.form.get('lng')
          lat = request.form.get('lat')
          name_company = request.form.get('compname')
          catchPrase = request.form.get('catchPhrase')
          bs = request.form.get('bs')

         
          user_add = Users(name = name, username = username, email = email, 
                           phone = phone, website = website, street = street,
                           suite = suite, city = city, zipcode = zipcode, 
                           lng = lng, lat = lat, name_company = name_company,
                           catchPhrase = catchPhrase, bs = bs)
          db.session.add(user_add)
          db.session.commit()
          flash("Note added ", category="success")

     return render_template('home.html')



