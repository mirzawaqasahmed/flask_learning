from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('forms_index.html')

@app.route('/singup_form')
def singup_form():
    return render_template('forms_signup.html')

@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')

    return render_template('forms_thankyou.html', first=first, last=last)

@app.errorhandler(404)
def page_not_found(err):
    return render_template('forms_404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)