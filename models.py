from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    __tablename__ = "movies"

    mid = db.Column(db.Integer, primary_key=True)
    m_name = db.Column(db.String(200), nullable=False)
    release_date = db.Column(db.String(200), nullable=False)
    genre = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            "mid": self.mid,
            "m_name": self.m_name,
            "release_date": self.release_date,
            "genre": self.genre,
            "country":self.country
        }
