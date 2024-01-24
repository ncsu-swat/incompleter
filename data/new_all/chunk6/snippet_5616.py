# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60090995/typeerror-an-integer-is-required-got-type-tuple
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(368942)

except ImportError:
    pass
try:
    import numpy as np
    _l_(368944)

except ImportError:
    pass
try:
    import pytesseract
    _l_(368946)

except ImportError:
    pass
try:
    from langdetect import detect_langs
    _l_(368948)

except ImportError:
    pass
try:
    from pytesseract import *
    _l_(368950)

except ImportError:
    pass
try:
    from flask import Flask,request
    _l_(368952)

except ImportError:
    pass
try:
    import requests
    _l_(368954)

except ImportError:
    pass

try:
    _l_(368960)

    from PIL import Image
    _l_(368955)
except _n_(368956, "ImportError", lambda: ImportError):
    _l_(368959)

    try:
        import Image
        _l_(368958)

    except ImportError:
        pass

#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


img = _c_(368963, _a_(368962, _n_(368961, "Image", lambda: Image), "open"), 'G:/Agrima/example_code_API/OCR/FDA.png')
_l_(368964)

#h, w, c = img.shape

d = _c_(368970, _a_(368966, _n_(368965, "pytesseract", lambda: pytesseract), "image_to_data"), _n_(368967, "img", lambda: img),output_type=_a_(368969, _n_(368968, "Output", lambda: Output), "DICT"))
_l_(368971)


detected_ocr = _c_(368974, _n_(368972, "image_to_string", lambda: image_to_string), _n_(368973, "img", lambda: img))
_l_(368975)
points = []
_l_(368976)
n_boxes = _c_(368979, _n_(368977, "len", lambda: len), _n_(368978, "d", lambda: d)['text'])
_l_(368980)
for i in _c_(368983, _n_(368981, "range", lambda: range), _n_(368982, "n_boxes", lambda: n_boxes)):
    _l_(369019)

    if _c_(368987, _n_(368984, "int", lambda: int), _n_(368985, "d", lambda: d)['conf'][_n_(368986, "i", lambda: i)]) > 60:
        _l_(369018)

        (x, y, w, h) = (_n_(368988, "d", lambda: d)['left'][_n_(368989, "i", lambda: i)], _n_(368990, "d", lambda: d)['top'][_n_(368991, "i", lambda: i)], _n_(368992, "d", lambda: d)['width'][_n_(368993, "i", lambda: i)],_n_(368994, "d", lambda: d)['height'][_n_(368995, "i", lambda: i)])
        _l_(368996)
        img = _c_(369006, _a_(368998, _n_(368997, "cv2", lambda: cv2), "rectangle"), _n_(368999, "img", lambda: img), (_n_(369000, "x", lambda: x), _n_(369001, "y", lambda: y)), (_n_(369002, "x", lambda: x) + _n_(369003, "w", lambda: w), _n_(369004, "y", lambda: y) + _n_(369005, "h", lambda: h)), (0, 255, 0), 2)
        _l_(369007)
        mark = {'x':_n_(369008, "x", lambda: x),'y':_n_(369009, "y", lambda: y),'width':_n_(369010, "w", lambda: w),'height':_n_(369011, "h", lambda: h)}
        _l_(369012)
        _c_(369016, _a_(369014, _n_(369013, "points", lambda: points), "append"), {'mark':_n_(369015, "mark", lambda: mark)})
        _l_(369017)

# print(points)
_c_(369023, _a_(369021, _n_(369020, "cv2", lambda: cv2), "imshow"), 'img', _n_(369022, "img", lambda: img))
_l_(369024)
_c_(369027, _a_(369026, _n_(369025, "cv2", lambda: cv2), "waitKey"), 0)
_l_(369028)