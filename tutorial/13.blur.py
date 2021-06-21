import cv2

src = cv2.imread("image/test.jpg", cv2.IMREAD_COLOR)

# 단순 흐림 효과 함수(cv2.blur)로 입력 이미지에 흐림 효과를 적용
# 단순 흐림 효과는 각 픽셀에 대해 커널을 적용해 모든 픽셀의 단순 평균을 구하는 연산
# dst = cv2.blur(src, ksize, anchor, borderType)는 입력 이미지(src)를 커널 크기(ksize), 고정점(anchor), 테두리 외삽법(borderType)으로 흐림 효과를 적용한 결과 이미지(dst)를 반환
# 커널, 고정점, 테두리 외삽법에 대한 내용은 다음과 같다.
dst = cv2.blur(src, (9, 9), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()