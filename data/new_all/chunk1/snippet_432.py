# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45803286/typeerror-cannot-create-a-consistent-mro-for-bases-mixin-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import connections
    _l_(400587)

except ImportError:
    pass
try:
    from django.db.models.query import QuerySet
    _l_(400589)

except ImportError:
    pass

class QuerySetExplainMixin:
    _l_(400615)

    def explain(self):
        _l_(400614)

        cursor = _c_(400594, _a_(400593, _n_(400590, "connections", lambda: connections)[_a_(400592, _n_(400591, "self", lambda: self), "db")], "cursor"))
        _l_(400595)
        query, params = _c_(400599, _a_(400598, _a_(400597, _n_(400596, "self", lambda: self), "query"), "sql_with_params"))
        _l_(400600)
        _c_(400605, _a_(400602, _n_(400601, "cursor", lambda: cursor), "execute"), 'explain %s' % _n_(400603, "query", lambda: query), _n_(400604, "params", lambda: params))
        _l_(400606)
        aux = _c_(400612, _a_(400607, '\n', "join"), (_n_(400608, "r", lambda: r)[0] for r in _c_(400611, _a_(400610, _n_(400609, "cursor", lambda: cursor), "fetchall"))))
        _l_(400613)
        return aux

_n_(400616, "QuerySet", lambda: QuerySet).__bases__ += (_n_(400617, "QuerySetExplainMixin", lambda: QuerySetExplainMixin),)
_l_(400618)