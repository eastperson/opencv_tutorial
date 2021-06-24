import cv2

# 내장 카메라 or 외장 카메라 정보 획득
# 보통 노트북 내장 웹캠은 0번, 추가적으로 연결하여 외장 카메라를 사용하는 경우 1~n번
capture = cv2.VideoCapture(0)

# 카메라 너비 640, 카메라 높이 480
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 33ms에 한 번씩 화면을 읽는다.
# 0번 키를 누를 때 까지 무한 루프
while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

# 카메라 장치에서 받아온 메모리 해체
capture.release()
# 특정 윈도우 창만 닫을 수 있다.
cv2.destroyWindow("VideoFrame")