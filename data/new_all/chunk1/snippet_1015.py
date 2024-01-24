# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54308619/how-to-fix-a-type-error-for-non-iterabble-socket-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
sock = _c_(385045, _a_(385040, _n_(385039, "socket", lambda: socket), "socket"), _a_(385042, _n_(385041, "socket", lambda: socket), "AF_INET"), _a_(385044, _n_(385043, "socket", lambda: socket), "SOCK_STREAM"))
_l_(385046)
# just a list of connections
connection = {

}
_l_(385047)
def n_remover(user):
    _l_(385099)

    with _c_(385049, _n_(385048, "open", lambda: open), "UserPass.txt" , 'r') as f:
        _l_(385098)

        passuser = _c_(385052, _a_(385051, _n_(385050, "f", lambda: f), "readlines"))
        _l_(385053)
        for x in _n_(385054, "passuser", lambda: passuser):
            _l_(385091)

            _c_(385057, _n_(385055, "print", lambda: print), _n_(385056, "x", lambda: x))
            _l_(385058)
            for area, value in _c_(385061, _n_(385059, "enumerate", lambda: enumerate), _n_(385060, "x", lambda: x)):
                _l_(385090)

                _c_(385065, _n_(385062, "print", lambda: print), _n_(385063, "value", lambda: value), _n_(385064, "area", lambda: area))
                _l_(385066)
                if _n_(385067, "value", lambda: value) == '\n':
                    _l_(385089)

                    _c_(385071, _n_(385068, "print", lambda: print), _n_(385069, "value", lambda: value),_n_(385070, "area", lambda: area))
                    _l_(385072)
                    _n_(385073, "passuser", lambda: passuser)[_c_(385077, _a_(385075, _n_(385074, "passuser", lambda: passuser), "index"), _n_(385076, "x", lambda: x))] = _n_(385078, "passuser", lambda: passuser)[_c_(385082, _a_(385080, _n_(385079, "passuser", lambda: passuser), "index"), _n_(385081, "x", lambda: x))][0:_n_(385083, "area", lambda: area)]
                    _l_(385084)
                    _c_(385087, _n_(385085, "print", lambda: print), _n_(385086, "passuser", lambda: passuser)[0])
                    _l_(385088)
        aux = _n_(385092, "passuser", lambda: passuser)[_c_(385096, _a_(385094, _n_(385093, "passuser", lambda: passuser), "index"), _n_(385095, "user", lambda: user))]
        _l_(385097)
        return aux

def file_len(file):
    _l_(385110)

    with _c_(385101, _n_(385100, "open", lambda: open), 'UserPass.txt', 'r') as f:
        _l_(385107)

        for length, value in _c_(385104, _n_(385102, "enumerate", lambda: enumerate), _n_(385103, "f", lambda: f)):
            _l_(385106)

            pass
            _l_(385105)
    aux = _n_(385108, "length", lambda: length)+1
    _l_(385109)
    return aux

# this bind the server to any ip in ipv4 and any port above 10000
def __init__(self):
    _l_(385121)

    _c_(385114, _a_(385113, _a_(385112, _n_(385111, "self", lambda: self), "sock"), "bind"), ('0.0.0.0', 10000))
    _l_(385115)
    _c_(385119, _a_(385118, _a_(385117, _n_(385116, "self", lambda: self), "sock"), "listen"), 1)
    _l_(385120)

# this handles sending out data to all of the users and handels the disconnect of a user the a arg is a ip and port. and c is the threaded connection.
def handler(self, c, a):
    _l_(385212)

    while True:
        _l_(385211)

        data = _c_(385124, _a_(385123, _n_(385122, "c", lambda: c), "recv"), 1024)
        _l_(385125)
        _c_(385130, _n_(385126, "print", lambda: print), _c_(385129, _n_(385127, "str", lambda: str), _n_(385128, "data", lambda: data))[0:1])
        _l_(385131)
        if _c_(385134, _n_(385132, "str", lambda: str), _n_(385133, "data", lambda: data))[0:1] == "/p":
            _l_(385210)

            datasplit = _c_(385140, _a_(385139, _c_(385138, _n_(385135, "str", lambda: str), _a_(385137, _n_(385136, "self", lambda: self), "data")), "split"), " ")
            _l_(385141)
            password_name = [_a_(385143, _n_(385142, "self", lambda: self), "datasplit")[1] + ' ' + _a_(385145, _n_(385144, "self", lambda: self), "datasplit")[2]]
            _l_(385146)
            with _c_(385148, _n_(385147, "open", lambda: open), "UserPass.txt" , 'r+') as f:
                _l_(385164)

                passuser = _c_(385151, _n_(385149, "n_remover", lambda: n_remover), _n_(385150, "password_name", lambda: password_name))
                _l_(385152)
                for key, value in _n_(385153, "connection", lambda: connection):
                    _l_(385163)

                    if _n_(385154, "c", lambda: c) == _n_(385155, "key", lambda: key):
                        _l_(385162)

                        _a_(385157, _n_(385156, "self", lambda: self), "connection")[_n_(385158, "c", lambda: c)] = _a_(385160, _n_(385159, "self", lambda: self), "datasplit")[1]
                        _l_(385161)
        else:
            _c_(385168, _n_(385165, "print", lambda: print), _a_(385167, _n_(385166, "self", lambda: self), "connection"))
            _l_(385169)

            try:
                _l_(385180)

                l = _a_(385171, _n_(385170, "self", lambda: self), "connection")[_n_(385172, "c", lambda: c)]
                _l_(385173)

            except _n_(385174, "IndexError", lambda: IndexError):
                _l_(385179)

                _a_(385176, _n_(385175, "self", lambda: self), "connection")[_n_(385177, "c", lambda: c)] = "anon"
                _l_(385178)

            for key,value in _a_(385182, _n_(385181, "self", lambda: self), "connection"):
                _l_(385193)

                _c_(385191, _a_(385184, _n_(385183, "key", lambda: key), "send"), _c_(385190, _n_(385185, "bytes", lambda: bytes), _a_(385187, _n_(385186, "self", lambda: self), "connection")[_n_(385188, "c", lambda: c)] + ': ' + _n_(385189, "data", lambda: data)))
                _l_(385192)

            if not _n_(385194, "data", lambda: data):
                _l_(385209)

                _c_(385202, _n_(385195, "print", lambda: print), _c_(385198, _n_(385196, "str", lambda: str), _n_(385197, "a", lambda: a)[0]) + ':' + _c_(385201, _n_(385199, "str", lambda: str), _n_(385200, "a", lambda: a)[1], "disconnected"))
                _l_(385203)
                del self.connection[c]
                _l_(385204)
                _a_(385206, _n_(385205, "c", lambda: c), "close")
                _l_(385207)
                break
                _l_(385208)