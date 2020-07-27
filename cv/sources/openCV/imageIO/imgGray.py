from cv2 import cv2

#이미지를 칼라와 흑백 둘다 사용

print("Image converting has been started ... ")
#이미지파일을 불러오기(이미지파일(절대.상대경로 가능, 플래그(칼라,흑백,알파값등)
img_color = cv2.imread('../input/openCVUbuntu.jpeg', cv2.IMREAD_COLOR)

#named함수를 사용하여 윈도우생성
cv2.namedWindow('Show Imgae')

#이미지를 윈도우 화면에 출력(윈도우 식별자(타이틀), 칼라로 생성))
cv2.imshow('Show Image', img_color)

#이미지를 gray scale로 변환(변환할 대상 이미지, 변환방법)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

#이미지를 윈도우 화면에 출력(윈도우 식별자(타이틀), 흑백으로 생성))
cv2.imshow('Show Gray Image', img_gray)

#이미지를 저장하는 함수 imwrite
cv2.imwrite('../output/openCVUbuntu_grey.jpeg', img_gray)

#대기()을 넣고, 사용자의 입력을 대기함 // 0이면 무한대
cv2.waitKey(1)

#종료시 윈도우 자원 해제
cv2.destroyAllWindows()
print("...Done")
