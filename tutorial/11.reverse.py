import cv2

src = cv2.imread("image/test.jpg", cv2.IMREAD_COLOR)

# NOT 연산 함수(cv2.bitwise_not)로 이미지에 NOT 연산을 적용할 수 없다.
# dst = cv2.bitwise_not(src, mask)는 입력 이미지(src), 마스크(mask)로 출력 이미지(dst)을 생성
# 마스크는 Not 연산을 적용할 특정 영역을 의미한다. 마스크 배열이 포함되어있다면 해당 영역만 반전 연산을 적용.
# Tip : not 연산 이외에도 and, or, xor 연산이 존재
dst = cv2.bitwise_not(src)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()