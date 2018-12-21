import os
import requests
from flask import Flask , request
app = Flask(__name__)



token=os.getenv('TELEGRAM_BOT_TOKEN')

@app.route("/")
def hello():
    return "열려라 참깨"
    
    
    
@app.route(f"/{token}",methods=['POST'])
def telegram():
    
    #구조 확인하기
    from_telegram = request.get_json()  #dictionary 형태로 자료를 저장
    
    print(from_telegram)
    
    #그대로 돌려보내기
    #['message'] => 키가 없으면 에러
    #.get('message')=> 키가 없으면 NONE
    
    if from_telegram.get('message') is not None:
        chat_id=from_telegram['message']['from']['id']
        text=from_telegram['message']['text']
        requests.get(f'https://api.hphk.io/telegram/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
    return '', 200
    
    
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))