# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56324165/python-error-attributeerror-module-scipy-misc-has-no-attribute-logsumexp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from lifetimes.plotting import *
    _l_(410531)

except ImportError:
    pass
try:
    from lifetimes.utils import *
    _l_(410533)

except ImportError:
    pass
try:
    from lifetimes.estimation import *
    _l_(410535)

except ImportError:
    pass
data = _c_(410538, _n_(410536, "summary_data_from_transaction_data", lambda: summary_data_from_transaction_data), _n_(410537, "df", lambda: df), 'CustomerID','InvoiceDate', monetary_value_col='Sales', observation_period_end='2011-12-9')
_l_(410539)
_c_(410544, _n_(410540, "print", lambda: print), _c_(410543, _a_(410542, _n_(410541, "data", lambda: data), "head")))
_l_(410545)