import datetime
import cv2

capture = cv2.VideoCapture("video/test.mp4")

# fourcc를 생성하여 디지털 미디어 포맷 코드를 생성합니다. cv2.VideoWriter_fourcc(*'코덱')을 사용하여 인코딩 방식을 설정한다.
# record 변수를 생성하여 녹화 유/무를 설정한다.
# Tip : FourCC(Four Character Code) : 디지털 미디어 포맷 코드입니다. 즉, 코덱의 인코딩 방식을 의미한다.
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

while True:
    if (capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("video/test.mp4")

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    # datetime 모듈을 포함하여 현재 시간을 받아와 제목으로 사용
    # ow에 파일의 제목을 설정합니다. 날짜_시간-분-초의 형식으로 제목이 생성
    now = datetime.datetime.now().strftime("%d_%H-%M-%S")

    # key 값에 현재 눌러진 키보드 키의 값이 저장됩니다. 33ms마다 갱신
    key = cv2.waitKey(33)

    # if-elif`문을 이용하여 눌러진 키의 값을 판단
    # 27 = ESC, 26 = Ctrl + Z, 24 = Ctrl + X, 3 = Ctrl + C를 의미

    # ESC키를 눌렀을 경우, 프로그램을 종료
    if key == 27:
        break
    # Ctrl + Z를 눌렀을 경우, 현재 화면을 캡쳐합니다. cv2.imwrite("경로 및 제목", 이미지)를 이용하여 해당 이미지를 저장
    elif key == 26:
        print("캡쳐")
        cv2.imwrite("D:/" + str(now) + ".png", frame)

    # Ctrl + X를 눌렀을 경우, 녹화를 시작합니다. video에 녹화할 파일 형식을 설정
    # cv2.VideoWriter("경로 및 제목", 비디오 포맷 코드, FPS, (녹화 파일 너비, 녹화 파일 높이))를 의미
    elif key == 24:
        print("녹화 시작")
        record = True
        video = cv2.VideoWriter("D:/" + str(now) + ".avi", fourcc, 20.0, (frame.shape[1], frame.shape[0]))

    # Ctrl + C를 눌렀을 경우, 녹화를 중지합니다. video.release()를 사용하여 메모리를 해제
    # 녹화 시작할 때, record를 True로, 녹화를 중지할 때 record를 False로 변경
    elif key == 3:
        print("녹화 중지")
        record = False
        video.release()

    # Tip : key 값은 아스키 값을 사용
    # Tip : FPS(Frame Per Second) : 영상이 바뀌는 속도를 의미합니다. 즉, 화면의 부드러움을 의미
    # Tip : frame.shape는 (높이, 너비, 채널)의 값이 저장

    # if문을 이용하여 record가 True일때 video에 `프레임을 저장
    # video.write(저장할 프레임)을 사용하여 프레임을 저장
    if record == True:
        print("녹화 중..")
        video.write(frame)

capture.release()
cv2.destroyAllWindows()