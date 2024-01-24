# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64607460/what-am-i-missing-because-i-keep-getting-a-typeerror-list-indices-must-be-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def add_rows(sq_list):
    _l_(608533)

    rowNum = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    _l_(608520)
    
    for row in _n_(608521, "rowNum", lambda: rowNum):
        _l_(608532)

        total = 0
        _l_(608522)
        for column in _n_(608523, "sq_list", lambda: sq_list)[_n_(608524, "row", lambda: row)]:
            _l_(608527)

            total += _n_(608525, "column", lambda: column)
            _l_(608526)
        _c_(608530, _n_(608528, "print", lambda: print), "Row total is:", _n_(608529, "total", lambda: total))
        _l_(608531)
_c_(608535, _n_(608534, "add_rows", lambda: add_rows), [[1, 3, 8],
          [2, 4, 6],
          [7, 9, 0]])
_l_(608536)