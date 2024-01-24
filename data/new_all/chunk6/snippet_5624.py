# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60090995/typeerror-an-integer-is-required-got-type-tuple
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(337751)

except ImportError:
    pass
try:
    import numpy as np
    _l_(337753)

except ImportError:
    pass
try:
    import pytesseract
    _l_(337755)

except ImportError:
    pass
try:
    from langdetect import detect_langs
    _l_(337757)

except ImportError:
    pass
try:
    from pytesseract import *
    _l_(337759)

except ImportError:
    pass
try:
    from flask import Flask,request
    _l_(337761)

except ImportError:
    pass
try:
    import requests
    _l_(337763)

except ImportError:
    pass

try:
    _l_(337769)

    from PIL import Image
    _l_(337764)
except _n_(337765, "ImportError", lambda: ImportError):
    _l_(337768)

    try:
        import Image
        _l_(337767)

    except ImportError:
        pass

#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


img = _c_(337772, _a_(337771, _n_(337770, "Image", lambda: Image), "open"), 'G:/Agrima/example_code_API/OCR/FDA.png')
_l_(337773)

#h, w, c = img.shape

d = _c_(337779, _a_(337775, _n_(337774, "pytesseract", lambda: pytesseract), "image_to_data"), _n_(337776, "img", lambda: img),output_type=_a_(337778, _n_(337777, "Output", lambda: Output), "DICT"))
_l_(337780)


detected_ocr = _c_(337783, _n_(337781, "image_to_string", lambda: image_to_string), _n_(337782, "img", lambda: img))
_l_(337784)
points = []
_l_(337785)
n_boxes = _c_(337788, _n_(337786, "len", lambda: len), _n_(337787, "d", lambda: d)['text'])
_l_(337789)
for i in _c_(337792, _n_(337790, "range", lambda: range), _n_(337791, "n_boxes", lambda: n_boxes)):
    _l_(337828)

    if _c_(337796, _n_(337793, "int", lambda: int), _n_(337794, "d", lambda: d)['conf'][_n_(337795, "i", lambda: i)]) > 60:
        _l_(337827)

        (x, y, w, h) = (_n_(337797, "d", lambda: d)['left'][_n_(337798, "i", lambda: i)], _n_(337799, "d", lambda: d)['top'][_n_(337800, "i", lambda: i)], _n_(337801, "d", lambda: d)['width'][_n_(337802, "i", lambda: i)],_n_(337803, "d", lambda: d)['height'][_n_(337804, "i", lambda: i)])
        _l_(337805)
        img = _c_(337815, _a_(337807, _n_(337806, "cv2", lambda: cv2), "rectangle"), _n_(337808, "img", lambda: img), (_n_(337809, "x", lambda: x), _n_(337810, "y", lambda: y)), (_n_(337811, "x", lambda: x) + _n_(337812, "w", lambda: w), _n_(337813, "y", lambda: y) + _n_(337814, "h", lambda: h)), (0, 255, 0), 2)
        _l_(337816)
        mark = {'x':_n_(337817, "x", lambda: x),'y':_n_(337818, "y", lambda: y),'width':_n_(337819, "w", lambda: w),'height':_n_(337820, "h", lambda: h)}
        _l_(337821)
        _c_(337825, _a_(337823, _n_(337822, "points", lambda: points), "append"), {'mark':_n_(337824, "mark", lambda: mark)})
        _l_(337826)

# print(points)
_c_(337832, _a_(337830, _n_(337829, "cv2", lambda: cv2), "imshow"), 'img', _n_(337831, "img", lambda: img))
_l_(337833)
_c_(337836, _a_(337835, _n_(337834, "cv2", lambda: cv2), "waitKey"), 0)
_l_(337837)