from flask import Flask, render_template, request
from utils.difference import get_similar

app = Flask(__name__, template_folder='templates')


@app.route("/", methods=["GET"])
def main():
    return render_template('first.html')

@app.route("/search", methods=["GET", "POST"])
def search():
    pass





if __name__ == "__main__":
    app.run(debug=True)