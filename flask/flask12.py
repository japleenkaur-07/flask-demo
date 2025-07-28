from flask import Flask
from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"
@app.route('/<name>')
def greet(name):
    return f"Hello, {name}!"
@app.route('/home/red')
## redirects to home
def redirect_home():
    return redirect(url_for('home'))
@app.route('/web')
def webb():
    return render_template('web.html')

if __name__ == '__main__':
    app.run(debug=True)
## to create requirments.txt file do pip freeze > requirements.txt
## to install requirments.txt do pip install -r requirements.txt