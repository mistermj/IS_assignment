import cv2
import numpy as np

img = cv2.imread('image_2.jpg')
cv2.imshow("Preview", img)

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#OR

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
cv2.imshow("Preview", res)
cv2.imshow("original", img)
cv2.moveWindow("original", 0, 0)
cv2.waitKey(0)
