# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65727635/pandas-read-excel-new-string-type-error-when-passing-string-using-converters-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df = _c_(523930, _a_(523928, _n_(523927, "pd", lambda: pd), "read_excel"), _n_(523929, "xlsx_input_path", lambda: xlsx_input_path), 'Sheet1',  engine="openpyxl")  
_l_(523931)  
df = _c_(523934, _a_(523933, _n_(523932, "df", lambda: df), "astype"), dtype={"col_1": "string", "col_2": "string"})
_l_(523935)
_c_(523939, _n_(523936, "print", lambda: print), f"6 -\n{_a_(523938, _n_(523937, 'df', lambda: df), 'dtypes')}\n ")
_l_(523940)

df = _c_(523945, _a_(523942, _n_(523941, "pd", lambda: pd), "read_excel"), _n_(523943, "xlsx_input_path", lambda: xlsx_input_path), 'Sheet1', dtype={"col_1": "string", "col_2": _n_(523944, "str", lambda: str)}, engine="openpyxl")
_l_(523946)
_c_(523950, _n_(523947, "print", lambda: print), f"7 -\n{_a_(523949, _n_(523948, 'df', lambda: df), 'dtypes')}\n ")
_l_(523951)

df = _c_(523957, _a_(523953, _n_(523952, "pd", lambda: pd), "read_excel"), _n_(523954, "xlsx_input_path", lambda: xlsx_input_path), 'Sheet1', converters={"col_1": _n_(523955, "str", lambda: str), "col_2": _n_(523956, "str", lambda: str)}, engine="openpyxl")
_l_(523958)
_c_(523962, _n_(523959, "print", lambda: print), f"8 -\n{_a_(523961, _n_(523960, 'df', lambda: df), 'dtypes')}\n ") 
_l_(523963) 