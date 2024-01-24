#Source: https://stackoverflow.com/questions/64627848/attributeerror-numpy-ndarray-object-has-no-attribute-imwrite
import cv2
img = cv2.imread("input.jpg")
img.imwrite("output.jpg")