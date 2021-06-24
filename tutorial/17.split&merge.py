import cv2

src = cv2.imread("image/image.png", cv2.IMREAD_COLOR)

# 채널 분리 함수(cv2.split)로 이미지에서 채널을 분리할 수 있다.
# mv = cv2.split(src)는 입력 이미지(src)에서 채널을 분리해 단일 채널 이미지 배열(mv)을 생성할 수 있다.
# mv는 목록(list) 형식으로 반환되며, b, g, r 등으로 형태로 각 목록의 원솟값을 변수로 지정할 수 있다.
# 분리된 채널의 순서에 맞게 각 변수에 할당된다.
# Tip : 분리된 채널들은 단일 채널이므로 흑백 색상으로 표현된다.
b, g, r = cv2.split(src)

# 채널 병합 함수(cv2.merge)로 분리된 채널을 병합해 하나의 이미지로 합칠 수 있다.
# dst = cv2.merge(mv)로 단일 채널 이미지 배열(mv)를 병합해 출력 이미지(dst)를 생성한다.
# 채널을 변형한 뒤에 다시 합치거나 순서를 변경해 병합할 수 있다.
# 순서가 변경될 경우, 원본 이미지와 다른 색상으로 표현될 수 있다.
inverse = cv2.merge((r, g, b))

cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
cv2.imshow("inverse", inverse)
cv2.waitKey()
cv2.destroyAllWindows()