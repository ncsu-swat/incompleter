# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71921746/typeerror-list-indices-must-be-integers-or-slices-not-str-python-zabbixapi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for i in _c_(631607, _n_(631605, "range", lambda: range), _n_(631606, "geteventlist", lambda: geteventlist)):
    _l_(631618)

    _n_(631608, "i", lambda: i)['host'] = _n_(631609, "i", lambda: i)['hosts']['host']
    _l_(631610)
    _n_(631611, "i", lambda: i)['hostid'] = _n_(631612, "i", lambda: i)['hosts']['hostid']
    _l_(631613)
    _n_(631614, "i", lambda: i)['location'] = _n_(631615, "i", lambda: i)['hosts']['name']
    _l_(631616)
    del i['hosts']
    _l_(631617)