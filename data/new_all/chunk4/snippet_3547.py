# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72387864/python-typeerror-bad-operand-type-for-unary-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(586700)

except ImportError:
    pass
try:
    import math
    _l_(586702)

except ImportError:
    pass

a = ""
_l_(586703)
b = ""
_l_(586704)
c = ""
_l_(586705)


def clicked():
    _l_(586757)

    global a
    _l_(586706)
    a = _c_(586711, _n_(586707, "int", lambda: int), _c_(586710, _a_(586709, _n_(586708, "entry_a", lambda: entry_a), "get")))
    _l_(586712)
    global b
    _l_(586713)
    a = _c_(586718, _n_(586714, "int", lambda: int), _c_(586717, _a_(586716, _n_(586715, "entry_b", lambda: entry_b), "get")))
    _l_(586719)
    global c
    _l_(586720)
    c = _c_(586725, _n_(586721, "int", lambda: int), _c_(586724, _a_(586723, _n_(586722, "entry_a", lambda: entry_a), "get")))
    _l_(586726)
    result1 = _c_(586736, _n_(586727, "str", lambda: str), (-_n_(586728, "b", lambda: b) + _c_(586734, _a_(586730, _n_(586729, "math", lambda: math), "sqrt"), _n_(586731, "b", lambda: b) ** 2 - 4 * _n_(586732, "a", lambda: a) * _n_(586733, "c", lambda: c))) / 2 * _n_(586735, "a", lambda: a))
    _l_(586737)
    result2 = _c_(586747, _n_(586738, "str", lambda: str), (-_n_(586739, "b", lambda: b) - _c_(586745, _a_(586741, _n_(586740, "math", lambda: math), "sqrt"), _n_(586742, "b", lambda: b) ** 2 - 4 * _n_(586743, "a", lambda: a) * _n_(586744, "c", lambda: c))) / 2 * _n_(586746, "a", lambda: a))
    _l_(586748)
    result = "x1 = " + _n_(586749, "result1", lambda: result1) + ", x2 = " + _n_(586750, "result2", lambda: result2)
    _l_(586751)
    _c_(586755, _a_(586753, _n_(586752, "text4", lambda: text4), "config"), text=_n_(586754, "result", lambda: result))
    _l_(586756)


root = _c_(586760, _a_(586759, _n_(586758, "tkinter", lambda: tkinter), "Tk"))
_l_(586761)
_c_(586764, _a_(586763, _n_(586762, "root", lambda: root), "title"), "Univariate quadratic equation Calculator")
_l_(586765)
_c_(586768, _a_(586767, _n_(586766, "root", lambda: root), "geometry"), "350x450")
_l_(586769)
text1 = _c_(586773, _a_(586771, _n_(586770, "tkinter", lambda: tkinter), "Label"), _n_(586772, "root", lambda: root), text="a=")
_l_(586774)
_c_(586777, _a_(586776, _n_(586775, "text1", lambda: text1), "grid"), row=0, column=0)
_l_(586778)
text2 = _c_(586782, _a_(586780, _n_(586779, "tkinter", lambda: tkinter), "Label"), _n_(586781, "root", lambda: root), text="b=")
_l_(586783)
_c_(586786, _a_(586785, _n_(586784, "text2", lambda: text2), "grid"), row=0, column=2)
_l_(586787)
text3 = _c_(586791, _a_(586789, _n_(586788, "tkinter", lambda: tkinter), "Label"), _n_(586790, "root", lambda: root), text="c=")
_l_(586792)
_c_(586795, _a_(586794, _n_(586793, "text3", lambda: text3), "grid"), row=0, column=4)
_l_(586796)
text4 = _c_(586800, _a_(586798, _n_(586797, "tkinter", lambda: tkinter), "Label"), _n_(586799, "root", lambda: root), text="Nothing")
_l_(586801)
_c_(586804, _a_(586803, _n_(586802, "text4", lambda: text4), "grid"), row=1, column=0)
_l_(586805)
entry_a = _c_(586809, _a_(586807, _n_(586806, "tkinter", lambda: tkinter), "Entry"), _n_(586808, "root", lambda: root), width=5)
_l_(586810)
_c_(586813, _a_(586812, _n_(586811, "entry_a", lambda: entry_a), "grid"), row=0, column=1)
_l_(586814)
entry_b = _c_(586818, _a_(586816, _n_(586815, "tkinter", lambda: tkinter), "Entry"), _n_(586817, "root", lambda: root), width=5)
_l_(586819)
_c_(586822, _a_(586821, _n_(586820, "entry_b", lambda: entry_b), "grid"), row=0, column=3)
_l_(586823)
entry_c = _c_(586827, _a_(586825, _n_(586824, "tkinter", lambda: tkinter), "Entry"), _n_(586826, "root", lambda: root), width=5)
_l_(586828)
_c_(586831, _a_(586830, _n_(586829, "entry_c", lambda: entry_c), "grid"), row=0, column=5)
_l_(586832)
btn = _c_(586837, _a_(586834, _n_(586833, "tkinter", lambda: tkinter), "Button"), _n_(586835, "root", lambda: root), text="Confirm", command=_n_(586836, "clicked", lambda: clicked))
_l_(586838)
_c_(586841, _a_(586840, _n_(586839, "btn", lambda: btn), "grid"), row=0, column=6)
_l_(586842)
_c_(586845, _a_(586844, _n_(586843, "root", lambda: root), "mainloop"))
_l_(586846)