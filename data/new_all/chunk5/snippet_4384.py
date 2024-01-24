# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58706487/attributeerror-numpy-ndarray-object-has-no-attribute-sqrt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df=_c_(654259, _a_(654258, _n_(654257, "pd", lambda: pd), "DataFrame"), {'Value':[-0.016,-0.006,0.003,-0.011,-0.036,-0.031,-0.014,-0.006,-0.01 ,-0.009,0.004,0.001,-0.012,-0.021,-0.008,0.001,-0.011,-0.01,-0.006,0.002,0.004],'Nmae':[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]})
_l_(654260)

x=_c_(654278, _a_(654262, _n_(654261, "pd", lambda: pd), "DataFrame"), [_c_(654270, _a_(654265, _a_(654264, _n_(654263, "x", lambda: x), "values"), "sqrt"), _c_(654269, _a_(654267, _n_(654266, "np", lambda: np), "mean"), _n_(654268, "df2", lambda: df2)['Value']**2)) for x in _c_(654277, _a_(654272, _n_(654271, "np", lambda: np), "array_split"), _n_(654273, "df2", lambda: df2), (_c_(654276, _n_(654274, "len", lambda: len), _n_(654275, "df2", lambda: df2))/10))])
_l_(654279)