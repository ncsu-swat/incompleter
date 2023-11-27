# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/256222/which-exception-should-i-raise-on-bad-illegal-argument-combinations-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def import_to_orm(name, save=False, recurse=False):
    _l_(1538640)

    if _n_(1538634, "recurse", lambda: recurse) and not _n_(1538635, "save", lambda: save):
        _l_(1538639)

        raise _c_(1538637, _n_(1538636, "ValueError", lambda: ValueError), "save must be True if recurse is True")
        _l_(1538638)

