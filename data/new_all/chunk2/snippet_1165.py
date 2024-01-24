# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/18613839/python-nameerror-when-defining-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class NetVend:
    _l_(441602)

    def blankCallback(data):
        _l_(441586)

        pass
        _l_(441585)

    def sendCommand(command, callback=_a_(441588, _n_(441587, "NetVend", lambda: NetVend), "blankCallback")):
        _l_(441599)

        aux = _c_(441597, _a_(441590, _n_(441589, "NetVend", lambda: NetVend), "sendSignedCommand"), _n_(441591, "command", lambda: command), _c_(441595, _a_(441593, _n_(441592, "NetVend", lambda: NetVend), "signCommand"), _n_(441594, "command", lambda: command)), _n_(441596, "callback", lambda: callback))
        _l_(441598)
        return aux

    def sendSignedCommand(command, signature, callback):
        _l_(441601)

        pass
        _l_(441600)