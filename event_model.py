from google.appengine.ext import db

import random
import string
import hashlib

class Event(db.Model):
    event_id = db.IntegerProperty(required = True)
    event_date = db.DateTimeProperty(required = True)
    event_venue = db.StringProperty(required = True)
    ticket_price = db.IntegerProperty(required = True)
    celebrities = db.StringProperty(required = True)
    organizer = db.StringProperty(required = True)
    start_time = db.StringProperty(required = True)
    end_time = db.StringProperty(required = True)
    total_guests = db.StringProperty(required = True)    
    created  = db.DateTimeProperty(auto_now_add=True)
    
    @classmethod
    def create_event(cls,event_id, event_date, event_venue, ticket_price, celebrities, organizer, start_time, end_time, total_guests, created):
        results  = cls.gql("WHERE event_id=:1", event_id)
        count   = results.count()
        
        if count==0 and event_id:
            newEvent= Event(event_id = event_id, event_date = event_date, event_venue = event_venue, ticket_price = ticket_price, celebrities = celebrities, 
                            organizer = organizer, start_time = start_time, end_time = end_time, total_guests = total_guests)
            newEvent.put() 
        elif count>0:
            return
        
