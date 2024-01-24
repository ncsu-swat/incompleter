# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48971429/python-attribute-error-im-not-sure-what-is-causing-this-is-it-because-my-web-c
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
     import cv2
     _l_(681526)

except ImportError:
     pass
try:
     import numpy as np
     _l_(681528)

except ImportError:
     pass

cap = _c_(681531, _a_(681530, _n_(681529, "cv2", lambda: cv2), "Videocapture"), 0)
_l_(681532)
while True:
     _l_(681549)

     ret,frame = _c_(681535, _a_(681534, _n_(681533, "cap", lambda: cap), "read"))
     _l_(681536)
     _c_(681540, _a_(681538, _n_(681537, "cv2", lambda: cv2), "imshow"), 'frame',_n_(681539, "frame", lambda: frame))
     _l_(681541)
     if _c_(681544, _a_(681543, _n_(681542, "cv2", lambda: cv2), "waitKey"), 1) & 0xFF == _c_(681546, _n_(681545, "ord", lambda: ord), 'q'):
          _l_(681548)

          break
          _l_(681547)
_c_(681552, _a_(681551, _n_(681550, "cap", lambda: cap), "release"))
_l_(681553)
_c_(681556, _a_(681555, _n_(681554, "cv2", lambda: cv2), "destroyAllWindows"))
_l_(681557)