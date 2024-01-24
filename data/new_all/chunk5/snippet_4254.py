# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60774729/im-getting-a-ufunctypeerror-when-doing-a-linear-regression-with-sklearn
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(703368, _n_(703365, "print", lambda: print), _a_(703367, _n_(703366, "X", lambda: X), "dtype"))
_l_(703369)
_c_(703373, _n_(703370, "print", lambda: print), _a_(703372, _n_(703371, "y", lambda: y), "dtype"))
_l_(703374)

lin_reg = _c_(703376, _n_(703375, "LinearRegression", lambda: LinearRegression))
_l_(703377)
_c_(703382, _a_(703379, _n_(703378, "lin_reg", lambda: lin_reg), "fit"), _n_(703380, "X", lambda: X), _n_(703381, "y", lambda: y))
_l_(703383)
_c_(703392, _n_(703384, "print", lambda: print), "Score: " + _c_(703391, _n_(703385, "str", lambda: str), _c_(703390, _a_(703387, _n_(703386, "lin_reg", lambda: lin_reg), "score"), _n_(703388, "X", lambda: X),_n_(703389, "y", lambda: y))))
_l_(703393)
_c_(703399, _n_(703394, "print", lambda: print), "Coefs: " + _c_(703398, _n_(703395, "str", lambda: str), _a_(703397, _n_(703396, "lin_reg", lambda: lin_reg), "coef_")))
_l_(703400)
_c_(703406, _n_(703401, "print", lambda: print), "Intercept: " + _c_(703405, _n_(703402, "str", lambda: str), _a_(703404, _n_(703403, "lin_reg", lambda: lin_reg), "intercept_")))
_l_(703407)