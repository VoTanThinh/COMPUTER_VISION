import cv2
import numpy as np
import object_detection 



cap = cv2.VideoCapture("HIGHWAY1.mp4")
while True:
    _,frame = cap.read()
    cv2.imshow("Frame", frame)
    #detect objects on frame

        


    key = cv2.waitKey(1)
    if key ==27:
        break


cap.release()
