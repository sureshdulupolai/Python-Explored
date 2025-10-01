from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional

class RegistrationForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(message="We need your name, it cannot be empty"), Length(min=2, max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Register")

# DataRequired(message="We need your name, it cannot be empty") -> custom message
# DataRequired() → ensure karega ki field empty na ho (Django me blank=False jaisa).
# Email() → check karega ki jo value dala gaya hai wo valid email hai ya nahi (e.g. test@domain.com).
# Length(max=...) → email ki length ko limit karta hai (DB me max_length=120 jaisa).