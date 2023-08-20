from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/hi')
def hi():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/financials')
def personal_finance():
    return render_template('personal_finance.html')

@app.route('/life')
def life():
    return render_template('life.html')

@app.route('/')
def index():
    return render_template('modern.html')

if __name__ == "__main__":
    freezer.freeze()
