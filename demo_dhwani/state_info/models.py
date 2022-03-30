from email.policy import default
from mongoengine import *
from mongoengine.base.fields import ObjectIdField
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, StringField
from bson import ObjectId 
import datetime

class State(Document):
    name = StringField()
    description = StringField()
    date_added = DateTimeField(default=datetime.datetime.utcnow)

class District(Document):
    state_name = StringField()
    name = StringField()
    date_added = DateTimeField(default=datetime.datetime.utcnow)
