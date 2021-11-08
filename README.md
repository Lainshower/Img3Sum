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
        <b>English</b> | 
        <a href="https://github.com/Lainshower/Img3Sum/blob/main/README_ko.md">한국어</a>
    <p>
</h4>
        
#### Open-source project that supports translating, summarizing and converting images to text.

## Core Concept

When there is an image with bunch of English sentences, we want to know what the key sentence is in that image. 

This open source project helps you identify important sentences in the image at your earliest convenience.

## Official Document

(updating) [Img3Sum Offical Document](https://img3sum.readthedocs.io/)

## Features

1. Optical character recognition of an image file with English text

2. Summarize extracted English text to 3 sentences 

3. Translate summarized English text to Korean

4. (planned) check for grammatical errors in extracted English text

5. (planned) Optical character recognition of an image file with Korean text

## How to Run?

### Prerequisites & Installation

>**Papago API**

To use Papago translation, you must first register the application at the [Naver Developer Center]  and get a client ID and client secret issued.
write your private key in [extract.py](https://github.com/Lainshower/Img3Sum/blob/main/extract.py)<br/>

```python
>export CLIENT_ID='Your application's client id'
>export CLIENT_SECRET='Your application's client secret'
```

Visit **[Naver Developers]** and Log in. If you don't have an ID, please sign up.

1. Select **Application > Application Registration** from the menu of Naver Developer Center.
2. The application details on the Application Registration (API Application) page are as follows:<br/>
        a. Enter the name of the application you want to register in the application name.<br/>
        b. Select and add Papago translation from the API used.<br/>
        c. Add an environment to service the application in a non-logged open API service environment and enter the necessary details.<br/>
3. When the application is registered normally, a submenu is created under the **Application > My Application** menu in the Naver Developer Center.
4. By clicking the application name, you can **check the client ID and client secret** assigned to the application on the Overview tab.
5. Add your Client ID and Client Secret in [extract.py](https://github.com/Lainshower/Img3Sum/blob/main/extract.py)
<br/>

**Register Application**

<img src="https://developers.naver.com/proxyapi/rawgit/naver/naver-openapi-guide/master/ko/papago-apis/images/papago-nmt-01.png" width="600">

**Check client ID and Client Secret**

<img src="https://developers.naver.com/proxyapi/rawgit/naver/naver-openapi-guide/master/ko/papago-apis/images/papago-nmt-02.png" width="600">

<br/>

[Naver Developers]:https://developers.naver.com/main/
[Naver Developer Center]: https://developers.naver.com/apps/#/wizard/register


>**OCR**

Install **tesseract** to use OCR application in [OCR_RUN.py](https://github.com/Lainshower/Img3Sum/blob/main/OCR_RUN.py)

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

To use Papago translation, Flask should be installed. Please refer to the flask installation, version page.<br/>

<img src="https://user-images.githubusercontent.com/63241893/140640023-7c37ab45-c5e8-47bc-b135-340afbdda798.jpg" width="50%"><br/>

[Flask Installation]: https://flask.palletsprojects.com/en/2.0.x/installation/#python-version <br/>

[Version Check]: https://flask.palletsprojects.com/en/2.0.x/changes/# <br/>

### Running on Localhost

> Clone

```bash
  $ git clone https://github.com/Lainshower/Img3Sum.git
```   

> Run

1. Create conda environment 
```bash
  $ conda create --name 'your env name'
```

2. Unpackage our conda environment configuration
```bash
  $ conda env create --file img3sum.yaml
```

3. Activate conda environment
```bash
  $ conda activate 'your env name'
```

4. Run [app.py](https://github.com/Lainshower/Img3Sum/blob/main/app.py)
```bash
  $ python app.py
```

## Demos

<p align="center">
        <img alt="License" src="https://postfiles.pstatic.net/MjAyMTExMDhfODkg/MDAxNjM2MzQyODAyMDM0.6WSr4WG-dQ5dEjKT4jz6P7lAbrHd6oEuB0uP7iMUwz4g.WEN1m-qjhFA_Q5NX85auseKWbhOtgELLW-Ct9ySS6Fog.JPEG.kaoara/Img3SumDemo3.jpeg?type=w773">
</p>     

## Release

### v0.0.0

## Authors

- Joonwon Jang
  - Github: [Lainshower](https://github.com/Lainshower)
- GeonYeong Son
  - Github : [GeonYeongSon](https://github.com/GeonYeongSon?tab=repositories)
- YiYoung Yoon
  - Github : [y20ng](https://github.com/y20ng?tab=repositories)
- JuHeon Oh
  - Github : [OZOOOOOH](https://github.com/OZOOOOOH)

## License

Copyright © 2021 [Lainshower](https://github.com/Lainshower).<br />
This project is available under the [Apache-2.0 License](https://github.com/Lainshower/Img3Sum/blob/main/LICENSE).
