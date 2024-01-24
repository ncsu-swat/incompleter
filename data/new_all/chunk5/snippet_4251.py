# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60774729/im-getting-a-ufunctypeerror-when-doing-a-linear-regression-with-sklearn
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(698810, _n_(698807, "print", lambda: print), _a_(698809, _n_(698808, "X", lambda: X), "dtype"))
_l_(698811)
_c_(698815, _n_(698812, "print", lambda: print), _a_(698814, _n_(698813, "y", lambda: y), "dtype"))
_l_(698816)

lin_reg = _c_(698818, _n_(698817, "LinearRegression", lambda: LinearRegression))
_l_(698819)
_c_(698824, _a_(698821, _n_(698820, "lin_reg", lambda: lin_reg), "fit"), _n_(698822, "X", lambda: X), _n_(698823, "y", lambda: y))
_l_(698825)
_c_(698834, _n_(698826, "print", lambda: print), "Score: " + _c_(698833, _n_(698827, "str", lambda: str), _c_(698832, _a_(698829, _n_(698828, "lin_reg", lambda: lin_reg), "score"), _n_(698830, "X", lambda: X),_n_(698831, "y", lambda: y))))
_l_(698835)
_c_(698841, _n_(698836, "print", lambda: print), "Coefs: " + _c_(698840, _n_(698837, "str", lambda: str), _a_(698839, _n_(698838, "lin_reg", lambda: lin_reg), "coef_")))
_l_(698842)
_c_(698848, _n_(698843, "print", lambda: print), "Intercept: " + _c_(698847, _n_(698844, "str", lambda: str), _a_(698846, _n_(698845, "lin_reg", lambda: lin_reg), "intercept_")))
_l_(698849)