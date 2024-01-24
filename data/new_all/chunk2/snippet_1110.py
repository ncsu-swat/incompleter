# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45739240/nameerror-name-apply-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(442261)

except ImportError:
    pass

movieList = ["1 Frozen 06/15 11:35 95", "3 Frozen 06/18 11:35 95",
        "4 Frozen 06/30 11:25 95", "5 Frozen 07/02 11:45 95",
        "6 Frozen 07/05 12:30 95"]
_l_(442262)

master = _c_(442264, _n_(442263, "Tk", lambda: Tk))
_l_(442265)

option = _c_(442268, _n_(442266, "StringVar", lambda: StringVar), _n_(442267, "master", lambda: master))
_l_(442269)
_c_(442273, _a_(442271, _n_(442270, "option", lambda: option), "set"), _n_(442272, "movieList", lambda: movieList)[0]) # Set the first value to be the default option
_l_(442274) # Set the first value to be the default option

w = _c_(442282, _n_(442275, "apply", lambda: apply), _n_(442276, "OptionMenu", lambda: OptionMenu), (_n_(442277, "master", lambda: master), _n_(442278, "option", lambda: option)) + _c_(442281, _n_(442279, "tuple", lambda: tuple), _n_(442280, "movieList", lambda: movieList)))
_l_(442283)
_c_(442286, _a_(442285, _n_(442284, "w", lambda: w), "pack"))
_l_(442287)

_c_(442289, _n_(442288, "mainloop", lambda: mainloop))
_l_(442290)