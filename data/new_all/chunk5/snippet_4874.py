# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44064232/nameerror-with-echo-client-server-test-client-unable-to-send-custom-message-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys, socket
    _l_(693710)

except ImportError:
    pass
try:
    import tincanchat
    _l_(693712)

except ImportError:
    pass

HOST = _a_(693714, _n_(693713, "sys", lambda: sys), "argv")[-1] if _c_(693718, _n_(693715, "len", lambda: len), _a_(693717, _n_(693716, "sys", lambda: sys), "argv")) > 1 else '127.0.0.1'
_l_(693719)
PORT = _a_(693721, _n_(693720, "tincanchat", lambda: tincanchat), "PORT")
_l_(693722)

if _n_(693723, "__name__", lambda: __name__) == '__main__':
    _l_(693790)

    while True:
        _l_(693789)

        try:
            _l_(693788)

            sock = _c_(693730, _a_(693725, _n_(693724, "socket", lambda: socket), "socket"), _a_(693727, _n_(693726, "socket", lambda: socket), "AF_INET"), _a_(693729, _n_(693728, "socket", lambda: socket), "SOCK_STREAM"))
            _l_(693731)
            _c_(693736, _a_(693733, _n_(693732, "sock", lambda: sock), "connect"), (_n_(693734, "HOST", lambda: HOST), _n_(693735, "PORT", lambda: PORT)))
            _l_(693737)
            _c_(693743, _n_(693738, "print", lambda: print), _c_(693742, _a_(693739, '\nConnected to {}:{}', "format"), _n_(693740, "HOST", lambda: HOST), _n_(693741, "PORT", lambda: PORT)))
            _l_(693744)
            _c_(693746, _n_(693745, "print", lambda: print), "Type message, enter to send, 'q' to quit")
            _l_(693747)
            msg = _c_(693749, _n_(693748, "input", lambda: input))
            _l_(693750)
            if _n_(693751, "msg", lambda: msg) == 'q':
                _l_(693752)

break            _c_(693757, _a_(693754, _n_(693753, "tincanchat", lambda: tincanchat), "send_msg"), _n_(693755, "sock", lambda: sock), _n_(693756, "msg", lambda: msg)) # Blocks until sent
            _l_(693758) # Blocks until sent
            _c_(693763, _n_(693759, "print", lambda: print), _c_(693762, _a_(693760, 'Sent message: {}', "format"), _n_(693761, "msg", lambda: msg)))
            _l_(693764)
            msg = _c_(693768, _a_(693766, _n_(693765, "tincanchat", lambda: tincanchat), "recv_msg"), _n_(693767, "sock", lambda: sock)) # Block until
            _l_(693769) # Block until
                                        # received complete
                                        # message
            _c_(693772, _n_(693770, "print", lambda: print), 'Received echo: ' + _n_(693771, "msg", lambda: msg))
            _l_(693773)
        except _n_(693774, "ConnectionError", lambda: ConnectionError):
            _l_(693779)

            _c_(693776, _n_(693775, "print", lambda: print), 'Socket error')
            _l_(693777)
            break
            _l_(693778)
        finally:
            _l_(693787)

            _c_(693782, _a_(693781, _n_(693780, "sock", lambda: sock), "close"))
            _l_(693783)
            _c_(693785, _n_(693784, "print", lambda: print), 'Closed connection to server\n')
            _l_(693786)