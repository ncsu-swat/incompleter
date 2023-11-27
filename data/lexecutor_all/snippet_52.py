# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
py = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
_l_(1548650)

sort_on = "name"
_l_(1548651)
decorated = [(_n_(1548652, "dict_", lambda: dict_)[_n_(1548653, "sort_on", lambda: sort_on)], _n_(1548654, "dict_", lambda: dict_)) for dict_ in _n_(1548655, "py", lambda: py)]
_l_(1548656)
_c_(1548659, _a_(1548658, _n_(1548657, "decorated", lambda: decorated), "sort"))
_l_(1548660)
result = [_n_(1548661, "dict_", lambda: dict_) for (key, dict_) in _n_(1548662, "decorated", lambda: decorated)]
_l_(1548663)

_n_(1548664, "result", lambda: result)
_l_(1548665)
[{'age': 10, 'name': 'Bart'}, {'age': 39, 'name': 'Homer'}]
_l_(1548666)

