import cv2

#
capture = cv2.VideoCapture("video/test.mp4")

# capture.get()은 비디오 속상을 반환하는 메서드이다.
# 현재 반환하는 프레임(capture.get(cv2.CAP_PROP_POS_FRAMES))과 동영상의 총 프레임수가 같다면 현재 재생하고 있는 프레임(capture.get(cv2.CAP_PROP_FRAME_COUNT))이 마지막이 된다.
# 마지막 프레임이 되면 종료를 한다. capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
while cv2.waitKey(33) < 0:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()