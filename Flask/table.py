from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

users = [{"#": "1", "first": "Mark","last": "Otto", "handle": "@mdo"},
         {"#": "2", "first": "Jacob","last": "Thornton", "handle": "@mfat"},
         {"#": "3", "first": "Waqas","last": "Ahmed", "handle": "@mwa"},
         {"#": "4", "first": "Farah","last": "Waqas", "handle": "@mfar"}
         ]

@app.route('/')
def index():
    return render_template('table_index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
