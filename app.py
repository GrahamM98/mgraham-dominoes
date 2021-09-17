from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from api.TestConnect import TestConnect

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(TestConnect, '/test_connect')
