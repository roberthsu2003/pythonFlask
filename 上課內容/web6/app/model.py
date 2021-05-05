from . import db

class City(db.Model):
    __tablename__ = "city"
    id = db.Column(db.Integer, primary_key=True)
    cityName = db.Column(db.String(15))
    continent = db.Column(db.String(15))
    country = db.Column(db.String(15))
    image = db.Column(db.String)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    url = db.Column(db.String)

    def __repr__(self):
        return f"<City cityName={self.cityName}>"