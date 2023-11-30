# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6390393/matplotlib-make-tick-labels-font-size-smaller
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib as mpl
    _l_(1544496)

except ImportError:
    pass
label_size = 8
_l_(1544497)
_a_(1544499, _n_(1544498, "mpl", lambda: mpl), "rcParams")['xtick.labelsize'] = _n_(1544500, "label_size", lambda: label_size) 
_l_(1544501) 

