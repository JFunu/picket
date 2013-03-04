from google.appengine.ext import db

class Celebrity(db.Model):
    stageName = db.StringProperty()
    industry = db.StringProperty()
    base = db.StringProperty()
    
    
    def addCelebrity(self, stageName, industry, base):
        celebrity = Celebrity(stageName=stageName, industry=industry, base=base)
        celebrity.put()
        