# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60917020/dictionary-with-lists-typeerror-unhashable-type-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def satisfied(self, assignment: _n_(470131, "Dict", lambda: Dict)[_n_(470132, "str", lambda: str), _n_(470133, "List", lambda: List)[_n_(470134, "str", lambda: str)]]) -> _n_(470135, "bool", lambda: bool):
        _l_(470167)

        row: _n_(470136, "str", lambda: str) = _a_(470138, _n_(470137, "self", lambda: self), "variables")[0]
        _l_(470139)
        column: _n_(470140, "str", lambda: str) = _a_(470142, _n_(470141, "self", lambda: self), "variables")[1]
        _l_(470143)

        # If either variable is not in the assignment then it is not
        # yet possible for them to conflict
        if _n_(470144, "row", lambda: row) not in _n_(470145, "assignment", lambda: assignment) or _n_(470146, "column", lambda: column) not in _n_(470147, "assignment", lambda: assignment):
                _l_(470149)

                aux = True
                _l_(470148)
                return aux

        row_num: _n_(470150, "int", lambda: int) = _c_(470153, _n_(470151, "int", lambda: int), _n_(470152, "row", lambda: row)[3:])
        _l_(470154)
        col_num: _n_(470155, "int", lambda: int) = _c_(470158, _n_(470156, "int", lambda: int), _n_(470157, "column", lambda: column)[3:])
        _l_(470159)
        aux = _n_(470160, "assignment", lambda: assignment)[_n_(470161, "row", lambda: row)][_n_(470162, "col_num", lambda: col_num)] == _n_(470163, "assignment", lambda: assignment)[_n_(470164, "col", lambda: col)][_n_(470165, "row_num", lambda: row_num)] # here is this error
        _l_(470166) # here is this error

        return aux # here is this error