# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62054884/using-a-lambda-function-for-pandas-dataframe-boolean-indexing-reports-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(653965)

except ImportError:
    pass

sowpods = _c_(653968, _a_(653967, _n_(653966, "pd", lambda: pd), "read_csv"), 'sowpods.csv', names=['Word'])
_l_(653969)

possible_combination = 'RE'
_l_(653970)
possible_words = _c_(653973, _a_(653972, _n_(653971, "pd", lambda: pd), "DataFrame"), [], columns=['Word'])
_l_(653974)

comb_in_word = lambda _: True if (_n_(653975, "possible_combination", lambda: possible_combination) in _n_(653976, "_", lambda: _)) else False # ------ line 8
_l_(653977) # ------ line 8

sowpods_bool = _c_(653981, _a_(653979, _n_(653978, "sowpods", lambda: sowpods)['Word'], "apply"), _n_(653980, "comb_in_word", lambda: comb_in_word)) # --------------------------- line 10
_l_(653982) # --------------------------- line 10
_c_(653988, _a_(653984, _n_(653983, "possible_words", lambda: possible_words), "append"), _a_(653986, _n_(653985, "sowpods", lambda: sowpods), "loc")[_n_(653987, "sowpods_bool", lambda: sowpods_bool), 'Word'])
_l_(653989)