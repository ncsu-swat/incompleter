# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59199749/typeerror-while-trying-to-add-label-widgets-in-tkinter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = 10
_l_(360743)
y = 10
_l_(360744)
i = 0
_l_(360745)
Labels = ['Name', 'RName', 'Gender', 'Age', 'Cast', 'Add', 'Mob No.', 'Adhar No.']   
_l_(360746)   
for Label in _n_(360747, "Labels", lambda: Labels):
    _l_(360762)

    lbp1n = _c_(360753, _n_(360748, "Label", lambda: Label), _n_(360749, "window", lambda: window), text=_c_(360752, _n_(360750, "str", lambda: str), _n_(360751, "Label", lambda: Label)))
    _l_(360754)
    _c_(360759, _a_(360756, _n_(360755, "lbp1n", lambda: lbp1n), "place"), x=_n_(360757, "x", lambda: x), y=_n_(360758, "x", lambda: x))
    _l_(360760)
    x += 10
    _l_(360761)