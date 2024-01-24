# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/25577228/how-can-i-fix-this-error-typeerror-unsupported-operand-types-for-str-an
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(699424)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(699426)

except ImportError:
    pass
def mhello():
    _l_(699438)

    text1 = _n_(699427, "total", lambda: total)
    _l_(699428)
    mlabel1 = _c_(699431, _n_(699429, "Label", lambda: Label), text=_n_(699430, "text1", lambda: text1), fg ="red")
    _l_(699432)
    _c_(699435, _a_(699434, _n_(699433, "mlabel1", lambda: mlabel1), "pack"))
    _l_(699436)
    aux = ""
    _l_(699437)
    return aux
dog = _c_(699440, _n_(699439, "Tk", lambda: Tk))
_l_(699441)
input0 = _c_(699443, _n_(699442, "StringVar", lambda: StringVar))
_l_(699444)
input1 = _c_(699446, _n_(699445, "StringVar", lambda: StringVar))
_l_(699447)
input2 = _c_(699449, _n_(699448, "StringVar", lambda: StringVar))
_l_(699450)
_c_(699453, _a_(699452, _n_(699451, "dog", lambda: dog), "geometry"), '450x450')
_l_(699454)
_c_(699457, _a_(699456, _n_(699455, "dog", lambda: dog), "title"), "Tip Calculator")
_l_(699458)
mlabel = _c_(699460, _n_(699459, "Label", lambda: Label), text='This is a Simple Tip Calculator', fg ="red")
_l_(699461)
_c_(699464, _a_(699463, _n_(699462, "mlabel", lambda: mlabel), "pack"))
_l_(699465)
mentry = _c_(699469, _n_(699466, "Entry", lambda: Entry), _n_(699467, "dog", lambda: dog), textvariable=_n_(699468, "input0", lambda: input0))
_l_(699470)
_c_(699473, _a_(699472, _n_(699471, "mentry", lambda: mentry), "pack"))
_l_(699474)
mentry0 = _c_(699478, _n_(699475, "Entry", lambda: Entry), _n_(699476, "dog", lambda: dog), textvariable=_n_(699477, "input1", lambda: input1))
_l_(699479)
_c_(699482, _a_(699481, _n_(699480, "mentry0", lambda: mentry0), "pack"))
_l_(699483)
mentry1 = _c_(699487, _n_(699484, "Entry", lambda: Entry), _n_(699485, "dog", lambda: dog), textvariable=_n_(699486, "input2", lambda: input2))
_l_(699488)
_c_(699491, _a_(699490, _n_(699489, "mentry1", lambda: mentry1), "pack"))
_l_(699492)
meal = _c_(699495, _a_(699494, _n_(699493, "input0", lambda: input0), "get"))
_l_(699496)
tax = _c_(699499, _a_(699498, _n_(699497, "input1", lambda: input1), "get"))
_l_(699500)
tip = _c_(699503, _a_(699502, _n_(699501, "input2", lambda: input2), "get"))
_l_(699504)
tip = _n_(699505, "tip", lambda: tip) / 100
_l_(699506)
tax = _n_(699507, "tax", lambda: tax) / 100
_l_(699508)
meal = _n_(699509, "meal", lambda: meal) + _n_(699510, "meal", lambda: meal) * _n_(699511, "tax", lambda: tax)
_l_(699512)
total = _n_(699513, "meal", lambda: meal) + _n_(699514, "meal", lambda: meal) * _n_(699515, "tip", lambda: tip)
_l_(699516)
mbutton = _c_(699519, _n_(699517, "Button", lambda: Button), text='Calculate',command = _n_(699518, "mhello", lambda: mhello))
_l_(699520)
_c_(699523, _a_(699522, _n_(699521, "mbutton", lambda: mbutton), "pack"))
_l_(699524)

_c_(699527, _a_(699526, _n_(699525, "dog", lambda: dog), "mainloop"))
_l_(699528)