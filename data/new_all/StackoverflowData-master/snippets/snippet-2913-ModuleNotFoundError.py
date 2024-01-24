#Source: https://stackoverflow.com/questions/58572142/typeerror-argument-of-type-windowspath-is-not-iterable
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
from os import listdir

from pathlib import Path

all_images = list(Path(r'D:/face/train').glob('**/*.jpg'))
np.array([np.array(cv2.imread(str(file))).flatten() for file in all_images])
Path = r'D:\face\train'
print(all_images[0])