# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58754833/im-getting-name-error-when-running-this-code
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(701671)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup as bs
    _l_(701673)

except ImportError:
    pass

session = _c_(701676, _a_(701675, _n_(701674, "request", lambda: request), "session"))
_l_(701677)

def get_sizes_in_stock():
    _l_(701714)

    global session
    _l_(701678)
    endpoint = "https://www.off---white.com/en/SE/men/products/omia065r208000010100#"
    _l_(701679)
    response = _c_(701683, _a_(701681, _n_(701680, "session", lambda: session), "get"), _n_(701682, "endpoint", lambda: endpoint))
    _l_(701684)

    soup = _c_(701688, _n_(701685, "bs", lambda: bs), _a_(701687, _n_(701686, "response", lambda: response), "text"),"html.parser")
    _l_(701689)

    ul = _c_(701692, _a_(701691, _n_(701690, "soup", lambda: soup), "find"), "ul",{"class":"styled-radio"})
    _l_(701693)
    all_sizes = _c_(701696, _a_(701695, _n_(701694, "ul", lambda: ul), "find_all"), "li")
    _l_(701697)

    sizes_in_stock = []
    _l_(701698)
    for size in _n_(701699, "all_sizes", lambda: all_sizes):
        _l_(701711)

        if "availability not_on_sale" not in _n_(701700, "size", lambda: size)["class"]:
            _l_(701710)

            size_id = _n_(701701, "size", lambda: size)["id"]
            _l_(701702)
            _c_(701708, _a_(701704, _n_(701703, "sizes_in_stock", lambda: sizes_in_stock), "append"), _c_(701707, _a_(701706, _n_(701705, "size_id", lambda: size_id), "split"), "_")[1])
            _l_(701709)
    aux = _n_(701712, "sizes_in_stock", lambda: sizes_in_stock)
    _l_(701713)

    return aux

_c_(701718, _n_(701715, "print", lambda: print), _c_(701717, _n_(701716, "get_sizes_in_stock", lambda: get_sizes_in_stock)))
_l_(701719)