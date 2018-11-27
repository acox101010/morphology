# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2 
import numpy as np

im_path = (r'C:\Users\Reaper124\.spyder-py3\Scripts\objectCount\die.jpg')

img = cv2.imread(im_path, cv2.IMREAD_GRAYSCALE)

#Add to perform a Gaussian filter
#blur = cv2.GaussianBlur(img,(5,5),0)

_, mask = cv2.threshold(img, 175, 250, cv2.THRESH_BINARY)

kernel = np.ones((1, 1), np.uint8)
dilation = cv2.dilate(mask, kernel)

cv2.imshow("Image", img)
cv2.imshow("Mask", mask)
cv2.imshow("Dilation", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()