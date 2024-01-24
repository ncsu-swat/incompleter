# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44721821/typeerror-a-common-type-cannot-be-infered-from-types-float-string-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import graphlab
    _l_(539697)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(539699)

except ImportError:
    pass
try:
    import numpy as np
    _l_(539701)

except ImportError:
    pass
try:
    import matplotlib.pyplot as pt
    _l_(539703)

except ImportError:
    pass
try:
    from numpy import array
    _l_(539705)

except ImportError:
    pass
try:
    from graphlab import SFrame
    _l_(539707)

except ImportError:
    pass


user_columns =['No','User id','User Name','Skill','Given Test Name','Given Test ID','Recommend Test','Recommend Test ID','Time Start','Time End','Score','Max Score']
_l_(539708)

data=_c_(539712, _a_(539710, _n_(539709, "pd", lambda: pd), "read_table"), 'http://tech4partner.com.cp-in-5.webhostbox.net/recommend_test.php', sep='^',header=None,names = _n_(539711, "user_columns", lambda: user_columns))
_l_(539713)

df2 = _a_(539715, _n_(539714, "data", lambda: data), "ix")[2:]
_l_(539716)

df3=_c_(539719, _a_(539718, _n_(539717, "df2", lambda: df2), "reset_index"))
_l_(539720)

df4=_c_(539723, _a_(539722, _n_(539721, "df3", lambda: df3), "drop"), 'index', axis=1)
_l_(539724)

df5=_c_(539732, _a_(539726, _n_(539725, "df4", lambda: df4), "drop"), _a_(539728, _n_(539727, "df4", lambda: df4), "index")[_c_(539731, _n_(539729, "len", lambda: len), _n_(539730, "df4", lambda: df4))-1])
_l_(539733)

df5=_c_(539739, _a_(539735, _n_(539734, "df5", lambda: df5), "reset_index"), 1,[_c_(539738, _n_(539736, "len", lambda: len), _n_(539737, "df5", lambda: df5))-1])
_l_(539740)

df7 = _c_(539743, _a_(539742, _n_(539741, "df5", lambda: df5), "reset_index"))
_l_(539744)

df8=_c_(539747, _a_(539746, _n_(539745, "df7", lambda: df7), "drop"), 'index', axis=1)
_l_(539748)

df9=_c_(539754, _a_(539750, _n_(539749, "df8", lambda: df8), "head"), _c_(539753, _n_(539751, "len", lambda: len), _n_(539752, "df8", lambda: df8)))
_l_(539755)

_n_(539756, "df9", lambda: df9).index = _c_(539762, _a_(539758, _n_(539757, "np", lambda: np), "arange"), 1, _c_(539761, _n_(539759, "len", lambda: len), _n_(539760, "df9", lambda: df9)) + 1)
_l_(539763)

df9=_c_(539766, _a_(539765, _n_(539764, "df9", lambda: df9), "head"), 50)
_l_(539767)

_n_(539768, "df9", lambda: df9)
_l_(539769)