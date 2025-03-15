from pymongo import MongoClient
from os import environ

MONGI_HOST   =  environ.get("MONGI_HOST",'localhost')

client = MongoClient(MONGI_HOST,27017)

db = client['ks']

coll = db['names']