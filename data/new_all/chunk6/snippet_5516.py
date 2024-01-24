# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62111479/typeerror-can-only-concatenate-str-not-int-to-str-what-does-it-mean
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import*
    _l_(345809)

except ImportError:
    pass
try:
    import random
    _l_(345811)

except ImportError:
    pass
try:
    from tkinter import messagebox
    _l_(345813)

except ImportError:
    pass
window=_c_(345815, _n_(345814, "Tk", lambda: Tk))
_l_(345816)
_c_(345819, _a_(345818, _n_(345817, "window", lambda: window), "title"), "Random Tools")
_l_(345820)
_c_(345823, _a_(345822, _n_(345821, "window", lambda: window), "configure"), background="light green")
_l_(345824)
textvaria = _c_(345826, _n_(345825, "IntVar", lambda: IntVar))
_l_(345827)
textvaria2 = _c_(345829, _n_(345828, "IntVar", lambda: IntVar))
_l_(345830)

label0 = _c_(345833, _n_(345831, "Label", lambda: Label), _n_(345832, "window", lambda: window), text = "Min", bg ="light green")
_l_(345834)
_c_(345837, _a_(345836, _n_(345835, "label0", lambda: label0), "grid"), row=1, column=0)
_l_(345838)

spinboxmin = _c_(345842, _n_(345839, "Spinbox", lambda: Spinbox), _n_(345840, "window", lambda: window), from_=1, to=9999, increment=1, textvariable=_n_(345841, "textvaria", lambda: textvaria))
_l_(345843)
_c_(345846, _a_(345845, _n_(345844, "spinboxmin", lambda: spinboxmin), "grid"), row=2, column=0)
_l_(345847)
a = _c_(345850, _a_(345849, _n_(345848, "spinboxmin", lambda: spinboxmin), "get"))
_l_(345851)

label1 = _c_(345854, _n_(345852, "Label", lambda: Label), _n_(345853, "window", lambda: window), text="Max", bg="light green")
_l_(345855)
_c_(345858, _a_(345857, _n_(345856, "label1", lambda: label1), "grid"), row=3, column=0)
_l_(345859)

spinboxmax = _c_(345863, _n_(345860, "Spinbox", lambda: Spinbox), _n_(345861, "window", lambda: window), from_=1, to=9999, increment=1, textvariable=_n_(345862, "textvaria2", lambda: textvaria2))
_l_(345864)
_c_(345867, _a_(345866, _n_(345865, "spinboxmax", lambda: spinboxmax), "grid"), row = 4, column =0)
_l_(345868)
b = _c_(345871, _a_(345870, _n_(345869, "spinboxmax", lambda: spinboxmax), "get"))
_l_(345872)

def submit2():
    _l_(345885)

    if _n_(345873, "a", lambda: a) <= _n_(345874, "b", lambda: b):
        _l_(345884)

        _c_(345878, _a_(345876, _n_(345875, "answertext", lambda: answertext), "delete"), '1.0', _n_(345877, "END", lambda: END))
        _l_(345879)
    else:
        _c_(345882, _a_(345881, _n_(345880, "messagebox", lambda: messagebox), "showerror"), "Error", "Max must be greater than min!")
        _l_(345883)

submit = _c_(345888, _n_(345886, "Button", lambda: Button), text="Submit", command=_n_(345887, "submit2", lambda: submit2))
_l_(345889)
_c_(345892, _a_(345891, _n_(345890, "submit", lambda: submit), "grid"), row=4, column=2)
_l_(345893)

n = _c_(345898, _a_(345895, _n_(345894, "random", lambda: random), "randint"), _n_(345896, "a", lambda: a), _n_(345897, "b", lambda: b)+1)
_l_(345899)

answertext = _c_(345902, _n_(345900, "Text", lambda: Text), text=_n_(345901, "n", lambda: n))
_l_(345903)
_c_(345906, _a_(345905, _n_(345904, "answertext", lambda: answertext), "grid"), row=5, column=0)
_l_(345907)


_c_(345910, _a_(345909, _n_(345908, "window", lambda: window), "mainloop"))
_l_(345911)