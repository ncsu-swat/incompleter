# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11346283/renaming-column-names-in-pandas
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
new_cols = ['a', 'b', 'c', 'd', 'e']
_l_(63199)
new_names_map = {_a_(63201, _n_(63200, "df", lambda: df), "columns")[_n_(63202, "i", lambda: i)]:_n_(63203, "new_cols", lambda: new_cols)[_n_(63204, "i", lambda: i)] for i in _c_(63209, _n_(63205, "range", lambda: range), _c_(63208, _n_(63206, "len", lambda: len), _n_(63207, "new_cols", lambda: new_cols)))}
_l_(63210)

_c_(63214, _a_(63212, _n_(63211, "df", lambda: df), "rename"), _n_(63213, "new_names_map", lambda: new_names_map), axis=1, inplace=True)
_l_(63215)

