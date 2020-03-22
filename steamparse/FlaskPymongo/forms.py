from wtforms import Form, StringField, SelectField
from flask_pymongo import PyMongo

class DBaseSearch(Form):
    DBase = []
    select = SelectField('Search for Steam:', DBase=DBase)
    search = StringField('')
