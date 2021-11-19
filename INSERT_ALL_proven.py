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
        event = db.todos.insert_many([
            {'_id': 0, 'title': "Select the car to be modified", 'body': "No comments."},
            {'_id': 1, 'title': "Upgrade the brake system", 'body': "Any sort of vehicle modding/tuning should get started with the brake system upgrade."},
            {'_id': 2, 'title': "Remove non-vital parts", 'body': "The lighter your car gets, the faster it becomes and the better acceleration can be achieved."},
            {'_id': 3, 'title': "Swap/modify the engine", 'body': "Engine is a heart of your vehicle. Apart from an engine itself, a gearbox as well as other engine parts should be modified."},
            {'_id': 4, 'title': "Modfiy transmission and suspension", 'body': "New transmission and suspension should be installed so that the gearbox an engine weight as well as their power output could be properly handled."},
            {'_id': 5, 'title': "Think about personal safety and comfort", 'body': "Install a roll cage and bash bar as well as sport seats and other things of your choice so that the car could become more convenient and safe-to-drive."},
            {'_id': 6, 'title': "Test and configure", 'body': "Once everything is done, test and configure your vehicle so that the performance could be at its best."},
            ], ordered = True)
        return { 
            'statusCode' : 200,
            'message' : "Successfully inserted 7 records to the database."
        }