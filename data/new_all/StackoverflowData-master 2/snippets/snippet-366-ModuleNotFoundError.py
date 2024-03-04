#Source: https://stackoverflow.com/questions/44714626/how-to-solve-the-typeerror-nonetype-object-is-not-subscriptable-in-opencv-cv
import numpy as np
import cv2
img = cv2.imread('freelancer.jpg',cv2.IMREAD_COLOR)
px  = img[55,55]
print(px)