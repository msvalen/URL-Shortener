from flask import Flask, redirect, render_template, request, url_for
from flask_cors import CORS 
from flask_sqlalchemy import SQLAlchemy
from controllers import urls as Urls
import os

#from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

try:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
except:
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

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['original_url']
        boolean = checkurl(url)
        if boolean:
            resp, code = Urls.create(url)
            return render_template('index.html', url=resp), code
        else:
            return render_template('index.html', url='that is not a url'), 200
    else: 
        return render_template('index.html')

@app.route('/<short_url>')
def new_link(short_url):
        resp, code = Urls.redir(short_url)
        return redirect(resp, 302, None), 302

def checkurl(url):
    condition = '.com' in url or '.co.uk' in url or '.es' in url or '.org' in url or '.net' in url
    return url.startswith('http') and condition

'''
@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500
'''

# if __name__ == "__main__":
#     app.run()