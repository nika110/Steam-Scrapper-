from flask import Flask, render_template
from flask_pymongo import PyMongo
#import settings


app = Flask(__name__)
#app.config["MONGO_URI"] = settings.MONGODB_HOST + ":" + settings.MONGODB_PORT + "/" + settings.MONGODB_DB
#mongo = PyMongo(app)

@app.route('/dbfinder',methods = ['POST', 'GET'])
def main():
    return render_template('first.html')

if __name__ == '__main__':
    app.run(debug=True)
