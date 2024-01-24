# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69679658/i-am-getting-this-error-in-my-python-code-fr-height-fr-width-frame-shape-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(608628)

except ImportError:
    pass
try:
    from PIL import ImageGrab
    _l_(608630)

except ImportError:
    pass
try:
    import numpy as np
    _l_(608632)

except ImportError:
    pass
try:
    import cv2
    _l_(608634)

except ImportError:
    pass
try:
    from win32api import GetSystemMetrics
    _l_(608636)

except ImportError:
    pass
try:
    import sys
    _l_(608638)

except ImportError:
    pass

width = _c_(608640, _n_(608639, "GetSystemMetrics", lambda: GetSystemMetrics), 0)
_l_(608641)
height = _c_(608643, _n_(608642, "GetSystemMetrics", lambda: GetSystemMetrics), 1)
_l_(608644)
time_stamp = _c_(608650, _a_(608649, _c_(608648, _a_(608647, _a_(608646, _n_(608645, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), '%Y-%m-%d %H-%M-%S')
_l_(608651)
file_name = f'{_n_(608652, "time_stamp", lambda: time_stamp)}.mp4'
_l_(608653)
fourcc = _c_(608656, _a_(608655, _n_(608654, 'cv2', lambda: cv2), 'VideoWriter_fourcc'), 'm', 'p', '4', 'v')
_l_(608657)
captured_video = _c_(608664, _a_(608659, _n_(608658, 'cv2', lambda: cv2), 'VideoWriter'), _n_(608660, 'file_name', lambda: file_name), _n_(608661, 'fourcc', lambda: fourcc), 20.0, (_n_(608662, 'width', lambda: width), _n_(608663, 'height', lambda: height)))
_l_(608665)

webcam = _c_(608668, _a_(608667, _n_(608666, 'cv2', lambda: cv2), 'VideoCapture'), 1)
_l_(608669)

while True:
    _l_(608719)

    img = _c_(608674, _a_(608671, _n_(608670, 'ImageGrab', lambda: ImageGrab), 'grab'), bbox=(0, 0, _n_(608672, 'width', lambda: width), _n_(608673, 'height', lambda: height)))
    _l_(608675)
    img_np = _c_(608679, _a_(608677, _n_(608676, 'np', lambda: np), 'array'), _n_(608678, 'img', lambda: img))
    _l_(608680)
    img_final = _c_(608686, _a_(608682, _n_(608681, 'cv2', lambda: cv2), 'cvtColor'), _n_(608683, 'img_np', lambda: img_np), _a_(608685, _n_(608684, 'cv2', lambda: cv2), 'COLOR_BGR2RGB'))
    _l_(608687)
    _, frame = _c_(608690, _a_(608689, _n_(608688, 'webcam', lambda: webcam), 'read'))
    _l_(608691)
    fr_height, fr_width, _ = _a_(608693, _n_(608692, 'frame', lambda: frame), 'shape')
    _l_(608694)
    _n_(608695, 'img_final', lambda: img_final)[0:_n_(608696, 'fr_height', lambda: fr_height), 0: _n_(608697, 'fr_width', lambda: fr_width), :] = _n_(608698, 'frame', lambda: frame)[0: _n_(608699, 'fr_height', lambda: fr_height), 0: _n_(608700, 'fr_width', lambda: fr_width), :]
    _l_(608701)
    _c_(608705, _a_(608703, _n_(608702, 'cv2', lambda: cv2), 'imshow'), 'Secret Capture', _n_(608704, 'img_final', lambda: img_final))
    _l_(608706)

    # cv2.imshow('webcam', frame)

    _c_(608710, _a_(608708, _n_(608707, 'captured_video', lambda: captured_video), 'write'), _n_(608709, 'img_final', lambda: img_final))
    _l_(608711)
    if _c_(608714, _a_(608713, _n_(608712, 'cv2', lambda: cv2), 'waitKey'), 10) == _c_(608716, _n_(608715, 'ord', lambda: ord), 'q'):
        _l_(608718)

        break
        _l_(608717)