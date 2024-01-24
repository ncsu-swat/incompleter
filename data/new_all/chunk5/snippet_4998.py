# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/25577228/how-can-i-fix-this-error-typeerror-unsupported-operand-types-for-str-an
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(702277)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(702279)

except ImportError:
    pass
def mhello():
    _l_(702291)

    text1 = _n_(702280, "total", lambda: total)
    _l_(702281)
    mlabel1 = _c_(702284, _n_(702282, "Label", lambda: Label), text=_n_(702283, "text1", lambda: text1), fg ="red")
    _l_(702285)
    _c_(702288, _a_(702287, _n_(702286, "mlabel1", lambda: mlabel1), "pack"))
    _l_(702289)
    aux = ""
    _l_(702290)
    return aux
dog = _c_(702293, _n_(702292, "Tk", lambda: Tk))
_l_(702294)
input0 = _c_(702296, _n_(702295, "StringVar", lambda: StringVar))
_l_(702297)
input1 = _c_(702299, _n_(702298, "StringVar", lambda: StringVar))
_l_(702300)
input2 = _c_(702302, _n_(702301, "StringVar", lambda: StringVar))
_l_(702303)
_c_(702306, _a_(702305, _n_(702304, "dog", lambda: dog), "geometry"), '450x450')
_l_(702307)
_c_(702310, _a_(702309, _n_(702308, "dog", lambda: dog), "title"), "Tip Calculator")
_l_(702311)
mlabel = _c_(702313, _n_(702312, "Label", lambda: Label), text='This is a Simple Tip Calculator', fg ="red")
_l_(702314)
_c_(702317, _a_(702316, _n_(702315, "mlabel", lambda: mlabel), "pack"))
_l_(702318)
mentry = _c_(702322, _n_(702319, "Entry", lambda: Entry), _n_(702320, "dog", lambda: dog), textvariable=_n_(702321, "input0", lambda: input0))
_l_(702323)
_c_(702326, _a_(702325, _n_(702324, "mentry", lambda: mentry), "pack"))
_l_(702327)
mentry0 = _c_(702331, _n_(702328, "Entry", lambda: Entry), _n_(702329, "dog", lambda: dog), textvariable=_n_(702330, "input1", lambda: input1))
_l_(702332)
_c_(702335, _a_(702334, _n_(702333, "mentry0", lambda: mentry0), "pack"))
_l_(702336)
mentry1 = _c_(702340, _n_(702337, "Entry", lambda: Entry), _n_(702338, "dog", lambda: dog), textvariable=_n_(702339, "input2", lambda: input2))
_l_(702341)
_c_(702344, _a_(702343, _n_(702342, "mentry1", lambda: mentry1), "pack"))
_l_(702345)
meal = _c_(702348, _a_(702347, _n_(702346, "input0", lambda: input0), "get"))
_l_(702349)
tax = _c_(702352, _a_(702351, _n_(702350, "input1", lambda: input1), "get"))
_l_(702353)
tip = _c_(702356, _a_(702355, _n_(702354, "input2", lambda: input2), "get"))
_l_(702357)
tip = _n_(702358, "tip", lambda: tip) / 100
_l_(702359)
tax = _n_(702360, "tax", lambda: tax) / 100
_l_(702361)
meal = _n_(702362, "meal", lambda: meal) + _n_(702363, "meal", lambda: meal) * _n_(702364, "tax", lambda: tax)
_l_(702365)
total = _n_(702366, "meal", lambda: meal) + _n_(702367, "meal", lambda: meal) * _n_(702368, "tip", lambda: tip)
_l_(702369)
mbutton = _c_(702372, _n_(702370, "Button", lambda: Button), text='Calculate',command = _n_(702371, "mhello", lambda: mhello))
_l_(702373)
_c_(702376, _a_(702375, _n_(702374, "mbutton", lambda: mbutton), "pack"))
_l_(702377)

_c_(702380, _a_(702379, _n_(702378, "dog", lambda: dog), "mainloop"))
_l_(702381)