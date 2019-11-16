import recording
import numpy as np

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


video = recording.recordVideo()
snap = recording.takeSnap()
maskedVideo = []

videoLen = len(video)

for i,frame in enumerate(video):
    print(str(i/videoLen))
    mask = maskChangedPixels(snap,frame)
    maskedVideo.append(mask)


recording.playbackVideo(maskedVideo)
