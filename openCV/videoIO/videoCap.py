import cv2

#0번째, 캠을 불러오는 부분
cap = cv2.VideoCapture(0)


#캠으로 화면을 캡쳐하는 부분
ret, img_color = cap.read()

#캡쳐한 화면을 컬러로 불러오는 부분
cv2.imshow("Color", img_color)

#특정한 키 값의 입력을 대기하는 부분
cv2.waitKey(1)

#키가 눌리면 메모리에서 해제하고,
cap.release()

#화면을 끄는 기능
cv2.destroyAllWindows()
