from .db import db

class Ad(db.Document):
    title = db.StringField(required=True, unique=False)
    tags = db.ListField(db.StringField(), required=True)
    comments = db.ListField(db.StringField(), required=True)

