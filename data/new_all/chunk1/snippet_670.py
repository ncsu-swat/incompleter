# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61919865/typeerror-parameters-to-generic-types-must-be-types-got-ellipsis
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def get_list_from_tuple(board: _n_(407529, "Tuple", lambda: Tuple)[_n_(407530, "Tuple", lambda: Tuple)[_n_(407531, "Optional", lambda: Optional)[_n_(407532, "int", lambda: int)], ...], ...]) -> _n_(407533, "List", lambda: List)[_n_(407534, "List", lambda: List)[_n_(407535, "Optional", lambda: Optional)[_n_(407536, "int", lambda: int)], ...], ...]:
    _l_(407544)

    aux = _c_(407542, _n_(407537, "list", lambda: list), (_c_(407540, _n_(407538, "list", lambda: list), _n_(407539, "x", lambda: x)) for x in _n_(407541, "board", lambda: board)))
    _l_(407543)
    return aux