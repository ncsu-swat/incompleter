# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75619940/attributeerror-module-utils-has-no-attribute-svmtrain
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(597236)

except ImportError:
    pass
try:
    import numpy as np
    _l_(597238)

except ImportError:
    pass
try:
    import re
    _l_(597240)

except ImportError:
    pass
try:
    from matplotlib import pyplot
    _l_(597242)

except ImportError:
    pass
try:
    from scipy import optimize
    _l_(597244)

except ImportError:
    pass
try:
    from scipy.io import loadmat
    _l_(597246)

except ImportError:
    pass
try:
    import utils
    _l_(597248)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(597250)

except ImportError:
    pass
try:
    from sklearn.metrics import accuracy_score
    _l_(597252)

except ImportError:
    pass

data = _c_(597254, _n_(597253, "loadmat", lambda: loadmat), 'ex6data1.mat')
_l_(597255)
X, y = _n_(597256, "data", lambda: data)['X'], _n_(597257, "data", lambda: data)['y'][:, 0]
_l_(597258)

_c_(597263, _a_(597260, _n_(597259, "utils", lambda: utils), "plotData"), _n_(597261, "X", lambda: X), _n_(597262, "y", lambda: y))
_l_(597264)

_c_(597270, _a_(597266, _n_(597265, "pyplot", lambda: pyplot), "scatter"), _n_(597267, "X", lambda: X)[:,0], _n_(597268, "X", lambda: X)[:,1], c=_n_(597269, "y", lambda: y))
_l_(597271)
_a_(597273, _n_(597272, "pyplot", lambda: pyplot), "legend")
_l_(597274)
_c_(597277, _a_(597276, _n_(597275, "pyplot", lambda: pyplot), "show"))
_l_(597278)
C = 1
_l_(597279)
model = _c_(597287, _a_(597281, _n_(597280, "utils", lambda: utils), "svmTrain"), _n_(597282, "X", lambda: X), _n_(597283, "y", lambda: y), _n_(597284, "C", lambda: C), _a_(597286, _n_(597285, "utils", lambda: utils), "linearKernel"), 1e-3, 20)
_l_(597288)
_c_(597294, _a_(597290, _n_(597289, "utils", lambda: utils), "visualizeBoundaryLinear"), _n_(597291, "X", lambda: X), _n_(597292, "y", lambda: y), _n_(597293, "model", lambda: model))
_l_(597295)