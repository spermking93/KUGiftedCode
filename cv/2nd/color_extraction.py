import cv2

# 이미지파일을 칼라로 가져옴
img_color = cv2.imread('red_rose.jpg')

# 이미지의 높이와 넓이 값을 가져옴
height,width = img_color.shape[:2]

# BGR이미지를 HSV로 변환함
img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

# 범위를 정하여 원하는 색의 범위를 설정함
lower_red = (0, 30, 30)
upper_red = (20, 255, 220)

# 범위를 통해 img_hsv 이미지를 추출함 (범위내에 있으면 흰색, 나머진 검은색)
img_mask = cv2.inRange(img_hsv, lower_red, upper_red)

# binary 이미지(0과 1로 된 이미지)로 마스크를 씌움
img_result = cv2.bitwise_and(img_color, img_color, mask = img_mask)

# 각 이미지들을 출력
cv2.imshow('img_color', img_color)
cv2.imshow('img_mask', img_mask)
cv2.imshow('img_result', img_result)


# 키보드 입력대기
cv2.waitKey(0)

# 컴퓨터 자원을 회수하는 코드
cv2.destroyAllWindows()


