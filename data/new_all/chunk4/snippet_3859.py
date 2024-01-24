# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66470880/file-not-found-error-while-downloading-image-files
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(608132)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(608134)

except ImportError:
    pass
try:
    import requests
    _l_(608136)

except ImportError:
    pass

Final1 = _c_(608139, _a_(608138, _n_(608137, "pd", lambda: pd), "read_excel"), "Sneakers.xlsx")
_l_(608140)
_n_(608141, "Final1", lambda: Final1).index+=1
_l_(608142)

a = _c_(608146, _a_(608145, _a_(608144, _n_(608143, "Final1", lambda: Final1), "index"), "tolist"))
_l_(608147)
Images = _c_(608150, _a_(608149, _n_(608148, "Final1", lambda: Final1)["Images"], "tolist"))
_l_(608151)
Name = _c_(608157, _a_(608156, _c_(608155, _a_(608154, _a_(608153, _n_(608152, "Final1", lambda: Final1)["Name"], "str"), "lower")), "tolist"))
_l_(608158)
Brand = _c_(608164, _a_(608163, _c_(608162, _a_(608161, _a_(608160, _n_(608159, "Final1", lambda: Final1)["Brand"], "str"), "lower")), "tolist"))
_l_(608165)

s = _c_(608168, _a_(608167, _n_(608166, "requests", lambda: requests), "Session"))
_l_(608169)

for i,n,b,l in _c_(608175, _n_(608170, "zip", lambda: zip), _n_(608171, "a", lambda: a),_n_(608172, "Name", lambda: Name),_n_(608173, "Brand", lambda: Brand),_n_(608174, "Images", lambda: Images)):
    _l_(608193)

    r = _a_(608180, _c_(608179, _a_(608177, _n_(608176, "s", lambda: s), "get"), _n_(608178, "l", lambda: l)), "content")
    _l_(608181)
    with _c_(608186, _n_(608182, "open", lambda: open), "Images//" + f"{_n_(608183, 'i', lambda: i)}-{_n_(608184, 'n', lambda: n)}-{_n_(608185, 'b', lambda: b)}.jpg","wb") as f:
        _l_(608192)

        _c_(608190, _a_(608188, _n_(608187, "f", lambda: f), "write"), _n_(608189, "r", lambda: r))
        _l_(608191)