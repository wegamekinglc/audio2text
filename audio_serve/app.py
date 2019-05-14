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
from flask_restful import reqparse
from flask_restful import Api, Resource
from audio_serve.baidu import fetch_stt_baidu
from audio_serve.kdxf import fetch_stt_kdxf


app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
api = Api(app)


class AudioUpload(Resource):

    def post(self):
        data = request.files['mp3']
        data.save('t.mp3')
        return make_response(jsonify(dict(code=1, message="file upload succeeded", data=None)), 200)


class Audio2Text(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('vendor', type=str, help='vendor of stt', default='baidu')
        args = parser.parse_args()
        vendor = args['vendor']

        data = request.files['mp3']
        data.save('t.mp3')
        stream = ffmpeg.input('t.mp3')
        stream = ffmpeg.output(stream, 't.pcm', acodec='pcm_s16le', f='s16le', ac=1, ar=16000)
        ffmpeg.run(stream, overwrite_output=True)

        if vendor == 'baidu':
            res = fetch_stt_baidu('t.pcm')['result'][0]
        elif vendor == 'kdxf':
            res = fetch_stt_kdxf('t.pcm')
        else:
            raise ValueError('vendor is no recognized')
        return make_response(jsonify(dict(code=1, message="speech to sentence succeeded", data={'query': res})), 200)


api.add_resource(AudioUpload, '/audioupload')
api.add_resource(Audio2Text, '/audio2text')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8128)