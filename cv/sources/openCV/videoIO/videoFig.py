# 도형을 판별하는 방법

import cv2 as cv

# 컨투어내부에 도형의 이름(00각형)을 출력하는 setLabel함수
def setLabel(image, str, contour):
    (text_width, text_height), baseline = cv.getTextSize(str, cv.FONT_HERSHEY_SIMPLEX, 0.7, 1)

    # 주어진 컨투어 내부를 둘러싸는 박스의 크기를 계산(위치, 높이와 너비) 그리고 중간에 도형의 이름을 출력함
    x,y,width,height = cv.boundingRect(contour)
    pt_x = x+int((width-text_width)/2)
    pt_y = y+int((height + text_height)/2)
    cv.rectangle(image, (pt_x, pt_y+baseline), (pt_x+text_width, pt_y-text_height), (200,200,200), cv.FILLED)
    cv.putText(image, str, (pt_x, pt_y), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 1, 8)


# 컬러 이미지를 가져옴
img_color = cv.imread('R_img.PNG', cv.IMREAD_COLOR)
cv.imshow('result', img_color)
cv.waitKey(0)

# 흑백 이미지로 변경
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
cv.imshow('result', img_gray)
cv.waitKey(0)

# 바이너리 이미지로 변경 (배경이 검정색, 흰색이 오브젝트가 되도록 해야함)
ret,img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
cv.imshow('result', img_binary)
cv.waitKey(0)

# 바이너리 이미지에서 이미지속의 컨투어를 검출함 // cv.RETR_EXTERNAL 외곽의 컨투어만 검출 // cv.CHAIN_APPROX_SIMPLE 검출되는 컨투어의 갯수를 줄여줌(직선이면, 양끝점만 저장)
contours, hierarchy = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    # 컨투어를 하나씩 꺼냄
    size = len(cnt)

    # 현재 컨투어를 출력함(아주 많음 / 근사화 이후 많이 줄여줌)
    print(size)

    # 직선으로 컨투어를 근사화
    epsilon = 0.005 * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)

    # 근사화 이후 줄여진 컨투어를 출력함
    size = len(approx)
    print(size)

    # 직선으로 근사화된 컨투어를 컬러 이미지 위에 그려줌 (녹색선, 3굵기)
    cv.line(img_color, tuple(approx[0][0]), tuple(approx[size-1][0]), (0, 255, 0), 3)
    for k in range(size-1):
        cv.line(img_color, tuple(approx[k][0]), tuple(approx[k+1][0]), (0, 255, 0), 3)

    # 직선의 갯수를 정리하여 컨투어 갯수에 따라 이미지 속에 있는 도형의 각형을 이름으로 출력함
    if cv.isContourConvex(approx): #오목하게 들어간 도형을 제외시키는 함수
        if size == 3:
            setLabel(img_color, "triangle", cnt)
        elif size == 4:
            setLabel(img_color, "rectangle", cnt)
        elif size == 5:
            setLabel(img_color, "pentagon", cnt)
        elif size == 6:
            setLabel(img_color, "hexagon", cnt)
        elif size == 8:
            setLabel(img_color, "octagon", cnt)
        elif size == 10:
            setLabel(img_color, "decagon", cnt)
        else:
            setLabel(img_color, str(size), cnt)
    else:
        setLabel(img_color, str(size), cnt)

cv.imshow('result', img_color)
cv.waitKey(0)
