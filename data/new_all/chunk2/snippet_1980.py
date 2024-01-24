# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73660841/attributeerror-list-object-has-no-attribute-set-canvas
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(426468)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(426470)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(426472)

except ImportError:
    pass
try:
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    _l_(426474)

except ImportError:
    pass

def f(x, a, b, c):
    _l_(426481)

    aux = _n_(426475, "a", lambda: a)*_n_(426476, "x", lambda: x)**2+_n_(426477, "b", lambda: b)*_n_(426478, "x", lambda: x)+_n_(426479, "c", lambda: c)
    _l_(426480)
    return aux

xlist = _c_(426484, _a_(426483, _n_(426482, "np", lambda: np), "linspace"), -10, 10, num = 1000)
_l_(426485)
##print(xlist)

a = 5
_l_(426486)
b = 1
_l_(426487)
c = 4
_l_(426488)
ylist = _c_(426494, _n_(426489, "f", lambda: f), _n_(426490, "xlist", lambda: xlist), _n_(426491, "a", lambda: a), _n_(426492, "b", lambda: b), _n_(426493, "c", lambda: c))
_l_(426495)

_c_(426498, _a_(426497, _n_(426496, "plt", lambda: plt), "figure"), num = 0, dpi = 120)
_l_(426499)

ax = _c_(426504, _a_(426501, _n_(426500, "plt", lambda: plt), "plot"), _n_(426502, "xlist", lambda: xlist), _n_(426503, "ylist", lambda: ylist), label = 'f(x)')
_l_(426505)
_c_(426510, _n_(426506, "print", lambda: print), _c_(426509, _n_(426507, "type", lambda: type), _n_(426508, "ax", lambda: ax)))
_l_(426511)

_c_(426514, _a_(426513, _n_(426512, "plt", lambda: plt), "title"), 'Plotting Example')
_l_(426515)
_c_(426518, _a_(426517, _n_(426516, "plt", lambda: plt), "xlabel"), 'Distance / ft')
_l_(426519)
_c_(426522, _a_(426521, _n_(426520, "plt", lambda: plt), "ylabel"), 'Height / ft')
_l_(426523)
_c_(426526, _a_(426525, _n_(426524, "plt", lambda: plt), "legend"))
_l_(426527)
_c_(426530, _a_(426529, _n_(426528, "plt", lambda: plt), "grid"), True)
_l_(426531)
# plt.show()
# __________________________________________________________________
my_w = _c_(426534, _a_(426533, _n_(426532, "tk", lambda: tk), "Tk"))
_l_(426535)
_c_(426538, _a_(426537, _n_(426536, "my_w", lambda: my_w), "geometry"), '1000x820+50+50')
_l_(426539)
_c_(426542, _a_(426541, _n_(426540, "my_w", lambda: my_w), "title"), 'data view on tk graph')
_l_(426543)

wrapper1 = _c_(426547, _a_(426545, _n_(426544, "tk", lambda: tk), "LabelFrame"), _n_(426546, "my_w", lambda: my_w))
_l_(426548)
wrapper2 = _c_(426552, _a_(426550, _n_(426549, "tk", lambda: tk), "LabelFrame"), _n_(426551, "my_w", lambda: my_w))
_l_(426553)
_c_(426556, _a_(426555, _n_(426554, "wrapper1", lambda: wrapper1), "pack"), fill="both", expand="yes", padx=5, pady=5)
_l_(426557)
_c_(426560, _a_(426559, _n_(426558, "wrapper2", lambda: wrapper2), "pack"), fill="both", padx=5, pady=5)
_l_(426561)


canvas = _c_(426565, _a_(426563, _n_(426562, "tk", lambda: tk), "Canvas"), _n_(426564, "wrapper1", lambda: wrapper1), bg="#595656", height=200)
_l_(426566)

_c_(426569, _a_(426568, _n_(426567, "canvas", lambda: canvas), "pack"), fill="both", expand=True)
_l_(426570)
# __________________________________________________________________


plot1 = _c_(426574, _n_(426571, "FigureCanvasTkAgg", lambda: FigureCanvasTkAgg), _n_(426572, "ax", lambda: ax), _n_(426573, "canvas", lambda: canvas))
_l_(426575)
_c_(426578, _a_(426577, _n_(426576, "plot1", lambda: plot1), "draw"))
_l_(426579)
_c_(426584, _a_(426583, _c_(426582, _a_(426581, _n_(426580, "plot1", lambda: plot1), "get_tk_widget")), "pack"), fill="both", expand="yes", padx=5, pady=5)
_l_(426585)

ctrl_frame = _c_(426589, _a_(426587, _n_(426586, "tk", lambda: tk), "Frame"), _n_(426588, "wrapper2", lambda: wrapper2), bg='green', height=100)
_l_(426590)
_c_(426593, _a_(426592, _n_(426591, "ctrl_frame", lambda: ctrl_frame), "pack"), fill="both")
_l_(426594)

_c_(426602, _a_(426599, _c_(426598, _a_(426596, _n_(426595, "tk", lambda: tk), "Button"), _n_(426597, "ctrl_frame", lambda: ctrl_frame), text='View', width=15, command=lambda:None), "place"), relx=0.9, rely=0.5, anchor=_a_(426601, _n_(426600, "tk", lambda: tk), "E"))
_l_(426603)

_c_(426606, _a_(426605, _n_(426604, "my_w", lambda: my_w), "mainloop"))
_l_(426607)