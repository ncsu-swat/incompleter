# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63231901/tkinter-child-objects-typeerror-list-indices-must-be-integers-or-slices-not-s
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(471300)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(471302)

except ImportError:
    pass


class DummyParent(_a_(471304, _n_(471303, "ttk", lambda: ttk), "Frame")):
    _l_(471336)

    def __init__(self, master=None):
        _l_(471335)

        _c_(471308, _a_(471306, _n_(471305, "super", lambda: super)(), "__init__"), _n_(471307, "master", lambda: master))
        _l_(471309)
        _c_(471312, _a_(471311, _n_(471310, "master", lambda: master), "title"), 'Test')
        _l_(471313)
        _n_(471314, "self", lambda: self).children = []
        _l_(471315)
        for i in _c_(471317, _n_(471316, "range", lambda: range), 4):
            _l_(471334)

            _c_(471324, _a_(471320, _a_(471319, _n_(471318, "self", lambda: self), "children"), "append"), _c_(471323, _n_(471321, "DummyChild", lambda: DummyChild), _n_(471322, "self", lambda: self)))
            _l_(471325)
            _c_(471332, _a_(471329, _a_(471327, _n_(471326, "self", lambda: self), "children")[_n_(471328, "i", lambda: i)], "grid"), row=_n_(471330, "i", lambda: i)//2, column=_n_(471331, "i", lambda: i)%2)
            _l_(471333)


class DummyChild(_a_(471338, _n_(471337, "ttk", lambda: ttk), "Frame")):
    _l_(471352)

    def __init__(self, master):
        _l_(471351)

        _c_(471342, _a_(471340, _n_(471339, "super", lambda: super)(), "__init__"), _n_(471341, "master", lambda: master))
        _l_(471343)
        _c_(471349, _a_(471345, _n_(471344, "self", lambda: self), "state"), _c_(471348, _a_(471347, _n_(471346, "ttk", lambda: ttk), "Label"), text='Test'))
        _l_(471350)


root = _c_(471355, _a_(471354, _n_(471353, "tk", lambda: tk), "Tk"))
_l_(471356)

dP = _c_(471359, _n_(471357, "DummyParent", lambda: DummyParent), master=_n_(471358, "root", lambda: root))
_l_(471360)
_c_(471363, _a_(471362, _n_(471361, "dP", lambda: dP), "mainloop"))
_l_(471364)