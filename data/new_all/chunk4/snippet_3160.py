# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35820418/compound-function-typeerror-int-object-is-not-iterable
# Here is the market
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
_l_(607440)

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
_l_(607441)


def compute_total_value(food):
    _l_(607468)

    total = 0
    _l_(607442)
    for items in _n_(607443, "food", lambda: food):
        _l_(607465)

        while _c_(607447, _n_(607444, "sum", lambda: sum), _n_(607445, "stock", lambda: stock)[_n_(607446, "items", lambda: items)]) != 0:
            _l_(607458)

            if _n_(607448, "stock", lambda: stock)[_n_(607449, "items", lambda: items)] != 0:
                _l_(607457)

                total += _n_(607450, "prices", lambda: prices)[_n_(607451, "items", lambda: items)]
                _l_(607452)
                _n_(607453, "stock", lambda: stock)[_n_(607454, "items", lambda: items)] -= 1
                _l_(607455)
            else:
                continue
                _l_(607456)
        if _c_(607462, _n_(607459, "sum", lambda: sum), _n_(607460, "stock", lambda: stock)[_n_(607461, "items", lambda: items)]) == 0:
            _l_(607464)

            break
            _l_(607463)
    aux = _n_(607466, "total", lambda: total)
    _l_(607467)
    return aux

market_items = ["banana", "orange", "apple", "pear"]
_l_(607469)

total_market_value = _c_(607472, _n_(607470, "compute_total_value", lambda: compute_total_value), _n_(607471, "market_items", lambda: market_items))
_l_(607473)

_c_(607476, _n_(607474, "print", lambda: print), _n_(607475, "total_market_value", lambda: total_market_value))
_l_(607477)