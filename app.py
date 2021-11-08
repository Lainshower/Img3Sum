# app.py
#import os
from flask import Flask, render_template, request
#NLP MODEL import 


#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 url
def index():
  return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
  file = request.files['chooseFile']
  # NLP 모델에 image 파일을 넣어주고 return 값으로 결과값 추출 
  # ex ) {origin, summ} = BERT(dd, image)
  # NLP에서 받아온 데이터를 아래 변수에 넣어준다. 
  return render_template('upload.html',data={'origin':"fdsfdsk",'summ':"dadsaadsa",}) 
 


if __name__=="__main__":
  app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)