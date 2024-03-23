# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_length_list(input_list):
    _l_(93292)

    max_length = _c_(93287, _n_(93282, "max", lambda: max), (_c_(93285, _n_(93283, "len", lambda: len), _n_(93284, "x", lambda: x)) for x in _n_(93286, "input_list", lambda: input_list)))
    _l_(93288)
    aux = (_n_(93289, "max_length", lambda: max_length), _n_(93290, "max_list", lambda: max_list))
    _l_(93291)
    return aux

def min_length_list(input_list):
    _l_(93308)

    min_length = _c_(93298, _n_(93293, "min", lambda: min), (_c_(93296, _n_(93294, "len", lambda: len), _n_(93295, "x", lambda: x)) for x in _n_(93297, "input_list", lambda: input_list)))
    _l_(93299)
    min_list = _c_(93303, _n_(93300, "min", lambda: min), _n_(93301, "input_list", lambda: input_list), key=_n_(93302, "len", lambda: len))
    _l_(93304)
    aux = (_n_(93305, "min_length", lambda: min_length), _n_(93306, "min_list", lambda: min_list))
    _l_(93307)
    return aux
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
_l_(93309)
_c_(93311, _n_(93310, "print", lambda: print), 'Original list:')
_l_(93312)
_c_(93315, _n_(93313, "print", lambda: print), _n_(93314, "list1", lambda: list1))
_l_(93316)
_c_(93318, _n_(93317, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93319)
_c_(93324, _n_(93320, "print", lambda: print), _c_(93323, _n_(93321, "max_length_list", lambda: max_length_list), _n_(93322, "list1", lambda: list1)))
_l_(93325)
_c_(93327, _n_(93326, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93328)
_c_(93333, _n_(93329, "print", lambda: print), _c_(93332, _n_(93330, "min_length_list", lambda: min_length_list), _n_(93331, "list1", lambda: list1)))
_l_(93334)
list1 = [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
_l_(93335)
_c_(93337, _n_(93336, "print", lambda: print), 'Original list:')
_l_(93338)
_c_(93341, _n_(93339, "print", lambda: print), _n_(93340, "list1", lambda: list1))
_l_(93342)
_c_(93344, _n_(93343, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93345)
_c_(93350, _n_(93346, "print", lambda: print), _c_(93349, _n_(93347, "max_length_list", lambda: max_length_list), _n_(93348, "list1", lambda: list1)))
_l_(93351)
_c_(93353, _n_(93352, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93354)
_c_(93359, _n_(93355, "print", lambda: print), _c_(93358, _n_(93356, "min_length_list", lambda: min_length_list), _n_(93357, "list1", lambda: list1)))
_l_(93360)
list1 = [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
_l_(93361)
_c_(93363, _n_(93362, "print", lambda: print), 'Original list:')
_l_(93364)
_c_(93367, _n_(93365, "print", lambda: print), _n_(93366, "list1", lambda: list1))
_l_(93368)
_c_(93370, _n_(93369, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93371)
_c_(93376, _n_(93372, "print", lambda: print), _c_(93375, _n_(93373, "max_length_list", lambda: max_length_list), _n_(93374, "list1", lambda: list1)))
_l_(93377)
_c_(93379, _n_(93378, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93380)
_c_(93385, _n_(93381, "print", lambda: print), _c_(93384, _n_(93382, "min_length_list", lambda: min_length_list), _n_(93383, "list1", lambda: list1)))
_l_(93386)