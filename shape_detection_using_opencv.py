import numpy as np
import cv2

img=cv2.imread('shapes.jpg')
imgGrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('shapes',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
