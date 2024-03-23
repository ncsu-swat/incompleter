# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42125227/attributeerror-object-has-no-attribute-listbox
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(607479)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(607481)

except ImportError:
    pass

class MyApp(_n_(607482, "Tk", lambda: Tk)):
    _l_(607536)

    def __init__(self):
        _l_(607526)

        _c_(607486, _a_(607484, _n_(607483, "Tk", lambda: Tk), "__init__"), _n_(607485, "self", lambda: self))
        _l_(607487)

        # App data in controller
        _n_(607488, "self", lambda: self).app_data = {"listbox":    _c_(607490, _n_(607489, "StringVar", lambda: StringVar))}
        _l_(607491)

        container = _c_(607495, _a_(607493, _n_(607492, "ttk", lambda: ttk), "Frame"), _n_(607494, "self", lambda: self))
        _l_(607496)
        _c_(607499, _a_(607498, _n_(607497, "container", lambda: container), "pack"), side="top", fill="both", expand = True)
        _l_(607500)
        _n_(607501, "self", lambda: self).frames = {}
        _l_(607502)

        for F in (_n_(607503, "Page1", lambda: Page1), _n_(607504, "Page2", lambda: Page2)):
            _l_(607520)

            frame = _c_(607508, _n_(607505, "F", lambda: F), _n_(607506, "container", lambda: container), _n_(607507, "self", lambda: self))
            _l_(607509)
            _a_(607511, _n_(607510, "self", lambda: self), "frames")[_n_(607512, "F", lambda: F)] = _n_(607513, "frame", lambda: frame)
            _l_(607514)
            _c_(607518, _a_(607516, _n_(607515, "frame", lambda: frame), "grid"), row=0, column=0, sticky = _n_(607517, "NSEW", lambda: NSEW))
            _l_(607519)
        _c_(607524, _a_(607522, _n_(607521, "self", lambda: self), "show_frame"), _n_(607523, "Page1", lambda: Page1))
        _l_(607525)

    def show_frame(self, cont):
        _l_(607535)

        frame = _a_(607528, _n_(607527, "self", lambda: self), "frames")[_n_(607529, "cont", lambda: cont)]
        _l_(607530)
        _c_(607533, _a_(607532, _n_(607531, "frame", lambda: frame), "tkraise"))
        _l_(607534)

class Page1(_a_(607538, _n_(607537, "ttk", lambda: ttk), "Frame")):
    _l_(607591)

    def __init__(self, parent, controller):
        _l_(607590)

        _c_(607544, _a_(607541, _a_(607540, _n_(607539, "ttk", lambda: ttk), "Frame"), "__init__"), _n_(607542, "self", lambda: self), _n_(607543, "parent", lambda: parent))
        _l_(607545)
        _n_(607546, "self", lambda: self).controller = _n_(607547, "controller", lambda: controller)
        _l_(607548)

        listbox = _c_(607551, _n_(607549, "Listbox", lambda: Listbox), _n_(607550, "self", lambda: self),exportselection=0)
        _l_(607552)
        _c_(607555, _a_(607554, _n_(607553, "listbox", lambda: listbox), "grid"))
        _l_(607556)
        for item in [0,1,2,3,4,5]:
            _l_(607563)

            _c_(607561, _a_(607558, _n_(607557, "listbox", lambda: listbox), "insert"), _n_(607559, "END", lambda: END), _n_(607560, "item", lambda: item))
            _l_(607562)

        button1 = _c_(607584, _a_(607565, _n_(607564, "ttk", lambda: ttk), "Button"), _n_(607566, "self", lambda: self),text="Next Page"
                             ,command=lambda: _c_(607570, _a_(607568, _n_(607567, "controller", lambda: controller), "show_frame"), _n_(607569, "Page2", lambda: Page2))
                             or _c_(607583, _a_(607574, _a_(607573, _a_(607572, _n_(607571, "self", lambda: self), "controller"), "app_data")["listbox"], "set"), _c_(607582, _a_(607577, _a_(607576, _n_(607575, "self", lambda: self), "listbox"), "get"), _c_(607581, _a_(607580, _a_(607579, _n_(607578, "self", lambda: self), "listbox"), "curselection")))))
        _l_(607585)
        _c_(607588, _a_(607587, _n_(607586, "button1", lambda: button1), "grid"))
        _l_(607589)

class Page2(_a_(607593, _n_(607592, "ttk", lambda: ttk), "Frame")):
    _l_(607649)

    def __init__(self, parent, controller):
        _l_(607635)

        _c_(607599, _a_(607596, _a_(607595, _n_(607594, "ttk", lambda: ttk), "Frame"), "__init__"), _n_(607597, "self", lambda: self), _n_(607598, "parent", lambda: parent))
        _l_(607600)
        _n_(607601, "self", lambda: self).controller = _n_(607602, "controller", lambda: controller)
        _l_(607603)
        _c_(607609, _a_(607608, _c_(607607, _a_(607605, _n_(607604, "ttk", lambda: ttk), "Label"), _n_(607606, "self", lambda: self), text='Next Page'), "grid"), padx=(20,20), pady=(20,20))
        _l_(607610)
        button1 = _c_(607618, _a_(607612, _n_(607611, "ttk", lambda: ttk), "Button"), _n_(607613, "self", lambda: self), text='Select Page',
                             command=lambda: _c_(607617, _a_(607615, _n_(607614, "controller", lambda: controller), "show_frame"), _n_(607616, "Page1", lambda: Page1)))
        _l_(607619)
        _c_(607622, _a_(607621, _n_(607620, "button1", lambda: button1), "grid"))
        _l_(607623)
        button2 = _c_(607629, _a_(607625, _n_(607624, "ttk", lambda: ttk), "Button"), _n_(607626, "self", lambda: self), text='print value', command=_a_(607628, _n_(607627, "self", lambda: self), "print_value"))
        _l_(607630)
        _c_(607633, _a_(607632, _n_(607631, "button2", lambda: button2), "grid"))
        _l_(607634)
    def print_value(self):
        _l_(607648)

        value = _c_(607640, _a_(607639, _a_(607638, _a_(607637, _n_(607636, "self", lambda: self), "controller"), "app_data")["listbox"], "get"))
        _l_(607641)
        _c_(607646, _n_(607642, "print", lambda: print), 'The value stored in StartPage some_entry = ' + _c_(607645, _n_(607643, "str", lambda: str), _n_(607644, "value", lambda: value)))
        _l_(607647)

app = _c_(607651, _n_(607650, "MyApp", lambda: MyApp))
_l_(607652)
_c_(607655, _a_(607654, _n_(607653, "app", lambda: app), "mainloop"))
_l_(607656)