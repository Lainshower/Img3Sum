import pytesseract
import cv2
import numpy as np
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
# Error prevention code


def ocr_from_img(path):

    img_array = np.fromfile(path, np.uint8)
    #한글경로 오류 방지 코드
    img = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)    # img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    adaptive_threshold = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

    text = pytesseract.image_to_string(adaptive_threshold, lang='eng')

    return text

