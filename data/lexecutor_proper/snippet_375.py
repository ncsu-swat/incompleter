# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-the-x-or-y-axis
# Note the super cluttered ticks on both X and Y axis.

# inputs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = _c_(62569, _a_(62568, _n_(62567, "np", lambda: np), "arange"), 1, 101)
_l_(62570)
y = _n_(62571, "x", lambda: x) * _c_(62575, _a_(62573, _n_(62572, "np", lambda: np), "log"), _n_(62574, "x", lambda: x)) 
_l_(62576) 

fig = _c_(62579, _a_(62578, _n_(62577, "plt", lambda: plt), "figure"))     # create figure
_l_(62580)     # create figure
ax = _c_(62583, _a_(62582, _n_(62581, "fig", lambda: fig), "add_subplot"), 111)
_l_(62584)
_c_(62589, _a_(62586, _n_(62585, "ax", lambda: ax), "plot"), _n_(62587, "x", lambda: x), _n_(62588, "y", lambda: y))
_l_(62590)
_c_(62594, _a_(62592, _n_(62591, "ax", lambda: ax), "set_xticks"), _n_(62593, "x", lambda: x))        # set xtick values
_l_(62595)        # set xtick values
_c_(62599, _a_(62597, _n_(62596, "ax", lambda: ax), "set_yticks"), _n_(62598, "y", lambda: y))        # set ytick values
_l_(62600)        # set ytick values

_c_(62603, _a_(62602, _n_(62601, "plt", lambda: plt), "show"))
_l_(62604)

# inputs
x = _c_(62607, _a_(62606, _n_(62605, "np", lambda: np), "arange"), 1, 101)
_l_(62608)
y = _n_(62609, "x", lambda: x) * _c_(62613, _a_(62611, _n_(62610, "np", lambda: np), "log"), _n_(62612, "x", lambda: x))
_l_(62614)

fig = _c_(62617, _a_(62616, _n_(62615, "plt", lambda: plt), "figure"))       # create figure
_l_(62618)       # create figure
ax = _c_(62621, _a_(62620, _n_(62619, "fig", lambda: fig), "add_subplot"), 111)
_l_(62622)
_c_(62627, _a_(62624, _n_(62623, "ax", lambda: ax), "plot"), _n_(62625, "x", lambda: x), _n_(62626, "y", lambda: y))
_l_(62628)

_c_(62632, _a_(62630, _n_(62629, "ax", lambda: ax), "set_xticks"), _n_(62631, "x", lambda: x))
_l_(62633)
_c_(62637, _a_(62635, _n_(62634, "ax", lambda: ax), "set_yticks"), _n_(62636, "y", lambda: y))
_l_(62638)

# which values need to be shown?
# here, we show every third value from `x` and `y`
show_every = 3
_l_(62639)

sparse_xticks = [None] * _a_(62641, _n_(62640, "x", lambda: x), "shape")[0]
_l_(62642)
_n_(62643, "sparse_xticks", lambda: sparse_xticks)[::_n_(62644, "show_every", lambda: show_every)] = _n_(62645, "x", lambda: x)[::_n_(62646, "show_every", lambda: show_every)]
_l_(62647)

sparse_yticks = [None] * _a_(62649, _n_(62648, "y", lambda: y), "shape")[0]
_l_(62650)
_n_(62651, "sparse_yticks", lambda: sparse_yticks)[::_n_(62652, "show_every", lambda: show_every)] = _n_(62653, "y", lambda: y)[::_n_(62654, "show_every", lambda: show_every)]
_l_(62655)

_c_(62659, _a_(62657, _n_(62656, "ax", lambda: ax), "set_xticklabels"), _n_(62658, "sparse_xticks", lambda: sparse_xticks), fontsize=6)   # set sparse xtick values
_l_(62660)   # set sparse xtick values
_c_(62664, _a_(62662, _n_(62661, "ax", lambda: ax), "set_yticklabels"), _n_(62663, "sparse_yticks", lambda: sparse_yticks), fontsize=6)   # set sparse ytick values
_l_(62665)   # set sparse ytick values

_c_(62668, _a_(62667, _n_(62666, "plt", lambda: plt), "show"))
_l_(62669)

