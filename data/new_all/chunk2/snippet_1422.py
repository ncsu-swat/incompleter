# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60716018/filenotfounderror-when-trying-to-rename-all-the-files-in-a-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(435812)

except ImportError:
    pass


def main():
    _l_(435829)

    x = 0
    _l_(435813)
    file_ext = ".jpg"
    _l_(435814)

    for filename in _c_(435817, _a_(435816, _n_(435815, "os", lambda: os), "listdir"), "images/jaguar"):
        _l_(435828)

        _c_(435825, _a_(435819, _n_(435818, "os", lambda: os), "rename"), _n_(435820, "filename", lambda: filename), "Jaguar_" + _c_(435823, _n_(435821, "str", lambda: str), _n_(435822, "x", lambda: x)) + _n_(435824, "file_ext", lambda: file_ext))
        _l_(435826)
        x += 1
        _l_(435827)


if _n_(435830, "__name__", lambda: __name__) == '__main__':
    _l_(435834)

    _c_(435832, _n_(435831, "main", lambda: main))
    _l_(435833)