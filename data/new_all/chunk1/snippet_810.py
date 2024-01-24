# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62768022/typeerror-zip-argument-1-must-support-iteration-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df1=_c_(385408, _a_(385407, _n_(385406, "pd", lambda: pd), "DataFrame"), {'A':[1,3,4,7,8,11,1,15,20,15,16,87],
                 'B':[1,3,4,6,8,11,1,19,20,15,16,87],
                 'flag':[0,0,0,0,1,1,1,0,0,1,0,0]})
_l_(385409)
         
N = 2
_l_(385410)
s = [_n_(385411, "x", lambda: x) for s, e in _c_(385416, _n_(385412, "zip", lambda: zip), _n_(385413, "idx", lambda: idx)-_n_(385414, "N", lambda: N),_n_(385415, "idx", lambda: idx)) for x in _c_(385420, _n_(385417, "range", lambda: range), _n_(385418, "s", lambda: s), _n_(385419, "e", lambda: e)+1)]
_l_(385421)
df_before_2rows=_a_(385423, _n_(385422, "df1", lambda: df1), "loc")[_c_(385428, _a_(385426, _a_(385425, _n_(385424, "df1", lambda: df1), "index"), "intersection"), _n_(385427, "s", lambda: s))]
_l_(385429)