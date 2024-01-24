# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44999650/error-nameerror-name-values-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def summary_stats(col_name, col_data):
    _l_(652828)

    values = {'column name' : _n_(652810, "col_name", lambda: col_name),
    'mean' : _c_(652814, _a_(652812, _n_(652811, "np", lambda: np), "mean"), _n_(652813, "col_data", lambda: col_data)),
    'median' : _c_(652818, _a_(652816, _n_(652815, "np", lambda: np), "median"), _n_(652817, "col_data", lambda: col_data)),
    'variance' : _c_(652822, _a_(652820, _n_(652819, "np", lambda: np), "var"), _n_(652821, "col_data", lambda: col_data)),
    'standard deviation' : _c_(652826, _a_(652824, _n_(652823, "np", lambda: np), "std"), _n_(652825, "col_data", lambda: col_data))}
    _l_(652827)

for key, value in _c_(652831, _a_(652830, _n_(652829, "values", lambda: values), "items")):
    _l_(652837)

    _c_(652835, _n_(652832, "print", lambda: print), _n_(652833, "key", lambda: key), ':' , _n_(652834, "value", lambda: value))
    _l_(652836)