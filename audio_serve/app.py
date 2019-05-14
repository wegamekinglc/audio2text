# -*- coding: utf-8 -*-
"""
Created on 2019-5-13

@author: cheng.li
"""

import ffmpeg
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from flask_restful import Api, Resource
from audio_serve.audio2text import fetch_sst

app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
api = Api(app)


class Audio2Text(Resource):

    def post(self):
        data = request.files['mp3']
        data.save('t.mp3')
        stream = ffmpeg.input('t.mp3')
        stream = ffmpeg.output(stream, 't.pcm', acodec='pcm_s16le', f='s16le', ac=1, ar=16000)
        ffmpeg.run(stream, overwrite_output=True)

        res = fetch_sst('t.pcm')['result'][0]
        return make_response(jsonify(dict(code=1, message="file upload succeeded", data={'query': res})), 200)


api.add_resource(Audio2Text, '/audio2text')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8128)