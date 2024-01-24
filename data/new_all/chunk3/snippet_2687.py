# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66802437/attributeerror-int-object-has-no-attribute-append-getting-dict-out-of-two
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(538794)

except ImportError:
    pass
final_dict = _c_(538797, _n_(538795, "defaultdict", lambda: defaultdict), _n_(538796, "list", lambda: list))
_l_(538798)
list_keys= ['A', 'A', 'B', 'C']
_l_(538799)
list_values= [1,2,3,4]
_l_(538800)

for i in _c_(538805, _n_(538801, "range", lambda: range), _c_(538804, _n_(538802, "len", lambda: len), _n_(538803, "list_keys", lambda: list_keys))):
    _l_(538824)

    if _n_(538806, "list_keys", lambda: list_keys)[_n_(538807, "i", lambda: i)] in _n_(538808, "final_dict", lambda: final_dict):
        _l_(538823)

        _c_(538815, _a_(538812, _n_(538809, "final_dict", lambda: final_dict)[_n_(538810, "list_keys", lambda: list_keys)[_n_(538811, "i", lambda: i)]], "append"), _n_(538813, "list_values", lambda: list_values)[_n_(538814, "i", lambda: i)])
        _l_(538816)
    else:
        _n_(538817, "final_dict", lambda: final_dict)[_n_(538818, "list_keys", lambda: list_keys)[_n_(538819, "i", lambda: i)]] = _n_(538820, "list_values", lambda: list_values)[_n_(538821, "i", lambda: i)]
        _l_(538822)