# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39652480/pillow-image-typeerror-an-integer-is-required-got-type-tuple
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image, ImageChops,ImageDraw,ImageFilter
    _l_(438476)

except ImportError:
    pass
try:
    import math
    _l_(438478)

except ImportError:
    pass
try:
    import glob
    _l_(438480)

except ImportError:
    pass
try:
    import os.path
    _l_(438482)

except ImportError:
    pass
try:
    from os import  listdir;
    _l_(438484)

except ImportError:
    pass
try:
    import numpy
    _l_(438486)

except ImportError:
    pass


image_list = []
_l_(438487)

redPixels = []
_l_(438488)
greenPixels = []
_l_(438489)
bluePixels = []
_l_(438490)

for filename in _c_(438493, _a_(438492, _n_(438491, "glob", lambda: glob), "glob"), r"C:\Users\Elias\Desktop\Proj1\images\*.png"):
    _l_(438504)

    im = _c_(438497, _a_(438495, _n_(438494, "Image", lambda: Image), "open"), _n_(438496, "filename", lambda: filename))
    _l_(438498)
    _c_(438502, _a_(438500, _n_(438499, "image_list", lambda: image_list), "append"), _n_(438501, "im", lambda: im))
    _l_(438503)
im = _c_(438509, _a_(438506, _n_(438505, "Image", lambda: Image), "open"), _c_(438508, _n_(438507, "open", lambda: open), r"C:\Users\Elias\Desktop\Proj1\images\1.png",'rb'))
_l_(438510)
width, height = _a_(438512, _n_(438511, "im", lambda: im), "size")
_l_(438513)
_c_(438516, _n_(438514, "print", lambda: print), _n_(438515, "height", lambda: height))
_l_(438517)
_c_(438520, _n_(438518, "print", lambda: print), _n_(438519, "width", lambda: width))
_l_(438521)

result = _c_(438526, _a_(438523, _n_(438522, "Image", lambda: Image), "new"), 'RGB', (_n_(438524, "width", lambda: width),_n_(438525, "height", lambda: height)))
_l_(438527)
newpix = _c_(438530, _a_(438529, _n_(438528, "result", lambda: result), "load"))
_l_(438531)
for x in _c_(438534, _n_(438532, "range", lambda: range), _n_(438533, "width", lambda: width)):
    _l_(438608)

    for y in _c_(438537, _n_(438535, "range", lambda: range), _n_(438536, "height", lambda: height)):
        _l_(438607)

        for z in _n_(438538, "image_list", lambda: (image_list)):
            _l_(438572)

            red  = _c_(438543, _a_(438540, _n_(438539, "z", lambda: z), "getpixel"), (_n_(438541, "x", lambda: x),_n_(438542, "y", lambda: y)))
            _l_(438544)
            blue = _c_(438549, _a_(438546, _n_(438545, "z", lambda: z), "getpixel"), (_n_(438547, "x", lambda: x),_n_(438548, "y", lambda: y)))
            _l_(438550)
            green = _c_(438555, _a_(438552, _n_(438551, "z", lambda: z), "getpixel"), (_n_(438553, "x", lambda: x),_n_(438554, "y", lambda: y)))
            _l_(438556)

            _c_(438560, _a_(438558, _n_(438557, "redPixels", lambda: redPixels), "append"), _n_(438559, "red", lambda: red))
            _l_(438561)
            _c_(438565, _a_(438563, _n_(438562, "greenPixels", lambda: greenPixels), "append"), _n_(438564, "green", lambda: green))
            _l_(438566)
            _c_(438570, _a_(438568, _n_(438567, "bluePixels", lambda: bluePixels), "append"), _n_(438569, "blue", lambda: blue))
            _l_(438571)
        red = _c_(438575, _n_(438573, "sorted", lambda: sorted), _n_(438574, "redPixels", lambda: redPixels))
        _l_(438576)
        blue = _c_(438579, _n_(438577, "sorted", lambda: sorted), _n_(438578, "bluePixels", lambda: bluePixels))
        _l_(438580)
        green = _c_(438583, _n_(438581, "sorted", lambda: sorted), _n_(438582, "greenPixels", lambda: greenPixels))
        _l_(438584)

        mid = _c_(438589, _n_(438585, "int", lambda: int), (_c_(438588, _n_(438586, "len", lambda: len), _n_(438587, "image_list", lambda: image_list))+1)/2)-1
        _l_(438590)

        newRed = _n_(438591, "redPixels", lambda: redPixels)[_n_(438592, "mid", lambda: mid)]
        _l_(438593)
        newBlue = _n_(438594, "bluePixels", lambda: bluePixels)[_n_(438595, "mid", lambda: mid)]
        _l_(438596)
        newGreen = _n_(438597, "greenPixels", lambda: greenPixels)[_n_(438598, "mid", lambda: mid)]
        _l_(438599)
        _n_(438600, "newpix", lambda: newpix)[_n_(438601, "x", lambda: x),_n_(438602, "y", lambda: y)] = (_n_(438603, "newRed", lambda: newRed),_n_(438604, "newGreen", lambda: newGreen),_n_(438605, "newBlue", lambda: newBlue))
        _l_(438606)

_c_(438611, _a_(438610, _n_(438609, "result", lambda: result), "save"), "Stacked.png")
_l_(438612)