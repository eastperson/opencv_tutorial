import cv2

src = cv2.imread("image/test.jpg", cv2.IMREAD_COLOR)

# 이미지 속성을 가져와서 출력 이미지 크기를 설정할 수 있다.
height, width, channel = src.shape

# 이미지 확대 함수(cv2.pyrUp)
# dst = cv2.pyrUp(src, dstSize, borderType)는 입력 이미지(src), 출력 이미지 크기(dstSize), 테두리 외삽법(borderType)으로 출력 이미지(dst)을 생성
dst = cv2.pyrUp(src, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT)

# 이미지 축소 함수는 
dst2 = cv2.pyrDown(src)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()