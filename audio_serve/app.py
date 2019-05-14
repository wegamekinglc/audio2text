# -*- coding: utf-8 -*-
"""
Created on 2019-5-13

@author: cheng.li
"""

import werkzeug
from io import BytesIO
import base64
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from flask_restful import Api, Resource
from flask_restful import reqparse

app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
api = Api(app)


class Audio2Text(Resource):

    def post(self):
        data = request.files['mp3']
        return make_response(jsonify(dict(code=1, message="file upload succeeded", data=None)), 200)

api.add_resource(Audio2Text, '/audio2text')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')