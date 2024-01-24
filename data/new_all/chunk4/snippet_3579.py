# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71921746/typeerror-list-indices-must-be-integers-or-slices-not-str-python-zabbixapi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for i in _c_(604982, _n_(604980, "range", lambda: range), _n_(604981, "geteventlist", lambda: geteventlist)):
    _l_(604993)

    _n_(604983, "i", lambda: i)['host'] = _n_(604984, "i", lambda: i)['hosts']['host']
    _l_(604985)
    _n_(604986, "i", lambda: i)['hostid'] = _n_(604987, "i", lambda: i)['hosts']['hostid']
    _l_(604988)
    _n_(604989, "i", lambda: i)['location'] = _n_(604990, "i", lambda: i)['hosts']['name']
    _l_(604991)
    del i['hosts']
    _l_(604992)