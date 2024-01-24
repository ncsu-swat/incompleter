# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57560922/typeerror-function-object-is-not-iterable-when-i-am-not-calling-any-functions
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(437719)

except ImportError:
    pass
try:
    from datetime import datetime, timedelta
    _l_(437721)

except ImportError:
    pass

data = ['2019-01-01']
_l_(437722)
only_onboarding = _c_(437726, _a_(437724, _n_(437723, "pd", lambda: pd), "DataFrame"), _n_(437725, "data", lambda: data), columns = ['ClosedDate'])
_l_(437727)

cycle_times = _a_(437729, _n_(437728, "pd", lambda: pd), "DataFrame");
_l_(437730)
today = _c_(437733, _a_(437732, _n_(437731, "datetime", lambda: datetime), "today"));
_l_(437734)
for i in _c_(437738, _n_(437735, "range", lambda: range), _a_(437737, _n_(437736, "today", lambda: today), "month") - 1):
    _l_(437758)

    regx = "";
    _l_(437739)

    if (_n_(437740, "i", lambda: i) + 1 < 10):
        _l_(437757)

        regx = _c_(437744, _n_(437741, "str", lambda: str), _a_(437743, _n_(437742, "today", lambda: today), "year")) + '-0' + _c_(437747, _n_(437745, "str", lambda: str), _n_(437746, "i", lambda: i) + 1) + '-\d\d$';
        _l_(437748)
    else:
        regx = _c_(437752, _n_(437749, "str", lambda: str), _a_(437751, _n_(437750, "today", lambda: today), "year")) + '-' + _c_(437755, _n_(437753, "str", lambda: str), _n_(437754, "i", lambda: i) + 1) + '-\d\d$';
        _l_(437756)

of_month = _c_(437766, _a_(437760, _n_(437759, "only_onboarding", lambda: only_onboarding)['ClosedDate'], "filter"), lambda x: _c_(437765, _a_(437762, _n_(437761, "re", lambda: re), "match"), _n_(437763, "regx", lambda: regx), _n_(437764, "x", lambda: x)));
_l_(437767)