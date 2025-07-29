from flask import Flask
from flask import Flask, redirect, url_for,render_template

app = Flask(__name__,static_folder='static')

@app.route('/')
def home():
    return render_template('web.html')
@app.route("/japleen")
def japleeen():
    return "<h1>I LOVE YOU JAPLEEN</h1>"
if __name__ == '__main__':
    app.run(debug=True)
## to create requirments.txt file do pip freeze > requirements.txt
## to install requirments.txt do pip install -r requirements.txt
