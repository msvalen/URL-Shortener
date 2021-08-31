from flask import Flask, request, jsonify
from flask.templating import render_template
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

'''
dummy_urls = [
    {'url': 'www.url1.co.uk/homepage'},
    {'url': 'www.url1.co.uk/homepage'},
    {'url': 'www.url1.co.uk/homepage'}

]
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    return



@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404


'''
@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500
'''

if __name__ == "__main__":
    app.run(debug=True)