#using OCR - Optical Character Recognition

import pytesseract as pyt
import cv2

img = cv2.imread("image.png")

pyt.pytesseract.tesseract_cmd = "C:\\Users\\sruja\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

text = pyt.image_to_string(img)

print(text)

