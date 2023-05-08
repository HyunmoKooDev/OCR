import pytesseract
import cv2
from exif import Image
import numpy as np

# imgSource = 'C://Users//Hyunmo//Desktop//IMG_1447.jpg' # ocr 사진
imgSource = 'C:\\Users\\Hyunmo\\Desktop\\tesst.jpg'  # gps 사진

def getImageSize(image):
    w,h = image.shape
    return w,h

def getImageInfo(imgPath):
    image = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
    h,w = getImageSize(image)
    return image,h,w


# GPS 좌표 뽑기
def getmetaimage(ImgSource):
    try :
        with open(ImgSource, "rb") as f:
            img = Image(f)
        print(img.has_exif)
        print(img.gps_latitude, img.gps_longitude)
    except :
        print("Not Available Data")

def main():
    image,h,w = getImageInfo(imgSource)
    wS = int(w / 3)
    hS = int(h / 3)

    divide = []

    for i in range(3):
        for j in range(3):
            x,y = j *  wS , i * hS
            roi = (x, y, wS, hS)
            divide.append(roi)
    for i, roi in enumerate(divide):
        x,y,w,h = roi
        roi_img = image[y:y+h, x:x+w]
        roi_text = pytesseract.image_to_string(roi_img, lang='eng',
                                               config='--psm 6 -c tessedit_char_whitelist=0123456789')
        # cv2.imshow("toto" , roi_img)
        # cv2.waitKey()
        print(f"ROI {i + 1}: {roi_text}")

    print("======================")
    getmetaimage(imgSource)

if __name__ == '__main__':
    main()

