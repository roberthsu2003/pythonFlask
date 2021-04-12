from . import db

class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    cityName = db.Column(db.String(64), unique=True)
    continent = db.Column(db.String(64), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    image = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    url = db.Column(db.String(256))

    def __repr__(self):
        return '<City %r>' % self.cityName