# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66146515/typeerror-when-trying-to-pass-output-of-one-function-to-another-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import threading
    _l_(643811)

except ImportError:
    pass
try:
    import socket
    _l_(643813)

except ImportError:
    pass
try:
    import subprocess
    _l_(643815)

except ImportError:
    pass

_c_(643818, _a_(643817, _n_(643816, "subprocess", lambda: subprocess), "run"), "./ipaddress.sh")
_l_(643819)

with _c_(643821, _n_(643820, "open", lambda: open), "ip_addr.txt", 'r') as f:
    _l_(643826)

    file = _c_(643824, _a_(643823, _n_(643822, "f", lambda: f), "readline"))
    _l_(643825)

host = _n_(643827, "file", lambda: file)
_l_(643828)
port = 48812
_l_(643829)

server = _c_(643836, _a_(643831, _n_(643830, "socket", lambda: socket), "socket"), _a_(643833, _n_(643832, "socket", lambda: socket), "AF_INET"), _a_(643835, _n_(643834, "socket", lambda: socket), "SOCK_STREAM"))
_l_(643837)
_c_(643842, _a_(643839, _n_(643838, "server", lambda: server), "bind"), (_n_(643840, "host", lambda: host), _n_(643841, "port", lambda: port)))
_l_(643843)
_c_(643846, _a_(643845, _n_(643844, "server", lambda: server), "listen"))
_l_(643847)

clients = []
_l_(643848)
nicknames = []
_l_(643849)

def broadcast(message):
    _l_(643857)

    for client in _n_(643850, "clients", lambda: clients):
        _l_(643856)

        _c_(643854, _a_(643852, _n_(643851, "client", lambda: client), "send"), _n_(643853, "message", lambda: message))
        _l_(643855)

def handle(client):
    _l_(643898)

    while True:
        _l_(643897)

        try:
            _l_(643896)

            message = _c_(643860, _a_(643859, _n_(643858, "client", lambda: client), "recv"), 1024)
            _l_(643861)
            _c_(643864, _n_(643862, "broadcast", lambda: broadcast), _n_(643863, "message", lambda: message))
            _l_(643865)

        except:
            _l_(643895)

            index = _c_(643869, _a_(643867, _n_(643866, "clients", lambda: clients), "index"), _n_(643868, "client", lambda: client))
            _l_(643870)
            _c_(643874, _a_(643872, _n_(643871, "clients", lambda: clients), "remove"), _n_(643873, "client", lambda: client))
            _l_(643875)
            _c_(643878, _a_(643877, _n_(643876, "client", lambda: client), "close"))
            _l_(643879)
            nickname = _n_(643880, "nicknames", lambda: nicknames)[_n_(643881, "index", lambda: index)]
            _l_(643882)
            _c_(643887, _n_(643883, "broadcast", lambda: broadcast), _c_(643886, _a_(643885, f"{_n_(643884, 'nickname', lambda: nickname)} left the chat", "encode"), 'ascii'))
            _l_(643888)
            _c_(643892, _a_(643890, _n_(643889, "nicknames", lambda: nicknames), "remove"), _n_(643891, "nickname", lambda: nickname))
            _l_(643893)
            break
            _l_(643894)
def receive():
    _l_(643958)

    while True:
        _l_(643957)

        client, address = _c_(643901, _a_(643900, _n_(643899, "server", lambda: server), "accept"))
        _l_(643902)
        _c_(643907, _n_(643903, "print", lambda: print), f"Connected with{_c_(643906, _n_(643904, 'str', lambda: str), _n_(643905, 'address', lambda: address))}")
        _l_(643908)

        _c_(643913, _a_(643910, _n_(643909, "client", lambda: client), "send"), _c_(643912, _a_(643911, "NICK", "encode"), "ascii"))
        _l_(643914)
        nickname = _c_(643919, _a_(643918, _c_(643917, _a_(643916, _n_(643915, "client", lambda: client), "recv"), 1024), "decode"), 'ascii')
        _l_(643920)
        _c_(643924, _a_(643922, _n_(643921, "nicknames", lambda: nicknames), "append"), _n_(643923, "nickname", lambda: nickname))
        _l_(643925)
        _c_(643929, _a_(643927, _n_(643926, "clients", lambda: clients), "append"), _n_(643928, "client", lambda: client))
        _l_(643930)

        _c_(643933, _n_(643931, "print", lambda: print), f"Nickname of client is {_n_(643932, 'nickname', lambda: nickname)}\n")
        _l_(643934)
        _c_(643939, _n_(643935, "broadcast", lambda: broadcast), _c_(643938, _a_(643937, f'{_n_(643936, "nickname", lambda: nickname)}joined the chat!\n', 'encode'), 'ascii'))
        _l_(643940)
        _c_(643945, _a_(643942, _n_(643941, 'client', lambda: client), 'send'), _c_(643944, _a_(643943, "Connected to the server!\n", 'encode'), 'ascii'))
        _l_(643946)

        thread = _c_(643951, _a_(643948, _n_(643947, 'threading', lambda: threading), 'Thread'), target=_n_(643949, 'handle', lambda: handle), args=(_n_(643950, 'client', lambda: client),))
        _l_(643952)
        _c_(643955, _a_(643954, _n_(643953, 'thread', lambda: thread), 'start'))
        _l_(643956)


_c_(643960, _n_(643959, 'print', lambda: print), "Server is listening...")
_l_(643961)
_c_(643963, _n_(643962, 'receive', lambda: receive))
_l_(643964)