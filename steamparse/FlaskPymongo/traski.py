from flask import Flask, render_template, request
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)




@api.route('/DBase')
class language(Resource):
    def get(self):
        return {'ID' : 'Steamid'}

    @api.route('/DBaseSearch', methods=['GET','POST'])
    def post(self):
        search = DBaseSearch(request.form)
        if request.method == 'POST':
            return search_results(search)

    @api.route('/DBaseResult')
    def search_results(search):
        results = []
        search_id = search.data['search']

        if search.data['search'] == None:
            return render_template("NotFound.html")

        


        

if __name__ == '__main__':
    app.run(debug=True)

