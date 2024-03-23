#Source: https://stackoverflow.com/questions/57291924/code-to-detect-if-a-line-in-a-file-is-unicode-typeerror-string-argument-withou
import glob
from chardet.universaldetector import UniversalDetector

detector = UniversalDetector()
files = glob.glob(r'C:\Users\name\Documents\folder\*.txt')

for filename in files:
    print (filename.ljust(60))
    detector.reset()
    for line in filename:
        detector.feed(line)
        if detector.done: break
    detector.close()
    print (detector.result)