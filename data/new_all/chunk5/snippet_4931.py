# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39884564/when-using-flask-with-python-3-and-simpleitk-0-10-0-together-i-am-getting-attri
from __future__ import print_function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(684623)
try:
    import SimpleITK
    _l_(684625)

except ImportError:
    pass
try:
    from flask import Flask
    _l_(684627)

except ImportError:
    pass
try:
    import time
    _l_(684629)

except ImportError:
    pass

app = _c_(684632, _n_(684630, "Flask", lambda: Flask), _n_(684631, "__name__", lambda: __name__))
_l_(684633)


@_c_(684636, _a_(684635, _n_(684634, "app", lambda: app), "route"), '/fuse')
def fuse():
    _l_(684690)

    image = _c_(684639, _a_(684638, _n_(684637, "SimpleITK", lambda: SimpleITK), "ReadImage"), "CT/IMG-0002-000001.dcm")
    _l_(684640)

    mean_image = _c_(684644, _a_(684642, _n_(684641, "SimpleITK", lambda: SimpleITK), "BoxMean"), _n_(684643, "image", lambda: image), [3,3,1])
    _l_(684645)

    all_keys = _c_(684648, _a_(684647, _n_(684646, "image", lambda: image), "GetMetaDataKeys"))
    _l_(684649)
    for key in _n_(684650, "all_keys", lambda: all_keys):
        _l_(684660)

        _c_(684658, _a_(684652, _n_(684651, "mean_image", lambda: mean_image), "SetMetaData"), _n_(684653, "key", lambda: key), _c_(684657, _a_(684655, _n_(684654, "image", lambda: image), "GetMetaData"), _n_(684656, "key", lambda: key)))
        _l_(684659)
    _c_(684663, _a_(684662, _n_(684661, "mean_image", lambda: mean_image), "SetMetaData"), "0008|0008", "DERIVED\SECONDARY")
    _l_(684664)
    modification_time = _c_(684667, _a_(684666, _n_(684665, "time", lambda: time), "strftime"), "%H%M%S")
    _l_(684668)
    modification_date = _c_(684671, _a_(684670, _n_(684669, "time", lambda: time), "strftime"), "%Y%m%d")
    _l_(684672)
    _c_(684676, _a_(684674, _n_(684673, "mean_image", lambda: mean_image), "SetMetaData"), "0008|0031", _n_(684675, "modification_time", lambda: modification_time))
    _l_(684677)
    _c_(684681, _a_(684679, _n_(684678, "mean_image", lambda: mean_image), "SetMetaData"), "0008|0021", _n_(684680, "modification_date", lambda: modification_date))
    _l_(684682)

    _c_(684687, _n_(684683, "print", lambda: print), _c_(684686, _a_(684685, _n_(684684, "mean_image", lambda: mean_image), "GetMetaData"), "0008|0031"))
    _l_(684688)
    aux = "finish"
    _l_(684689)
    return aux