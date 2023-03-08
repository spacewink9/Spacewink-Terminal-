from flask import Flask
from flask_restful import Api

from api.resources import ExampleResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ExampleResource, '/example')

if __name__ == '__main__':
    app.run(debug=True)
