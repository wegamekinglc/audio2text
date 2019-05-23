# coding=utf-8

import base64
import random
import requests


API_SETTINGS = [
    dict(API_KEY='zyZAIS9gQck9xycaGLHGkins', SECRET_KEY='7Q9rSvApvoAGtMzjUFQetxFBwokSy0Nt'),
    dict(API_KEY='whVEYPaFDe0WgoRYEort9U6M', SECRET_KEY='9PdrEiVMbM0TLeWYoPFb3K3nRmMvEWTq'),
    dict(API_KEY='7cOfriRPD4W9ueH111KGHkyf', SECRET_KEY='43LD6caUnm08zssRxVElGw6deCiBKy4Y')
]

FORMAT = 'pcm'  # 文件后缀只支持 pcm/wav/amr
RATE = 16000  # 固定值

tokens = ['24.759027c2fc63c21b3d8b357acb77ab44.2592000.1561188848.282335-16232520',
          '24.6728085aa0a8667fab5993ac1d5c793e.2592000.1561188849.282335-16323950',
          '24.b7e4209835972e63f245a4395c7bd550.2592000.1561188849.282335-15178355']

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


def fetch_token(n):
    params = {'grant_type': 'client_credentials',
              'client_id': API_SETTINGS[n]['API_KEY'],
              'client_secret': API_SETTINGS[n]['SECRET_KEY']}

    resp = requests.post(TOKEN_URL, data=params)
    result = resp.json()
    return result['access_token']


"""  TOKEN end """


def fetch_stt_chinese_baidu(audio_file):
    dev_pid = 80001
    asr_url = 'https://vop.baidu.com/pro_api'

    n = random.randint(0, len(tokens) - 1)
    token = tokens[n]
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
              'cuid': "sunmi_" + str(n),
              'channel': 1,
              'speech': speech,
              'len': length
              }

    resp = requests.post(asr_url, json=params)
    return resp.json()


def fetch_stt_english_baidu(audio_file):
    dev_pid = 1737
    asr_url = 'http://vop.baidu.com/server_api'

    n = random.randint(0, len(tokens) - 1)
    token = tokens[n]
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
              'cuid': "sunmi_" + str(n),
              'channel': 1,
              'speech': speech,
              'len': length
              }

    resp = requests.post(asr_url, json=params)
    return resp.json()


if __name__ == '__main__':
    for i in range(3):
        print(fetch_token(i))
