from flask import Flask, render_template, request
from flask_cors import CORS 
#from werkzeug import exceptions

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_template('index.html')
    else: 
        return render_template('index.html')


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