from flask import Blueprint, render_template, request,flash
from .models import Users

views = Blueprint("views", __name__)

@views.route("/", methods=["GET","POST"])
def home():
     
     return render_template('base.html')


