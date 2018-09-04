from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    puppies = ['Fluffy', 'Rufus', 'Spike']
    name = "Waqas"
    letters = list(name)
    pup_dictionary = {'pup_name': 'Sammy'}

    user_logged_in = True

    return render_template('templates_example.html', name=name, letters=letters, pup_dictionary=pup_dictionary, puppies=puppies, user_logged_in=user_logged_in)

if __name__ == '__main__':
    app.run(debug=True)