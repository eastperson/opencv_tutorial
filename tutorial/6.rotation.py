import cv2

src = cv2.imread("image/test.jpg", cv2.IMREAD_COLOR)

# 회전의 중심점을 설정하기 위해서 이미지의 속성을 가져온다.
height, width, channel = src.shape

# 이미지의 정중앙(width/2, height/2)을 중심점으로 잡는다. (튜플 형태로 잡는다)
# 2×3 회전 행렬 생성 함수(cv2.getRotationMatrix2D)로 회전 변환 행렬을 계산
# matrix = cv2.getRotationMatrix2D(center, angle, scale (이미지 확대 및 축소 비율)
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)

# 아핀 변환 함수(cv2.warpAffine)로 회전 변환을 계산
# dst = cv2.warpAffine(src, M, dsize)는 원본 이미지(src)에 M(아핀 맵 행렬)을 적용하고 출력 이미지 크기(dsize)로 변형해서 출력 이미지(dst)를 반환
dst = cv2.warpAffine(src, matrix, (width, height))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()