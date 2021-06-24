import cv2

src = cv2.imread("image/test.jpg", cv2.IMREAD_COLOR)

dst = src.copy()

# 추출할 영역을 roi 이미지를 생성하여 src[높이(행), 너비(열)]로 관심 영역을 설정합니다.
roi = src[000:200, 000:200]

# 추출한 이미지와 같은 크기로 설정하여 해당 위치에 붙인다.
dst[200:400, 200:400] = roi

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()