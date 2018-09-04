from flask import Flask, render_template,flash, session, redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class SimpleForm(FlaskForm):

    breed = StringField('What breed is your dog?')
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():

    form = SimpleForm()

    if form.validate_on_submit():

        session['breed'] = form.breed.data
        flash(f"The breed you entered is: {session['breed']}")
        # flash("The breed you entered is: ")

        # flash('Thank you very much!')
        # flash('See you again!')

        return redirect(url_for('index'))

    return render_template('flash_message_index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=5003)
