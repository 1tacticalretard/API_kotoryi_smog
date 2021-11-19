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
    event = db.todos.delete_many({})
    return { 
            'statusCode' : 200,
            'message' : "Succesfully deleted all records."
    }
