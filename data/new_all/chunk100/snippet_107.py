# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(61396)

except ImportError:
    pass
fig, ax = _c_(61399, _a_(61398, _n_(61397, "plt", lambda: plt), "subplots"), nrows=1, ncols=1 )  # create figure & 1 axis
_l_(61400)  # create figure & 1 axis
_c_(61403, _a_(61402, _n_(61401, "ax", lambda: ax), "plot"), [0,1,2], [10,20,3])
_l_(61404)
_c_(61407, _a_(61406, _n_(61405, "fig", lambda: fig), "savefig"), 'path/to/save/image/to.png')   # save the figure to file
_l_(61408)   # save the figure to file
_c_(61412, _a_(61410, _n_(61409, "plt", lambda: plt), "close"), _n_(61411, "fig", lambda: fig))    # close the figure window
_l_(61413)    # close the figure window

