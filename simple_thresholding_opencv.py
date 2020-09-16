import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('gradient.png',0)
_, th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
_, th2=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
_, th3=cv.threshold(img,127,255,cv.THRESH_TRUNC)

titles=['Original Image','BINARY','BINARY_INV','TRUNC']
images=[img,th1,th2,th3]

for i in range(6):
    plt.subplot(1,1,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
#cv.imshow('image',img)
#cv.imshow('th1',th1)
#cv.imshow('th2',th2)
#cv.imshow('th3',th3)
plt.show()

#cv.waitKey(0)
#cv.destroyAllWindows()
