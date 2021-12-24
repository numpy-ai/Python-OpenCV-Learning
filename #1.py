import cv2

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while cv2.waitKey(33) < 0 :
    ret, frame = capture.read()
    cv2.imshow("Videoframe", frame)

capture.release()
cv2.destroyAllWindows()
