# Img3Sum

![Crates.io](https://img.shields.io/crates/l/rustc-serialize?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

#### Open-source project that supports translating, summarizing and converting images to text.

## Core Concept

When there is an image with bunch of English sentences, we want to know what the key sentence is in that image. 

This open source project helps you identify important sentences in the image at your earliest convenience.

## Official Document

readthedocs link

## Features

1. Optical character recognition of an image file with English text

2. Summarize extracted English text to 3 sentences 

3. Translate summarized English text to Korean

4. (planned) check for grammatical errors in extracted English text

5. (planned) Optical character recognition of an image file with Korean text

## Installation

가상환경 여는 방법

### Prerequisites

#### Papago

To use Papago translation, you must first register the application at the [Naver Developer Center]  and get a client ID and client secret issued.
> write your private key in [extract.py](https://github.com/Lainshower/Img3Sum/blob/main/extract.py)
>```python
>export CLIENT_ID='Your application's client id'
>export CLIENT_SECRET='Your application's client secret'
>```



Visit **[Naver Developers]** and Log in. if you don't have an ID, please sign up.

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

<img src="https://developers.naver.com/proxyapi/rawgit/naver/naver-openapi-guide/master/ko/papago-apis/images/papago-nmt-01.png" width="650">

**check the client ID and Client Secret**

<img src="https://developers.naver.com/proxyapi/rawgit/naver/naver-openapi-guide/master/ko/papago-apis/images/papago-nmt-02.png" width="650">

**Write your ID and Secrete in [extract.py](https://github.com/Lainshower/Img3Sum/blob/main/extract.py)**
```python
export CLIENT_ID='Your application's client id'
export CLIENT_SECRET='Your application's client secret'
```
<br/>

[Naver Developers]:https://developers.naver.com/main/
[Naver Developer Center]: https://developers.naver.com/apps/#/wizard/register


#### OCR

> chage path in OCR_RUN.py
```python3
how to use ...
```

#### Backend

### Running on Localhost

> Clone

> Run
>1. run conda env export > img3sum.Run yaml
>```python3
>  conda env export > img3sum.yaml
>```
>2. Flask should be installed. Please refer to the flask installation, version page.<br/>
> [Flask Installation]: https://flask.palletsprojects.com/en/2.0.x/installation/#python-version <br/>
> [version]: https://flask.palletsprojects.com/en/2.0.x/changes/# <br/>
>3. Run python app.py
>```python3
>  conda activate 'your env name'
>  python app.py
>```



## Online demos
### (Planned)

## Release

### v0.0.0

## Authors

- Joonwon Jang
  - Github: [@Lainshower](https://github.com/Lainshower)
- GeonYeong Son
  - Github : [GeonYeongSon](https://github.com/GeonYeongSon?tab=repositories)
- YiYoung Yoon
  - Github : [y20ng](https://github.com/y20ng?tab=repositories)
- JuHeon Oh
  - Github : [OZOOOOOH](https://github.com/OZOOOOOH)

## License

Copyright © 2021 [Lainshower](https://github.com/Lainshower).<br />
This project is available under the [Apache-2.0 License](https://github.com/Lainshower/Img3Sum/blob/main/LICENSE).
