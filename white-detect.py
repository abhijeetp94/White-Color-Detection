import cv2
import numpy as np
import math
video= cv2.VideoCapture(0)

while True:

    ret,frame = video.read()
    if not ret:
        video=cv2.VideoCapture(0)
        continue
        frame=cv2.GaussianBlur(orig_frame,(5,5),0)
        res = cv.bitwise_and(frame, frame, mask=mask)
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_yellow=np.array([0,0,175])
    up_yellow=np.array([135,60,245])
    mask=cv2.inRange(hsv,low_yellow,up_yellow)
    edges=cv2.Canny(mask,1,20)
    lines=cv2.HoughLinesP(edges,2,np.pi/180,100,minLineLength=20, maxLineGap=50)
    if lines is not None:
        for line in lines:
          x1, y1 , x2, y2= line[0]
          cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)

    if lines is not None:
        for x1,y1,x2,y2 in lines[0]:
            cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)
            slope=(y2-y1)/(x2-x1)
            print('slope',math.atan(slope))

    else:
        print("No lines")

    cv2.imshow("frame", frame)
    cv2.imshow("edges",edges)
    key = cv2.waitKey(2)
    if key==27:

     break
