from flask import Blueprint

from .extensions import mongo

main = Blueprint('main', __name__)

@main.route('/')

def index():
    user_collector = mongo.MONGODB_DB.MONGODB_COLLECTION
    user_collector.insert({"###insert MZADAA mognodbstvis###"})
    return 'Your User'
