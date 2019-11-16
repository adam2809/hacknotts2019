import recording as r
import numpy as np
import cv2 as cv

def getBlackPixel():
    return np.array([0,0,0])

def getWhitePixel():
    return np.array([255,255,255])


def pixelsNotSimilar(p1,p2):
    return not np.allclose(p1,p2)


def maskChangedPixels(original,new):
    mask = np.zeros_like(original)
    m=0
    for i,line in enumerate(original):
        for j,pixel in enumerate(line):
            mask[i][j] = getWhitePixel() if pixelsNotSimilar(pixel,new[i][j]) else getBlackPixel()
    return mask


# r.recordNewTestStuff()
video,snap = r.loadTestStuff()
graysnap = cv.cvtColor(snap, cv.COLOR_BGR2GRAY)





# maskedVideo = []
#
# videoLen = len(video)
#
# for i,frame in enumerate(video):
#     print(str(i/videoLen))
#     mask = maskChangedPixels(snap,frame)
#     maskedVideo.append(mask)
#
#
# np.save('maskedVideo.npy',maskedVideo)
# r.playbackVideo(maskedVideo)
