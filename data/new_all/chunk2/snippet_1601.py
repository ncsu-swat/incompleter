# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61939039/typeerror-username-object-is-not-iterable-in-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(422854)

except ImportError:
    pass
try:
    import sys
    _l_(422856)

except ImportError:
    pass

class usernames(_n_(422857, "object", lambda: object)):
    _l_(422880)

    def __init__(self, filename: _n_(422858, "str", lambda: str)):
        _l_(422866)

        _n_(422859, "self", lambda: self).filename = _n_(422860, "filename", lambda: filename)
        _l_(422861)
        _n_(422862, "self", lambda: self).words = _a_(422864, _n_(422863, "self", lambda: self), "file_to_text")
        _l_(422865)

    def file_to_text(self):
        _l_(422879)

        with _c_(422870, _n_(422867, "open", lambda: open), _a_(422869, _n_(422868, "self", lambda: self), "filename"), "r") as f:
            _l_(422876)

            name_list = [_c_(422873, _a_(422872, _n_(422871, "line", lambda: line), "rstrip")) for line in _n_(422874, "f", lambda: f)]
            _l_(422875)
        aux = _n_(422877, "name_list", lambda: name_list)
        _l_(422878)

        return aux


def main():
    _l_(422924)

    user_files = []
    _l_(422881)

    if _c_(422887, _a_(422884, _a_(422883, _n_(422882, "os", lambda: os), "path"), "isfile"), _a_(422886, _n_(422885, "sys", lambda: sys), "argv")[1]):
        _l_(422907)

        filename = _c_(422895, _a_(422894, _c_(422893, _a_(422890, _a_(422889, _n_(422888, "os", lambda: os), "path"), "splitext"), _a_(422892, _n_(422891, "sys", lambda: sys), "argv")[1])[-1], "lower"))
        _l_(422896)
        if _c_(422899, _a_(422898, _n_(422897, "filename", lambda: filename), "endswith"), '.txt'):
            _l_(422906)

            _c_(422904, _a_(422901, _n_(422900, "user_files", lambda: user_files), "append"), _a_(422903, _n_(422902, "sys", lambda: sys), "argv")[1])
            _l_(422905)

    for files in _n_(422908, "user_files", lambda: user_files):
        _l_(422917)

        test_name = _c_(422911, _n_(422909, "usernames", lambda: usernames), _n_(422910, "files", lambda: files))
        _l_(422912)
        _c_(422915, _n_(422913, "print", lambda: print), _n_(422914, "test_name", lambda: test_name))
        _l_(422916)
    for test in _n_(422918, "test_name", lambda: test_name):
        _l_(422923)

        _c_(422921, _n_(422919, "print", lambda: print), _n_(422920, "test", lambda: test))
        _l_(422922)


if _n_(422925, "__name__", lambda: __name__) == '__main__':
    _l_(422929)

    _c_(422927, _n_(422926, "main", lambda: main))
    _l_(422928)