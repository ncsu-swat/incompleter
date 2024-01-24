# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61016046/pil-and-tkinter-error-typeerror-expected-str-bytes-or-os-pathlike-object-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(470488)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(470490)

except ImportError:
    pass
try:
    import random
    _l_(470492)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(470494)

except ImportError:
    pass
window=_c_(470496, _n_(470495, "Tk", lambda: Tk))
_l_(470497)
_c_(470500, _a_(470499, _n_(470498, "window", lambda: window), "geometry"), '500x550')
_l_(470501)
_c_(470504, _a_(470503, _n_(470502, "window", lambda: window), "resizable"), False, False)
_l_(470505)
f=_c_(470508, _a_(470507, _n_(470506, "tk", lambda: tk), "Frame"))
_l_(470509)
_c_(470512, _a_(470511, _n_(470510, "f", lambda: f), "config"), bg='blue', height='500', width='500')
_l_(470513)
_c_(470516, _a_(470515, _n_(470514, "f", lambda: f), "pack"))
_l_(470517)
cat=_c_(470521, _a_(470519, _n_(470518, "tk", lambda: tk), "Button"), _n_(470520, "window", lambda: window), text='Cat')
_l_(470522)
_c_(470525, _a_(470524, _n_(470523, "cat", lambda: cat), "config"))
_l_(470526)
_c_(470530, _a_(470528, _n_(470527, "cat", lambda: cat), "pack"), fill=_n_(470529, "X", lambda: X))
_l_(470531)
dog=_c_(470535, _a_(470533, _n_(470532, "tk", lambda: tk), "Button"), _n_(470534, "window", lambda: window), text='Dog')
_l_(470536)
_c_(470539, _a_(470538, _n_(470537, "dog", lambda: dog), "config"))
_l_(470540)
_c_(470544, _a_(470542, _n_(470541, "dog", lambda: dog), "pack"), fill=_n_(470543, "X", lambda: X))
_l_(470545)
images=['cat1.jpg', 'cat2.jpg', 'cat3.jpg', 'cube1.jpg', 'cube2.jpg', 'cube3.jpg']
_l_(470546)
imgimport = _c_(470552, _n_(470547, "open", lambda: open), _c_(470551, _a_(470549, _n_(470548, "random", lambda: random), "sample"), _n_(470550, "images", lambda: images), 1))
_l_(470553)
img = _c_(470558, _a_(470556, _a_(470555, _n_(470554, "PIL", lambda: PIL), "Image"), "open"), _n_(470557, "imgimport", lambda: imgimport))
_l_(470559)
_c_(470562, _a_(470561, _n_(470560, "img", lambda: img), "show"))
_l_(470563)