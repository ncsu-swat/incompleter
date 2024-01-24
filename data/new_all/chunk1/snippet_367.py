# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56307152/python-3-typeerror-cannot-astype-a-datetimelike-from-datetime64ns-to-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
buy_per_min = _c_(415149, _a_(415148, _c_(415147, _a_(415142, _c_(415141, _a_(415140, _c_(415139, _a_(415136, _c_(415135, _a_(415134, _c_(415133, _a_(415132, _c_(415131, _a_(415128, _c_(415127, _a_(415126, _a_(415125, _c_(415124, _a_(415120, _n_(415119, "buy", lambda: buy), "groupby"), [_c_(415123, _a_(415122, _n_(415121, "pd", lambda: pd), "Grouper"), key='timestamp', freq='Min'), 'price']), "shares"), "sum")), "apply"), _a_(415130, _n_(415129, "np", lambda: np), "log")), "to_frame"), 'shares'), "reset_index"), 'price'), "between_time"), _n_(415137, "market_open", lambda: market_open), _n_(415138, "market_close", lambda: market_close)), "groupby"), level='timestamp', as_index=False, group_keys=False), "apply"), lambda x: _c_(415146, _a_(415144, _n_(415143, "x", lambda: x), "nlargest"), columns='price', n=_n_(415145, "depth", lambda: depth))), "reset_index"))
_l_(415150)
_n_(415151, "buy_per_min", lambda: buy_per_min).timestamp = _c_(415159, _a_(415157, _c_(415156, _a_(415154, _a_(415153, _n_(415152, "buy_per_min", lambda: buy_per_min), "timestamp"), "add"), _n_(415155, "utc_offset", lambda: utc_offset)), "astype"), _n_(415158, "int", lambda: int))
_l_(415160)
_c_(415163, _a_(415162, _n_(415161, "buy_per_min", lambda: buy_per_min), "info"))
_l_(415164)