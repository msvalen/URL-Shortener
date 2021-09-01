from example import db
from datetime import datetime
import string 
from random import choices

class Url(db.Model):
    __tablename__ = 'urls'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now)
    origin = db.Column(db.String(100), unique=True)
    final = db.Column(db.String(3), unique=True)

    def __init__(self, origin):
        self.origin = origin
        self.final = self.short_generator()

    def __repr__(self):
        return 'id: {}'.format(self.id)

    def  short_generator(self):
        characters = string.digits + string.ascii_letters
        short_url = "".join(choices(characters, k=3))

        link = self.query.filter_by(final=short_url).first()
        if link:
            return self.short_generator()
        return short_url

    @property
    def serialize(self):
        return {
            'id': self.id, 
            'date': self.date,
            'origin': self.origin,
            'final':self.final
        }