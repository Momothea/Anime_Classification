# This file contains the view for the authentification
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)




@auth.route('/login')
def login():
    return render_template("login.html", var ="something") # How to pass variables



#@auth.route('/logout')


@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")