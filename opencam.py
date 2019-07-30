import cv2

cv2.namedWindow("Session")

capture = cv2.VideoCapture(0)

if capture.isOpened():
    ret, frame = capture.read()
else:
    ret = False

while ret:
    cv2.imshow("Preview", frame)
    ret, frame = capture.read()
    key = cv2.waitKey(20)

    if key == 27:
        break

cv2.destroyAllWindows()
capture.release()

