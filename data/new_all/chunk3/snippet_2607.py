# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67638541/f5-tlm-typeerror-object-of-type-nodes-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from f5.bigip import ManagementRoot
    _l_(550068)

except ImportError:
    pass
try:
    import json
    _l_(550070)

except ImportError:
    pass

user = 'admin'
_l_(550071)
password = 'secret'
_l_(550072)
f5_ip = '10.0.0.10'
_l_(550073)
partition = 'PART1'
_l_(550074)


mgmt = _c_(550079, _n_(550075, "ManagementRoot", lambda: ManagementRoot), _n_(550076, "f5_ip", lambda: f5_ip), _n_(550077, "user", lambda: user), _n_(550078, "password", lambda: password))
_l_(550080)
ltm = _a_(550083, _a_(550082, _n_(550081, "mgmt", lambda: mgmt), "tm"), "ltm")
_l_(550084)

nodes = _c_(550088, _a_(550087, _a_(550086, _n_(550085, "ltm", lambda: ltm), "nodes"), "get_collection"))
_l_(550089)

for node in _n_(550090, "nodes", lambda: nodes):
    _l_(550103)

    node_dict = _a_(550092, _n_(550091, "node", lambda: node), "raw")
    _l_(550093)
    node_json = _c_(550097, _a_(550095, _n_(550094, "json", lambda: json), "dumps"), _n_(550096, "node_dict", lambda: node_dict), indent=4)
    _l_(550098)
    _c_(550101, _n_(550099, "print", lambda: print), _n_(550100, "node_json", lambda: node_json))
    _l_(550102)