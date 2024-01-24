# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60706749/getting-filenotfounderror-when-calling-python-coded-file-from-robot-framework
# setup.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from robot.libraries.BuiltIn import BuiltIn
    _l_(648429)

except ImportError:
    pass
try:
    import xlrd
    _l_(648431)

except ImportError:
    pass


def get_variables(env):
    _l_(648474)

    file_location = "values.xlsx"
    _l_(648432)
    workbook = _c_(648436, _a_(648434, _n_(648433, "xlrd", lambda: xlrd), "open_workbook"), _n_(648435, "file_location", lambda: file_location))
    _l_(648437)
    sheet = _c_(648441, _a_(648439, _n_(648438, "workbook", lambda: workbook), "sheet_by_name"), _n_(648440, "env", lambda: env))
    _l_(648442)
    _c_(648446, _n_(648443, "print", lambda: print), "Env : " + _a_(648445, _n_(648444, "sheet", lambda: sheet), "name"))
    _l_(648447)
    data = [[_c_(648452, _a_(648449, _n_(648448, "sheet", lambda: sheet), "cell_value"), _n_(648450, "r", lambda: r), _n_(648451, "c", lambda: c)) for c in _c_(648456, _n_(648453, "range", lambda: range), _a_(648455, _n_(648454, "sheet", lambda: sheet), "ncols"))] for r in _c_(648460, _n_(648457, "range", lambda: range), _a_(648459, _n_(648458, "sheet", lambda: sheet), "nrows"))]
    _l_(648461)
    _c_(648464, _n_(648462, "print", lambda: print), _n_(648463, "data", lambda: data))
    _l_(648465)
    _c_(648470, _a_(648468, _c_(648467, _n_(648466, "BuiltIn", lambda: BuiltIn)), "log_to_console"), _n_(648469, "data", lambda: data))
    _l_(648471)
    aux = _n_(648472, "data", lambda: data)
    _l_(648473)
    return aux