import secrets
from PIL import Image
import os
from projet.models import User, recette, Cuisine
from flask import render_template, url_for, flash, redirect, request
from projet.forms import RegistrationForm, LoginForm, UpdateProfileForm
from projet import app, bcrypt, db
from flask_login import (
    login_required,
    login_user,
    current_user,
    logout_user,
    login_required,
)



with app.app_context():
    db.create_all()  # Crée toutes les tables définies par tes modèles
    print("Tables créées avec succès")
    # Créer un nouvel utilisateur
    #user_1 = User(fname = 'imane', lname = 'najjahi', username = 'imane', email = 'imane@gmail.com', password = 'R@yane1917')
    #db.session.add(user_1)

    #user_2 = User(fname = 'anas', lname = 'najjahi', username = 'anas' , email = 'anas@gmail.com', password = 'R@yane1917')
    #db.session.add(user_2)
    #db.session.commit()
    #user_3 = User(fname = 'izdi', lname = 'najjahi', username = 'izdi' , email = 'izdi@gmail.com', password = 'R@yane1917')
    #db.session.add(user_3)
    #db.session.commit()

    # Afficher tous les utilisateurs
    users = User.query.all()
    for user in users:
        print(f"{user.fname} {user.lname}, Email: {user.email}")

recettes = [{
    'title': 'Demande de recette',
    'course': 'Braiser de la viande',
    'author': 'Imane',
    'thumbnail': 'braiser.jpg'
},
{'title': 'Demande de recette',
    'course': 'Rôtissage de la viande',
    'author': 'Soukaina',
    'thumbnail': 'Rotissage.jpg'
},
{'title': 'Demande de recette',
    'course': 'Cuisson à la vapeur',
    'author': 'Imane',
    'thumbnail': 'Cuisson_vapeur.jpg'
},
{'title': 'Demande de recette',
    'course': 'Sauté',
    'author': 'Soukaina',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Demande de recette',
    'course': 'Grillades',
    'author': 'Imane',
    'thumbnail': 'Demande de recette',
},
{'title': 'Request Library Course',
    'course': 'Friture',
    'author': 'Soukaina',
    'thumbnail': 'thumbnail.jpg'
},
]

cuisine = [
{
        'name': 'Cuisine traditionnelle',
        'icon': 'python.svg',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

    {
        'name': 'Cuisine végétarienne',
        'icon': 'analysis.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

    {
        'name': 'Cuisine végétalienne',
        'icon': 'machine-learning.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'Cuisine sans gluten',
        'icon': 'web.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'Cuisine exotique',
        'icon': 'blockchain.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'Cuisine marocaine',
        'icon': 'idea.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', recettes=recettes, cuisine=cuisine)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        #existing_user = User.query.filter_by(email=form.email.data).first()
        #if existing_user:
            #flash("Email already exists! Please choose a different one", "danger")
        #else:    
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")        
            
        user = User(
            fname=form.fname.data, 
            lname=form.lname.data, 
            username=form.username.data, 
            email=form.email.data, 
            password = hashed_password,
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Account created successfully for {form.username.data}", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash("You have been logged in!", "success")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check credentials", "danger")
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/dashboard")
@login_required
def dashboard():
    profile_form = UpdateProfileForm()
    if profile_form.validate_on_submit():
        if profile_form.picture.data:
            picture_file = save_picture(profile_form.picture.data)
            current_user.image_file = picture_file
        current_user.username = profile_form.username.data
        current_user.email = profile_form.email.data
        current_user.bio = profile_form.bio.data
        db.session.commit()
        flash("Your profile has been updated", "success")
        return redirect(url_for("dashboard"))
    elif request.method == "GET":
        profile_form.username.data = current_user.username
        profile_form.email.data = current_user.email
        profile_form.bio.data = current_user.bio
    image_file = url_for("static", filename=f"user_pics/{current_user.image_file}")
    return render_template(
        "dashboard.html",
        title="Dashboard",
        profile_form=profile_form,
        image_file=image_file,
    )