from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
app = Flask(__name__)

app.config ['SECRET_KEY'] = '7fba4a3c2e00cfe32d5b6e78300fb46e'

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[Email(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

@app.route("/", methods=['GET', 'POST'])
def home():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Welcome, {form.username.data}!')
        return redirect(url_for('login'))
    return render_template('index.html', form=form)

@app.route("/login")
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
