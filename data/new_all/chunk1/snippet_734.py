# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67601549/trying-to-rename-files-with-os-rename-throws-a-filenotfounderror-errno-2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
        import sys
        _l_(404818)

except ImportError:
        pass
try:
        import os
        _l_(404820)

except ImportError:
        pass

path = _c_(404823, _a_(404822, _n_(404821, "os", lambda: os), "listdir"), "/home/user/Downloads/student-02-c3f0f7fe19ef/data/")
_l_(404824)
for i in _n_(404825, "path", lambda: path):
        _l_(404840)

        _c_(404828, _n_(404826, "print", lambda: print), _n_(404827, "i", lambda: i))
        _l_(404829)
        if "jane" in _n_(404830, "i", lambda: i):
                _l_(404839)

                _c_(404837, _a_(404832, _n_(404831, "os", lambda: os), "rename"), _n_(404833, "i", lambda: i), _c_(404836, _a_(404835, _n_(404834, "i", lambda: i), "replace"), "jane", "jdoe"))
                _l_(404838)