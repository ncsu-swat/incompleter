# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42044225/typeerror-integer-argument-expected-got-float-in-pil
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(421490)

except ImportError:
    pass

def change_contrast(img, level):
    _l_(421540)

    def truncate(v):
        _l_(421495)

        aux = 0 if _n_(421491, "v", lambda: v) < 0 else 255 if _n_(421492, "v", lambda: v) > 255 else _n_(421493, "v", lambda: v)
        _l_(421494)
        return aux


    img = _c_(421498, _a_(421497, _n_(421496, "Image", lambda: Image), "open"), "C:\\Users\\omar\\Desktop\\Site\\Images\\obama.png")
    _l_(421499)
    _c_(421502, _a_(421501, _n_(421500, "img", lambda: img), "load"))
    _l_(421503)

    factor = (259 * (_n_(421504, "level", lambda: level)+255)) / (255 * (259-_n_(421505, "level", lambda: level)))
    _l_(421506)
    for x in _c_(421510, _n_(421507, "range", lambda: range), _a_(421509, _n_(421508, "img", lambda: img), "size")[0]):
        _l_(421537)

        for y in _c_(421514, _n_(421511, "range", lambda: range), _a_(421513, _n_(421512, "img", lambda: img), "size")[1]):
            _l_(421536)

            color = _c_(421519, _a_(421516, _n_(421515, "img", lambda: img), "getpixel"), (_n_(421517, "x", lambda: x), _n_(421518, "y", lambda: y)))
            _l_(421520)
            new_color = _c_(421527, _n_(421521, "tuple", lambda: tuple), (_c_(421525, _n_(421522, "truncate", lambda: truncate), _n_(421523, "factor", lambda: factor) * (_n_(421524, "c", lambda: c)-128) + 128) for c in _n_(421526, "color", lambda: color)))
            _l_(421528)
            _c_(421534, _a_(421530, _n_(421529, "img", lambda: img), "putpixel"), (_n_(421531, "x", lambda: x), _n_(421532, "y", lambda: y)), _n_(421533, "new_color", lambda: new_color))
            _l_(421535)
    aux = _n_(421538, "img", lambda: img)
    _l_(421539)

    return aux

result = _c_(421542, _n_(421541, "change_contrast", lambda: change_contrast), 'test_image1.jpg', 128)
_l_(421543)
_c_(421546, _a_(421545, _n_(421544, "result", lambda: result), "save"), 'test_image1_output.jpg')
_l_(421547)
_c_(421549, _n_(421548, "print", lambda: print), 'done')
_l_(421550)