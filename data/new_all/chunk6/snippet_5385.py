# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59686429/pyspark-python3-pickle-picklingerror-could-not-serialize-object-typeerror-ca
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
udf_call = _c_(348377, _n_(348373, "udf", lambda: udf), _n_(348374, "udf_funct", lambda: udf_funct), _c_(348376, _n_(348375, "StringType", lambda: StringType)))
_l_(348378)
col_columns = [_c_(348381, _n_(348379, "col", lambda: col), _n_(348380, "c", lambda: c)) for c in _a_(348383, _n_(348382, "df", lambda: df), "columns")]
_l_(348384)
_c_(348387, _n_(348385, "print", lambda: print), _n_(348386, "col_columns", lambda: col_columns)) 
_l_(348388) 
#has list with bytecodes Column<b' which is not in case of 2.7
_c_(348393, _n_(348389, "udf_call", lambda: udf_call), _c_(348392, _n_(348390, "struct", lambda: struct), *_n_(348391, "col_columns", lambda: col_columns)))
_l_(348394)