from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from models import Url
from server import db

class Urls():
    '''Returns a list of objects'''
    def index():
        urls = Url.query.all()
        return [url.serialize for url in urls], 200

    '''Returns the longurl as str if it find it on the system'''
    def redir(short_url):
        url = Url.query.filter_by(final=short_url).first_or_404()
        return str(url.origin), 200

    '''Returns the new url as str'''
    def create(long_url):    
        actual = Url.query.filter_by(origin=long_url).first()
        if actual:
            return actual.final, 302
        else:
            url=Url(
                    origin=long_url
                )
            db.session.add(url)
            db.session.commit()
            return str(url.final), 302
        
