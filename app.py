# app.py
import os
from flask import Flask, render_template, request

#OCR MODEL
from OCR_RUN import ocr_from_img

#NLP MODEL import 
from extract import get_summary

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 url
def index():
  return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
  #이미지 파일 선택(bring image) (만약 이미지를 가져오지 않을 경우)
  if not request.files['chooseFile'] : return app.response_class(
    response={"이미지를 가져오세요(Bring Your Image First, and then Click Submmit Button) & 뒤로가기를 누르세요(Please Push Back Button '<-')"}
  )
  #이미지 파일 선택(bring image)
  img = request.files['chooseFile']
  #이미지를 text 원본으로 변환(image->text)
  origin_text = ocr_from_img(img)
  #text 원본을 한글, 영어 요약으로 변환
  eng, kor = get_summary(origin_text)
  # get_summary에서 받아온 데이터를 아래 변수에 넣어준다. 
  return render_template('upload.html', data={'origin':origin_text,'summ_eng':eng, 'summ_kor':kor}) 
 


if __name__=="__main__":
  app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)