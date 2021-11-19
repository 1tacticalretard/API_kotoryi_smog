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
    event = db.todos.find_one_and_replace({'_id': 0}, {'title': "[THIS PART WAS MODIFIED] Task complete. The car for the modification has been successfully selected."})
    todo = 'MODIFIED: ID: {}; TITLE: {}; BODY: [DELETED]'.format(event ['_id'], event['title'])  

    return { 
            'statusCode' : 200,
            'body' : todo
    }
