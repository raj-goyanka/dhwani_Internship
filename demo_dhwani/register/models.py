from mongoengine import *
from mongoengine.document import Document
from mongoengine.fields import StringField

class User(Document):
    username = StringField()
    password = StringField()
