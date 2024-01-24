# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75006215/fix-the-error-typeerror-function-object-is-not-subscriptable-with-out-chan
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
empty_rlist = None
_l_(349931)


def make_rlist(first, rest):
    _l_(349945)

    """Make a recursive list from its first element and the rest."""
    def dispatch(message, value=None):
        _l_(349942)

        if _n_(349932, "message", lambda: message) == 'getitem':
            _l_(349941)

            if _n_(349933, "value", lambda: value) == 0:
                _l_(349936)

                aux = _n_(349934, "first", lambda: first)
                _l_(349935)
                return aux
            aux = _c_(349939, _n_(349937, "rest", lambda: rest), 'getitem', _n_(349938, "value", lambda: value) - 1)
            _l_(349940)
            return aux
    aux = _n_(349943, "dispatch", lambda: dispatch)
    _l_(349944)
    return aux


def make_mutable_rlist():
    _l_(349991)

    """Return a functional implementation of a mutable recursive list."""
    contents = _n_(349946, "empty_rlist", lambda: empty_rlist)
    _l_(349947)

    def dispatch(message, value=None):
        _l_(349987)

        nonlocal contents
        _l_(349948)
        if _n_(349949, "message", lambda: message) == 'len':
            _l_(349986)

            aux = _c_(349952, _n_(349950, "len_rlist", lambda: len_rlist), _n_(349951, "contents", lambda: contents))
            _l_(349953)
            return aux
        elif _n_(349954, "message", lambda: message) == 'getitem':
            _l_(349985)

            aux = _c_(349958, _n_(349955, "getitem_rlist", lambda: getitem_rlist), _n_(349956, "contents", lambda: contents), _n_(349957, "value", lambda: value))
            _l_(349959)
            return aux
        elif _n_(349960, "message", lambda: message) == 'push_first':
            _l_(349984)

            contents = _c_(349964, _n_(349961, "make_rlist", lambda: make_rlist), _n_(349962, "value", lambda: value), _n_(349963, "contents", lambda: contents))
            _l_(349965)
        elif _n_(349966, "message", lambda: message) == 'pop_first':
            _l_(349983)

            f = _c_(349969, _n_(349967, "first", lambda: first), _n_(349968, "contents", lambda: contents))
            _l_(349970)
            contents = _c_(349973, _n_(349971, "rest", lambda: rest), _n_(349972, "contents", lambda: contents))
            _l_(349974)
            aux = _n_(349975, "f", lambda: f)
            _l_(349976)
            return aux
        elif _n_(349977, "message", lambda: message) == 'str':
            _l_(349982)

            aux = _c_(349980, _n_(349978, "str", lambda: str), _n_(349979, "contents", lambda: contents))
            _l_(349981)
            return aux
    aux = _n_(349988, "dispatch", lambda: dispatch), _n_(349989, "contents", lambda: contents)
    _l_(349990)
    return aux


def len_rlist(s):
    _l_(350003)

    """Return the length of recursive list s."""
    length = 0
    _l_(349992)
    while _n_(349993, "s", lambda: s) != _n_(349994, "empty_rlist", lambda: empty_rlist):
        _l_(350000)

        s, length = _c_(349997, _n_(349995, "rest", lambda: rest), _n_(349996, "s", lambda: s)), _n_(349998, "length", lambda: length) + 1
        _l_(349999)
    aux = _n_(350001, "length", lambda: length)
    _l_(350002)
    return aux


def getitem_rlist(s, i):
    _l_(350015)

    """Return the element at index i of recursive list s."""
    while _n_(350004, "i", lambda: i) > 0:
        _l_(350010)

        s, i = _c_(350007, _n_(350005, "rest", lambda: rest), _n_(350006, "s", lambda: s)), _n_(350008, "i", lambda: i) - 1
        _l_(350009)
    aux = _c_(350013, _n_(350011, "first", lambda: first), _n_(350012, "s", lambda: s))
    _l_(350014)
    return aux


def first(s):
    _l_(350019)

    """Return the first element of a recursive list s."""
    aux = _c_(350017, _n_(350016, "s", lambda: s), 'getitem', 0)
    _l_(350018)
    return aux

def rest(s):
    _l_(350023)

    """Return the rest of the elements of a recursive list s."""
    aux = _c_(350021, _n_(350020, "s", lambda: s), 'getitem', 1)
    _l_(350022)
    return aux


my_list = _c_(350025, _n_(350024, "make_mutable_rlist", lambda: make_mutable_rlist))[0]
_l_(350026)
for x in _c_(350028, _n_(350027, "range", lambda: range), 4):
    _l_(350033)

    _c_(350031, _n_(350029, "my_list", lambda: my_list)['push_first'], _n_(350030, "x", lambda: x))
    _l_(350032)

_c_(350037, _n_(350034, "print", lambda: print), _c_(350036, _n_(350035, "my_list", lambda: my_list), "len"))
_l_(350038)