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
from audio_serve.baidu import fetch_stt_chinese_baidu
from audio_serve.baidu import fetch_stt_english_baidu
from audio_serve.kdxf import fetch_stt_chinese_kdxf
from audio_serve.kdxf import fetch_stt_english_kdxf


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
        parser.add_argument('language', type=str, help='language to stt', default='chinese')
        args = parser.parse_args()
        vendor = args['vendor']
        language = args['language']

        data = request.files['mp3']
        data.save('t.mp3')
        stream = ffmpeg.input('t.mp3')
        stream = ffmpeg.output(stream, 't.pcm', acodec='pcm_s16le', f='s16le', ac=1, ar=16000)
        ffmpeg.run(stream, overwrite_output=True)

        if vendor == 'baidu':
            if language == 'chinese':
                res = fetch_stt_chinese_baidu('t.pcm')['result'][0]
            elif language == 'english':
                res = fetch_stt_english_baidu('t.pcm')['result'][0]
            else:
                raise ValueError('language is not recognized')

        elif vendor == 'kdxf':
            if language == 'chinese':
                res = fetch_stt_chinese_kdxf('t.pcm')['data']
            elif language == 'english':
                res = fetch_stt_english_kdxf('t.pcm')['data']
            else:
                raise ValueError('language is not recognized')
        else:
            raise ValueError('vendor is no recognized')
        return make_response(jsonify(dict(code=1, message="speech to sentence succeeded", data={'query': res})), 200)


api.add_resource(AudioUpload, '/audioupload')
api.add_resource(Audio2Text, '/audio2text')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8128)