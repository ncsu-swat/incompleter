# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70097223/adding-image-to-legend-in-matplotlib-returns-error-attributeerror-barcontaine
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(405379)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(405381)

except ImportError:
    pass
try:
    import os, sys
    _l_(405383)

except ImportError:
    pass

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
_l_(405384)
men_means = [20, 34, 30, 35, 27]
_l_(405385)
women_means = [25, 32, 34, 20, 25]
_l_(405386)

x = _c_(405392, _a_(405388, _n_(405387, "np", lambda: np), "arange"), _c_(405391, _n_(405389, "len", lambda: len), _n_(405390, "labels", lambda: labels)))  # the label locations
_l_(405393)  # the label locations
width = 0.35
_l_(405394)

fig, ax = _c_(405397, _a_(405396, _n_(405395, "plt", lambda: plt), "subplots"))
_l_(405398)
rects1 = _c_(405405, _a_(405400, _n_(405399, "ax", lambda: ax), "bar"), _n_(405401, "x", lambda: x) - _n_(405402, "width", lambda: width)/2, _n_(405403, "men_means", lambda: men_means), _n_(405404, "width", lambda: width), label='Men')
_l_(405406)
rects2 = _c_(405413, _a_(405408, _n_(405407, "ax", lambda: ax), "bar"), _n_(405409, "x", lambda: x) + _n_(405410, "width", lambda: width)/2, _n_(405411, "women_means", lambda: women_means), _n_(405412, "width", lambda: width), label='Women')
_l_(405414)

# Add some text for labels, title and custom x-axis tick labels, etc.
_c_(405417, _a_(405416, _n_(405415, "ax", lambda: ax), "set_ylabel"), 'Scores')
_l_(405418)
_c_(405421, _a_(405420, _n_(405419, "ax", lambda: ax), "set_title"), 'Scores by group and gender')
_l_(405422)
_c_(405426, _a_(405424, _n_(405423, "ax", lambda: ax), "set_xticks"), _n_(405425, "x", lambda: x))
_l_(405427)
_c_(405430, _a_(405429, _n_(405428, "ax", lambda: ax), "legend")) # oringinal legend
_l_(405431) # oringinal legend

_c_(405435, _a_(405433, _n_(405432, "ax", lambda: ax), "bar_label"), _n_(405434, "rects1", lambda: rects1), padding=3)
_l_(405436)
_c_(405440, _a_(405438, _n_(405437, "ax", lambda: ax), "bar_label"), _n_(405439, "rects2", lambda: rects2), padding=3)
_l_(405441)
_c_(405444, _a_(405443, _n_(405442, "fig", lambda: fig), "tight_layout"))
_l_(405445)
_c_(405448, _a_(405447, _n_(405446, "plt", lambda: plt), "savefig"), 'bar.png')
_l_(405449)