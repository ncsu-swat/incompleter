# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51756290/python-functions-within-classes-nameerror-function-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from convert import CollateCSV
    _l_(698396)

except ImportError:
    pass
x = _c_(698398, _n_(698397, "CollateCSV", lambda: CollateCSV), "./csv_files", "./file_list.csv", output=False)
_l_(698399)

_c_(698404, _n_(698400, "print", lambda: print), _c_(698403, _a_(698402, _n_(698401, "x", lambda: x), "list_files_to_reas")))
_l_(698405)