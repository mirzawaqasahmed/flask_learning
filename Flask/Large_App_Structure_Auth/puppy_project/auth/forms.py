from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):

    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    submit = SubmitField('Log in')

class RegistrationForm(FlaskForm):

    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    username = StringField('Username',
                           validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                             EqualTo('pass_confirm',
                                     message = 'Password must match!')])
    pass_confirm = PasswordField('Confirm Password',
                                 validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        # this is querying the User table in our models.py and confirming
        # whether the data entered in the email field already exist or not.
        # we are doing the same validation with username check too.
        if User.query.filter_by(email=field.data).first():

            raise ValidationError('Your email has been already registered!')

    def check_username(self, field):

        if User.query.filter_by(username=field.data).first():

            raise ValidationError('Username is taken')
