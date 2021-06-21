import cv2

src = cv2.imread("image/test.jpg", cv2.IMREAD_COLOR)

# 이미지 크기 조절 함수(cv2.resize)로 이미지의 크기를 변경
# dst = cv2.resize(src, dstSize, fx, fy, interpolation)는 입력 이미지(src), 절대 크기(dstSize), 상대 크기(fx, fy), 보간법(interpolation)으로 출력 이미지(dst)을 생성
# 절대 크기는 튜플(Tuple) 형식으로 (너비, 높이)의 값을 할당해 사용
dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)

# 상대 크기는 절대 크기에 (0,0)을 할당한 다음, 상대 크기의 값을 할당해 사용
# 절대 크기에 (0,0)을 할당하는 이유는 fx와 fy에서 계산된 크기가 dsize에 할당되기 때문
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()