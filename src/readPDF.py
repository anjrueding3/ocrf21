try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2


#specify path of tesseract bin cmd
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

img = cv2.imread('/Users/andrewding/Desktop/20074433-images/pdfSample.jpg')

IHDtag = img[638:750, 1175:1438]


cv2.imshow('PO20074433',IHDtag)
cv2.waitKey(0)
cv2.destroyAllWindows()

string = pytesseract.image_to_string(Image.open('src/IHDtag.jpg'))
print(string)
