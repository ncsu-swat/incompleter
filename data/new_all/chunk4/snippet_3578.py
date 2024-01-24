# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71921746/typeerror-list-indices-must-be-integers-or-slices-not-str-python-zabbixapi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for i in _c_(607899, _n_(607895, "range", lambda: range), _c_(607898, _n_(607896, "len", lambda: len), _n_(607897, "geteventlist", lambda: geteventlist))):
    _l_(607910)

    _n_(607900, "i", lambda: i)['host'] = _n_(607901, "i", lambda: i)['hosts']['host']
    _l_(607902)
    _n_(607903, "i", lambda: i)['hostid'] = _n_(607904, "i", lambda: i)['hosts']['hostid']
    _l_(607905)
    _n_(607906, "i", lambda: i)['location'] = _n_(607907, "i", lambda: i)['hosts']['name']
    _l_(607908)
    del i['hosts']
    _l_(607909)