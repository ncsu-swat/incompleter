# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a = ['a', 'b', 'c', 'd']
_l_(1548850)
_c_(1548853, _a_(1548852, _n_(1548851, "a", lambda: a), "pop"), 1)
_l_(1548854)

# now a is ['a', 'c', 'd']

a = ['a', 'b', 'c', 'd']
_l_(1548855)
_c_(1548858, _a_(1548857, _n_(1548856, "a", lambda: a), "pop"))
_l_(1548859)

# now a is ['a', 'b', 'c']

