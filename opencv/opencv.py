import numpy as np
import cv2

img = cv2.imread('image.jpg')
print(img.shape)

# ************************************************** resize.
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

resized = cv2.resize(img, (100, 100))

cv2.imshow('image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
