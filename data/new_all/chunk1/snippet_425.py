# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46823004/sympy-typeerror-cannot-determine-truth-value-of-relational-when-using-sympy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = _c_(390964, _n_(390963, "symbols", lambda: symbols), 'x',real=True)
_l_(390965)
h = _c_(390967, _n_(390966, "symbols", lambda: symbols), 'h',real=True)
_l_(390968)
f = _c_(390971, _n_(390969, "symbols", lambda: symbols), 'f',cls=_n_(390970, "Function", lambda: Function))    
_l_(390972)    
sym_dexpr = _c_(390984, _a_(390983, _c_(390982, _a_(390974, _n_(390973, "f_diff", lambda: f_diff), "subs"), _c_(390977, _n_(390975, "f", lambda: f), _n_(390976, "x", lambda: x)), _n_(390978, "x", lambda: x)*_c_(390981, _n_(390979, "exp", lambda: exp), -_n_(390980, "x", lambda: x)**2)), "doit"))
_l_(390985)
f_diff = _c_(390991, _a_(390989, _c_(390988, _n_(390986, "f", lambda: f), _n_(390987, "x", lambda: x)), "diff"), _n_(390990, "x", lambda: x),1)
_l_(390992)
expr_diff = _c_(391002, _n_(390993, "as_finite_diff", lambda: as_finite_diff), _n_(390994, "f_diff", lambda: f_diff), [_n_(390995, "x", lambda: x), _n_(390996, "x", lambda: x)-_n_(390997, "h", lambda: h),_n_(390998, "x", lambda: x)-2*_n_(390999, "h", lambda: h),_n_(391000, "x", lambda: x)-3*_n_(391001, "h", lambda: h)])
_l_(391003)
w=_c_(391005, _n_(391004, "Wild", lambda: Wild), 'w')
_l_(391006)
c=_c_(391008, _n_(391007, "Wild", lambda: Wild), 'c')
_l_(391009)
patterns = [_c_(391016, _a_(391011, _n_(391010, "arg", lambda: arg), "match"), _n_(391012, "c", lambda: c)*_c_(391015, _n_(391013, "f", lambda: f), _n_(391014, "w", lambda: w))) for arg in _a_(391018, _n_(391017, "expr_diff", lambda: expr_diff), "args")]
_l_(391019)
coefficients = [_n_(391020, "t", lambda: t)[_n_(391021, "c", lambda: c)] for t in _c_(391026, _n_(391022, "sorted", lambda: sorted), _n_(391023, "patterns", lambda: patterns), key=lambda t:_n_(391024, "t", lambda: t)[_n_(391025, "w", lambda: w)])]
_l_(391027)
_c_(391030, _n_(391028, "print", lambda: print), _n_(391029, "coefficients", lambda: coefficients))
_l_(391031)