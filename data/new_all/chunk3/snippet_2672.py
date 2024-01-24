# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67229203/typeerror-data-type-list-not-understood
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a = {'Id': {0: 1, 1: 2, 2: 3},
 'col': {0: 5.1, 1: 4.9, 2: 4.9}}
_l_(552693)
d = _c_(552698, _a_(552696, _a_(552695, _n_(552694, "pd", lambda: pd), "DataFrame"), "from_dict"), _n_(552697, "a", lambda: a))
_l_(552699)
attr_unique_val = _c_(552704, _a_(552703, _c_(552702, _a_(552701, _n_(552700, "d", lambda: d), "groupby"), 'col')['Id'], "unique"))
_l_(552705)
attr_unique_val = _c_(552708, _a_(552707, _n_(552706, "attr_unique_val", lambda: attr_unique_val), "astype"), 'list')
_l_(552709)