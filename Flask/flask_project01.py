# Set up your imports and your flask app.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # This home page should have the form.
    return render_template('project01_index.html')


# This page will be the page after the form
@app.route('/report')
def report():
    # Check the user name for the 3 requirements.
    username = request.args.get('username')

    capital_check = bool(username) and username[-1].isdigit()
    upper_check = any(c.isupper() for c in username)
    lower_check = any(c.islower() for c in username)

    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input
    
    message = []
    
    if not capital_check:
        message.append('Must have a number at the end.')
    if not upper_check:
        message.append('Must have an upper case letter somewhere.')        
    if not lower_check:
        message.append('Must have a lower case letter somewhere')


    # Return the information to the report page html.
    return render_template('project01_submit.html',
                            username=username, message=message)

if __name__ == '__main__':
    # Fill this in!
    app.run(debug=True, port=5001)
