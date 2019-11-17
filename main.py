import recording as r
import numpy as np
import cv2 as cv
from vfx import VFX
import wave

def recordNewSnapAndVideo(videoName,snapName):
    snap = r.takeSnap()
    np.save(f'testVids/{snapName}.npy',snap)
    input("Click to record video")
    frames = r.recordNFrames(3)
    np.save(f'testVids/{videoName}.npy',frames)


# def takeNFramesThenSnap(videoName,snapName,n):
#     frames = np.zeros((n,480,640,3))
#     for i in range(n):
#         frames[i] = r.takeSnap()
#     snap = r.takeSnap()
#     np.save(f'testVids/{snapName}.npy',snap)
#     input("Click to record video")
#     frames = r.recordNFrames(150)
#     np.save(f'testVids/{videoName}.npy',frames)
#     return np.c


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


NAME = 'shortTest'

# recordNewSnapAndVideo(f'{NAME}Vid',f'{NAME}Snap')
# loadAndDisplayUntilExit(f'{NAME}Vid')

video = np.load(f'testVids/{NAME}Vid.npy')
snap = np.load(f'testVids/{NAME}Snap.npy')

print(video.shape)

# amp = extractNormalizedAmplitudeFromWavFile('lomaylomay5secs.wav',150)
amp = [0.2,0.5,0.7]
colors = [
    np.array([255,0,0]),
    np.array([0,255,0]),
    np.array([0,0,255])
]

vfx = VFX(video,snap)
vfx.maskVideo()
r.playbackVideoUntilExited(vfx.videoWithFX)
vfx.scaleBrightnessWithArray(amp)
r.playbackVideoUntilExited(vfx.videoWithFX)
vfx.applyColoredStrobeFX(colors)

np.save(f'testVids/{NAME}.npy',vfx.videoWithFX)
vid = np.load(f'testVids/{NAME}.npy')
r.playbackVideoUntilExited(vid)
