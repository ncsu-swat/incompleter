# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60019820/using-mnist-to-load-a-dataset-but-getting-file-not-found-error-windows-10-pyth
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from mnist import MNIST
    _l_(700662)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(700664)

except ImportError:
    pass
try:
    import numpy as np
    _l_(700666)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(700668)

except ImportError:
    pass
mndata = _c_(700670, _n_(700669, "MNIST", lambda: MNIST), '.')
_l_(700671)
images, labels = _c_(700674, _a_(700673, _n_(700672, "mndata", lambda: mndata), "load_training"))
_l_(700675)