from flask import Flask, render_template, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import Url

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
    urls = Url.Url.query.all()
  
    return jsonify([url.serialize for url in urls])

@app.route("/add/<url>")
def add_url(url):
    #origin='second.com'#request.args.get('url')
    try:
        actual = Url.Url.query.filter_by(origin=url).first()
        if actual:
            return jsonify(actual.final)
        else:
            url=Url.Url(
                origin=url
            )
            db.session.add(url)
            db.session.commit()
            return str(url.final)
    except Exception as e:
        print(e)
        return jsonify(e)
        
if __name__ == '__main__':
    app.run(debug=True)
