import recording as r
import numpy as np
import cv2 as cv
from vfx import VFX

r.playbackVideo(np.load('testVids/properColoredStrobe.npy'))










# np.save('testVids/properColoredStrobeSnap.npy',r.takeSnap())
# input("Click to film")
# r.saveVideo('testVids/properColoredStrobeVid.npy')

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
