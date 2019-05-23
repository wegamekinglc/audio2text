# coding=utf-8

import json
import base64

import requests
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode


API_KEY = 'zyZAIS9gQck9xycaGLHGkins'
SECRET_KEY = '7Q9rSvApvoAGtMzjUFQetxFBwokSy0Nt'
FORMAT = 'pcm'  # 文件后缀只支持 pcm/wav/amr
CUID = '123456PYTHON'
RATE = 16000  # 固定值

# 免费版

# DEV_PID = 1536  # 1537 表示识别普通话，使用输入法模型。1536表示识别普通话，使用搜索模型。根据文档填写PID，选择语言及识别模型
# ASR_URL = 'http://vop.baidu.com/server_api'
# SCOPE = 'audio_voice_assistant_get'  # 有此scope表示有asr能力，没有请在网页里勾选，非常旧的应用可能没有

# 收费极速版 打开注释的话请填写自己申请的appkey appSecret ，并在网页中开通极速版

# DEV_PID = 80001
# ASR_URL = 'https://vop.baidu.com/pro_api'
# SCOPE = 'brain_enhanced_asr'  # 有此scope表示有收费极速版能力，没有请在网页里开通极速版


# 忽略scope检查，非常旧的应用可能没有
# SCOPE = False

class DemoError(Exception):
    pass


"""  TOKEN start """

TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'


def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}

    resp = requests.post(TOKEN_URL, data=params)
    result = resp.json()
    return result['access_token']


"""  TOKEN end """


def fetch_stt_chinese_baidu(audio_file):
    dev_pid = 80001
    asr_url = 'https://vop.baidu.com/pro_api'

    token = fetch_token()
    with open(audio_file, 'rb') as speech_file:
        speech_data = speech_file.read()

    length = len(speech_data)
    if length == 0:
        raise DemoError('file %s length read 0 bytes' % audio_file)
    speech = base64.b64encode(speech_data)
    speech = str(speech, 'utf-8')
    params = {'dev_pid': dev_pid,
              'format': FORMAT,
              'rate': RATE,
              'token': token,
              'cuid': CUID,
              'channel': 1,
              'speech': speech,
              'len': length
              }

    resp = requests.post(asr_url, json=params)
    return resp.json()


def fetch_stt_english_baidu(audio_file):
    dev_pid = 1737
    asr_url = 'http://vop.baidu.com/server_api'

    token = fetch_token()
    with open(audio_file, 'rb') as speech_file:
        speech_data = speech_file.read()

    length = len(speech_data)
    if length == 0:
        raise DemoError('file %s length read 0 bytes' % audio_file)
    speech = base64.b64encode(speech_data)
    speech = str(speech, 'utf-8')
    params = {'dev_pid': dev_pid,
              'format': FORMAT,
              'rate': RATE,
              'token': token,
              'cuid': CUID,
              'channel': 1,
              'speech': speech,
              'len': length
              }

    resp = requests.post(asr_url, json=params)
    return resp.json()


if __name__ == '__main__':
    pass
