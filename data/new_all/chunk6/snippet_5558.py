# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51621735/pandas-feeding-slice-as-pandas-core-indexes-numeric-int64index-getting-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(350267)

except ImportError:
    pass

data = [['edward',1],['edward',0],['edward',0],['norm',1],['norm',0],['norm',0] ]
_l_(350268)

df_names = _c_(350272, _a_(350270, _n_(350269, "pd", lambda: pd), "DataFrame"), _n_(350271, "data", lambda: data) )
_l_(350273)

criteria = _n_(350274, "df_names", lambda: df_names)[1] == 1
_l_(350275)

df_just_changes = _n_(350276, "df_names", lambda: df_names)[ _n_(350277, "criteria", lambda: criteria) ]
_l_(350278)

_c_(350281, _n_(350279, "print", lambda: print), _n_(350280, "df_names", lambda: df_names))
_l_(350282)
_c_(350286, _n_(350283, "print", lambda: print), _a_(350285, _n_(350284, "df_just_changes", lambda: df_just_changes), "index"))
_l_(350287)
_c_(350295, _n_(350288, "print", lambda: print), _c_(350294, _a_(350289, "type of  df_just_changes.index {} ", "format"), _c_(350293, _n_(350290, "type", lambda: type), _a_(350292, _n_(350291, "df_just_changes", lambda: df_just_changes), "index") ) ) )
_l_(350296)
_c_(350304, _n_(350297, "print", lambda: print), _c_(350303, _a_(350298, "type of  df_just_changes.index[0] {} ", "format"), _c_(350302, _n_(350299, "type", lambda: type), _a_(350301, _n_(350300, "df_just_changes", lambda: df_just_changes), "index")[0] ) ) )
_l_(350305)
_c_(350311, _n_(350306, "print", lambda: print), _a_(350308, _n_(350307, "df_names", lambda: df_names), "values")[_a_(350310, _n_(350309, "df_just_changes", lambda: df_just_changes), "index") : 2 ])
_l_(350312)