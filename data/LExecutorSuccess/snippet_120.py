# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1747817/create-a-dictionary-with-comprehension
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
names = ['a', 'b', 'd', 'f', 'c']
_l_(1548360)
names_to_id = {_n_(1548361, "v", lambda: v):_n_(1548362, "k", lambda: k) for k, v in _c_(1548365, _n_(1548363, "enumerate", lambda: enumerate), _n_(1548364, "names", lambda: names))}
_l_(1548366)
# {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'f': 4}

names = ['a', 'b', 'd', 'f', 'd', 'c']
_l_(1548367)
sorted_list = _c_(1548372, _n_(1548368, "list", lambda: list), _c_(1548371, _n_(1548369, "set", lambda: set), _n_(1548370, "names", lambda: names)))
_l_(1548373)
_c_(1548376, _a_(1548375, _n_(1548374, "sorted_list", lambda: sorted_list), "sort"))
_l_(1548377)
names_to_id = {_n_(1548378, "v", lambda: v):_n_(1548379, "k", lambda: k) for k, v in _c_(1548382, _n_(1548380, "enumerate", lambda: enumerate), _n_(1548381, "sorted_list", lambda: sorted_list))}
_l_(1548383)
# {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'f': 4}

names = [1,2,5,5,6,2,1]
_l_(1548384)
names_to_id = {_n_(1548385, "v", lambda: v):_n_(1548386, "k", lambda: k) for k, v in _c_(1548391, _n_(1548387, "enumerate", lambda: enumerate), _c_(1548390, _n_(1548388, "set", lambda: set), _n_(1548389, "names", lambda: names)))}
_l_(1548392)
# {1: 0, 2: 1, 5: 2, 6: 3}

