# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50157962/python3-typeerror-list-indices-must-be-integers-or-slices-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
selected_env='mydev2'
_l_(444782)
server_list=[{'mydev': ['192.168.56.102', '192.168.56.102', '192.168.56.102']}, {'mydev2': ['192.168.56.102', '192.168.56.102', '192.168.56.102']}]         
_l_(444783)         
for item in _n_(444784, "server_list", lambda: server_list) :
    _l_(444791)

    host_list=[_n_(444785, "item", lambda: item) for item in _n_(444786, "server_list", lambda: server_list)[_n_(444787, "selected_env", lambda: selected_env)] if _n_(444788, "selected_env", lambda: selected_env) in _n_(444789, "server_list", lambda: server_list)]
    _l_(444790)

_c_(444794, _n_(444792, "print", lambda: print), _n_(444793, "host_list", lambda: host_list))
_l_(444795)