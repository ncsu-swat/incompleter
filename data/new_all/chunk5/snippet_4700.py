# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52103088/python-error-attributeerror-io-textiowrapper-object-has-no-attribute-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(671333, _n_(671332, "open", lambda: open), 'C:\\temp\\XXX\\names.csv','r') as rf:
    _l_(671353)

    with _c_(671335, _n_(671334, "open", lambda: open), 'C:\\temp\\XXX\\Testcopyx.csv','w') as wf:
        _l_(671352)

        for line in _n_(671336, "rf", lambda: rf):
            _l_(671351)

            _c_(671340, _a_(671338, _n_(671337, "wf", lambda: wf), "write"), _n_(671339, "line", lambda: line))                
            _l_(671341)                
            _c_(671349, _a_(671343, _n_(671342, "wf", lambda: wf), "insert"), 0, 'New_ID', _c_(671348, _n_(671344, "range", lambda: range), 0, 0 + _c_(671347, _n_(671345, "len", lambda: len), _n_(671346, "wf", lambda: wf))))
            _l_(671350)
_a_(671355, _n_(671354, "wf", lambda: wf), "close")
_l_(671356)