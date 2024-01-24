# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31909929/webscraping-with-python3-ignoring-duplicate-attribute-errors
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(404667)

except ImportError:
    pass
try:
    from xml.dom.minidom import parse, parseString
    _l_(404669)

except ImportError:
    pass


class Scraper:
    _l_(404687)


    def __init__( self ):
        _l_(404671)


        pass
        _l_(404670)

    def list(self,pages=1):
        _l_(404686)


        response = _c_(404674, _a_(404673, _n_(404672, "requests", lambda: requests), "get"), 'http://example.com')
        _l_(404675)

        dom = _c_(404679, _n_(404676, "parseString", lambda: parseString), _a_(404678, _n_(404677, "response", lambda: response), "text"))
        _l_(404680)

        _c_(404684, _n_(404681, "print", lambda: print), _a_(404683, _n_(404682, "dom", lambda: dom), "toxml"))
        _l_(404685)


if _n_(404688, "__name__", lambda: __name__) == "__main__":
    _l_(404696)


    scraper = _c_(404690, _n_(404689, "Scraper", lambda: Scraper))
    _l_(404691)

    _c_(404694, _a_(404693, _n_(404692, "scraper", lambda: scraper), "list"))
    _l_(404695)