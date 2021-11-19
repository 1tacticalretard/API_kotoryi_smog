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
            task = json.loads(dumps(db.todos.find_one({'_id': int(event['pathParameters']['_id'])})))
            todo = 'Result:\n ID: {};\n TITLE: {};\n BODY: {}'.format(task ['_id'], task['title'], task['body'])  
            return {"statusCode": 200, "body": todo}
