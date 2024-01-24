# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52103088/python-error-attributeerror-io-textiowrapper-object-has-no-attribute-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(670946, _n_(670945, "open", lambda: open), 'C:\\temp\\XXX\\names.csv','r') as rf:
    _l_(670966)

    with _c_(670948, _n_(670947, "open", lambda: open), 'C:\\temp\\XXX\\Testcopyx.csv','w') as wf:
        _l_(670965)

        for line in _n_(670949, "rf", lambda: rf):
            _l_(670964)

            _c_(670953, _a_(670951, _n_(670950, "wf", lambda: wf), "write"), _n_(670952, "line", lambda: line))                
            _l_(670954)                
            _c_(670962, _a_(670956, _n_(670955, "wf", lambda: wf), "insert"), 0, 'New_ID', _c_(670961, _n_(670957, "range", lambda: range), 0, 0 + _c_(670960, _n_(670958, "len", lambda: len), _n_(670959, "wf", lambda: wf))))
            _l_(670963)
_a_(670968, _n_(670967, "wf", lambda: wf), "close")
_l_(670969)