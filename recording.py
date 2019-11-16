import cv2 as cv
import numpy as np

WAIT_FOR_KEY = 34

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
        print(f)
        cv.imshow("Frame",f)
        key = cv.waitKey(WAIT_FOR_KEY)
        if(key == 101):
            break
