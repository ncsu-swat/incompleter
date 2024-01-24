# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65727635/pandas-read-excel-new-string-type-error-when-passing-string-using-converters-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df = _c_(534054, _a_(534052, _n_(534051, "pd", lambda: pd), "read_excel"), _n_(534053, "xlsx_input_path", lambda: xlsx_input_path), 'Sheet1', converters={"col_1": "string", "col_2": "string"}, engine="openpyxl")
_l_(534055)
_c_(534059, _n_(534056, "print", lambda: print), f"9 -\n{_a_(534058, _n_(534057, 'df', lambda: df), 'dtypes')}\n ")  # TypeError: 'str' object is not callable
_l_(534060)  # TypeError: 'str' object is not callable

df = _c_(534066, _a_(534062, _n_(534061, "pd", lambda: pd), "read_excel"), _n_(534063, "xlsx_input_path", lambda: xlsx_input_path), 'Sheet1', converters={"col_1": _n_(534064, "string", lambda: string), "col_2": _n_(534065, "string", lambda: string)}, engine="openpyxl")
_l_(534067)
_c_(534071, _n_(534068, "print", lambda: print), f"9 -\n{_a_(534070, _n_(534069, 'df', lambda: df), 'dtypes')}\n ")  # NameError: name 'string' is not defined
_l_(534072)  # NameError: name 'string' is not defined