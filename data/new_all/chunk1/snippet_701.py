# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54071217/attributeerror-module-socket-has-no-attribute-msg-dontwait
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
RECV_BUFFER_SIZE = 1024
_l_(400351)
buff = _c_(400356, _n_(400352, "memoryview", lambda: memoryview), _c_(400355, _n_(400353, "bytearray", lambda: bytearray), _n_(400354, "RECV_BUFFER_SIZE", lambda: RECV_BUFFER_SIZE)))
_l_(400357)
x = _c_(400364, _a_(400359, _n_(400358, "client_socket", lambda: client_socket), "recv_into"), _n_(400360, "buff", lambda: buff), _n_(400361, "RECV_BUFFER_SIZE", lambda: RECV_BUFFER_SIZE), _a_(400363, _n_(400362, "socket", lambda: socket), "MSG_DONTWAIT"))
_l_(400365)