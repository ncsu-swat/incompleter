#Source: https://stackoverflow.com/questions/63647817/attributeerror-module-cv2-cv2-has-no-attribute-createmat
import cv2

def warpImage(image, corners, target):
    mat = cv2.CreateMat(3, 3, cv2.CV_32F)
    cv2.GetPerspectiveTransform(corners, target, mat)
    out = cv2.CreateMat(height, width, cv2.CV_8UC3)
    cv2.WarpPerspective(image, out, mat, cv2.CV_INTER_CUBIC)
    return out


if __name__ == '__main__':
    width, height = 400, 250
    corners = [(171,72),(331,93),(333,188),(177,210)]
    target = [(0,0),(width,0),(width,height),(0,height)]
    image = cv2.imread('fries_warped.jpg')
    out = warpImage(image, corners, target)
    cv2.imwrite('fries_rect.jpg', out)