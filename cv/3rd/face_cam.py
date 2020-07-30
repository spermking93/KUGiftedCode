import cv2

# 웹캠에서 영상을 읽음
cap = cv2.VideoCapture(0)
cap.set(3, 640) # WIDTH
cap.set(4, 480) # HEIGHT

# 얼굴 인식 캐스케이드 파일 읽음
#cascadeClassifier은 영상 이미지 내에서 찾고자하는 물체 (얼굴)을 찾는 기능을 수행함.
#구체적으로는 이미지 전체를 가변적인 크기의 스캔을 진행하여 목표하는 객체를 탐색하는 함수.

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_facecam.xml')

while(True):
    # frame(하나의 이미지) 별로 capture 함 
    ret, frame = cap.read()

    #각 프레임의 이미지를 BGR(blue/green/red) 에서 gray(회색)으로 색상을 변환하고 변수 gray에 저장함.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #변환된 이미지를 이용하여 얼굴을 찾음.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 인식된 얼굴 갯수를 출력 / 인식된 얼굴이 1개 이상일때 개수를 출력
    if(len(faces)>0):
        print(len(faces))

    # 인식된 얼굴들에 사각형을 출력
    for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # 화면(캠)에 출력(Q키를 누른 경우 종료함)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#종료되면 캠을 해제하고, 화면리소스를 운영체제에 반환
cap.release()
cv2.destroyAllWindows()