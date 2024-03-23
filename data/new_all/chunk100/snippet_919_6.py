# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_length_list(input_list):
    _l_(93610)

    max_length = _c_(93600, _n_(93595, "max", lambda: max), (_c_(93598, _n_(93596, "len", lambda: len), _n_(93597, "x", lambda: x)) for x in _n_(93599, "input_list", lambda: input_list)))
    _l_(93601)
    max_list = _c_(93605, _n_(93602, "max", lambda: max), _n_(93603, "input_list", lambda: input_list), key=_n_(93604, "len", lambda: len))
    _l_(93606)
    aux = (_n_(93607, "max_length", lambda: max_length), _n_(93608, "max_list", lambda: max_list))
    _l_(93609)
    return aux

def min_length_list(input_list):
    _l_(93626)

    min_length = _c_(93616, _n_(93611, "min", lambda: min), (_c_(93614, _n_(93612, "len", lambda: len), _n_(93613, "x", lambda: x)) for x in _n_(93615, "input_list", lambda: input_list)))
    _l_(93617)
    min_list = _c_(93621, _n_(93618, "min", lambda: min), _n_(93619, "input_list", lambda: input_list), key=_n_(93620, "len", lambda: len))
    _l_(93622)
    aux = (_n_(93623, "min_length", lambda: min_length), _n_(93624, "min_list", lambda: min_list))
    _l_(93625)
    return aux
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
_l_(93627)
_c_(93629, _n_(93628, "print", lambda: print), 'Original list:')
_l_(93630)
_c_(93633, _n_(93631, "print", lambda: print), _n_(93632, "list1", lambda: list1))
_l_(93634)
_c_(93636, _n_(93635, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93637)
_c_(93642, _n_(93638, "print", lambda: print), _c_(93641, _n_(93639, "max_length_list", lambda: max_length_list), _n_(93640, "list1", lambda: list1)))
_l_(93643)
_c_(93645, _n_(93644, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93646)
_c_(93651, _n_(93647, "print", lambda: print), _c_(93650, _n_(93648, "min_length_list", lambda: min_length_list), _n_(93649, "list1", lambda: list1)))
_l_(93652)
_c_(93654, _n_(93653, "print", lambda: print), 'Original list:')
_l_(93655)
_c_(93658, _n_(93656, "print", lambda: print), _n_(93657, "list1", lambda: list1))
_l_(93659)
_c_(93661, _n_(93660, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93662)
_c_(93667, _n_(93663, "print", lambda: print), _c_(93666, _n_(93664, "max_length_list", lambda: max_length_list), _n_(93665, "list1", lambda: list1)))
_l_(93668)
_c_(93670, _n_(93669, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93671)
_c_(93676, _n_(93672, "print", lambda: print), _c_(93675, _n_(93673, "min_length_list", lambda: min_length_list), _n_(93674, "list1", lambda: list1)))
_l_(93677)
list1 = [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
_l_(93678)
_c_(93680, _n_(93679, "print", lambda: print), 'Original list:')
_l_(93681)
_c_(93684, _n_(93682, "print", lambda: print), _n_(93683, "list1", lambda: list1))
_l_(93685)
_c_(93687, _n_(93686, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93688)
_c_(93693, _n_(93689, "print", lambda: print), _c_(93692, _n_(93690, "max_length_list", lambda: max_length_list), _n_(93691, "list1", lambda: list1)))
_l_(93694)
_c_(93696, _n_(93695, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93697)
_c_(93702, _n_(93698, "print", lambda: print), _c_(93701, _n_(93699, "min_length_list", lambda: min_length_list), _n_(93700, "list1", lambda: list1)))
_l_(93703)