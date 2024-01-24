# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59853281/attributeerror-set-object-has-no-attribute-timeout
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def main():
    _l_(524501)

    url = 'https://www.nur.kz/'
    _l_(524488)
    op = _c_(524491, _n_(524489, "get_html", lambda: get_html), _n_(524490, "url", lambda: url))
    _l_(524492)
    take_links = _c_(524495, _n_(524493, "get_links", lambda: get_links), _n_(524494, "op", lambda: op))
    _l_(524496)
    start_parse = _c_(524499, _n_(524497, "parse", lambda: parse), _n_(524498, "take_links", lambda: take_links))
    _l_(524500)


if _n_(524502, "__name__", lambda: __name__) == '__main__':
    _l_(524506)

    _c_(524504, _n_(524503, "main", lambda: main))
    _l_(524505)