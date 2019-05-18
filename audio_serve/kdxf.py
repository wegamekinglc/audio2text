# -*- coding: utf-8 -*-
# 语音听写 WebAPI 接口调用示例 接口文档（必看）：https://doc.xfyun.cn/rest_api/%E8%AF%AD%E9%9F%B3%E5%90%AC%E5%86%99.html
# webapi 听写服务参考帖子（必看）：http://bbs.xfyun.cn/forum.php?mod=viewthread&tid=38947&extra=
# 语音听写WebAPI 服务，热词使用方式：登陆开放平台https://www.xfyun.cn/后，找到控制台--我的应用---语音听写---服务管理--上传热词
# （Very Important）创建完webapi应用添加听写服务之后一定要设置ip白名单，找到控制台--我的应用--设置ip白名单，如何设置参考：http://bbs.xfyun.cn/forum.php?mod=viewthread&tid=41891
# 注意：热词只能在识别的时候会增加热词的识别权重，需要注意的是增加相应词条的识别率，但并不是绝对的，具体效果以您测试为准。
# 错误码链接：https://www.xfyun.cn/document/error-code （code返回错误码时必看）
# * @author iflytek

import requests
import time
import hashlib
import base64
import json

# 听写的webapi接口地址
URL = "http://api.xfyun.cn/v1/service/v1/iat"
# 应用APPID（必须为webapi类型应用，并开通语音听写服务，参考帖子如何创建一个webapi应用：http://bbs.xfyun.cn/forum.php?mod=viewthread&tid=36481）
APPID = "5cd8324f"
# 接口密钥（webapi类型应用开通听写服务后，控制台--我的应用---语音听写---相应服务的apikey）
API_KEY = "db49a6eb7d3af87aa885201d559a0d60"


def get_header(aue, engineType):
    cur_time = str(int(time.time()))
    # cur_time = '1526542623'
    param = "{\"aue\":\"" + aue + "\"" + ",\"engine_type\":\"" + engineType + "\"}"
    param_base64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')
    m2 = hashlib.md5()
    m2.update((API_KEY + cur_time + param_base64).encode('utf-8'))
    check_sum = m2.hexdigest()
    # http请求头
    header = {
        'X-CurTime': cur_time,
        'X-Param': param_base64,
        'X-Appid': APPID,
        'X-CheckSum': check_sum,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    return header


def get_body(filepath):
    binfile = open(filepath, 'rb')
    data = {'audio': base64.b64encode(binfile.read())}
    return data


def fetch_stt_chinese_kdxf(audio_file):
    data = get_body(audio_file)
    headers = get_header("raw", "sms16k")
    r = requests.post(URL, headers=headers, data=data)
    return json.loads(r.content.decode('utf-8'))


def fetch_stt_english_kdxf(audio_file):
    data = get_body(audio_file)
    headers = get_header("raw", engineType="sms-en16k")
    r = requests.post(URL, headers=headers, data=data)
    return json.loads(r.content.decode('utf-8'))
