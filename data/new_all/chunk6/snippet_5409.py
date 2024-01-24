# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55257479/attributeerror-list-object-has-no-attribute-get-in-nested-dictionary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(353362)

except ImportError:
    pass

with _c_(353364, _n_(353363, "open", lambda: open), 'console_data.json', 'r') as console_data:
    _l_(353374)

    parsed_data = _c_(353367, _a_(353366, _n_(353365, "console_data", lambda: console_data), "read"))
    _l_(353368)
    nodes = _c_(353372, _a_(353370, _n_(353369, "json", lambda: json), "loads"), _n_(353371, "parsed_data", lambda: parsed_data))
    _l_(353373)

last_node = _n_(353375, "nodes", lambda: nodes)[-1]                   # extract last dictionary
_l_(353376)                   # extract last dictionary

_c_(353378, _n_(353377, "print", lambda: print), "\n\n\n")
_l_(353379)
for item in _n_(353380, "last_node", lambda: last_node):
    _l_(353394)

    tags = _c_(353384, _a_(353383, _n_(353381, "last_node", lambda: last_node)[_n_(353382, "item", lambda: item)], "get"), "Tags", {})
    _l_(353385)
    try:
        _l_(353393)

        _c_(353388, _n_(353386, "print", lambda: print), _n_(353387, "tags", lambda: tags))
        _l_(353389)
    except _n_(353390, "AttributeError", lambda: AttributeError):
        _l_(353392)

        pass
        _l_(353391)