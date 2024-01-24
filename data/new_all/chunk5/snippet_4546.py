# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55817018/undefined-name-error-when-minimizing-using-scipy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(666262)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(666264)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(666266)

except ImportError:
    pass
try:
    from scipy.optimize import minimize
    _l_(666268)

except ImportError:
    pass
try:
    from sklearn.metrics import r2_score
    _l_(666270)

except ImportError:
    pass

url = 'test_data.txt'
_l_(666271)
z = _c_(666275, _a_(666273, _n_(666272, "pd", lambda: pd), "read_csv"), _n_(666274, "url", lambda: url))
_l_(666276)
#
e1 = _a_(666278, _n_(666277, "z", lambda: z)['strain'], "values")
_l_(666279)
sigx = _a_(666281, _n_(666280, "z", lambda: z)['stress'], "values")
_l_(666282)
e=_c_(666286, _a_(666284, _n_(666283, "np", lambda: np), "array"), _n_(666285, "e1", lambda: e1))
_l_(666287)
sig1=_c_(666291, _a_(666289, _n_(666288, "np", lambda: np), "array"), _n_(666290, "sigx", lambda: sigx))
_l_(666292)
#print (sig1)

def sig2(e):
    _l_(666312)

    j=[1000,0.2]
    _l_(666293)
    aux = _c_(666310, _a_(666295, _n_(666294, "np", lambda: np), "mean"), (_n_(666296, "sig1", lambda: sig1)-(_n_(666297, "j", lambda: j)[0]*_c_(666302, _a_(666299, _n_(666298, "np", lambda: np), "power"), _n_(666300, "e", lambda: e),_n_(666301, "j", lambda: j)[1])))*(_n_(666303, "sig1", lambda: sig1)-(_n_(666304, "j", lambda: j)[0]*_c_(666309, _a_(666306, _n_(666305, "np", lambda: np), "power"), _n_(666307, "e", lambda: e),_n_(666308, "j", lambda: j)[1]))))
    _l_(666311)
    return aux
_c_(666317, _n_(666313, "print", lambda: print), _c_(666316, _n_(666314, "sig2", lambda: sig2), _n_(666315, "e", lambda: e)))
_l_(666318)

res= _c_(666322, _n_(666319, "minimize", lambda: minimize), _n_(666320, "sig2", lambda: sig2),_n_(666321, "j", lambda: j))
_l_(666323)
_c_(666326, _n_(666324, "print", lambda: print), _n_(666325, "res", lambda: res))
_l_(666327)