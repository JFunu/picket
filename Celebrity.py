from google.appengine.ext import db

class Celebrity(db.Model):
    stageName = db.StringProperty()
    industry = db.StringProperty()
    base = db.StringProperty()