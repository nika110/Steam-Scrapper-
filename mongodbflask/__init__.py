from flask import Flask

from .extensions import mongo
from .main import main

def webapp(config_obj='mongodbflask.settings'):
    app = Flask(__name__)

    app.config.from_object(config_obj)

    mongo.init_app(app)

    app.register_blueprint(main)

    return app
