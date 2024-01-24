# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/18299930/typeerror-when-using-tkinter-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import *
    _l_(397487)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(397489)

except ImportError:
    pass

class match:
    _l_(397504)

    def __init__(self):
        _l_(397492)

        _n_(397490, "self", lambda: self).players = 4*[None]
        _l_(397491)

    def commandos(self):
        _l_(397499)

        _c_(397494, _n_(397493, "print", lambda: print), "show commands:")
        _l_(397495)
        _c_(397497, _n_(397496, "print", lambda: print), "now commands for you!")
        _l_(397498)

    def choice(self, choose):
        _l_(397503)

        _c_(397501, _n_(397500, "print", lambda: print), "No choice")
        _l_(397502)

class Application(_n_(397505, "Frame", lambda: Frame)):
    _l_(397571)


    def __init__(self, master, match):
        _l_(397528)

        _c_(397510, _a_(397507, _n_(397506, "Frame", lambda: Frame), "__init__"), _n_(397508, "self", lambda: self), _n_(397509, "master", lambda: master))
        _l_(397511)
        _c_(397514, _a_(397513, _n_(397512, "self", lambda: self), "grid"))
        _l_(397515)
        _c_(397518, _a_(397517, _n_(397516, "self", lambda: self), "create_widgets"))
        _l_(397519)
        _n_(397520, "self", lambda: self).match = _n_(397521, "match", lambda: match)
        _l_(397522)
        _c_(397526, _a_(397525, _a_(397524, _n_(397523, "self", lambda: self), "match"), "commandos"))
        _l_(397527)

    def create_widgets(self):
        _l_(397553)

        _n_(397529, "self", lambda: self).submit_button = _c_(397534, _n_(397530, "Button", lambda: Button), _n_(397531, "self", lambda: self), text = "Submit", command = _a_(397533, _n_(397532, "self", lambda: self), "button_click"))
        _l_(397535)
        _c_(397540, _a_(397538, _a_(397537, _n_(397536, "self", lambda: self), "submit_button"), "grid"), row = 2, column = 0, sticky = _n_(397539, "W", lambda: W))
        _l_(397541)

        _n_(397542, "self", lambda: self).entry = _c_(397545, _n_(397543, "Entry", lambda: Entry), _n_(397544, "self", lambda: self))
        _l_(397546)
        _c_(397551, _a_(397549, _a_(397548, _n_(397547, "self", lambda: self), "entry"), "grid"), row = 1, column = 1, sticky = _n_(397550, "W", lambda: W))
        _l_(397552)

    def button_click(self):
        _l_(397570)

        choose = _c_(397557, _a_(397556, _a_(397555, _n_(397554, "self", lambda: self), "entry"), "get"))
        _l_(397558)
        while _n_(397559, "choose", lambda: choose) != 'S':
            _l_(397569)

            _c_(397564, _a_(397562, _a_(397561, _n_(397560, "self", lambda: self), "match"), "choice"), _n_(397563, "choose", lambda: choose))
            _l_(397565)
            choose = _c_(397567, _n_(397566, "input", lambda: input))
            _l_(397568)

root = _c_(397573, _n_(397572, "Tk", lambda: Tk))
_l_(397574)
_c_(397577, _a_(397576, _n_(397575, "root", lambda: root), "title"), "StackQuestion")
_l_(397578)
_c_(397581, _a_(397580, _n_(397579, "root", lambda: root), "geometry"), "250x150")
_l_(397582)
app = _c_(397586, _n_(397583, "Application", lambda: Application), _n_(397584, "root", lambda: root), _n_(397585, "match", lambda: match))
_l_(397587)

_c_(397590, _a_(397589, _n_(397588, "root", lambda: root), "mainloop"))
_l_(397591)