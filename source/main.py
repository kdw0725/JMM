import os
from source import crawling
from flask import Flask, request, jsonify
#from test import microdust_1
from source import insert
from source import choice



app = Flask(__name__)


@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons":["대화하기","도움말"]
    }
    return jsonify(dataSend)

@app.route('/message',methods = ['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    if content == u"대화하기":
        dataSend = {
            "message":{
                "text" : "지역과 음식 종류를 입력해 주세요 ex) 오류동 짜장면 " #"점머먹 명령어 목록 \n1. 도움말\n2. 안녕\n3.저기"
            }
        }
    elif content =='choice':
        dataSend = {
            "message":{
                "text":choice.choice_preference()
            }

        }
    elif content =='insert':
        dataSend={
            "message":{
                "text":insert.choice_insert()
            }

        }
    else:
        dataSend = {
            "message": {
                "text": "http://place.map.daum.net/27467658"
            }
        }
        '''
    elif content == u"도움말":
        dataSend = {
            "message" : {
                "text" : "곧 점머먹 개장합니다."
            }
        }
    elif u"안녕" in content:
        dataSend = {
            "message" : {
                "text": "http://place.map.daum.net/27467658"
            }
        }
    elif u"저기" in content:
        dataSend = {
            "message" : {
                "text" : "꺼져 병신아"
            }
        }
    else:
        dataSend = {
            "message" : {
                "text" : content
            }
        }
        '''
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
