import cv2

#0번째, 캠을 불러오는 부분
cap = cv2.VideoCapture(0)

#동영상저장시 사용할 코덱설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#동영상을 저장(파일명, 코텍명, 프레임, 크기(캡쳐이미지와 동일해야 함))
writer = cv2.VideoWriter('output.avi',fourcc, 30.0, (640, 480))

while(True):
    #캠으로 화면을 캡쳐하는 부분
    ret, img_color = cap.read()

    #캠쳐가 안되면 다시 캡쳐를 진행
    if ret == False:
        continue

    #캡펴한 화면을 회색(grayscale)로 변환하는 부분
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    #캡쳐한 화면을 컬러로 불러오는 부분
    cv2.imshow("Color", img_color)

    #캡쳐한 화면을 흑백으로 불러오는 부분
    cv2.imshow("Gray", img_gray)

    #반복적으로 저장하여 동영상으로 만듬
    writer.write(img_color)

    #ESC키 값의 입력을 1초간? 대기하는 부분
    if cv2.waitKey(1) & 0xff == 27:
        break

#키가 눌리면 메모리에서 해제함
cap.release()

#사용이 끝난 writer 객체를 해제함
writer.release()

#화면을 끄는 기능
cv2.destroyAllWindows()
