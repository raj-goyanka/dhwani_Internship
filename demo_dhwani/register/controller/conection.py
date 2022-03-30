from mongoengine import connect
from pymongo import database
import pymongo

connect(db="demo_db_2", host="localhost", port=27017)
url = "mongodb://localhost:27017"
client = pymongo.MongoClient(url)
database = client.demo_db_2
# Issue the serverStatus command and print the results
# serverStatusResult=database.command("serverStatus"