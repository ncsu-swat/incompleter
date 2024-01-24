# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40110816/attributeerror-nonetype-object-has-no-attribute-recv
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from src.lib import irc as irc_
    _l_(557161)

except ImportError:
    pass
try:
    from src.lib import functions_general
    _l_(557163)

except ImportError:
    pass
try:
    from src.lib import functions_commands as commands
    _l_(557165)

except ImportError:
    pass
try:
    from src.config import config
    _l_(557167)

except ImportError:
    pass

class PartyMachine:
    _l_(557221)


    def __init__(self, config):
        _l_(557183)

        _n_(557168, "self", lambda: self).config = _n_(557169, "config", lambda: config)
        _l_(557170)
        _n_(557171, "self", lambda: self).irc = _c_(557175, _a_(557173, _n_(557172, "irc_", lambda: irc_), "irc"), _n_(557174, "config", lambda: config))
        _l_(557176)
        _n_(557177, "self", lambda: self).socket = _c_(557181, _a_(557180, _a_(557179, _n_(557178, "self", lambda: self), "irc"), "get_irc_socket_object"))
        _l_(557182)


    def sock(self):
        _l_(557220)

        irc = _a_(557185, _n_(557184, "self", lambda: self), "irc")
        _l_(557186)
        sock = _a_(557188, _n_(557187, "self", lambda: self), "socket")
        _l_(557189)
        config = _a_(557191, _n_(557190, "self", lambda: self), "config")
        _l_(557192)
        kage = _n_(557193, "sock", lambda: sock)
        _l_(557194)

        while True:
            _l_(557219)

            data = _c_(557199, _a_(557198, _c_(557197, _a_(557196, _n_(557195, "sock", lambda: sock), "recv"), 2048), "rstrip"))
            _l_(557200)

            if _c_(557203, _n_(557201, "len", lambda: len), _n_(557202, "data", lambda: data)) == 0:
                _l_(557212)

                _c_(557205, _n_(557204, "pp", lambda: pp), 'Connection was lost, reconnecting.')
                _l_(557206)
                sock = _c_(557210, _a_(557209, _a_(557208, _n_(557207, "self", lambda: self), "irc"), "get_irc_socket_object"))
                _l_(557211)

            if _n_(557213, "config", lambda: config)['debug']:
                _l_(557218)

                _c_(557216, _n_(557214, "print", lambda: print), _n_(557215, "data", lambda: data))
                _l_(557217)