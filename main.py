import cv2 as cv
import numpy as np

img = cv.imread('testImg.jpg')

imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imggray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img,contours,-1,(0,255,0),3)
