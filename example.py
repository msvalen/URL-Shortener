from flask import Flask, render_template, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from controllers import urls as Urls
import os

app = Flask(__name__)

POSTGRES = {
    'user': 'debmon',
    'pw': 'secretpassword',
    'db': 'shortererl',
    'host': 'localhost',
    'port': '5430',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/")
def home():
    resp, code = Urls.index()
    return jsonify(resp), code
    # return render('file.html', url= resp), code

@app.route("/add/<url>")
def add_url(url):
    resp, code = Urls.create(url)
    return jsonify(resp), code
        
if __name__ == '__main__':
    app.run(debug=True)
