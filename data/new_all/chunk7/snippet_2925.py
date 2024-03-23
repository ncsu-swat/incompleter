# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58156230/filenotfounderror-winerror-3-the-system-cannot-find-the-path-specified
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(564685)

except ImportError:
    pass
try:
    import cv2
    _l_(564687)

except ImportError:
    pass
folder = ['test images', 'ALB', 'BET', 'DOL', 'LAG', 'NoF', 'OTHER', 
'SHARK', 'YFT' ]
_l_(564688)
Path = r'D:\ncfm\train'
_l_(564689)

for i in _c_(564691, _n_(564690, "range", lambda: range), 9):
    _l_(564718)

    listing = _c_(564697, _a_(564693, _n_(564692, "os", lambda: os), "listdir"), _n_(564694, "path", lambda: path)+'/'+_n_(564695, "folder", lambda: folder)[_n_(564696, "i", lambda: i)])
    _l_(564698)
    _n_(564699, "folder", lambda: folder)[_n_(564700, "i", lambda: i)+1] = _c_(564716, _a_(564702, _n_(564701, "np", lambda: np), "array"), [_c_(564714, _a_(564713, _c_(564712, _a_(564704, _n_(564703, "np", lambda: np), "array"), _c_(564711, _a_(564706, _n_(564705, "cv2", lambda: cv2), "imread"), _n_(564707, "path", lambda: path)+'/'+_n_(564708, "folder", lambda: folder)[_n_(564709, "i", lambda: i)]+'/'+_n_(564710, "file", lambda: file))), "flatten"))
for file in _n_(564715, "listing", lambda: listing)])
    _l_(564717)