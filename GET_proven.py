import json
from flask_pymongo import PyMongo
import flask
from pymongo.errors import BulkWriteError

app = flask.Flask(__name__)
app.config["MONGO_URI"] = <link>
mongodb_client = PyMongo(app)
db = mongodb_client.db

# Proved to work fine:
def lambda_handler(event, context):
    event = db.todos.find_one({"_id": 4})
    todo = 'Result: ID: {}; TITLE: {}; BODY: {}'.format(event ['_id'], event['title'], event['body'])  
    return { 
            'statusCode' : 200,
            'body' : todo
    }
