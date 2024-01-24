# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62111479/typeerror-can-only-concatenate-str-not-int-to-str-what-does-it-mean
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import*
    _l_(353531)

except ImportError:
    pass
try:
    import random
    _l_(353533)

except ImportError:
    pass
try:
    from tkinter import messagebox
    _l_(353535)

except ImportError:
    pass
window=_c_(353537, _n_(353536, "Tk", lambda: Tk))
_l_(353538)
_c_(353541, _a_(353540, _n_(353539, "window", lambda: window), "title"), "Random Tools")
_l_(353542)
_c_(353545, _a_(353544, _n_(353543, "window", lambda: window), "configure"), background="light green")
_l_(353546)
textvaria = _c_(353548, _n_(353547, "IntVar", lambda: IntVar))
_l_(353549)
textvaria2 = _c_(353551, _n_(353550, "IntVar", lambda: IntVar))
_l_(353552)

label0 = _c_(353555, _n_(353553, "Label", lambda: Label), _n_(353554, "window", lambda: window), text = "Min", bg ="light green")
_l_(353556)
_c_(353559, _a_(353558, _n_(353557, "label0", lambda: label0), "grid"), row=1, column=0)
_l_(353560)

spinboxmin = _c_(353564, _n_(353561, "Spinbox", lambda: Spinbox), _n_(353562, "window", lambda: window), from_=1, to=9999, increment=1, textvariable=_n_(353563, "textvaria", lambda: textvaria))
_l_(353565)
_c_(353568, _a_(353567, _n_(353566, "spinboxmin", lambda: spinboxmin), "grid"), row=2, column=0)
_l_(353569)
a = _c_(353572, _a_(353571, _n_(353570, "spinboxmin", lambda: spinboxmin), "get"))
_l_(353573)

label1 = _c_(353576, _n_(353574, "Label", lambda: Label), _n_(353575, "window", lambda: window), text="Max", bg="light green")
_l_(353577)
_c_(353580, _a_(353579, _n_(353578, "label1", lambda: label1), "grid"), row=3, column=0)
_l_(353581)

spinboxmax = _c_(353585, _n_(353582, "Spinbox", lambda: Spinbox), _n_(353583, "window", lambda: window), from_=1, to=9999, increment=1, textvariable=_n_(353584, "textvaria2", lambda: textvaria2))
_l_(353586)
_c_(353589, _a_(353588, _n_(353587, "spinboxmax", lambda: spinboxmax), "grid"), row = 4, column =0)
_l_(353590)
b = _c_(353593, _a_(353592, _n_(353591, "spinboxmax", lambda: spinboxmax), "get"))
_l_(353594)

def submit2():
    _l_(353607)

    if _n_(353595, "a", lambda: a) <= _n_(353596, "b", lambda: b):
        _l_(353606)

        _c_(353600, _a_(353598, _n_(353597, "answertext", lambda: answertext), "delete"), '1.0', _n_(353599, "END", lambda: END))
        _l_(353601)
    else:
        _c_(353604, _a_(353603, _n_(353602, "messagebox", lambda: messagebox), "showerror"), "Error", "Max must be greater than min!")
        _l_(353605)

submit = _c_(353610, _n_(353608, "Button", lambda: Button), text="Submit", command=_n_(353609, "submit2", lambda: submit2))
_l_(353611)
_c_(353614, _a_(353613, _n_(353612, "submit", lambda: submit), "grid"), row=4, column=2)
_l_(353615)

n = _c_(353620, _a_(353617, _n_(353616, "random", lambda: random), "randint"), _n_(353618, "a", lambda: a), _n_(353619, "b", lambda: b)+1)
_l_(353621)

answertext = _c_(353624, _n_(353622, "Text", lambda: Text), text=_n_(353623, "n", lambda: n))
_l_(353625)
_c_(353628, _a_(353627, _n_(353626, "answertext", lambda: answertext), "grid"), row=5, column=0)
_l_(353629)


_c_(353632, _a_(353631, _n_(353630, "window", lambda: window), "mainloop"))
_l_(353633)