---
layout: page
title: Features
permalink: /feature
---

### Core Features

1. Optical character recognition of an image file with English text

2. Summarize extracted English text to 3 sentences

3. Translate summarized English text to Korean

### Core Technology

#### TextRank
[TextRank][Img3Sum-textrank] is a graph-based ranking model for text processing which can be used in order to find the most relevant sentences in text and also to find keywords.

#### OCR
OCR program used to extract the text of the image is [pyteseract][Img3Sum-ocr] which is a wrapper for Google's Tesseract-OCR Engine.

#### Web
Backend was built as a [flask][Img3Sum-flask], and frontend was referred to [W3S][Img3Sum-w3s].

#### Papago
[Papago][Img3Sum-papago] is a multilingual machine translation cloud service provided by Naver Corporation.

[Img3Sum-textrank]:https://aclanthology.org/W04-3252/
[Img3Sum-ocr]:https://github.com/madmaze/pytesseract
[Img3Sum-papago]:https://papago.naver.com/
[Img3Sum-flask]:https://flask.palletsprojects.com/en/2.0.x/
[Img3Sum-w3s]:https://www.w3schools.com/