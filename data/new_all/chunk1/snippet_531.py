# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49163393/twisted-python3-typeerror-init-missing-1-required-positional-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from twisted.internet.protocol import Protocol, Factory
    _l_(385645)

except ImportError:
    pass
try:
    from twisted.internet.endpoints import TCP4ServerEndpoint
    _l_(385647)

except ImportError:
    pass
try:
    from twisted.internet import reactor
    _l_(385649)

except ImportError:
    pass
try:
    from twisted.internet import task
    _l_(385651)

except ImportError:
    pass
try:
    from twisted.internet import protocol
    _l_(385653)

except ImportError:
    pass

#from screenhelp import ScreenHelp ** Not relevant to error


class Screen(_n_(385654, "Protocol", lambda: Protocol)):
    _l_(385707)


    def __init__(self, factory):
        _l_(385674)

        _n_(385655, "self", lambda: self).factory = _n_(385656, "factory", lambda: factory)
        _l_(385657)
        _n_(385658, "self", lambda: self).connection = False
        _l_(385659)
        _n_(385660, "self", lambda: self).loop = _c_(385664, _a_(385662, _n_(385661, "task", lambda: task), "LoopingCall"), _n_(385663, "screenRefresh", lambda: screenRefresh))
        _l_(385665)
        _n_(385666, "self", lambda: self).loopDeferred = None
        _l_(385667)
        _n_(385668, "self", lambda: self).stack = []
        _l_(385669)
        _n_(385670, "self", lambda: self).cs = _c_(385672, _n_(385671, "ScreenHelp", lambda: ScreenHelp))
        _l_(385673)

    def connectionMade(self):
        _l_(385682)

        _n_(385675, "self", lambda: self).loopDeferred = _c_(385680, _a_(385678, _a_(385677, _n_(385676, "self", lambda: self), "loop"), "start"), _n_(385679, "self", lambda: self),5)
        _l_(385681)

    def connectionLost(self, reason):
        _l_(385689)

        _c_(385687, _a_(385685, _a_(385684, _n_(385683, "self", lambda: self), "loop"), "stop"), _n_(385686, "self", lambda: self))
        _l_(385688)

    def dataReceived(self, data):
        _l_(385696)

        _c_(385694, _a_(385692, _a_(385691, _n_(385690, "self", lambda: self), "stack"), "append"), _n_(385693, "data", lambda: data))
        _l_(385695)

    def screenRefresh(self):
        _l_(385706)


        #self.transport.write(self.cs.clr()) ** Not relevent - issues clear screen command.
        for x in _a_(385698, _n_(385697, "self", lambda: self), "stack"):
            _l_(385705)

            _c_(385703, _a_(385701, _a_(385700, _n_(385699, "self", lambda: self), "transport"), "write"), _n_(385702, "x", lambda: x))
            _l_(385704)

class ScreenFactory(_n_(385708, "Factory", lambda: Factory)):
    _l_(385713)

    def buildProtocol(self, addr):
        _l_(385712)

        aux = _c_(385710, _n_(385709, "Screen", lambda: Screen))
        _l_(385711)
        return aux


def main():
    _l_(385732)

    endpoint1 = _c_(385716, _n_(385714, "TCP4ServerEndpoint", lambda: TCP4ServerEndpoint), _n_(385715, "reactor", lambda: reactor), 64000)
    _l_(385717)
    _c_(385721, _a_(385719, _n_(385718, "endpoint1", lambda: endpoint1), "listen"), _n_(385720, "ScreenFactory", lambda: ScreenFactory))
    _l_(385722)
    _c_(385726, _a_(385724, _n_(385723, "reactor", lambda: reactor), "listenTCP"), 5000, _n_(385725, "fact", lambda: fact))
    _l_(385727)
    _c_(385730, _a_(385729, _n_(385728, "reactor", lambda: reactor), "run"))
    _l_(385731)


if _n_(385733, "__name__", lambda: __name__) == "__main__":
    _l_(385737)

    _c_(385735, _n_(385734, "main", lambda: main))
    _l_(385736)