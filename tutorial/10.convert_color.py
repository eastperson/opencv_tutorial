import cv2

src = cv2.imread("image/test.jpg", cv2.IMREAD_COLOR)

# dst = cv2.cvtcolor(src, code, dstCn)는 입력 이미지(src), 색상 변환 코드(code), 출력 채널(dstCn)으로 출력 이미지(dst)을 생성
# 색상 변환 코드는 원본 이미지 색상 공간 결과 또는 이미지 색상 공간을 의미
# 원본 이미지 색상 공간은 원본 이미지와 일치
# 출력 채널은 출력 이미지에 필요한 채널의 수를 설정
# Tip : BGR은 RGB 색상 채널을 의미합니다. (Byte 역순)
# Tip : 출력 채널은 기본값을 사용하여 자동으로 채널의 수를 결정
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)



# 원본 이미지 색상 공간은 원본 이미지와 일치
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()