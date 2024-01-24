# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66470880/file-not-found-error-while-downloading-image-files
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(639959)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(639961)

except ImportError:
    pass
try:
    import requests
    _l_(639963)

except ImportError:
    pass

Final1 = _c_(639966, _a_(639965, _n_(639964, "pd", lambda: pd), "read_excel"), "Sneakers.xlsx")
_l_(639967)
_n_(639968, "Final1", lambda: Final1).index+=1
_l_(639969)

a = _c_(639973, _a_(639972, _a_(639971, _n_(639970, "Final1", lambda: Final1), "index"), "tolist"))
_l_(639974)
Images = _c_(639977, _a_(639976, _n_(639975, "Final1", lambda: Final1)["Images"], "tolist"))
_l_(639978)
Name = _c_(639984, _a_(639983, _c_(639982, _a_(639981, _a_(639980, _n_(639979, "Final1", lambda: Final1)["Name"], "str"), "lower")), "tolist"))
_l_(639985)
Brand = _c_(639991, _a_(639990, _c_(639989, _a_(639988, _a_(639987, _n_(639986, "Final1", lambda: Final1)["Brand"], "str"), "lower")), "tolist"))
_l_(639992)

s = _c_(639995, _a_(639994, _n_(639993, "requests", lambda: requests), "Session"))
_l_(639996)

for i,n,b,l in _c_(640002, _n_(639997, "zip", lambda: zip), _n_(639998, "a", lambda: a),_n_(639999, "Name", lambda: Name),_n_(640000, "Brand", lambda: Brand),_n_(640001, "Images", lambda: Images)):
    _l_(640020)

    r = _a_(640007, _c_(640006, _a_(640004, _n_(640003, "s", lambda: s), "get"), _n_(640005, "l", lambda: l)), "content")
    _l_(640008)
    with _c_(640013, _n_(640009, "open", lambda: open), "Images//" + f"{_n_(640010, 'i', lambda: i)}-{_n_(640011, 'n', lambda: n)}-{_n_(640012, 'b', lambda: b)}.jpg","wb") as f:
        _l_(640019)

        _c_(640017, _a_(640015, _n_(640014, "f", lambda: f), "write"), _n_(640016, "r", lambda: r))
        _l_(640018)