import cv2
capture = cv2.VideoCapture('VideoFromCamera.mp4')
while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('video', rgb)
        k = cv2.waitKey(50)
        if k == 27:
            break
capture.release()
cv2.destoryALLWINDOWs()