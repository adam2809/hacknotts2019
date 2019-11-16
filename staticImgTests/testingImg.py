import cv2 as cv
import numpy as np
from PIL import Image

img = cv.imread('/home/adam/code/hacknotts2019/testDiagram.png')

imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imggray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

print(len(contours))
res = cv.drawContours(img,contours,0,(0,255,0),3)


dsp = Image.fromarray(res,'RGB')
dsp.show()
