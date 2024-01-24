#Source: https://stackoverflow.com/questions/42906206/python-module-nameerror
import cv2
import tkinter as tk
from tkinter.filedialog import askopenfilename


def main():
    framevalues = []
    count = 1
    selectedvideo = askopenfilename()
    selectedvideostring = str(selectedvideo)
    cap = cv2.VideoCapture(selectedvideo)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    while (cap.isOpened()): 
        ret, frame = cap.read()

        # check if read frame was successful
        if ret == False:
                break
        # show frame first
        cv2.imshow('frame',frame)

        # then waitKey
        frameclick = cv2.waitKey(0) & 0xFF

        if frameclick == ord('a'):
            swingTag(cap)

        elif frameclick == ord('r'):
            rewindFrames(cap)

        elif frameclick == ord('s'):
            stanceTag(cap)

        elif frameclick == ord('d'):
            unsureTag(cap)

        elif frameclick == ord('q'):
            with open((selectedvideostring + '.txt'), 'w') as textfile:
                for item in framevalues:
                    textfile.write("{}\n".format(item))
            break

        else:
            continue

    cap.release()
    cv2.destroyAllWindows()

def stanceTag(cap):    
    framevalues.append('0' + ' ' + '|' + ' ' + str(int(cap.get(1))))
    print (str(int(cap.get(1))), '/', length) 
    print(framevalues)

def swingTag(cap):
    framevalues.append('1' + ' ' + '|' + ' ' + str(int(cap.get(1))))
    print (str(int(cap.get(1))), '/', length)
    print(framevalues) 

def unsureTag(cap):
    framevalues.append('-1' + ' ' + '|' + ' ' + str(int(cap.get(1))))
    print (str(int(cap.get(1))), '/', length) 
    print(framevalues)

def rewindFrames(cap):
    cap.set(1,((int(cap.get(1)) - 2)))
    print (int(cap.get(1)), '/', length) 
    framevalues.pop()
    print(framevalues)  






if __name__ == '__main__':
    # this is called if this code was not imported ... ie it was directly run
    # if this is called, that means there is no GUI already running, so we need to create a root
    root = tk.Tk()
    root.withdraw()
    main()