# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66146515/typeerror-when-trying-to-pass-output-of-one-function-to-another-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import socket
    _l_(628798)

except ImportError:
    pass
try:
    import threading
    _l_(628800)

except ImportError:
    pass
try:
    import subprocess
    _l_(628802)

except ImportError:
    pass

nickname = _c_(628804, _n_(628803, "input", lambda: input), "Choose a nickname: ")
_l_(628805)
_c_(628808, _a_(628807, _n_(628806, "subprocess", lambda: subprocess), "run"), "./ipaddress.sh")
_l_(628809)

with _c_(628811, _n_(628810, "open", lambda: open), "ip_addr.txt", 'r') as f:
    _l_(628816)

    file = _c_(628814, _a_(628813, _n_(628812, "f", lambda: f), "readline"))
    _l_(628815)

client = _c_(628823, _a_(628818, _n_(628817, "socket", lambda: socket), "socket"), _a_(628820, _n_(628819, "socket", lambda: socket), "AF_INET"), _a_(628822, _n_(628821, "socket", lambda: socket), "SOCK_STREAM"))
_l_(628824)
_c_(628828, _a_(628826, _n_(628825, "client", lambda: client), "connect"), (_n_(628827, "file", lambda: file), 48812))
_l_(628829)

def receive():
    _l_(628854)

    while True:
        _l_(628853)

        try:
            _l_(628852)

            message = _c_(628834, _a_(628833, _c_(628832, _a_(628831, _n_(628830, "client", lambda: client), "recv"), 1024), "decode"), 'ascii')
            _l_(628835)
            if _n_(628836, "message", lambda: message) == 'NICK':
                _l_(628842)

                pass
                _l_(628837)
            else:
                _c_(628840, _n_(628838, "print", lambda: print), _n_(628839, "message", lambda: message))
                _l_(628841)

        except:
            _l_(628851)

            _c_(628844, _n_(628843, "print", lambda: print), "An error occurred!")
            _l_(628845)
            _c_(628848, _a_(628847, _n_(628846, "client", lambda: client), "close"))
            _l_(628849)
            break
            _l_(628850)


def write():
    _l_(628867)

    while True:
        _l_(628866)

        message = f'{_n_(628855, "nickname", lambda: nickname)}: {_c_(628857, _n_(628856, "input", lambda: input), "")}'
        _l_(628858)
        _c_(628864, _a_(628860, _n_(628859, 'client', lambda: client), 'send'), _c_(628863, _a_(628862, _n_(628861, 'message', lambda: message), 'encode'), 'ascii'))
        _l_(628865)


receive_thread = _c_(628871, _a_(628869, _n_(628868, 'threading', lambda: threading), 'Thread'), target=_n_(628870, 'receive', lambda: receive))
_l_(628872)
_c_(628875, _a_(628874, _n_(628873, 'receive_thread', lambda: receive_thread), 'start'))
_l_(628876)

write_thread = _c_(628880, _a_(628878, _n_(628877, 'threading', lambda: threading), 'Thread'), target=_n_(628879, 'write', lambda: write))
_l_(628881)
_c_(628884, _a_(628883, _n_(628882, 'write_thread', lambda: write_thread), 'start'))
_l_(628885)