# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62768022/typeerror-zip-argument-1-must-support-iteration-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df1=_c_(394487, _a_(394486, _n_(394485, "pd", lambda: pd), "DataFrame"), {'A':[1,3,4,7,8,11,1,15,20,15,16,87],
                     'B':[1,3,4,6,8,11,1,19,20,15,16,87],
                     'flag':[0,0,0,0,1,1,1,0,0,1,0,0]})
_l_(394488)

for item in _n_(394489, "idx", lambda: idx):
    _l_(394510)

    N = 2
    _l_(394490)
    s = [_n_(394491, "x", lambda: x) for s, e in _c_(394496, _n_(394492, "zip", lambda: zip), _n_(394493, "item", lambda: item)-_n_(394494, "N", lambda: N),_n_(394495, "item", lambda: item)) for x in _c_(394500, _n_(394497, "range", lambda: range), _n_(394498, "s", lambda: s), _n_(394499, "e", lambda: e)+1)]
    _l_(394501)
    df_before_2rows=_a_(394503, _n_(394502, "df1", lambda: df1), "loc")[_c_(394508, _a_(394506, _a_(394505, _n_(394504, "df1", lambda: df1), "index"), "intersection"), _n_(394507, "s", lambda: s))]
    _l_(394509)