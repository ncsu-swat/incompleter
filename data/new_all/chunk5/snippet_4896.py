# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42405289/typeerror-overlaps-missing-3-required-positional-arguments-y1-x2-and
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(680391)

except ImportError:
    pass
try:
    import tkinter.messagebox
    _l_(680393)

except ImportError:
    pass
root = _c_(680395, _n_(680394, "Tk", lambda: Tk))
_l_(680396)

coords = 1447, 474
_l_(680397)
canvas = _c_(680400, _n_(680398, "Canvas", lambda: Canvas), _n_(680399, "root", lambda: root), width=1480, height=960)
_l_(680401)
frame = _c_(680404, _n_(680402, "Frame", lambda: Frame), _n_(680403, "root", lambda: root), width=209, height=960)
_l_(680405)

def cords(event):
    _l_(680413)

    _c_(680411, _n_(680406, "print", lambda: print), _a_(680408, _n_(680407, "event", lambda: event), "x"), _a_(680410, _n_(680409, "event", lambda: event), "y"))
    _l_(680412)

def click(event):
    _l_(680430)

    canvas_id = _c_(680421, _a_(680415, _n_(680414, "canvas", lambda: canvas), "create_line"), _a_(680417, _n_(680416, "event", lambda: event), "x"), _a_(680419, _n_(680418, "event", lambda: event), "y"), _n_(680420, "coords", lambda: coords))
    _l_(680422)
    _c_(680428, _a_(680424, _n_(680423, "canvas", lambda: canvas), "after"), 100,_a_(680426, _n_(680425, "canvas", lambda: canvas), "delete"),_n_(680427, "canvas_id", lambda: canvas_id))
    _l_(680429)

line = _n_(680431, "click", lambda: click)
_l_(680432)

obj1=_c_(680435, _a_(680434, _n_(680433, "canvas", lambda: canvas), "create_rectangle"), 605,482,247,157)
_l_(680436)
obj2=_c_(680439, _a_(680438, _n_(680437, "canvas", lambda: canvas), "create_rectangle"), 802,720,270,640)
_l_(680440)

objoverlap2=_c_(680443, _a_(680442, _n_(680441, "canvas", lambda: canvas), "find_overlapping"), 802,720,1082, 473)
_l_(680444)

_c_(680448, _a_(680446, _n_(680445, "canvas", lambda: canvas), "bind"), '<Button-1>',_n_(680447, "line", lambda: line))
_l_(680449)
photo = _c_(680451, _n_(680450, "PhotoImage", lambda: PhotoImage), file='76.gif')
_l_(680452)
label = _c_(680456, _n_(680453, "Label", lambda: Label), _n_(680454, "frame", lambda: frame), image=_n_(680455, "photo", lambda: photo))
_l_(680457)
_c_(680461, _a_(680459, _n_(680458, "label", lambda: label), "config"), image=_n_(680460, "photo", lambda: photo))
_l_(680462)
_c_(680465, _a_(680464, _n_(680463, "label", lambda: label), "pack"))
_l_(680466)

_c_(680469, _a_(680468, _n_(680467, "frame", lambda: frame), "pack"), side='right')
_l_(680470)
_c_(680473, _a_(680472, _n_(680471, "canvas", lambda: canvas), "pack"), side='left')
_l_(680474)

while True:
    _l_(680484)

    _c_(680477, _a_(680476, _n_(680475, "canvas", lambda: canvas), "find_overlapping"), 605,156,247,482)!=_n_(680478, "line", lambda: line)
    _l_(680479)
    _c_(680482, _a_(680481, _n_(680480, "root", lambda: root), "mainloop"))
    _l_(680483)