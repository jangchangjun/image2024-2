#x,y,w,h = cv2.selectROI('img', img, False)
#selectRoi 직접 만들기
import cv2

def onMouse(event, x, y, flags, param):
    if(event == cv2.EVENT_LBUTTONDOWN):
        print("lbutton down")
        print(x, y)
        x0=x; y0=y
    elif(event == cv2.EVENT_MOUSEMOVE):
        # print("mouse move")
        # print(x, y)
        xx = 1
    elif(event == cv2.EVENT_LBUTTONUP):
        print("lbutton up")
        print(x,y)
        x1=x; y1=y


img = cv2.imread('./img/sunset.jpg')
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse)
cv2.waitKey()
cv2.destroyAllWindows()
