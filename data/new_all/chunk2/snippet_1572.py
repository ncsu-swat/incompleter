# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76359431/typeerror-in-django-float-argument-must-be-a-string-or-a-number-not-tuple
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ticker = _c_(434257, _a_(434254, _n_(434253, "yf", lambda: yf), "Ticker"), _n_(434255, "symbols", lambda: symbols)[_n_(434256, "pk", lambda: pk)])
_l_(434258)
price_arr = _c_(434261, _a_(434260, _n_(434259, "ticker", lambda: ticker), "history"), period='1d')['Close']
_l_(434262)
price = _c_(434266, _a_(434264, _n_(434263, "np", lambda: np), "array"), _n_(434265, "price_arr", lambda: price_arr))[0]
_l_(434267)