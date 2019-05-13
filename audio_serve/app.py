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
from flask_restful import Api, Resource
from flask_restful import reqparse

app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
api = Api(app)


class Audio2Text(Resource):

    def post(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('mp3', type=werkzeug.FileStorage, location='files')
        # args = parser.parse_args()
        # data = args['mp3'].stream
        data = request.files['mp3']
        # data.save('my_mp3.mp3')

api.add_resource(Audio2Text, '/audio2text')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')