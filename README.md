# Audio2Text

## Introduction

Audio2Text(Audio to Text) is a service to translate speech audio to written sentence.

## Implementation

Currently this service simply wrappers vendor STT(Speech to Text) service. What we have done is to switch between different vendors and languages.

Now the available vendors are [Baidu](https://cloud.baidu.com/) and [iFLYTEK](https://www.xfyun.cn/).

## How to start

### Build Image

Thanks to docker, the installment is very easy. Just type in following line under the project root:

```bash
$ sudo docker build -t audio2text -f docker/Dockerfile .
```

### Start the service

```bash
$ sudo docker run -it -p 8128:8128 -t audio2text
```

## Test the service

The service is communicated with HTTP protocol. If you successfully finish the previous part, the service will listen at the server's port 8128. We have upload some sample file under the folder [$PROJECT_ROOT/mp3](./mp3). Under this folder you can play with following query:

```bash
$ curl -F mp3=@sample1.mp3 http://localhost:8128/audio2text
```

the returned message should look like:

```json
{
  "code": 1,
  "data": {
    "query": "W1\u662f\u4e00\u6b3e\u4ec0\u4e48\u6837\u7684\u8def\u7531\u5668\uff1f"
  },
  "message": "speech to sentence succeeded"
}
```