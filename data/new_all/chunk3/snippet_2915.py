# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58443969/getting-typeerror-fit-missing-1-required-positional-argument-self
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
lm = _n_(568139, "LinearRegression", lambda: LinearRegression)
_l_(568140)

x = _n_(568141, "df", lambda: df)[['battery_power']]
_l_(568142)

y = _n_(568143, "df", lambda: df)['price']
_l_(568144)

_c_(568149, _a_(568146, _n_(568145, "lm", lambda: lm), "fit"), X=_n_(568147, "x", lambda: x), y=_n_(568148, "y", lambda: y))
_l_(568150)