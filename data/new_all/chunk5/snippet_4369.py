# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59117289/python-error-code-attributeerror-tuple-object-has-no-attribute-save
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(672443)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(672445)

except ImportError:
    pass
try:
    import numpy as np
    _l_(672447)

except ImportError:
    pass

def int_to_bin(rgb):
    _l_(672460)

    r, g, b = _n_(672448, "rgb", lambda: rgb)
    _l_(672449)
    aux = (_c_(672452, _a_(672450, '{0:08b}', "format"), _n_(672451, "r", lambda: r)), _c_(672455, _a_(672453, '{0:08b}', "format"), _n_(672454, "g", lambda: g)), _c_(672458, _a_(672456, '{0:08b}', "format"), _n_(672457, "b", lambda: b))) 
    _l_(672459) 
    return aux 

def merge_rgb(rgb1, rgb2):
    _l_(672474)

    r1, b1, g1 = _n_(672461, "rgb1", lambda: rgb1)
    _l_(672462)
    r2, b2, g2 = _n_(672463, "rgb2", lambda: rgb2)
    _l_(672464)

    rgb = (_n_(672465, "r1", lambda: r1)[:4] + _n_(672466, "r2", lambda: r2)[:4], _n_(672467, "g1", lambda: g1)[:4] + _n_(672468, "g2", lambda: g2)[:4], _n_(672469, "b1", lambda: b1)[:4] + _n_(672470, "b2", lambda: b2)[:4])
    _l_(672471)
    aux = _n_(672472, "rgb", lambda: rgb)
    _l_(672473)

    return aux

im = "bunga.jpg"
_l_(672475)
img1 =  _c_(672479, _a_(672477, _n_(672476, "Image", lambda: Image), "open"), _n_(672478, "im", lambda: im),'r')
_l_(672480)

im2 = "index.jpg"
_l_(672481)
img2 = _c_(672485, _a_(672483, _n_(672482, "Image", lambda: Image), "open"), _n_(672484, "im2", lambda: im2),'r')
_l_(672486)

pixel_map1 = _c_(672489, _a_(672488, _n_(672487, "img1", lambda: img1), "load"))
_l_(672490)
pixel_map2 = _c_(672493, _a_(672492, _n_(672491, "img2", lambda: img2), "load"))
_l_(672494)

for i in _c_(672498, _n_(672495, "range", lambda: range), _a_(672497, _n_(672496, "img1", lambda: img1), "size")[0]):
    _l_(672528)

    for j in _c_(672502, _n_(672499, "range", lambda: range), _a_(672501, _n_(672500, "img1", lambda: img1), "size")[1]):
        _l_(672527)

        rgb1 = _c_(672507, _n_(672503, "int_to_bin", lambda: int_to_bin), _n_(672504, "pixel_map1", lambda: pixel_map1)[_n_(672505, "i", lambda: i), _n_(672506, "j", lambda: j)])
        _l_(672508)

        if _n_(672509, "i", lambda: i) < _a_(672511, _n_(672510, "img2", lambda: img2), "size")[0] and _n_(672512, "j", lambda: j) < _a_(672514, _n_(672513, "img2", lambda: img2), "size")[1]:
            _l_(672526)

            rgb2 = _c_(672519, _n_(672515, "int_to_bin", lambda: int_to_bin), _n_(672516, "pixel_map2", lambda: pixel_map2)[_n_(672517, "i", lambda: i), _n_(672518, "j", lambda: j)])
            _l_(672520)
            rgb = _c_(672524, _n_(672521, "merge_rgb", lambda: merge_rgb), _n_(672522, "rgb1", lambda: rgb1), _n_(672523, "rgb2", lambda: rgb2))
            _l_(672525)

merged_image = _n_(672529, "rgb", lambda: rgb)
_l_(672530)
img = _c_(672533, _a_(672532, _n_(672531, "merged_image", lambda: merged_image), "save"), "decode_konversiGreykeBiner.jpg")
_l_(672534)