# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60049059/python-linear-regression-typeerror-invalid-type-promotion
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(376768)

except ImportError:
    pass
try:
    import numpy as np
    _l_(376770)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(376772)

except ImportError:
    pass
try:
    from sklearn.model_selection import train_test_split
    _l_(376774)

except ImportError:
    pass
try:
    from sklearn.linear_model import LinearRegression
    _l_(376776)

except ImportError:
    pass
data=_c_(376779, _a_(376778, _n_(376777, "pd", lambda: pd), "read_excel"), 'C:\\Users\\Proximo\\PycharmProjects\Counts\\venv\\Counts.xlsx')  
_l_(376780)  
_n_(376781, "data", lambda: data)['DATE'] = _c_(376785, _a_(376783, _n_(376782, "pd", lambda: pd), "to_datetime"), _n_(376784, "data", lambda: data)['DATE'])
_l_(376786)
_c_(376789, _a_(376788, _n_(376787, "data", lambda: data), "plot"), x = 'DATE', y = 'COUNT', style = 'o')
_l_(376790)
_c_(376793, _a_(376792, _n_(376791, "plt", lambda: plt), "title"), 'Corona Spread Over the Time')
_l_(376794)
_c_(376797, _a_(376796, _n_(376795, "plt", lambda: plt), "xlabel"), 'Date')
_l_(376798)
_c_(376801, _a_(376800, _n_(376799, "plt", lambda: plt), "ylabel"), 'Count')
_l_(376802)
_c_(376805, _a_(376804, _n_(376803, "plt", lambda: plt), "show"))
_l_(376806)

X=_c_(376810, _a_(376809, _a_(376808, _n_(376807, "data", lambda: data)['DATE'], "values"), "reshape"), -1,1)
_l_(376811)
y=_c_(376815, _a_(376814, _a_(376813, _n_(376812, "data", lambda: data)['COUNT'], "values"), "reshape"), -1,1)
_l_(376816)
X_train,X_test,Y_train,Y_test=_c_(376820, _n_(376817, "train_test_split", lambda: train_test_split), _n_(376818, "X", lambda: X),_n_(376819, "y", lambda: y),test_size=.2,random_state=0)
_l_(376821)
regressor = _c_(376823, _n_(376822, "LinearRegression", lambda: LinearRegression))  
_l_(376824)  
_c_(376829, _a_(376826, _n_(376825, "regressor", lambda: regressor), "fit"), _n_(376827, "X_train", lambda: X_train),_n_(376828, "Y_train", lambda: Y_train))
_l_(376830)
y_pre = _c_(376834, _a_(376832, _n_(376831, "regressor", lambda: regressor), "predict"), _n_(376833, "X_test", lambda: X_test))
_l_(376835)