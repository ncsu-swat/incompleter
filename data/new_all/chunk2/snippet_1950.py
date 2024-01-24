# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74878704/getting-error-typeerror-must-be-str-not-dict-when-substituting-variable-into
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(470915)

except ImportError:
    pass
try:
    from jsonpath_ng.ext import parse
    _l_(470917)

except ImportError:
    pass

with _c_(470919, _n_(470918, "open", lambda: open), './movies.json') as movies_json:
    _l_(470925)

    movies = _c_(470923, _a_(470921, _n_(470920, "json", lambda: json), "load"), _n_(470922, "movies_json", lambda: movies_json))
    _l_(470924)

recno = _c_(470927, _n_(470926, "str", lambda: str), 1)
_l_(470928)
query_main = f'parse("$.movies[{_n_(470929, "recno", lambda: recno)}]")'
_l_(470930)
jsonpath_expression = _n_(470931, 'query_main', lambda: query_main)
_l_(470932)
_c_(470935, _n_(470933, 'print', lambda: print), 'query main output is', _n_(470934, 'query_main', lambda: (query_main)))
_l_(470936)
_c_(470941, _n_(470937, 'print', lambda: print), 'query main type is', _c_(470940, _n_(470938, 'type', lambda: type), _n_(470939, 'query_main', lambda: query_main)))
_l_(470942)
_c_(470947, _n_(470943, 'print', lambda: print), 'jsonpath_expression type is', _c_(470946, _n_(470944, 'type', lambda: type), _n_(470945, 'jsonpath_expression', lambda: jsonpath_expression)))
_l_(470948)
for match in _c_(470952, _a_(470950, _n_(470949, 'jsonpath_expression', lambda: jsonpath_expression), 'find'), _n_(470951, 'movies', lambda: movies)):
    _l_(470958)

    _c_(470956, _n_(470953, 'print', lambda: print), _a_(470955, _n_(470954, 'match', lambda: match), 'value'))
    _l_(470957)