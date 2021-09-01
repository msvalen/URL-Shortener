from flask import Flask, render_template, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

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
from models import Url

@app.route("/")
def home():
    urls = Url.Url.query.all()
  
    return jsonify([url.serialize for url in urls])

@app.route("/add")
def add_url():
    origin='second.com'#request.args.get('url')
    final='dsfgh'
    try:
        url=Url.Url(
            origin=origin,
            final=final
        )
        db.session.add(url)
        db.session.commit()
        return "Url added. url id={}".format(url.id)
    except Exception as e:
        print(e)
        return str(e)
        
if __name__ == '__main__':
    app.run(debug=True)
