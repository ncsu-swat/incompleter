# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72385774/how-solved-attributeerror-numpy-ndarray-object-has-no-attribute-lower
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(600574)

except ImportError:
    pass
try:
    import numpy as np
    _l_(600576)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(600578)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(600580)

except ImportError:
    pass
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    _l_(600582)

except ImportError:
    pass

sting_array = ["hEllO","iNteRneT","pEopLe","sKay","sds","gbrhn","rHy"]
_l_(600583)
Array2D = _c_(600587, _a_(600585, _n_(600584, "np", lambda: np), "reshape"), _n_(600586, "sting_array", lambda: sting_array), [-1, 1])
_l_(600588)
Lower = _c_(600593, _a_(600591, _a_(600590, _n_(600589, "np", lambda: np), "char"), "lower"), _n_(600592, "Array2D", lambda: Array2D))
_l_(600594)

stand = _c_(600596, _n_(600595, "TfidfVectorizer", lambda: TfidfVectorizer))
_l_(600597)
 #fit data
Fit = _c_(600601, _a_(600599, _n_(600598, "stand", lambda: stand), "fit"), _n_(600600, "Lower", lambda: Lower))
_l_(600602)
 #transform data
x_scaled =_c_(600606, _a_(600604, _n_(600603, "stand", lambda: stand), "transform"), _n_(600605, "Lower", lambda: Lower))
_l_(600607)

_c_(600610, _n_(600608, "print", lambda: print), _n_(600609, "x_scaled", lambda: x_scaled))
_l_(600611)