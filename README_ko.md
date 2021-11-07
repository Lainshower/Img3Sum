# Img3Sum

<p align="center">
    <br>
    <img src="https://postfiles.pstatic.net/MjAyMTExMDhfMTgw/MDAxNjM2Mjk5NTEwOTQz.usISiht3P5F41AG-4S2XGLJ1KV89zPaW8Bgx9jGa79og.BTRnTACGJOJw8vj664wmrwG595heQ_oAKDvUWOh-pyQg.PNG.kaoara/Img3Sum.png?type=w773" width="300" height="300" />
    <br>
<p>

<p align="center">
        <img alt="License" src="https://img.shields.io/crates/l/rustc-serialize?style=for-the-badge">
        <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
        <img alt="NodeJS" src="https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white">
        <img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white">
</p>    
<h4 align="center">
    <p>
      <a href="https://github.com/Lainshower/Img3Sum/blob/main/README.md">English</a> | 
      <b>한국어</b>
    <p>
</h4>

#### 영문으로 된 이미지에서 핵심 문장과 번역본을 같이 제공하는 오픈소스 프로젝트

## Core concept

영문으로 된 이미지를 읽을 때, 핵심 문장이 무엇인지 알고 싶지 않으신가요?

저희는 문서 이미지 속 핵심 문장과 번역본을 제공해주는 오픈소스 프로젝트입니다.

## 공식 문서

(예정)

## 제공하는 기능

1. 영어 문장이 포함된 이미지 데이터에 대해서 OCR(ptical character recognition)을 통한 텍스트 추출

2. 추출된 영어문장 내 중요 문장 3개를 추출 요약  

3. 추출된 3개의 영어문장에 대한 한국어 번역 제공

4. (예정) 추출된 3개의 영어문장에 대한 교정 

5. (예정) 한국어 문장이 포함된 이미지 데이터에 대해서 OCR(ptical character recognition)을 통한 텍스트 추출

## 사용 방법

### 사전 설치 사항

> Papago API

Papago 번역 API를 사용하기 위해서는 먼저 [네이버 개발자 센터]에서 어플리케이션을 등록하고 클라이언트 ID와 비밀번호를 발급받아야 합니다.

1. 네이버 개발자 센터 상단의 메뉴에서 **Application > 애플리케이션 등록**을 선택합니다.
2. 애플리케이션 등록 (API이용신청) 페이지에서 애플리케이션 세부 정보를 입력하는 방법은 다음과 같습니다: <br/>
  a. 등록하려는 애플리케이션의 이름을 입력합니다.<br/>
  b. 사용 API에서 Papago 번역을 선택하여 추가합니다.<br/>
  c. 비로그인 오픈 API 서비스 환경에서 애플리케이션을 서비스할 환경을 추가하고 필요한 상세 정보를 입력합니다.<br/>
3. 애플리케이션이 정상적으로 등록되면 네이버 개발자 센터의 **Application > 내 어플리케이션** 메뉴 아래에 등록한 애플리케이션 이름으로 하위 메뉴가 생긴 것을 확인할 수 있습니다. 
4. 등록한 애플리케이션 이름을 클릭하면 개요 탭에서 애플리케이션에 부여된 클라이언트 ID와 비밀번호를 확인할 수 있습니다.
5. 발급 받은 클라이언트 ID와 비밀번호를 [extract.py](https://github.com/Lainshower/Img3Sum/blob/main/extract.py)에 입력해주세요

```python
export CLIENT_ID='Your application's client id'
export CLIENT_SECRET='Your application's client secret'
```
<br/>

**어플리케이션 등록**

<img src="https://developers.naver.com/proxyapi/rawgit/naver/naver-openapi-guide/master/ko/papago-apis/images/papago-nmt-01.png" width="650">

**클라이언트 ID와 비밀번호 확인**

<img src="https://developers.naver.com/proxyapi/rawgit/naver/naver-openapi-guide/master/ko/papago-apis/images/papago-nmt-02.png" width="650">

<br/>


[Naver Developers]:https://developers.naver.com/main/
[네이버 개발자 센터]: https://developers.naver.com/apps/#/wizard/register

>**OCR**

[OCR_RUN.py](https://github.com/Lainshower/Img3Sum/blob/main/OCR_RUN.py)에 있는 OCR 기능을 사용하기 위해 **tesseract**를 다운로드 합니다.

- **Windows**

https://github.com/UB-Mannheim/tesseract/wiki

- **Mac**

```
brew install tesseract
```

- **Linux**
  
```
sudo apt-get update
sudo apt-get install libleptonica-dev 
sudo apt-get install tesseract-ocr tesseract-ocr-dev
sudo apt-get install libtesseract-dev
```
>**Flask**

백엔드 실행을 위해 Flask를 설치하세요. (Flask 공식문서를 참고하세요.)<br/>

<img src="https://user-images.githubusercontent.com/63241893/140640023-7c37ab45-c5e8-47bc-b135-340afbdda798.jpg" width="50%"><br/>

[Flask 설치]: https://flask.palletsprojects.com/en/2.0.x/installation/#python-version <br/>

[버전 검사]: https://flask.palletsprojects.com/en/2.0.x/changes/# <br/>


### Localhost에서 실행

> Clone

```bash
  $ git clone https://github.com/Lainshower/Img3Sum.git
```   

> Run

1. Create 가상환경 만드세요.
```python3
  conda env create --file img3sum.yaml
```
2. [app.py](https://github.com/Lainshower/Img3Sum/blob/main/app.py) 를 실행하세요.

```python3
  conda activate 'your env name'
  python app.py
```

## 온라인 데모
### (예정)

## 베포 버전

### v0.0.0

## 오픈소스 기여자들

- Joonwon Jang
  - Github: [@Lainshwoer](https://github.com/Lainshower)
- GeonYeong Son
  - Github : [GeonYeongSon](https://github.com/GeonYeongSon?tab=repositories)
- YiYoung Yoon
  - Github : [y20ng](https://github.com/y20ng?tab=repositories)
- JuHeon Oh
  - Github : [OZOOOOOH](https://github.com/OZOOOOOH)

## 라이센스

Copyright © 2021 [Lainshower](https://github.com/Lainshower).<br />
This project is available under the [Apache-2.0 License](https://github.com/Lainshower/Img3Sum/blob/main/LICENSE).
