import cv2

#0번째, 캠을 불러오는 부분
cap = cv2.VideoCapture(0)

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

    #ESC키 값의 입력을 1초간? 대기하는 부분
    if cv2.waitKey(1) & 0xff == 27:
        break

#키가 눌리면 메모리에서 해제하고,
cap.release()

#화면을 끄는 기능
cv2.destroyAllWindows()
