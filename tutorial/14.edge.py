import cv2

src = cv2.imread("image/test.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 소벨 함수(cv2.Sobel)로 입력 이미지에서 가장자리를 검출
# 미분 값을 구할 때 가장 많이 사용되는 연산자이며, 인접한 픽셀들의 차이로 기울기(Gradient)의 크기를 구한다.
# 이때 인접한 픽셀들의 기울기를 계산하기 위해 컨벌루션 연산을 수행

# dst = cv2.Sobel(src, ddepth, dx, dy, ksize, scale, delta, borderType)은 입력 이미지(src)에 출력 이미지 정밀도(ddepth)를 설정하고
# dx(X 방향 미분 차수), dy(Y 방향 미분 차수), 커널 크기(ksize), 비율(scale), 오프셋(delta), 테두리 외삽법(borderType)을 설정하여 결과 이미지(dst)를 반환

# 출력 이미지 정밀도는 반환되는 결과 이미지의 정밀도를 설정
# X 방향 미분 차수는 이미지에서 X 방향으로 미분할 차수를 설정
# Y 방향 미분 차수는 이미지에서 Y 방향으로 미분할 차수를 설정
# 커널 크기는 소벨 마스크의 크기를 설정합니다. 1, 3, 5, 7 등의 홀수 값을 사용하며, 최대 31까지 설정
# 비율과 오프셋은 출력 이미지를 반환하기 전에 적용되며, 주로 시각적으로 확인하기 위해 사용
# 픽셀 외삽법은 이미지 가장자리 부분의 처리 방식을 설정
# Tip : X 방향 미분 차수와 Y 방향 미분 차수는 합이 1 이상이여야 하며, 0의 값은 해당 방향으로 미분하지 않음을 의미
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)

# 라플라시안 함수(cv2.Laplacian)로 입력 이미지에서 가장자리를 검출
# 라플라시안은 2차 미분의 형태로 가장자리가 밝은 부분에서 발생한 것인지, 어두운 부분에서 발생한 것인지 알 수 있다.
# 2차 미분 방식은 X 축과 Y 축을 따라 2차 미분한 합을 의미

# dst = cv2.laplacian(src, ddepth, ksize, scale, delta, borderType)은 입력 이미지(src)에 출력 이미지
# 정밀도(ddepth)를 설정하고 커널 크기(ksize), 비율(scale), 오프셋(delta), 테두리 외삽법(borderType)을 설정하여 결과 이미지(dst)를 반환
# 출력 이미지 정밀도는 반환되는 결과 이미지의 정밀도를 설정
# 커널 크기는 라플라시안 필터의 크기를 설정합니다. 커널의 값이 1일 경우, 중심값이 -4인 3 x 3 Aperture Size를 사용
# 비율과 오프셋은 출력 이미지를 반환하기 전에 적용되며, 주로 시각적으로 확인하기 위해 사용
# 픽셀 외삽법은 이미지 가장자리 부분의 처리 방식을 설정
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)

# 캐니 엣지는 라플라스 필터 방식을 개선한 방식으로 x와 y에 대해 1차 미분을 계산한 다음, 네 방향으로 미분
# 네 방향으로 미분한 결과로 극댓값을 갖는 지점들이 가장자리가 된다.
# 앞서 설명한 가장자리 검출기보다 성능이 월등히 좋으며 노이즈에 민감하지 않아 강한 가장자리를 검출하는 데 목적을 둔 알고리즘

# dst = cv2.Canny(src, threshold1, threshold2, apertureSize, L2gradient)는 입력 이미지(src)를 하위 임곗값(threshold1),
# 상위 임곗값(threshold2) ,소벨 연산자 마스크 크기(apertureSize), L2 그레이디언트(L2gradient)을 설정하여 결과 이미지(dst)를 반환
# 하위 임곗값과 상위 임곗값으로 픽셀이 갖는 최솟값과 최댓값을 설정해 검출을 진행
# 픽셀이 상위 임곗값보다 큰 기울기를 가지면 픽셀을 가장자리로 간주하고, 하위 임곗값보다 낮은 경우 가장자리로 고려하지 않는다.
# 소벨 연산자 마스크 크기는 소벨 연산을 활용하므로, 소벨 마스크의 크기를 설정
# L2 그레이디언트는 L2-norm으로 방향성 그레이디언트를 정확하게 계산할지, 정확성은 떨어지지만 속도가 더 빠른 L1-norm으로 계산할지를 선택
canny = cv2.Canny(src, 100, 255)

cv2.imshow("sobel", sobel)
cv2.imshow("laplacian", laplacian)
cv2.imshow("canny", canny)
cv2.waitKey()
cv2.destroyAllWindows()