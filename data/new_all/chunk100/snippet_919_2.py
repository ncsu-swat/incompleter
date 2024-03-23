# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_length_list(input_list):
    _l_(93187)

    max_list = _c_(93182, _n_(93179, "max", lambda: max), _n_(93180, "input_list", lambda: input_list), key=_n_(93181, "len", lambda: len))
    _l_(93183)
    aux = (_n_(93184, "max_length", lambda: max_length), _n_(93185, "max_list", lambda: max_list))
    _l_(93186)
    return aux

def min_length_list(input_list):
    _l_(93203)

    min_length = _c_(93193, _n_(93188, "min", lambda: min), (_c_(93191, _n_(93189, "len", lambda: len), _n_(93190, "x", lambda: x)) for x in _n_(93192, "input_list", lambda: input_list)))
    _l_(93194)
    min_list = _c_(93198, _n_(93195, "min", lambda: min), _n_(93196, "input_list", lambda: input_list), key=_n_(93197, "len", lambda: len))
    _l_(93199)
    aux = (_n_(93200, "min_length", lambda: min_length), _n_(93201, "min_list", lambda: min_list))
    _l_(93202)
    return aux
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
_l_(93204)
_c_(93206, _n_(93205, "print", lambda: print), 'Original list:')
_l_(93207)
_c_(93210, _n_(93208, "print", lambda: print), _n_(93209, "list1", lambda: list1))
_l_(93211)
_c_(93213, _n_(93212, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93214)
_c_(93219, _n_(93215, "print", lambda: print), _c_(93218, _n_(93216, "max_length_list", lambda: max_length_list), _n_(93217, "list1", lambda: list1)))
_l_(93220)
_c_(93222, _n_(93221, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93223)
_c_(93228, _n_(93224, "print", lambda: print), _c_(93227, _n_(93225, "min_length_list", lambda: min_length_list), _n_(93226, "list1", lambda: list1)))
_l_(93229)
list1 = [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
_l_(93230)
_c_(93232, _n_(93231, "print", lambda: print), 'Original list:')
_l_(93233)
_c_(93236, _n_(93234, "print", lambda: print), _n_(93235, "list1", lambda: list1))
_l_(93237)
_c_(93239, _n_(93238, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93240)
_c_(93245, _n_(93241, "print", lambda: print), _c_(93244, _n_(93242, "max_length_list", lambda: max_length_list), _n_(93243, "list1", lambda: list1)))
_l_(93246)
_c_(93248, _n_(93247, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93249)
_c_(93254, _n_(93250, "print", lambda: print), _c_(93253, _n_(93251, "min_length_list", lambda: min_length_list), _n_(93252, "list1", lambda: list1)))
_l_(93255)
list1 = [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
_l_(93256)
_c_(93258, _n_(93257, "print", lambda: print), 'Original list:')
_l_(93259)
_c_(93262, _n_(93260, "print", lambda: print), _n_(93261, "list1", lambda: list1))
_l_(93263)
_c_(93265, _n_(93264, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93266)
_c_(93271, _n_(93267, "print", lambda: print), _c_(93270, _n_(93268, "max_length_list", lambda: max_length_list), _n_(93269, "list1", lambda: list1)))
_l_(93272)
_c_(93274, _n_(93273, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93275)
_c_(93280, _n_(93276, "print", lambda: print), _c_(93279, _n_(93277, "min_length_list", lambda: min_length_list), _n_(93278, "list1", lambda: list1)))
_l_(93281)