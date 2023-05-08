path = 'C://Users//Hyunmo//Desktop//IMG_1447.jpg'
#
# image = cv2.imread(path)
# rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
# text = pytesseract.image_to_string(rgb_image, lang='kor+eng')
# print(text)


# img  =  cv2.imread(path, cv2.IMREAD_GRAYSCALE)
#
# print('img.shape', img.shape)
#
# h,w = img.shape
#
# print('height', h)
# print('width',w)






# # 사각형을 그리는 함수
# def setLabel(img, pts, label):
#     # 사각형 좌표 받아오기
#     (x, y, w, h) = cv2.boundingRect(pts)
#     pt1 = (x, y)
#     pt2 = (x + w, y + h)
#     cv2.rectangle(img, pt1, pt2, (0, 0, 255), 1)
#     cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
#
#
# def main():
#     img = cv2.imread(path, cv2.IMREAD_COLOR)
#
#     if img is None:
#         print('Image load failed!')
#         return
#
#     img = cv2.resize(img, dsize=(1500, 1500))
#
#     # 그레이스케일 영상으로 변환
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # 이진화, INV 이유는 배경이 흰색, 객체가 어두운 영상이므로
#     _, img_bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
#
#     # 외곽선 검출, EXTERNAL로 바깥 외곽선만 도출
#     contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#
#     # 외곽선 좌표 받아오기
#     for pts in contours:
#         if cv2.contourArea(pts) < 400:  # 노이즈 제거, 너무 작으면 무시
#             continue
#
#         # 근사화
#         approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)
#
#         # 근사화 결과 점 갯수
#         vtc = len(approx)
#
#         # 3이면 삼각형
#         if vtc == 3:
#             setLabel(img, pts, 'TRI')
#         # 4면 사각형
#         elif vtc == 4:
#             setLabel(img, pts, 'RECT')
#         else:
#             length = cv2.arcLength(pts, True)
#             area = cv2.contourArea(pts)
#             ratio = 4. * math.pi * area / (length * length)
#
#             if ratio > 0.85:
#                 setLabel(img, pts, 'CIR')
#
#     cv2.imshow('img', img)
#     cv2.waitKey()
#     cv2.destroyAllWindows()
#
#
# if __name__ == '__main__':
#     main()
