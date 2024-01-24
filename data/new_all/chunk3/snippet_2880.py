# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60068543/python-script-problems-with-type-error-type-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from scraper.config import Config
    _l_(543614)

except ImportError:
    pass
try:
    from scraper.scraper import Scraper
    _l_(543616)

except ImportError:
    pass
try:
    from scraper.spokeo import Spokeo
    _l_(543618)

except ImportError:
    pass


class EmailChecker:
    _l_(543691)

    def __init__(self):
        _l_(543626)

        config = _c_(543620, _n_(543619, "Config", lambda: Config))
        _l_(543621)

        # Open instance to chromedriver
        _n_(543622, "self", lambda: self).__scraper = _c_(543624, _n_(543623, "Scraper", lambda: Scraper))
        _l_(543625)

    def check_email(self, email):
        _l_(543690)

        config = _c_(543628, _n_(543627, "Config", lambda: Config))
        _l_(543629)
        results = {}
        _l_(543630)

        # for _ in (GooglePlus, Spokeo):
        for _ in _n_(543631, "Spokeo", lambda: (Spokeo)):
            _l_(543667)

            site = _c_(543635, _n_(543632, "_", lambda: _), _a_(543634, _n_(543633, "self", lambda: self), "__scraper"))
            _l_(543636)

            try:
                _l_(543649)

                result = _c_(543640, _a_(543638, _n_(543637, "site", lambda: site), "search_for_email"), _n_(543639, "email", lambda: email))
                _l_(543641)
            except _n_(543642, "Exception", lambda: Exception):
                _l_(543648)

                if _a_(543644, _n_(543643, "config", lambda: config), "debug"):
                    _l_(543646)

                    raise
                    _l_(543645)
                result = None
                _l_(543647)

            try:
                _l_(543661)

                _c_(543652, _a_(543651, _n_(543650, "site", lambda: site), "logout"))
                _l_(543653)
            except _n_(543654, "Exception", lambda: Exception):
                _l_(543660)

                if _a_(543656, _n_(543655, "config", lambda: config), "debug"):
                    _l_(543658)

                    raise
                    _l_(543657)
                pass
                _l_(543659)

            _n_(543662, "results", lambda: results)[_a_(543664, _n_(543663, "_", lambda: _), "__name__")] = _n_(543665, "result", lambda: result)
            _l_(543666)

        try:
            _l_(543677)

            _c_(543672, _a_(543671, _a_(543670, _a_(543669, _n_(543668, "self", lambda: self), "__scraper"), "driver"), "close"))
            _l_(543673)
        except _n_(543674, "Exception", lambda: Exception):
            _l_(543676)

            pass
            _l_(543675)

        try:
            _l_(543687)

            _c_(543682, _a_(543681, _a_(543680, _a_(543679, _n_(543678, "self", lambda: self), "__scraper"), "driver"), "quit"))
            _l_(543683)
        except _n_(543684, "Exception", lambda: Exception):
            _l_(543686)

            pass
            _l_(543685)
        aux = _n_(543688, "results", lambda: results)
        _l_(543689)

        return aux