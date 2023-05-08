import pytesseract
import cv2
from exif import Image
import easyocr

imgSource = 'C://Users//Hyunmo//Desktop//IMG_1447.jpg' # ocr 사진
# imgSource = 'C:\\Users\\Hyunmo\\Desktop\\tesst.jpg'  # gps 사진
output = 'C://Users//Hyunmo//PycharmProjects//ocr//output.jpg'
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

# def main():
#     image,h,w = getImageInfo(imgSource)
#     wS = int(w / 4)
#     hS = int(h / 4)
#     image_crop = image[wS*1: wS*2, hS*2: hS*4]
#     cv2.imshow("new", image_crop)
#     # text = pytesseract.image_to_string(image_crop, lang = 'eng')
#     text = pytesseract.image_to_string(image_crop,config='--psm 6')
#     print(text)
#     print("=========")
#     getmetaimage(imgSource)
#     cv2.waitKey()

def main():
    image,h,w = getImageInfo(imgSource)
    wS = int(w / 4)
    hS = int(h / 4)
    image_crop = image[wS*1: wS*2, hS*2: hS*4]
    # cv2.imshow("new", image_crop)
    # text = pytesseract.image_to_string(image_crop, lang = 'eng')
    # cv2.imwrite("output.jpg", image_crop)
    reader = easyocr.Reader(['ko','en'], gpu=False)
    img = cv2.imread(output,cv2.IMREAD_GRAYSCALE)
    # cv2.imshow("name", img)
    text = reader.readtext(img, detail = 0)
    print(text)

if __name__ == '__main__':
    main()

