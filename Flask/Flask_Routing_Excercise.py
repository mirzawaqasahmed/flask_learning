# Set up your imports here!
# import ...
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')  # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return '<h1> Waqas - Welcome! Go to /puppy_latin/name to see your name in puppy latin!</h1>'


@app.route('/puppy_latin/<name>')  # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    if name[-1] == 'y' or name[-1] == 'Y':
        return f"<h1>Hi {name}! Your puppylatin name is {name[:-1]}iful</h1>"
    else:
        return f"<h1>Hi {name}! Your puppylatin name is {name}y</h1>"
    # pupname = ''
    # if name[-1] == 'y':
    #     pupname = name[:-1]+'iful'
    # else:
    #     pupname = name+'y'

    # return "<h1>Hi {}! Your puppylatin name is {} </h1>".format(name, pupname)

if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
