import cv2 as cv                
#video = cv.VideoCapture(0) dùng cho cam máy tính
video = cv.VideoCapture('nhóm Quỳnh túi.mp4')
subtractor = cv.createBackgroundSubtractorMOG2(30,50)

while True:
    ret, frame = video.read()

    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('mask',mask)

        if cv.waitKey(5) == ord('x'):
            break
    else:
        video = cv.VideoCapture('nhóm Quỳnh túi.mp4')

cv.waitKey(0)
cv.destroyAllWindows()
video.release()
