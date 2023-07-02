import cv2 as cv
import numpy as np
camera = cv.VideoCapture(0)
while True:
    _, frame = camera.read()
    cv.imshow('camera',frame)
    laplaction = cv.Laplacian(frame, cv.CV_64F)
    laplaction  = np.uint8(laplaction)
    cv.imshow('laplacetion',laplaction)

    edges = cv.Canny(frame,100,100)
    cv.imshow('Candy',edges)

    if cv.waitKey(5)==ord('x'):
        break
camera.release()
cv.destroyAllWindows()