import cv2

src = cv2.imread("image/test.jpg", cv2.IMREAD_COLOR)

# flipCode < 0은 XY 축 대칭(상하좌우 대칭)을 적용
# flipCode = 0은 X 축 대칭(상하 대칭)을 적용
# flipCode > 0은 Y 축 대칭(좌우 대칭)을 적용
dst = cv2.flip(src, 1)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()