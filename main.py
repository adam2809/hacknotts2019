import recording as r
import numpy as np
import cv2 as cv
from vfx import VFX
import wave

def recordNewSnapAndVideo(videoName,snapName):
    snap = r.takeSnap()
    np.save(f'testVids/{snapName}.npy',snap)
    input("Click to record video")
    frames = r.recordNFrames(150)
    np.save(f'testVids/{videoName}.npy',frames)


def loadAndDisplayUntilExit(filename):
    r.playbackVideoUntilExited(np.load(f'testVids/{filename}.npy'))


def extractNormalizedAmplitudeFromWavFile(file,desiFrames):
    wav = wave.open(file)
    params = wav.getparams()
    frameCount = params[3]
    string = wav.readframes(frameCount)
    wav.close()

    npStr=np.absolute(np.fromstring(string,np.int16))

    blockSize = int(len(npStr)/desiFrames)
    blockMaximums = []
    for i in range(0,len(npStr),blockSize):
        blockMaximums.append(max(npStr[i:i+blockSize]))

    maxOfBlocks = max(blockMaximums)
    return list(map(lambda x:x/maxOfBlocks,blockMaximums))


# snap = np.load('testVids/vidWith150Frames.npy')
# video = np.load('testVids/snapWith150Frames.npy')

loadAndDisplayUntilExit('lomayTest')


# amp = extractNormalizedAmplitudeFromWavFile('lomaylomay5secs.wav',150)
# vfx = VFX(np.ones((150,480,640,3)),np.ones((480,640,3)))
# vfx.scaleBrightnessWithArray(amp)
# np.save('testVids/lomayTest.npy',vfx.videoWithFX)

## The making of proper colored strobe
# np.save('testVids/properColoredStrobeSnap.npy',r.takeSnap())
# input("Click to film")
# r.saveVideo('testVids/properColoredStrobeVid.npy')
#
# vid = r.loadVideo('testVids/properColoredStrobeVid.npy')
# snap = np.load('testVids/properColoredStrobeSnap.npy')
#
# vfx = VFX(vid,snap)
# vfx.maskVideo()
# colors = [
#     np.array([255,0,255]),
#     np.array([255,0,0]),
#     np.array([0,0,0]),
#     np.array([0,0,255]),
#     np.array([255,255,0])
# ]
# vfx.applyColoredStrobeFX(colors)
# np.save('testVids/properColoredStrobe.npy',vfx.videoWithFX)
