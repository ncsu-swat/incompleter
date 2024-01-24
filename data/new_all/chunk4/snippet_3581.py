# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71921746/typeerror-list-indices-must-be-integers-or-slices-not-str-python-zabbixapi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for i in _c_(591812, _n_(591808, "range", lambda: range), _c_(591811, _n_(591809, "len", lambda: len), _n_(591810, "geteventlist", lambda: geteventlist))):
    _l_(591823)

    _n_(591813, "i", lambda: i)['host'] = _n_(591814, "i", lambda: i)['hosts']['host']
    _l_(591815)
    _n_(591816, "i", lambda: i)['hostid'] = _n_(591817, "i", lambda: i)['hosts']['hostid']
    _l_(591818)
    _n_(591819, "i", lambda: i)['location'] = _n_(591820, "i", lambda: i)['hosts']['name']
    _l_(591821)
    del i['hosts']
    _l_(591822)