# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54870178/attributeerror-when-trying-to-save-pandas-dataframe-to-existing-excel-sheet
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
path = 'summary.xlsx'
_l_(388440)
book = _c_(388443, _n_(388441, "load_workbook", lambda: load_workbook), _n_(388442, "path", lambda: path))
_l_(388444)
writer = _c_(388448, _a_(388446, _n_(388445, "pd", lambda: pd), "ExcelWriter"), _n_(388447, "path", lambda: path), engine='openpyxl')
_l_(388449)
_n_(388450, "writer", lambda: writer).book = _n_(388451, "book", lambda: book)
_l_(388452)
_n_(388453, "writer", lambda: writer).sheets = _c_(388460, _n_(388454, "dict", lambda: dict), ((_a_(388456, _n_(388455, "ws", lambda: ws), "title"), _n_(388457, "ws", lambda: ws)) for ws in _a_(388459, _n_(388458, "book", lambda: book), "worksheets")))
_l_(388461)

_c_(388465, _a_(388463, _n_(388462, "df", lambda: df), "to_excel"), _n_(388464, "writer", lambda: writer), sheet_name="results")
_l_(388466)
_c_(388469, _a_(388468, _n_(388467, "writer", lambda: writer), "save"))
_l_(388470)