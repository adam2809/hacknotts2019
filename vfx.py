import cv2 as cv
import numpy as np

class VFX:
    def __init__(self,video,snap):
        self.video = video
        self.videoWithFX = video
        self.snap = snap


    def maskVideo(self):
        maskedVideo = []
        preppedSnap = self.prepImg(self.snap)
        for i,frame in enumerate(self.video):
            print(f"Prepping {i} frame")
            prepped = self.prepImg(frame)

            print(f"Masking {i} frame")
            maskedFrame = self.maskChangedPixels(preppedSnap,prepped)
            maskedVideo.append(maskedFrame)

        self.videoWithFX = np.array(maskedVideo)


    def pixelsNotSimilar(self,p1,p2):
        return abs(p1-p2) > 200


    def maskChangedPixels(self,original,new):
        mask = np.zeros_like(original)
        for i,line in enumerate(original):
            for j,pixel in enumerate(line):
                mask[i][j] = 0 if self.pixelsNotSimilar(pixel,new[i][j]) else 255
        return mask


    def prepImg(self,img):
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.GaussianBlur(img, (9, 9), 0)
        return img


    def applyColoredStrobeFX(self,colors):
        newShape = (*self.videoWithFX.shape,3)
        res = self.repeatVideoNTimes(np.zeros(newShape),len(colors))
        print('dupers')
        shape0 = res.shape[0]
        for i in range(shape0):
            print(f"Colored strobing frame {i} of {shape0}")
            res[i] = self.changeAllWhitePixelsToColor(self.videoWithFX[int(i/len(colors))],colors[i%len(colors)])

        self.videoWithFX = res



    def repeatVideoNTimes(self,video,n):
        reapeating = []
        for i in range(n):
            reapeating.append(video)
        return np.concatenate(reapeating)


    def changeAllWhitePixelsToColor(self,frame,color):
        res = np.zeros((*frame.shape,3))
        for i in range(frame.shape[0]):
            for j in range(frame.shape[1]):
                if frame[i][j] == 255:
                    res[i][j] = color
        return res


    def scaleBrightnessWithArray(self,array):
        # if not len(array) == self.videoWithFX.shape[0]:
        #     print('Could not modify brightness because array length doesnt equal the number of frames' )
        for i,frame in enumerate(self.videoWithFX):
            print(f'Scaling frame {i} of {self.videoWithFX.shape[0]} with {array[i]}')
            for j,line in enumerate(frame):
                for k,pixel in enumerate(line):
                    self.videoWithFX[i][j][k] = np.array([v*array[i] for v in pixel])
