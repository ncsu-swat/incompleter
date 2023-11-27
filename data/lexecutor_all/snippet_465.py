# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-yield-from-syntax-in-python-3-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def flatten(sequence):
    _l_(1547392)

    """flatten a multi level list or something
    >>> list(flatten([1, [2], 3]))
    [1, 2, 3]
    >>> list(flatten([1, [2], [3, [4]]]))
    [1, 2, 3, 4]
    """
    for element in _n_(1547380, "sequence", lambda: sequence):
        _l_(1547391)

        if _c_(1547383, _n_(1547381, "hasattr", lambda: hasattr), _n_(1547382, "element", lambda: element), '__iter__'):
            _l_(1547390)

            yield from _c_(1547386, _n_(1547384, "flatten", lambda: flatten), _n_(1547385, "element", lambda: element))
            _l_(1547387)
        else:
            yield _n_(1547388, "element", lambda: element)
            _l_(1547389)

_c_(1547398, _n_(1547393, "print", lambda: print), _c_(1547397, _n_(1547394, "list", lambda: list), _c_(1547396, _n_(1547395, "flatten", lambda: flatten), [1, [2], [3, [4]]])))
_l_(1547399)

