import cv2
import numpy as np
img=cv2.imread('lena.jpg')
lr1=cv2.pyrDown(img)
lr2=cv2.pyrDown(lr1)
hr2=cv2.pyrUp(lr2)

cv2.imshow('Orignal image',img)
cv2.imshow('pyDrown 1 image ',lr1)
cv2.imshow('pyDrown 2 image ',lr2)
cv2.imshow('pyrUp 1 image ',hr2)

cv2.waitKey(0)
cv2.destroyAllWindows()
