# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57698072/typeerror-list-indices-must-be-integers-or-slices-not-str-in-regression-anal
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(393782)

except ImportError:
    pass
try:
    import quandl
    _l_(393784)

except ImportError:
    pass
df= _c_(393787, _a_(393786, _n_(393785, "quandl", lambda: quandl), "get"), "FINRA/FORF_SYNVP", authtoken="sF7es4t9ozY6QjvZyL9M")
_l_(393788)
df=[['ShortVolume','TotalVolume']]
_l_(393789)
_n_(393790, "df", lambda: df)['change_PCT']=(_n_(393791, "df", lambda: df)['TotalVolume']-_n_(393792, "df", lambda: df)['ShortVolume'])/_n_(393793, "df", lambda: df)['ShortVolume']*100
_l_(393794)
df=_n_(393795, "df", lambda: df)[['change_PCT','ShortVolume']]
_l_(393796)
_c_(393801, _n_(393797, "print", lambda: print), _c_(393800, _a_(393799, _n_(393798, "df", lambda: df), "head")))
_l_(393802)