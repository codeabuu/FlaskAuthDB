from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "xyz"


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash("Email must be more than 4 characters", category="error")
        elif len(firstName) < 2:
            flash("firstName must be more than 2 characters", category="error")
        elif password1 != password2:
            flash("passwords don't match, please try again", category="error")
        elif len(password1) < 7:
            flash("password must be more than 7 characters", category="error")
        else:
            #add user to db
            new_user = User(email=email, firstName=firstName, password=)
            flash('account created succefully', category="success")

    return render_template("sign_up.html")
