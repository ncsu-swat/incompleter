# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_length_list(input_list):
    _l_(92976)

    max_length = _c_(92966, _n_(92961, "max", lambda: max), (_c_(92964, _n_(92962, "len", lambda: len), _n_(92963, "x", lambda: x)) for x in _n_(92965, "input_list", lambda: input_list)))
    _l_(92967)
    max_list = _c_(92971, _n_(92968, "max", lambda: max), _n_(92969, "input_list", lambda: input_list), key=_n_(92970, "len", lambda: len))
    _l_(92972)
    aux = (_n_(92973, "max_length", lambda: max_length), _n_(92974, "max_list", lambda: max_list))
    _l_(92975)
    return aux

def min_length_list(input_list):
    _l_(92992)

    min_length = _c_(92982, _n_(92977, "min", lambda: min), (_c_(92980, _n_(92978, "len", lambda: len), _n_(92979, "x", lambda: x)) for x in _n_(92981, "input_list", lambda: input_list)))
    _l_(92983)
    min_list = _c_(92987, _n_(92984, "min", lambda: min), _n_(92985, "input_list", lambda: input_list), key=_n_(92986, "len", lambda: len))
    _l_(92988)
    aux = (_n_(92989, "min_length", lambda: min_length), _n_(92990, "min_list", lambda: min_list))
    _l_(92991)
    return aux
_c_(92994, _n_(92993, "print", lambda: print), 'Original list:')
_l_(92995)
_c_(92998, _n_(92996, "print", lambda: print), _n_(92997, "list1", lambda: list1))
_l_(92999)
_c_(93001, _n_(93000, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93002)
_c_(93007, _n_(93003, "print", lambda: print), _c_(93006, _n_(93004, "max_length_list", lambda: max_length_list), _n_(93005, "list1", lambda: list1)))
_l_(93008)
_c_(93010, _n_(93009, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93011)
_c_(93016, _n_(93012, "print", lambda: print), _c_(93015, _n_(93013, "min_length_list", lambda: min_length_list), _n_(93014, "list1", lambda: list1)))
_l_(93017)
list1 = [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
_l_(93018)
_c_(93020, _n_(93019, "print", lambda: print), 'Original list:')
_l_(93021)
_c_(93024, _n_(93022, "print", lambda: print), _n_(93023, "list1", lambda: list1))
_l_(93025)
_c_(93027, _n_(93026, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93028)
_c_(93033, _n_(93029, "print", lambda: print), _c_(93032, _n_(93030, "max_length_list", lambda: max_length_list), _n_(93031, "list1", lambda: list1)))
_l_(93034)
_c_(93036, _n_(93035, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93037)
_c_(93042, _n_(93038, "print", lambda: print), _c_(93041, _n_(93039, "min_length_list", lambda: min_length_list), _n_(93040, "list1", lambda: list1)))
_l_(93043)
list1 = [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
_l_(93044)
_c_(93046, _n_(93045, "print", lambda: print), 'Original list:')
_l_(93047)
_c_(93050, _n_(93048, "print", lambda: print), _n_(93049, "list1", lambda: list1))
_l_(93051)
_c_(93053, _n_(93052, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93054)
_c_(93059, _n_(93055, "print", lambda: print), _c_(93058, _n_(93056, "max_length_list", lambda: max_length_list), _n_(93057, "list1", lambda: list1)))
_l_(93060)
_c_(93062, _n_(93061, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93063)
_c_(93068, _n_(93064, "print", lambda: print), _c_(93067, _n_(93065, "min_length_list", lambda: min_length_list), _n_(93066, "list1", lambda: list1)))
_l_(93069)