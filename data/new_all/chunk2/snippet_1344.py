# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30782676/attributeerror-exit-on-python-3-4
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(455753)

except ImportError:
    pass
try:
    import os
    _l_(455755)

except ImportError:
    pass
try:
    import latexmake
    _l_(455757)

except ImportError:
    pass
try:
    import mysql.connector
    _l_(455759)

except ImportError:
    pass
conn = _c_(455762, _a_(455761, _a_(455760, mysql, "connector"), "connect"), user='root',password='oilwell',host='localhost',database='sqlpush1')
_l_(455763)

with _n_(455764, "conn", lambda: conn):
    _l_(455769)

    mycursor = _c_(455767, _a_(455766, _n_(455765, "conn", lambda: conn), "cursor"))
    _l_(455768)
mycursor=_c_(455771, _n_(455770, "execute", lambda: execute), "SELECT DATE,oil,gas,oilprice,gasprice,totrev FROM results WHERE DATE BETWEEN '2011-01-01' AND '2027-12-01'")
_l_(455772)
rows = _c_(455775, _a_(455774, _n_(455773, "mycursor", lambda: mycursor), "fetchall"))
_l_(455776)
_c_(455779, _a_(455778, _n_(455777, "a", lambda: a), "write"), "\\documentclass{standalone}\\usepackage{booktabs}\n\n\\usepackage{siunitx}\r \n\
\r\n\\begin{document}\r\n\\begin{tabular}{ccS[table-format = 5.2]} \\\\ \\toprule\r")
_l_(455780)
_c_(455783, _a_(455782, _n_(455781, "a", lambda: a), "write"), "Date & Oil & Gas & Oil price & Gas price & Total Revenue \\\\ \\midrule \r")
_l_(455784)
for row in _n_(455785, "rows", lambda: rows):
    _l_(455818)

    a = _c_(455787, _n_(455786, "open", lambda: open), "testtest.tex", "w")
    _l_(455788)
    _c_(455809, _a_(455790, _n_(455789, "a", lambda: a), "write"), "" + _c_(455793, _n_(455791, "str", lambda: str), _n_(455792, "row", lambda: row)[0]) + " & " + _c_(455796, _n_(455794, "str", lambda: str), _n_(455795, "row", lambda: row)[1]) + " & " + _c_(455799, _n_(455797, "str", lambda: str), _n_(455798, "row", lambda: row)[2]) + " & " + _c_(455802, _n_(455800, "str", lambda: str), _n_(455801, "row", lambda: row)[3]) + " & " + _c_(455805, _n_(455803, "str", lambda: str), _n_(455804, "row", lambda: row)[4]) + " & " + _c_(455808, _n_(455806, "str", lambda: str), _n_(455807, "row", lambda: row)[5]) + " \\\\ \r")
    _l_(455810)

    _c_(455813, _a_(455812, _n_(455811, "a", lambda: a), "write"), "\\bottomrule \\end{tabular}\r\\end{document}")
    _l_(455814)
    _a_(455816, _n_(455815, "a", lambda: a), "close")
    _l_(455817)
_c_(455824, _n_(455819, "print", lambda: print), _c_(455823, _a_(455822, _a_(455821, _n_(455820, "os", lambda: os), "path"), "getsize"), "testtest.tex"))
_l_(455825)
_c_(455828, _a_(455827, _n_(455826, "os", lambda: os), "system"), 'latexmk.py -q testtest.tex')
_l_(455829)
_c_(455832, _a_(455831, _n_(455830, "mycursor", lambda: mycursor), "close"))
_l_(455833)
_c_(455836, _a_(455835, _n_(455834, "conn", lambda: conn), "close"))
_l_(455837)
_c_(455840, _a_(455839, _n_(455838, "a", lambda: a), "close"))
_l_(455841)