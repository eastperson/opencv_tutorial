import cv2

src = cv2.imread("image/test.jpg", cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)


# 빨간색 영역은 0 ~ 5, 170 ~ 179의 범위로 두 부분으로 나뉘어 있다.
# 이때, 두 부분을 합쳐서 한 번에 출력하기 위해서 사용한다.
# 배열 요소의 범위 설정 함수(cv2.inRange)를 사용하여 빨간색 영역의 범위를 검출한다.
# 배열 요소 범위 설정 함수는 다채널 이미지도 한 번에 범위를 설정한다.
lower_red = cv2.inRange(hsv, (0, 100, 100), (5, 255, 255))
upper_red = cv2.inRange(hsv, (170, 100, 100), (180, 255, 255))

# 색상을 분리한 두 배열을 배열 병합 함수(cv2.addWeighted)로 입력된 두 배열의 하나로 병합한다.
# dst = cv2.addWeighted(src1, alpha, src2, beta, gamma, dtype = None)은 입력 이미지1(src1)에 대한
# 가중치1(alpha) 곱과 입력 이미지2(src2)에 대한 가중치2(beta) 곱의 합에 추가 합(gamma)을 더해서 계산한다.
# 정밀도(dtype)는 출력 이미지(dst)의 정밀도를 설정하며, 할당하지 않을 경우, 입력 이미지1과 같은 정밀도로 할당한다.
# 두 이미지를 그대로 합칠 예정이므로, 가중치1과 가중치2의 값은 1.0으로 사용하고, 추가 합은 사용하지 않으므로 0.0을 할당한다.
added_red = cv2.addWeighted(lower_red, 1.0, upper_red, 1.0, 0.0)

red = cv2.bitwise_and(hsv, hsv, mask = added_red)
red = cv2.cvtColor(red, cv2.COLOR_HSV2BGR)

cv2.imshow("red", red)
cv2.waitKey()
cv2.destroyAllWindows()