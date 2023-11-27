# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def myfunc(outfile=None):
    _l_(1539422)

    if _n_(1539400, "outfile", lambda: outfile) is None:
        _l_(1539408)

        out = _a_(1539402, _n_(1539401, "sys", lambda: sys), "stdout")
        _l_(1539403)
    else:
        out = _c_(1539406, _n_(1539404, "open", lambda: open), _n_(1539405, "outfile", lambda: outfile), 'w')
        _l_(1539407)
    try:
        _l_(1539421)

        # do some stuff
        _c_(1539412, _a_(1539410, _n_(1539409, "out", lambda: out), "write"), _n_(1539411, "mytext", lambda: mytext) + '\n')
        _l_(1539413)
    finally:
        _l_(1539420)

        if _n_(1539414, "outfile", lambda: outfile) is not None:
            _l_(1539419)

            _c_(1539417, _a_(1539416, _n_(1539415, "out", lambda: out), "close"))
            _l_(1539418)

