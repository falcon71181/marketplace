from flask import Flask, render_template
from t import *

app = Flask(__name__)

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/market')
def market():
    items = rfun(50)
    return render_template('market.html', items=items)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555, debug=True)