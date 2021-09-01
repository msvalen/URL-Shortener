from flask import Flask, redirect, render_template, request
from flask_cors import CORS 
from flask_sqlalchemy import SQLAlchemy
from controllers import urls as Urls


#from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

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
        resp, code = Urls.create(request.form['original_url'])
        return render_template('index.html', url=resp), code
    else: 
        return render_template('index.html')

@app.route('/<short_url>')
def new_link(short_url):
        resp, code = Urls.redir(short_url)
        return redirect(resp), code
        




'''
@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500
'''

if __name__ == "__main__":
    app.run(debug=True)