from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    """ Registration from """
    
    username = StringField('username_label', # <label>
                           validators=[InputRequired(message="Username required"),
                                Length(min=4, max=24, message="Username must be 4-24 characters")]) 
    # render_kw={"placeholder": "Username"} alternative like in the html
    
    password = PasswordField('password_label', 
                           validators=[InputRequired(message="Password required"),
                                Length(min=4, max=24, message="Password must be 4-24 characters")])
    
    confirm_pswd = PasswordField('confirm_pswd_label', 
                           validators=[InputRequired(message="Retype Password"),
                                       EqualTo('password',message="Password must match")])
    
    submit_button = SubmitField('Create')