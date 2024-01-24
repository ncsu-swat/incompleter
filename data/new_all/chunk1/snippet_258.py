# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50355133/matplotlib-0-99-mplot3d-attributeerror-list-object-has-no-attribute-ndim
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cobra
    _l_(405573)

except ImportError:
    pass
try:
    import os
    _l_(405575)

except ImportError:
    pass
try:
    from os.path import join
    _l_(405577)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(405579)

except ImportError:
    pass
try:
    import numpy as np
    _l_(405581)

except ImportError:
    pass
try:
    from matplotlib import cm
    _l_(405583)

except ImportError:
    pass
try:
    from mpl_toolkits.mplot3d import Axes3D
    _l_(405585)

except ImportError:
    pass
data_dir ='/Users/stephenchapman/Documents/research/FBA_algae_digesate/COBRApy/iCZ843/iCZ843_models'
_l_(405586)
model = _c_(405593, _a_(405589, _a_(405588, _n_(405587, "cobra", lambda: cobra), "io"), "read_sbml_model"), _c_(405592, _n_(405590, "join", lambda: join), _n_(405591, "data_dir", lambda: data_dir), "iCZ843_hetero.xml"))
_l_(405594)
_a_(405596, _n_(405595, "model", lambda: model), "reactions")[15].upper_bound = -0 #ammonia
_l_(405597) #ammonia
_a_(405599, _n_(405598, "model", lambda: model), "reactions")[15].lower_bound = -98.3
_l_(405600)
_a_(405602, _n_(405601, "model", lambda: model), "reactions")[27].upper_bound = -0 #acetate
_l_(405603) #acetate
_a_(405605, _n_(405604, "model", lambda: model), "reactions")[27].lower_bound = -3.3
_l_(405606)
_a_(405608, _n_(405607, "model", lambda: model), "reactions")[14].upper_bound = -0 #phosphate
_l_(405609) #phosphate
_a_(405611, _n_(405610, "model", lambda: model), "reactions")[14].lower_bound = -10
_l_(405612)
_a_(405614, _n_(405613, "model", lambda: model), "reactions")[16].upper_bound = -0 #nitrate
_l_(405615) #nitrate
_a_(405617, _n_(405616, "model", lambda: model), "reactions")[16].lower_bound = -30.3
_l_(405618)
_a_(405620, _n_(405619, "model", lambda: model), "reactions")[20].upper_bound = -0 #magnesium
_l_(405621) #magnesium
_a_(405623, _n_(405622, "model", lambda: model), "reactions")[20].lower_bound = -0.56
_l_(405624)
_a_(405626, _n_(405625, "model", lambda: model), "reactions")[18].upper_bound = -0 #iron
_l_(405627) #iron
_a_(405629, _n_(405628, "model", lambda: model), "reactions")[18].lower_bound = -2.16
_l_(405630)
_n_(405631, "model", lambda: model).objective = _a_(405633, _n_(405632, "model", lambda: model), "reactions")[63]
_l_(405634)
solution = _c_(405637, _a_(405636, _n_(405635, "model", lambda: model), "optimize"))
_l_(405638)
_c_(405641, _a_(405640, _n_(405639, "model", lambda: model), "summary"))
_l_(405642)

ac_uptake = []
_l_(405643)
NH4_uptake = []
_l_(405644)
growth_rate = []
_l_(405645)
for i in _c_(405647, _n_(405646, "range", lambda: range), 0,85,5):
    _l_(405700)

    _a_(405649, _n_(405648, "model", lambda: model), "reactions")[27].lower_bound = -_n_(405650, "i", lambda: i) #acetate uptake
    _l_(405651) #acetate uptake
    _a_(405653, _n_(405652, "model", lambda: model), "reactions")[27].upper_bound = -_n_(405654, "i", lambda: i)
    _l_(405655)
    for j in (0,80,5):
        _l_(405699)

        _a_(405657, _n_(405656, "model", lambda: model), "reactions")[15].lower_bound = -_n_(405658, "i", lambda: i) #NH4 uptake
        _l_(405659) #NH4 uptake
        _a_(405661, _n_(405660, "model", lambda: model), "reactions")[15].upper_bound = -_n_(405662, "i", lambda: i)
        _l_(405663)
        _c_(405667, _n_(405664, "print", lambda: print), _a_(405666, _n_(405665, "solution", lambda: solution), "f"))
        _l_(405668)
        _c_(405673, _a_(405670, _n_(405669, "growth_rate", lambda: growth_rate), "append"), _a_(405672, _n_(405671, "solution", lambda: solution), "f"))
        _l_(405674)
        _c_(405680, _a_(405676, _n_(405675, "ac_uptake", lambda: ac_uptake), "append"), _a_(405679, _a_(405678, _n_(405677, "model", lambda: model), "reactions")[27], "lower_bound"))
        _l_(405681)
        _c_(405687, _a_(405683, _n_(405682, "NH4_uptake", lambda: NH4_uptake), "append"), _a_(405686, _a_(405685, _n_(405684, "model", lambda: model), "reactions")[15], "lower_bound"))
        _l_(405688)
        plot_ac_uptake = _c_(405692, _n_(405689, "list", lambda: list), _c_(405691, _n_(405690, "range", lambda: range), 0,85,5))
        _l_(405693)
        plot_NH4_uptake = _c_(405697, _n_(405694, "list", lambda: list), _c_(405696, _n_(405695, "range", lambda: range), 0,85,5))
        _l_(405698)

X = _n_(405701, "plot_ac_uptake", lambda: (plot_ac_uptake))
_l_(405702)
Y = _n_(405703, "plot_NH4_uptake", lambda: (plot_NH4_uptake))
_l_(405704)
X, Y = _c_(405709, _a_(405706, _n_(405705, "np", lambda: np), "meshgrid"), _n_(405707, "X", lambda: X), _n_(405708, "Y", lambda: Y))
_l_(405710)
Z = _n_(405711, "growth_rate", lambda: (growth_rate))
_l_(405712)
fig = _c_(405715, _a_(405714, _n_(405713, "plt", lambda: plt), "figure"))
_l_(405716)
ax = _c_(405719, _n_(405717, "Axes3D", lambda: Axes3D), _n_(405718, "fig", lambda: fig))
_l_(405720)
_c_(405728, _a_(405722, _n_(405721, "ax", lambda: ax), "plot_surface"), _n_(405723, "X", lambda: X), _n_(405724, "Y", lambda: Y), _n_(405725, "Z", lambda: Z), rstride=1, cstride=1, cmap=_a_(405727, _n_(405726, "cm", lambda: cm), "viridis"))
_l_(405729)
_c_(405732, _a_(405731, _n_(405730, "plt", lambda: plt), "show"))
_l_(405733)