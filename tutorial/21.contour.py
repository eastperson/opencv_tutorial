import cv2

src = cv2.imread("image/test.jpg", cv2.IMREAD_COLOR)

# 윤곽선(컨투어)를 검출하는 주된 요소는 하얀색의 객체를 검출
# 그러므로 배경은 검은색이며 검출하려는 물체는 하얀색의 성질을 띄게끔 변형
gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
# 이진화 처리 후, 반전시켜 검출하려는 물체를 하얀색의 성질을 띄도록 변환
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)


# cv2.findContours()를 이용하여 이진화 이미지에서 윤곽선(컨투어)를 검색
# cv2.findContours(이진화 이미지, 검색 방법, 근사화 방법)을 의미
# 반환값으로 윤곽선, 계층 구조를 반환
# 윤곽선은 Numpy 구조의 배열로 검출된 윤곽선의 지점들이 담겨있다.
# 계층 구조는 윤곽선의 계층 구조를 의미합니다. 각 윤곽선에 해당하는 속성 정보들이 담겨있다.
contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

# 반복문을 사용하여 검출된 윤곽선을 그리며 해당 윤곽선의 계층 구조를 표시
for i in range(len(contours)):
    # cv2.drawContours()을 이용하여 검출된 윤곽선을 그린다.
    # cv2.drawContours(이미지, [윤곽선], 윤곽선 인덱스, (B, G, R), 두께, 선형 타입)을 의미한다.
    # 윤곽선은 검출된 윤곽선들이 저장된 Numpy 배열이다.
    # 윤곽선 인덱스는 검출된 윤곽선 배열에서 몇 번째 인덱스의 윤곽선을 그릴지를 의미한다.
    # Tip : 윤곽선 인덱스를 0으로 사용할 경우 0 번째 인덱스의 윤곽선을 그리게 됩니다. 하지만, 윤곽선 인수를 대괄호로 다시 묶을 경우, 0 번째 인덱스가 최댓값인 배열로 변경된다.
    # Tip : 동일한 방식으로 [윤곽선], 0과 윤곽선, -1은 동일한 의미를 갖습니다. (-1은 윤곽선 배열 모두를 의미)
    cv2.drawContours(src, [contours[i]], 0, (0, 0, 255), 2)
    cv2.putText(src, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
    print(i, hierarchy[0][i])
    cv2.imshow("src", src)
    cv2.waitKey(0)

cv2.destroyAllWindows()