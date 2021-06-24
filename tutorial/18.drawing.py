import cv2
import numpy as np

src = np.zeros((768, 1366, 3), dtype=np.uint8)

# 직선 그리기 함수(cv2.line)로 입력 이미지에 직선을 그릴 수 있다.
# dst = cv2.line(src, pt1, pt2, color, thickness, lineType, shift)는 입력 이미지(src)에 시작 좌표(pt1)부터
# 도착 좌표(pt2)를 지나는 특정 색상(color)과 두께(thickness)의 직선을 그린다. 추가로 선형 타입(lineType), 비트 시프트(shift)를 설정할 수 있다.
# 설정된 입력값으로 그려진 직선이 포함된 출력 이미지(dst)을 생성한다.
src = cv2.line(src, (100, 100), (1200, 100), (0, 0, 255), 3, cv2.LINE_AA)

# 원 그리기 함수(cv2.circle)로 입력 이미지에 원을 그릴 수 있다.
# dst = cv2.circle(src, center, radius, color, thickness, lineType, shift)는 입력 이미지(src)에 중심점(center)으로부터
# 반지름(radius)크기의 특정 색상(color)과 두께(thickness)의 원을 그린다. 추가로 선형 타입(lineType), 비트 시프트(shift)를 설정할 수 있다.
# 만약, 내부가 채워진 원을 그리는 경우, 두께에 cv2.FILLED을 사용해 내부를 채울 수 있다.
# 설정된 입력값으로 그려진 원이 포함된 출력 이미지(dst)을 생성한다.
src = cv2.circle(src, (300, 300), 50, (0, 255, 0), cv2.FILLED, cv2.LINE_4)

# 사각형 그리기 함수(cv2.rectangle)로 입력 이미지에 원을 그릴 수 있다.
# dst = cv2.rectangle(src, pt1, pt2, color, thickness, lineType, shift)는 입력 이미지(src)에 좌측 상단 모서리 좌표(pt1)부터 우측
# 하단 모서리 좌표(pt2)로 구성된 특정 색상(color)과 두께(thickness)의 사각형을 그립니다. 추가로 선형 타입(lineType), 비트 시프트(shift)를 설정할 수 있다.
# 설정된 입력값으로 그려진 사각형이 포함된 출력 이미지(dst)을 생성한다.
src = cv2.rectangle(src, (500, 200), (1000, 400), (255, 0, 0), 5, cv2.LINE_8)

# 호 그리기 함수(cv2.ellipse)로 입력 이미지에 원을 그릴 수 있다.
# dst = cv2.ellipse(src, center, axes, angle, startAngle, endAngle, color, thickness, lineType, shift)는 입력 이미지(src)에
# 중심점(center)으로부터 장축과 단축(axes) 크기를 갖는 특정 색상(color)과 두께(thickness)의 호를 그린다.
# 각도(angle)는 장축이 기울어진 각도를 의미하며, 시작 각도(startAngle)와 도착 각도(endAngle)를 설정해 호의 형태를 구성합니다.
# 추가로 선형 타입(lineType), 비트 시프트(shift)를 설정할 수 있다.
# 설정된 입력값으로 그려진 호가 포함된 출력 이미지(dst)을 생성한다.
src = cv2.ellipse(src, (1200, 300), (100, 50), 0, 90, 180, (255, 255, 0), 2)

# poly 함수를 사용하는 경우, numpy 형태로 저장된 위치 좌표들이 필요하다.
# n개의 점이 저장된 경우, n 각형을 그릴 수 있다.
pts1 = np.array([[100, 500], [300, 500], [200, 600]])
pts2 = np.array([[600, 500], [800, 500], [700, 600]])

# 내부가 채워지지 않은 다각형 그리기 함수(cv2.polylines)로 입력 이미지에 다각형을 그릴 수 있다.
# dst = cv2.polylines(src, pts, isClosed, color, thickness, lineType, shift)는
# 입력 이미지(src)에 선들의 묶음(pts) 이뤄진 N개의 내부가 채워지지 않은 다각형을 그린다.
# 닫힘 여부(isClosed)를 설정해 처음 좌표와 마지막 좌표의 연결 여부를 설정하며, 설정한 색상(color)과 두께(thickness)의 다각형이 그려진다.
# 추가로 선형 타입(lineType), 비트 시프트(shift)를 설정할 수 있다.
# 설정된 입력값으로 그려진 다각형이 포함된 출력 이미지(dst)을 생성
src = cv2.polylines(src, [pts1], True, (0, 255, 255), 2)

# 내부가 채워진 다각형 그리기 함수(cv2.fillPoly)로 입력 이미지에 다각형을 그릴 수 있다.
# dst = cv2.fillPoly(src, pts, color, thickness, lineType, shift, offset)는
# 입력 이미지(src)에 선들의 묶음(pts) 이뤄진 N개의 내부가 채워지지 않은 다각형을 그린다.
# 설정한 색상(color)과 두께(thickness)의 다각형이 그려진다.
# 추가로 선형 타입(lineType), 비트 시프트(shift), 오프셋(offset)을 설정할 수 있다.
# 오프셋은 좌표를 (x, y)만큼 이동시켜 표시할 수 있다.
# 설정된 입력값으로 그려진 다각형이 포함된 출력 이미지(dst)을 생성한다.
src = cv2.fillPoly(src, [pts2], (255, 0, 255), cv2.LINE_AA)

# 문자 그리기 함수(cv2.putText)로 입력 이미지에 문자를 그릴 수 있다.
# dst = cv2.putText(src, text, org, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin)는
# 입력 이미지(src)에 문자열(text)을 텍스트 박스의 좌측 상단 모서리(org)를 기준으로 문자가 그려진다.
# 설정한 글꼴(fontFace)과 글자 크기(fontScale), 색상(color)과 두께(thickness)의 다각형이 그려진다.
# 추가로 선형 타입(lineType), 기준 좌표(bottomLeftOrigin)를 설정할 수 있다.
# 기준 좌표는 텍스트 박스 좌측 상단 모서리가 아닌 텍스트 박스 좌측 하단 모서리를 사용할 경우 기준 좌표에 true를 지정한다.
# 설정된 입력값으로 그려진 문자가 포함된 출력 이미지(dst)을 생성
src = cv2.putText(src, "EP", (900, 600), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)

cv2.imshow("src", src)
cv2.waitKey()
cv2.destroyAllWindows()