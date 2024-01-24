# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60090995/typeerror-an-integer-is-required-got-type-tuple
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(358538)

except ImportError:
    pass
try:
    import numpy as np
    _l_(358540)

except ImportError:
    pass
try:
    import pytesseract
    _l_(358542)

except ImportError:
    pass
try:
    from langdetect import detect_langs
    _l_(358544)

except ImportError:
    pass
try:
    from pytesseract import *
    _l_(358546)

except ImportError:
    pass
try:
    from flask import Flask,request
    _l_(358548)

except ImportError:
    pass
try:
    import requests
    _l_(358550)

except ImportError:
    pass

try:
    _l_(358556)

    from PIL import Image
    _l_(358551)
except _n_(358552, "ImportError", lambda: ImportError):
    _l_(358555)

    try:
        import Image
        _l_(358554)

    except ImportError:
        pass

#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


img = _c_(358559, _a_(358558, _n_(358557, "Image", lambda: Image), "open"), 'G:/Agrima/example_code_API/OCR/FDA.png')
_l_(358560)

#h, w, c = img.shape

d = _c_(358566, _a_(358562, _n_(358561, "pytesseract", lambda: pytesseract), "image_to_data"), _n_(358563, "img", lambda: img),output_type=_a_(358565, _n_(358564, "Output", lambda: Output), "DICT"))
_l_(358567)


detected_ocr = _c_(358570, _n_(358568, "image_to_string", lambda: image_to_string), _n_(358569, "img", lambda: img))
_l_(358571)
points = []
_l_(358572)
n_boxes = _c_(358575, _n_(358573, "len", lambda: len), _n_(358574, "d", lambda: d)['text'])
_l_(358576)
for i in _c_(358579, _n_(358577, "range", lambda: range), _n_(358578, "n_boxes", lambda: n_boxes)):
    _l_(358615)

    if _c_(358583, _n_(358580, "int", lambda: int), _n_(358581, "d", lambda: d)['conf'][_n_(358582, "i", lambda: i)]) > 60:
        _l_(358614)

        (x, y, w, h) = (_n_(358584, "d", lambda: d)['left'][_n_(358585, "i", lambda: i)], _n_(358586, "d", lambda: d)['top'][_n_(358587, "i", lambda: i)], _n_(358588, "d", lambda: d)['width'][_n_(358589, "i", lambda: i)],_n_(358590, "d", lambda: d)['height'][_n_(358591, "i", lambda: i)])
        _l_(358592)
        img = _c_(358602, _a_(358594, _n_(358593, "cv2", lambda: cv2), "rectangle"), _n_(358595, "img", lambda: img), (_n_(358596, "x", lambda: x), _n_(358597, "y", lambda: y)), (_n_(358598, "x", lambda: x) + _n_(358599, "w", lambda: w), _n_(358600, "y", lambda: y) + _n_(358601, "h", lambda: h)), (0, 255, 0), 2)
        _l_(358603)
        mark = {'x':_n_(358604, "x", lambda: x),'y':_n_(358605, "y", lambda: y),'width':_n_(358606, "w", lambda: w),'height':_n_(358607, "h", lambda: h)}
        _l_(358608)
        _c_(358612, _a_(358610, _n_(358609, "points", lambda: points), "append"), {'mark':_n_(358611, "mark", lambda: mark)})
        _l_(358613)

# print(points)
_c_(358619, _a_(358617, _n_(358616, "cv2", lambda: cv2), "imshow"), 'img', _n_(358618, "img", lambda: img))
_l_(358620)
_c_(358623, _a_(358622, _n_(358621, "cv2", lambda: cv2), "waitKey"), 0)
_l_(358624)