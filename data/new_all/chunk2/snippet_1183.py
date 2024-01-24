# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57761583/how-to-avoid-a-filenotfounderror-with-os-listdir
#loop
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for filename in _c_(447808, _a_(447806, _n_(447805, "os", lambda: os), "listdir"), _n_(447807, "root_dir", lambda: root_dir)):
    _l_(447818)

    if _c_(447811, _a_(447810, _n_(447809, "filename", lambda: filename), "endswith"), '.csv'):
        _l_(447817)


        # Pull in the file
        df = _c_(447815, _a_(447813, _n_(447812, "pd", lambda: pd), "read_csv"), _n_(447814, "filename", lambda: filename))
        _l_(447816)