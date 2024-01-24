# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75011399/typeerror-string-indices-must-be-integers-in-the-chess-com-api
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from chessdotcom import get_leaderboards
    _l_(465586)

except ImportError:
    pass
try:
    import pprint
    _l_(465588)

except ImportError:
    pass

printer = _c_(465591, _a_(465590, _n_(465589, "pprint", lambda: pprint), "PrettyPrinter"))
_l_(465592)


def print_leaderboards():
    _l_(465618)

    data = _a_(465595, _c_(465594, _n_(465593, "get_leaderboards", lambda: get_leaderboards)), "json")
    _l_(465596)
    categories = _c_(465599, _a_(465598, _n_(465597, "data", lambda: data), "keys"))
    _l_(465600)

    for category in _n_(465601, "categories", lambda: categories):
        _l_(465617)

        _c_(465604, _n_(465602, "print", lambda: print), 'Category:', _n_(465603, "category", lambda: category))
        _l_(465605)
        # idx = index
        for idx, entry in _c_(465609, _n_(465606, "enumerate", lambda: enumerate), _n_(465607, "data", lambda: data)[_n_(465608, "category", lambda: category)]):
            _l_(465616)

            _c_(465614, _n_(465610, "print", lambda: print), f'Rank: {_n_(465611, "idx", lambda: idx) + 1} | Username: {_n_(465612, "entry", lambda: entry)["username"]} | Rating: {_n_(465613, "entry", lambda: entry)["score"]}')
            _l_(465615)


_c_(465620, _n_(465619, 'print_leaderboards', lambda: print_leaderboards))
_l_(465621)