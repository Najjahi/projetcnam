from projet import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from projet.models import User, recette, Cuisine
from projet.forms import RegistrationForm, LoginForm
from flask_login import (
    login_required,
    login_user,
    current_user,
    logout_user,
    login_required,
)

with app.app_context():
    #db.create_all()  # Crée toutes les tables définies par tes modèles
    # Créer un nouvel utilisateur
    #user_1 = User(fname = 'imane', lname = 'najjahi', username = 'imane', email = 'imane@gmail.com', password = 'R@yane1917')
    #db.session.add(user_1)

    #user_2 = User(fname = 'anas', lname = 'najjahi', username = 'anas' , email = 'anas@gmail.com', password = 'R@yane1917')
    #db.session.add(user_2)
    #db.session.commit()

    print("Utilisateur ajouté avec succès")
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
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash(f"L'email {form.email.data} est déjà utilisé. Veuillez en choisir un autre.", "danger")
            return redirect(url_for("register"))
        
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
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Vous etes connecté!", "success")
            return redirect(url_for("home"))
        if ( 
            form.email.data == "imane@gmail.com"
            and form.password.data == "R@yane2017"
        ):  
           
            flash("Vous etes bien connecté!", "success")
            return redirect(url_for("home"))
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
    return render_template("dashboard.html", title="Dashboard")