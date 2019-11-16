import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

snap = np.zeros((480,640))
snapped = False

def getBlackPixel():
    return np.array([0,0,0])

def getWhitePixel():
    return np.array([255,255,255])


def pixelsDifferent(p1,p2):
    return not np.array_equal(p1,p2)


def maskChangedPixels(original,new):
    mask = np.zeros_like(original)
    for i,line in enumerate(original):
        for j,pixel in enumerate(line):
            mask[i][j] = getWhitePixel() if pixelsDifferent(pixel,new[i][j]) else getBlackPixel()
    return mask


while True:
    _, frame = cap.read()
    blurred_frame = cv.GaussianBlur(frame, (5, 5), 0)
    hsv = cv.cvtColor(blurred_frame, cv.COLOR_BGR2HSV)

    # if(snapped):
    #     mask = maskChangedPixels(frame,snap)
    #     cv.imshow("Mask", mask)

    cv.imshow("Frame", frame)



    key = cv.waitKey(100)
    if(key == 101):
        break

    if(key == 115):
        snap = frame.copy()
        snapped = True

    cv.imshow("Snap", snap)



cap.release()
cv.destroyAllWindows()
