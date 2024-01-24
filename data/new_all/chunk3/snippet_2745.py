# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64714925/retrieving-typeerror-nonetype-object-is-not-callable-socket
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
context = _c_(539184, _a_(539183, _n_(539182, "zmq", lambda: zmq), "Context"))
_l_(539185)
footage_socket = _c_(539190, _a_(539187, _n_(539186, "context", lambda: context), "socket"), _a_(539189, _n_(539188, "zmq", lambda: zmq), "SUB"))
_l_(539191)
_c_(539194, _a_(539193, _n_(539192, "footage_socket", lambda: footage_socket), "bind"), 'tcp://0.0.0.0:9999')
_l_(539195)
_c_(539203, _a_(539197, _n_(539196, "footage_socket", lambda: footage_socket), "setsockopt_string"), _a_(539199, _n_(539198, "zmq", lambda: zmq), "SUBSCRIBE"), _c_(539202, _a_(539201, _n_(539200, "np", lambda: np), "unicode"), ''))
_l_(539204)
while True:
   _l_(539218)

   frame = _c_(539207, _a_(539206, _n_(539205, "footage_socket", lambda: footage_socket), "recv_string"))
   _l_(539208)
   img = _c_(539212, _a_(539210, _n_(539209, "base64", lambda: base64), "b64decode"), _n_(539211, "frame", lambda: frame))
   _l_(539213)
   _c_(539216, _n_(539214, "print", lambda: print), _n_(539215, "img", lambda: img))
   _l_(539217)