# Img3Sum

![Crates.io](https://img.shields.io/crates/l/rustc-serialize?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

#### 많은 영어 문장이 포함된 이미지에서 중요 문장을 추출해 한국어 번역화 함께 제공하는 오픈소스 프로젝트

## Core concept

영어 문장으로 가득한 이미지를 보았을 때, 이미지 안에 있는 중요한 문장이 무엇인지 알고 싶지 않으신가요?

저희는 이미지 속 중요한 영어문장을 추출해 한국어 번역과 제공해주는 오픈소스 프로젝트입니다.

## 공식문서

readthedocs link

## 제공하는 기능

1. 영어 문장이 포함된 이미지 데이터에 대해서 OCR(ptical character recognition)을 통한 텍스트 추출

2. 추출된 영어문장 내 중요 문장 3개를 추출 요약  

3. 추출된 3개의 영어문장에 대한 한국어 번역 제공

4. (예정) 추출된 3개의 영어문장에 대한 교정 

5. (예정) 한국어 문장이 포함된 이미지 데이터에 대해서 OCR(ptical character recognition)을 통한 텍스트 추출

## 설치방법

가상환경 여는 방법

### 사전 설치 사항

#### Papago

> extract.py의 아래 부분을 수정하세요.
```python3
how to use ...
```

#### OCR

[OCR_RUN.py](https://github.com/Lainshower/Img3Sum/blob/main/OCR_RUN.py)을 이용하려면 **tesseract** 를 사전에 설치하세요.

**Windows**

https://github.com/UB-Mannheim/tesseract/wiki

**Mac**

```
brew install tesseract
```

**Linux**
  
```
sudo apt-get update
sudo apt-get install libleptonica-dev 
sudo apt-get install tesseract-ocr tesseract-ocr-dev
sudo apt-get install libtesseract-dev
```

### Running on Localhost

> Clone
>```bash
>  $ git clone https://github.com/Lainshower/Img3Sum.git
>```   

> 
>1. conda env export > img3sum.Run yaml 를 실행하세요.
>```python3
>  conda env export > img3sum.yaml
>```
>2. Flask를 설치합니다. flask 공식문서를 참고하세요.<br/>
> [Flask 설치]: https://flask.palletsprojects.com/en/2.0.x/installation/#python-version <br/>
> [버전 확인]: https://flask.palletsprojects.com/en/2.0.x/changes/# <br/>
>3. python app.py 를 실행하세요.
>```python3
>  conda activate 'your env name'
>  python app.py
>```


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
