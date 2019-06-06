from db_setup import *
from flask import Flask
from flask_pymongo import PyMongo
from pymongo.uri_parser import *

# Flask web app
app = Flask(__name__)


@app.route('/')
def index():
    return 'soup'


def init_db():
    try:
        app.config['MONGO_URI'] = db_connection_string
        mongo = PyMongo(app)
        return mongo.db
    except pymongo.errors.PyMongoError as error:
        # TODO: Implement better connection error handling
        print('Error initializing database: ')
        #print(error)
        return
