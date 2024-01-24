# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64885946/how-to-solve-typeerror-string-indices-must-be-integers-while-removing-specific
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(549274)

except ImportError:
    pass

df = _c_(549277, _a_(549276, _n_(549275, "pd", lambda: pd), "read_csv"), "Sample data.csv")
_l_(549278)
df1 = _c_(549281, _a_(549280, _n_(549279, "pd", lambda: pd), "DataFrame"))
_l_(549282)

_n_(549283, "df1", lambda: df1)['Sentiment'] = _c_(549288, _a_(549285, _n_(549284, "df", lambda: df)['Sentiment'], "apply"), lambda x: _n_(549286, "x", lambda: x) if _n_(549287, "x", lambda: x)['compound'] <= 0 else None)     # remove compound dictionary entry more than 1
_l_(549289)     # remove compound dictionary entry more than 1
_c_(549292, _a_(549291, _n_(549290, "df1", lambda: df1), "dropna"), inplace=True)           #remove none lines
_l_(549293)           #remove none lines
_c_(549296, _n_(549294, "print", lambda: print), _n_(549295, "df1", lambda: df1))
_l_(549297)