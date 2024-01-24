# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51733268/returning-file-not-found-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def main():
    _l_(699315)

    _c_(699313, _n_(699312, "FileRead", lambda: FileRead))
    _l_(699314)

def ReadFile(filename):
    _l_(699333)

    files = _c_(699318, _n_(699316, "open", lambda: open), _n_(699317, "filename", lambda: filename))
    _l_(699319)
    lines = _c_(699322, _a_(699321, _n_(699320, "files", lambda: files), "readlines"))
    _l_(699323)

    for index, line in _c_(699326, _n_(699324, "enumerate", lambda: enumerate), _n_(699325, "lines", lambda: lines)):
        _l_(699332)

        _c_(699330, _n_(699327, "print", lambda: print), _n_(699328, "index", lambda: index), "=", _n_(699329, "line", lambda: line))
        _l_(699331)

def FileRead():
    _l_(699344)

    try:
        _l_(699343)

        _c_(699335, _n_(699334, "ReadFile", lambda: ReadFile), "files.txt")
        _l_(699336)

    except _n_(699337, "IOError", lambda: IOError) as e:
        _l_(699342)

        _c_(699340, _n_(699338, "print", lambda: print), "Could not open file:", _n_(699339, "e", lambda: e))
        _l_(699341)

if _n_(699345, "__name__", lambda: __name__) == "__main__":
    _l_(699349)

    _c_(699347, _n_(699346, "main", lambda: main))
    _l_(699348)