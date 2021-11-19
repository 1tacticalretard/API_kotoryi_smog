import json
from flask_pymongo import PyMongo
import flask
import bson.json_util
#from bson.json_util import dumps

app = flask.Flask(__name__)
app.config["MONGO_URI"] = <link>
mongodb_client = PyMongo(app)
db = mongodb_client.db

# Proved to work fine:
def lambda_handler(event, context):
        all = str(len(list(db.todos.find())))
        info = 'There is a list of ' + all + ' todo(s) to be completed. Check them out by adding a /find/<number> line to the address field of your browser. The count starts from 0 and ends with total amount of todos minus 1.'
        return {
            'statusCode' : 200,
            'body' : info
        }