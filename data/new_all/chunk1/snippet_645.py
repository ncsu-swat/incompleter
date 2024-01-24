# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65172406/typeerror-qpixmap-argument-1-has-unexpected-type-figure
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(398692)

except ImportError:
    pass
try:
    import numpy as np
    _l_(398694)

except ImportError:
    pass

labels = ['Word', 'Excel', 'Chrome','Visual Studio Code'] 
_l_(398695) 
title = [20,32,22,25] 
_l_(398696) 
cores = ['lightblue','green','blue','red']
_l_(398697)
explode = (0,0.1,0,0)
_l_(398698)
_a_(398700, _n_(398699, "plt", lambda: plt), "rcParams")['font.size'] = '16'
_l_(398701)
total=_c_(398704, _n_(398702, "sum", lambda: sum), _n_(398703, "title", lambda: title))
_l_(398705)
_c_(398716, _a_(398707, _n_(398706, "plt", lambda: plt), "pie"), _n_(398708, "title", lambda: title),explode=_n_(398709, "explode", lambda: explode),labels=_n_(398710, "labels", lambda: labels),colors=_n_(398711, "cores", lambda: cores),autopct=lambda p: _c_(398715, _a_(398712, '{:.0f}', "format"), _n_(398713, "p", lambda: p)*_n_(398714, "total", lambda: total)/100), shadow=True, startangle=90)
_l_(398717)
_c_(398720, _a_(398719, _n_(398718, "plt", lambda: plt), "axis"), 'equal')
_l_(398721)
grafic = _c_(398724, _a_(398723, _n_(398722, "plt", lambda: plt), "gcf"))
_l_(398725)
_c_(398733, _a_(398729, _a_(398728, _a_(398727, _n_(398726, "self", lambda: self), "ui"), "grafig_1"), "setPixmap"), _c_(398732, _n_(398730, "QPixmap", lambda: QPixmap), _n_(398731, "grafic", lambda: grafic)))
_l_(398734)