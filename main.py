import recording as r
import numpy as np
import cv2 as cv

# def getBlackPixel():
#     return np.array([0,0,0])
#
# def getWhitePixel():
#     return np.array([255,255,255])


def pixelsNotSimilar(p1,p2):
    return abs(p1-p2) > 200


def maskChangedPixels(original,new):
    mask = np.zeros_like(original)
    for i,line in enumerate(original):
        for j,pixel in enumerate(line):
            mask[i][j] = 0 if pixelsNotSimilar(pixel,new[i][j]) else 255
    return mask


def prepImg(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.GaussianBlur(img, (9, 9), 0)
    return img

vid = r.loadVideo('maskedVideo.npy')
reapeating = []
[reapeating.extend(vid) for i in range(100)]
r.playbackVideo(reapeating)



## Masking short video test
# video,snap = r.loadTestStuff()
# snap = prepImg(snap)
#
# maskedVideo = []
# for i,frame in enumerate(video):
#     print(f"Prepping {i} frame")
#     prepped = prepImg(frame)
#
#     print(f"Masking {i} frame")
#     maskedFrame = maskChangedPixels(snap,prepped)
#     maskedVideo.append(maskedFrame)
#
#
# np.save('maskedVideo.npy',maskedVideo)




## Single picture test
# bg = prepImg(np.load('testBackground.npy'))
# frame = prepImg(np.load('testToMask.npy'))
#
# masked = maskChangedPixels(bg,frame)
# _, contours = cv.findContours(masked, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# print(contours)
# cv.drawContours(frame, contours, 0 (0, 255, 0), 3)


# cv.imshow("Snap",bg)
# cv.imshow("Frame",frame)
# cv.imshow("Masked",masked)
# cv.waitKey(100000)
# cv.destroyAllWindows()
