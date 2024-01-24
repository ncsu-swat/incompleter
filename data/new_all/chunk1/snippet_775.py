# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55895254/getting-filenotfounderror-when-trying-to-open-a-file-for-reading-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
working_dir = "data/"
_l_(402686)

for file in _c_(402690, _a_(402688, _n_(402687, "os", lambda: os), "listdir"), _n_(402689, "working_dir", lambda: working_dir)):
    _l_(402704)

    if (_c_(402693, _a_(402692, _n_(402691, "file", lambda: file), "find"), "mda") != -1):
        _l_(402703)

        SIC = _c_(402697, _a_(402695, _n_(402694, "re", lambda: re), "findall"), "__(\d+)", _n_(402696, "file", lambda: file))
        _l_(402698)
        f = _c_(402701, _n_(402699, "open", lambda: open), _n_(402700, "file", lambda: file), 'r')
        _l_(402702)