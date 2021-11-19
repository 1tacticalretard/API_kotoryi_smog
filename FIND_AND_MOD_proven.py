import json
from flask_pymongo import PyMongo
import flask
from pymongo.errors import BulkWriteError
from bson.json_util import dumps

app = flask.Flask(__name__)
app.config["MONGO_URI"] = <link>
mongodb_client = PyMongo(app)
db = mongodb_client.db

# Proved to work fine:
def lambda_handler(event, context):
    task = db.todos.find_one_and_update({'_id': int(event['pathParameters']['_id'])}, 
    {"$set": 
    {"title": "Task complete",
     "body": "[DELETED]"}})
    todo = 'MODIFIED:\n ID: {};\n TITLE: {};\n BODY: {}.'.format(task ['_id'], task['title'], task['body'])  
    return { 
            'statusCode' : 200,
            'body' : todo
    }