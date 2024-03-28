from .database import db

class Video(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    publishedAt = db.Column(db.DateTime, nullable=False)
    thumbnails = db.Column(db.String(255), nullable=False)
    videoId = db.Column(db.String(50), nullable=False)
