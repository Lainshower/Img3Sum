
#########################
Installation
#########################

Prerequisites
#############

These are libraries that must be installed for the program to operate normally.
Before proceeding with the program, install the library required by this page.

**requirements** ::

    # If possible, use the version below. There may be an unexpected error.

    aiohttp 
    asgiref==3.4.1
    astroid==2.3.3
    async-timeout==3.0.1
    attrs 
    boto3 
    botocore
    brotlipy==0.7.0
    cachetools
    certifi==2021.10.8
    cffi 
    chardet 
    charset-normalizer
    click==8.0.3
    colorama==0.4.4
    coverage 
    cryptography
    Cython 
    Django==3.2.8
    Flask==1.1.2
    gensim 
    google-api-core 
    google-auth 
    google-cloud-core 
    google-cloud-storage 
    google-crc32c 
    google-resumable-media 
    googleapis-common-protos 
    grpcio 
    gunicorn==20.1.0
    idna 
    importlib-metadata==4.8.1
    isort==4.3.21
    itsdangerous==2.0.1
    Jinja2==3.0.2
    jmespath 
    lazy-object-proxy==1.4.3
    MarkupSafe==2.0.1
    mccabe==0.6.1
    mkl-fft==1.3.1
    mkl-random 
    mkl-service==2.4.0
    multidict 
    numpy 
    opencv-contrib-python==4.5.4.58
    opencv-python==4.5.4.58
    Pillow==8.4.0
    protobuf==3.17.2
    pyasn1
    pyasn1-modules==0.2.8
    pycparser 
    pylint==2.4.4
    pyOpenSSL 
    PySocks 
    pytesseract==0.3.8
    python-dateutil 
    pytz==2021.3
    requests 
    rsa 
    s3transfer 
    scipy 
    six 
    smart-open 
    sqlparse==0.4.2
    typed-ast==1.4.0
    typing-extensions 
    urllib3==1.26.7
    Werkzeug==2.0.2
    win-inet-pton 
    wincertstore==0.2
    yarl 
    zipp==3.6.0


External Source
###############

We will explain how to install the OCR program and how to install the flask.
And explain how to create a virtual environment and run it on localhost.

Install OCR and Flask before entering the code.

OCR
****************
Install tesseract to use OCR application in `OCR_RUN.py <https://github.com/Lainshower/Img3Sum/blob/main/OCR_RUN.py>`_.

* **Windows**
   https://github.com/UB-Mannheim/tesseract/wiki/

* **Mac** ::

   brew install tesseract 

* **Linux** ::

   sudo apt-get update
   sudo apt-get install libleptonica-dev 
   sudo apt-get install tesseract-ocr tesseract-ocr-dev
   sudo apt-get install libtesseract-dev


Flask
******************
To use Papago translation, Flask should be installed. Please refer to the flask installation, version page.

.. image:: https://user-images.githubusercontent.com/63241893/140640023-7c37ab45-c5e8-47bc-b135-340afbdda798.jpg
    :height: 250 
    :width: 250 
    :scale: 150
    :alt: Flask Installation Page


`[Flask Installation] <https://flask.palletsprojects.com/en/2.0.x/installation/#python-version/>`_

`[Version Check] <https://flask.palletsprojects.com/en/2.0.x/changes/#/>`_