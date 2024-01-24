# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42751642/py2neo-v3-attributeerror-object-has-no-attribute-db-exists
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for row in _n_(390300, "data", lambda: data):
    _l_(390323)

    ds = _c_(390302, _n_(390301, "DataSource", lambda: DataSource))
    _l_(390303)
    #   parse Source of Information column as a list, trimming whitespace
    _n_(390304, "ds", lambda: ds).uri = _c_(390313, _n_(390305, "list", lambda: list), _c_(390312, _n_(390306, "map", lambda: map), _a_(390308, _n_(390307, "str", lambda: str), "strip"), _c_(390311, _a_(390310, _n_(390309, "row", lambda: row)['data_source'], "split"), ',')))
    _l_(390314)
    _n_(390315, "ds", lambda: ds).description = _n_(390316, "row", lambda: row)['data_source_description']
    _l_(390317)
    _c_(390321, _a_(390319, _n_(390318, "graph", lambda: graph), "merge"), _n_(390320, "ds", lambda: ds))
    _l_(390322)