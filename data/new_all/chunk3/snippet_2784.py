# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63065832/matplotlib-using-twinx-typeerror-axessubplot-object-does-not-support-item
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
fig, ax = _c_(555281, _a_(555280, _n_(555279, "plt", lambda: plt), "subplots"), 4,5,figsize=(8,8))
_l_(555282)
_n_(555283, "ax2", lambda: ax2)[0,0]=_c_(555286, _a_(555285, _n_(555284, "ax", lambda: ax)[0,0], "twinx"))
_l_(555287)