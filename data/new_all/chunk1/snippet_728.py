# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33661893/typeerror-unhashable-type-dict-dictionaries-within-lists
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
first_dict = {}
_l_(380393)
new_list_of_dict = [{"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"},
                    {"name": "Johno"}]
_l_(380394)
for i in _n_(380395, "new_list_of_dict", lambda: new_list_of_dict):
    _l_(380408)

    _c_(380398, _n_(380396, "print", lambda: print), _n_(380397, "i", lambda: i)["name"])
    _l_(380399)
    _n_(380400, "first_dict", lambda: first_dict)[_n_(380401, "i", lambda: i)] = _n_(380402, "i", lambda: i)["name"]
    _l_(380403)
    _c_(380406, _n_(380404, "print", lambda: print), _n_(380405, "first_dict", lambda: first_dict))
    _l_(380407)