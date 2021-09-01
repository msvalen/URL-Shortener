import db

class Url(db.Model):
    __tablename__: 'urls'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    origin = db.Column(db.String(100))
    final = db.Column(db.String(100))

    def __init__(self, origin, final):
        self.origin = origin
        self.final = final

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'date': self.date,
            'origin': self.origin,
            'final':self.final
        }