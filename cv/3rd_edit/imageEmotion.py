import cv2
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.models import load_model

# 얼굴 인식 XML 파일과 감정 인식 학습 데이터 hdf5 파일을 불러옴
face_detection = cv2.CascadeClassifier('haarcascade_frontalface.xml')
emotion_classifier = load_model('emotion_model.hdf5', compile=False)
EMOTIONS = ["Angry", "Disgusting", "Fearful", "Happy", "Sad", "Surpring", "Neutral"]

# 이미지 불러오기
camera = cv2.VideoCapture("face.jpg")

while True:
    # camera 로부터 이미지를 캡처
    ret, frame = camera.read()

    # gray scale로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # frame 에서 얼굴을 찾음
    faces = face_detection.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 얼굴이 찾아진 경우에만 감정 인식을 실행
    if len(faces) > 0:
        # 가장 큰 이미지에 대해서 실행
        face = sorted(faces, reverse=True, key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
        (fX, fY, fW, fH) = face
        # 이미지를 48x48 사이즈로 재조정 (neural network 위함)
        roi = gray[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (48, 48))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)

        # 감정을 예측 
        preds = emotion_classifier.predict(roi)[0]
        emotion_probability = np.max(preds)
        label = EMOTIONS[preds.argmax()]

        # 각 감정의 예측값을 출력하는 코드
        #####################################
        #                                   #
        #                                   #
        #####################################


    # 이미지를 보여줌 ("Emotion Recognition")
    cv2.imshow('Emotion Recognition', frame)

    # q 를 눌러 종료
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

# 프로그램을 clear 하고 창을 닫음
camera.release()
cv2.destroyAllWindows()