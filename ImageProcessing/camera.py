import cv2 as cv2
import numpy as np
cv2.namedWindow("CamReadTrial",cv2.WINDOW_AUTOSIZE)
webcam = cv2.VideoCapture(0)
while webcam.isOpened():
    _, frame = webcam.read()
    mask = np.zeros_like(frame)
    height, width, _ = frame.shape
    
    cv2.circle(mask,(width/2,height/2),200,(255,255,255),-1)
    frame = np.bitwise_and(frame, mask)
    
    cv2.imshow("CamReadTrial", frame)
    if cv2.waitKey(20) & 0xFF==27:
        break
    
webcam.release()
cv2.destroyAllWindows()
