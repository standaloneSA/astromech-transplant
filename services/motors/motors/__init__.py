#!/usr/bin/env python3
"""
Provides a network API for querying and setting motor state
"""

from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/list')
class ListMotors(Resource):
    def get(self):
        return {"motors": []}

if __name__ == '__main__':
    app.run()