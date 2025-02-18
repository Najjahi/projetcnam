from tokenize import String
from flask_wtf import FlaskForm
<<<<<<< HEAD
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
=======
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from projet.models import User
>>>>>>> f62f24c (Premier commit avec les fichiers)
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Regexp,
    EqualTo,
    ValidationError,
)

from projet.models import User

<<<<<<< HEAD

=======
>>>>>>> f62f24c (Premier commit avec les fichiers)
class RegistrationForm(FlaskForm):
    fname = StringField(
        "First Name", validators=[DataRequired(), Length(min=2, max=25)]
    )
    lname = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=25)])
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=25)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Regexp(
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$"
            ),
        ],
    )
    confirm_password = PasswordField(
<<<<<<< HEAD
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("S'inscrire")
=======
        "Confirmation du mot de passe", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("S'enregistrer")
>>>>>>> f62f24c (Premier commit avec les fichiers)

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
<<<<<<< HEAD
            raise ValidationError(
                "Username already exists! Please chosse a different one"
            )

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already exists! Please chosse a different one")


=======
            raise ValidationError("Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Cet email est déjà pris. Veuillez en choisir un autre.")
>>>>>>> f62f24c (Premier commit avec les fichiers)
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
        ],
    )
<<<<<<< HEAD
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")

class UpdateProfileForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=25)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    bio = TextAreaField("Bio")
    picture = FileField(
        "Update Profile Picture", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField("Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    "Username already exists! Please chosse a different one"
                )

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    "Email already exists! Please chosse a different one"
                )
=======
    remember = BooleanField("Souviens-toi de moi")
    submit = SubmitField("Se connecter")
>>>>>>> f62f24c (Premier commit avec les fichiers)
