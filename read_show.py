import cv2
from matplotlib import pyplot as plt

image = cv2.imread('image_2.jpg', 0)
plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

# cv2.imshow("Preview", image)
# cv2.waitKey(0)