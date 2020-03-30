from flask_mongoengine import MongoEngine
#from billboard.extensions import mongo as db

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)