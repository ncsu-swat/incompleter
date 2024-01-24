# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73122247/attributeerror-module-numpy-core-multiarray-has-no-attribute-from-dlpack
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(585302)

except ImportError:
    pass
try:
    import numpy as np
    _l_(585304)

except ImportError:
    pass
try:
    from deepface import (
        DeepFace,
        detectors as DeepFace_detectors
    )
    _l_(585306)

except ImportError:
    pass
try:
    import cv2
    _l_(585308)

except ImportError:
    pass
try:
    from cv2 import (
        CascadeClassifier,
    )
    _l_(585310)

except ImportError:
    pass
try:
    from mtcnn.mtcnn import MTCNN
    _l_(585312)

except ImportError:
    pass
try:
    from matplotlib import pyplot
    _l_(585314)

except ImportError:
    pass
_a_(585316, _n_(585315, "plt", lambda: plt), "rcParams")["axes.grid"] = False
_l_(585317)
try:
    from matplotlib.pyplot import (
        imread,
        imshow
    )
    _l_(585319)

except ImportError:
    pass
try:
    from matplotlib.patches import (
        Rectangle, 
        Circle
    )
    _l_(585321)

except ImportError:
    pass
try:
    import glob
    _l_(585323)

except ImportError:
    pass
try:
    import os
    _l_(585325)

except ImportError:
    pass
try:
    import time
    _l_(585327)

except ImportError:
    pass