import cv2 as cv
import numpy as np

WAIT_FOR_KEY = 200

# Starts on calling the function ends when e pressed
def recordVideo():
    cap = cv.VideoCapture(0)
    recording = []
    while True:
        _, frame = cap.read()

        cv.imshow("Frame", frame)
        recording.append(frame.copy())

        key = cv.waitKey(WAIT_FOR_KEY)
        if(key == 101):
            break

    cap.release()
    cv.destroyAllWindows()

    return recording


# Takes snap and returns it on e key press and exits
def takeSnap():
    return recordVideo()[-1]


def playbackVideo(frames):
    for f in frames:
        cv.imshow("Frame",f)
        key = cv.waitKey(WAIT_FOR_KEY)
        if(key == 101):
            break
    cv.destroyAllWindows()


def playbackVideoUntilExited(frames):
    exit = False
    while True:
        if exit:
            break
        for f in frames:
            cv.imshow("Frame",f)
            key = cv.waitKey(WAIT_FOR_KEY)
            if(key == 101):
                exit = True
                break
    cv.destroyAllWindows()


def saveVideo(file):
    video = recordVideo()
    np.save(file,video)


def loadVideo(file):
    return np.load(file)


def recordNewTestStuff():
    np.save('testSnap.npy',takeSnap())
    saveVideo("testVideo.npy")


def loadTestStuff():
    return loadVideo('testVideo.npy'),np.load('testSnap.npy')


def playbackTestStuff():
    cv.imshow("Snap",np.load('testSnap.npy'))
    playbackVideo(loadVideo('testVideo.npy'))
    cv.destroyAllWindows()


def displayImg(img):
    cv.imshow("Img",img)
    key = cv.waitKey(100000)
    if(key>0):
        cv.destroyAllWindows()


def recordNFrames(n):
    cap = cv.VideoCapture(0)
    recording = []
    for i in range(n):
        _, frame = cap.read()

        cv.imshow("Frame", frame)
        recording.append(frame.copy())

        key = cv.waitKey(WAIT_FOR_KEY)
        if(key == 101):
            break

    cap.release()
    cv.destroyAllWindows()

    return recording
