# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57441298/attributeerror-x962
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
server = _c_(412377, _n_(412376, "SSHTunnelForwarder", lambda: SSHTunnelForwarder), ('<ssh_host>', 22),
    ssh_username="<ssh_user>",
    ssh_config_file='<path_to_config>',
    ssh_pkey="<path_to_pkey>",
    remote_bind_address=('127.0.0.1', 5432)
)
_l_(412378)

_c_(412381, _a_(412380, _n_(412379, "server", lambda: server), "start"))
_l_(412382)