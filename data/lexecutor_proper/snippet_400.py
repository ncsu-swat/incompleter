# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13331698/how-to-apply-a-function-to-two-columns-of-pandas-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(62814)

except ImportError:
    pass

df = _c_(62817, _a_(62816, _n_(62815, "pd", lambda: pd), "DataFrame"), {'ID':['1','2','3'], 'col_1': [0,2,3], 'col_2':[1,4,5]})
_l_(62818)
mylist = ['a','b','c','d','e','f']
_l_(62819)

def get_sublist(sta,end):
    _l_(62824)

    aux = _n_(62820, "mylist", lambda: mylist)[_n_(62821, "sta", lambda: sta):_n_(62822, "end", lambda: end)+1]
    _l_(62823)
    return aux

def get_sublist_list(cols):
    _l_(62830)

    aux = [_c_(62828, _n_(62825, "get_sublist", lambda: get_sublist), _n_(62826, "cols", lambda: cols)[0],_n_(62827, "cols", lambda: cols)[1])]
    _l_(62829)
    return aux

def unlist(list_of_lists):
    _l_(62833)

    aux = _n_(62831, "list_of_lists", lambda: list_of_lists)[0]
    _l_(62832)
    return aux

_n_(62834, "df", lambda: df)['col_3'] = _c_(62841, _a_(62839, _c_(62838, _a_(62836, _n_(62835, "df", lambda: df)[['col_1','col_2']], "apply"), _n_(62837, "get_sublist_list", lambda: get_sublist_list),axis=1), "apply"), _n_(62840, "unlist", lambda: unlist))
_l_(62842)

_n_(62843, "df", lambda: df)
_l_(62844)

