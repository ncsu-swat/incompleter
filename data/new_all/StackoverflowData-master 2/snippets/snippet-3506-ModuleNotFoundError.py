#Source: https://stackoverflow.com/questions/73122247/attributeerror-module-numpy-core-multiarray-has-no-attribute-from-dlpack
import pandas as pd
import numpy as np

from deepface import (
    DeepFace,
    detectors as DeepFace_detectors
)

import cv2
from cv2 import (
    CascadeClassifier,
)
from mtcnn.mtcnn import MTCNN

from matplotlib import pyplot 
plt.rcParams["axes.grid"] = False
from matplotlib.pyplot import (
    imread,
    imshow
)
from matplotlib.patches import (
    Rectangle, 
    Circle
)
import glob
import os
import time