import cv2

#슬라이더(트랙바)를 사용하기 위해 생성시 더미 함수가 필요, 
def nothing(x):
    pass

#트랙바를 설치할 윈도우를 네임드 함수로 생성함(평소에는 작성하지 않아도 됨)
cv2.namedWindow('Binary')

#트랙바(트랙바 이름, 실행윈도우, 최소값, 최대값, 더미값)
cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)

#트랙바 생성시 초기위치 설정(트랙바이름, 실행윈도우, 초기값)
cv2.setTrackbarPos('threshold','Binary', 127)

#이미지 파일을 칼라로 불러옴
img_color = cv2.imread('../input/openCVUbuntu.jpeg', cv2.IMREAD_COLOR)

#칼라이미지를 출력
cv2.imshow('Color', img_color)

#사용자 입력을 대기함
cv2.waitKey(1)

#칼라를 gray scale로 변환
img_gray = cv2. cvtColor(img_color, cv2.COLOR_BGR2GRAY)

#gray scale 이미지를 화면에 출력
cv2.imshow('Gray', img_gray)

#사용자 입력을 대기함
cv2.waitKey(1)

while(True):
    #트랙바의 현재 값을 가져옴
    low = cv2.getTrackbarPos('threshold','Binary')

    #gray scale 이미지를 이진화(0~127은 0, 218~255은 1)
    #threshold(그레이스케일 이미지여야 함, threshold 값, threshold 값을 넘으면 대입할 값, threshold 방법)
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY)

    #이진화된 이미지를 출력
    cv2.imshow('binary', img_binary)
    cv2.imwrite('../output/openCVUbuntu_binary.jpeg', img_binary)

    #사용자 ESC 입력을 대기함
    if cv2.waitKey(1) & 0xFF == 27:
        break

#열린 창에 대한 리소스 회수하고 종료
cv2.destroyAllWindows()
