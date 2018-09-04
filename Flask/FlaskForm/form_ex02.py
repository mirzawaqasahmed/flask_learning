from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                    RadioField,SelectField,TextField,
                    TextAreaField,SubmitField)
from wtforms.validators import DataRequired
from flask_table import Table, Col

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

    breed = StringField('What breed is your dog?',
                        validators=[DataRequired()]
                        )
    neutered = BooleanField("Has the puppy been neutered?")
    mood = RadioField('Please choose your mood:',
                      choices=[('modd_one','Happy'),
                               ('mood_two','Excited')
                               ]
                      )
    food_choice = SelectField(u'Pick your favorite food:',
                              choices=[('chi','Chicken'),
                                       ('bf','Beef'),
                                       ('fish','Fish')
                                       ]
                              )
    feedback = TextAreaField()
    submit = SubmitField('Submit')

# Declare your table
class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')

# Get some objects
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
# items = [Item('Name1', 'Description1'),
#          Item('Name2', 'Description2'),
#          Item('Name3', 'Description3')]
# Or, equivalently, some dicts
items = [dict(name='Name1', description='Description1'),
         dict(name='Name2', description='Description2'),
         dict(name='Name3', description='Description3'),
         dict(name='Name4', description='Description4')
         ]

# Or, more likely, load items from your database with something like
# items = ItemModel.query.all()

# Populate the table
table = ItemTable(items, border=True, classes=['table table-bordered table-hover table-sm table-dark'])


@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))

    return render_template('form_ex02_index.html', form=form)

@app.route('/table_example')
def table_example():
    return  render_template('form_ex02_table_example.html', table=table)
    # return table.__html__()

@app.route('/thankyou')
def thankyou():
    return render_template('form_ex02_thankyou.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
