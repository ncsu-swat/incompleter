# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/19339/transpose-unzip-function-inverse-of-zip
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unzip(zipped):
    _l_(1543183)

    """Inverse of built-in zip function.
    Args:
        zipped: a list of tuples

    Returns:
        a tuple of lists

    Example:
        a = [1, 2, 3]
        b = [4, 5, 6]
        zipped = list(zip(a, b))

        assert zipped == [(1, 4), (2, 5), (3, 6)]

        unzipped = unzip(zipped)

        assert unzipped == ([1, 2, 3], [4, 5, 6])

    """

    unzipped = ()
    _l_(1543161)
    if _c_(1543164, _n_(1543162, "len", lambda: len), _n_(1543163, "zipped", lambda: zipped)) == 0:
        _l_(1543167)

        aux = _n_(1543165, "unzipped", lambda: unzipped)
        _l_(1543166)
        return aux

    dim = _c_(1543170, _n_(1543168, "len", lambda: len), _n_(1543169, "zipped", lambda: zipped)[0])
    _l_(1543171)

    for i in _c_(1543174, _n_(1543172, "range", lambda: range), _n_(1543173, "dim", lambda: dim)):
        _l_(1543180)

        unzipped = _n_(1543175, "unzipped", lambda: unzipped) + ([_n_(1543176, "tup", lambda: tup)[_n_(1543177, "i", lambda: i)] for tup in _n_(1543178, "zipped", lambda: zipped)], )
        _l_(1543179)
    aux = _n_(1543181, "unzipped", lambda: unzipped)
    _l_(1543182)

    return aux

