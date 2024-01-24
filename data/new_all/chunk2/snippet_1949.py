# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74878704/getting-error-typeerror-must-be-str-not-dict-when-substituting-variable-into
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(437220)

except ImportError:
    pass
try:
    from jsonpath_ng.ext import parse
    _l_(437222)

except ImportError:
    pass

with _c_(437224, _n_(437223, "open", lambda: open), './movies.json') as movies_json:
    _l_(437230)

    movies = _c_(437228, _a_(437226, _n_(437225, "json", lambda: json), "load"), _n_(437227, "movies_json", lambda: movies_json))
    _l_(437229)

jsonpath_expression = _c_(437232, _n_(437231, "parse", lambda: parse), "$.movies[1]")
_l_(437233)
_c_(437238, _n_(437234, "print", lambda: print), 'jsonpath_expression type is', _c_(437237, _n_(437235, "type", lambda: type), _n_(437236, "jsonpath_expression", lambda: jsonpath_expression)))
_l_(437239)
for match in _c_(437243, _a_(437241, _n_(437240, "jsonpath_expression", lambda: jsonpath_expression), "find"), _n_(437242, "movies", lambda: movies)):
    _l_(437249)

    _c_(437247, _n_(437244, "print", lambda: print), _a_(437246, _n_(437245, "match", lambda: match), "value"))
    _l_(437248)