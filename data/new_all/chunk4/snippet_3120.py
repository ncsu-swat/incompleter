# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43590043/interactive-brokers-official-python-api-gives-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from ibapi import wrapper
    _l_(601839)

except ImportError:
    pass
try:
    from ibapi.client import EClient
    _l_(601841)

except ImportError:
    pass
try:
    from ibapi.utils import iswrapper
    _l_(601843)

except ImportError:
    pass
try:
    from ibapi.common import *
    _l_(601845)

except ImportError:
    pass
try:
    from ibapi.contract import *
    _l_(601847)

except ImportError:
    pass
try:
    from ibapi.ticktype import *
    _l_(601849)

except ImportError:
    pass

class TestApp(_a_(601851, _n_(601850, "wrapper", lambda: wrapper), "EWrapper"), _n_(601852, "EClient", lambda: EClient)):
    _l_(601931)

    def __init__(self):
        _l_(601871)

        _c_(601857, _a_(601855, _a_(601854, _n_(601853, "wrapper", lambda: wrapper), "EWrapper"), "__init__"), _n_(601856, "self", lambda: self))
        _l_(601858)
        _c_(601863, _a_(601860, _n_(601859, "EClient", lambda: EClient), "__init__"), _n_(601861, "self", lambda: self), wrapper=_n_(601862, "self", lambda: self))
        _l_(601864)
        _n_(601865, "self", lambda: self).reqIsFinished = True
        _l_(601866)
        _n_(601867, "self", lambda: self).started = False
        _l_(601868)
        _n_(601869, "self", lambda: self).nextValidOrderId = 0
        _l_(601870)

    @_n_(601872, "iswrapper", lambda: iswrapper)
    def nextValidId(self, orderId:_n_(601873, "int", lambda: int)):
        _l_(601881)

        _c_(601876, _n_(601874, "print", lambda: print), "setting nextValidOrderId: %d", _n_(601875, "orderId", lambda: orderId))
        _l_(601877)
        _n_(601878, "self", lambda: self).nextValidOrderId = _n_(601879, "orderId", lambda: orderId)
        _l_(601880)
    # we can start now

    @_n_(601882, "iswrapper", lambda: iswrapper)
    def error(self, reqId:TickerId, errorCode:_n_(601883, "int", lambda: int), errorString:_n_(601884, "str", lambda: str)):
        _l_(601891)

        _c_(601889, _n_(601885, "print", lambda: print), "Error. Id: " , _n_(601886, "reqId", lambda: reqId), " Code: " , _n_(601887, "errorCode", lambda: errorCode) , " Msg: " ,     
        _n_(601888, "errorString", lambda: errorString))
        _l_(601890)

    @_n_(601892, "iswrapper", lambda: iswrapper)
# ! [contractdetails]
    def contractDetails(self, reqId: _n_(601893, "int", lambda: int), contractDetails: ContractDetails):
        _l_(601916)

        _c_(601898, _a_(601895, _n_(601894, "super", lambda: super)(), "contractDetails"), _n_(601896, "reqId", lambda: reqId), _n_(601897, "contractDetails", lambda: contractDetails))
        _l_(601899)
        _c_(601914, _n_(601900, "print", lambda: print), "ContractDetails. ReqId:", _n_(601901, "reqId", lambda: reqId), 
            _a_(601904, _a_(601903, _n_(601902, "contractDetails", lambda: contractDetails), "summary"), "symbol"),
            _a_(601907, _a_(601906, _n_(601905, "contractDetails", lambda: contractDetails), "summary"), "secType"), "ConId:", 
            _a_(601910, _a_(601909, _n_(601908, "contractDetails", lambda: contractDetails), "summary"), "conId"),
            _a_(601913, _a_(601912, _n_(601911, "contractDetails", lambda: contractDetails), "summary"), "exchange"))
        _l_(601915)
    # ! [contractdetails]

    @_n_(601917, "iswrapper", lambda: iswrapper)
# ! [contractdetailsend]
    def contractDetailsEnd(self, reqId: _n_(601918, "int", lambda: int)):
        _l_(601930)

        _c_(601922, _a_(601920, _n_(601919, "super", lambda: super)(), "contractDetailsEnd"), _n_(601921, "reqId", lambda: reqId))
        _l_(601923)
        _c_(601926, _n_(601924, "print", lambda: print), "ContractDetailsEnd. ", _n_(601925, "reqId", lambda: reqId), "\n")
        _l_(601927)
        _n_(601928, "self", lambda: self).done = True  # This ends the messages loop
        _l_(601929)  # This ends the messages loop

def main():
    _l_(601991)

    app = _c_(601933, _n_(601932, "TestApp", lambda: TestApp))
    _l_(601934)
    _c_(601937, _a_(601936, _n_(601935, "app", lambda: app), "connect"), "127.0.0.1", 4001, clientId=123)
    _l_(601938)
    _c_(601946, _n_(601939, "print", lambda: print), "serverVersion:%s connectionTime:%s" % (_c_(601942, _a_(601941, _n_(601940, "app", lambda: app), "serverVersion")),
                                        _c_(601945, _a_(601944, _n_(601943, "app", lambda: app), "twsConnectionTime"))))
    _l_(601947)

    _c_(601949, _n_(601948, "print", lambda: print), 'MSFT contract details:')
    _l_(601950)
    contract = _c_(601952, _n_(601951, "Contract", lambda: Contract))
    _l_(601953)
    _n_(601954, "contract", lambda: contract).symbol = "MSFT"
    _l_(601955)
    _n_(601956, "contract", lambda: contract).secType = "STK"
    _l_(601957)
    _n_(601958, "contract", lambda: contract).currency = "USD"
    _l_(601959)
    _n_(601960, "contract", lambda: contract).exchange = ""
    _l_(601961)
    _c_(601965, _a_(601963, _n_(601962, "app", lambda: app), "reqContractDetails"), 210, _n_(601964, "contract", lambda: contract))
    _l_(601966)
    _c_(601969, _a_(601968, _n_(601967, "app", lambda: app), "run"))
    _l_(601970)

    _c_(601972, _n_(601971, "print", lambda: print), 'IBM contract details:')
    _l_(601973)
    _n_(601974, "contract", lambda: contract).symbol = "IBM"
    _l_(601975)
    _n_(601976, "app", lambda: app).done = False # must be set before next run
    _l_(601977) # must be set before next run
    _c_(601981, _a_(601979, _n_(601978, "app", lambda: app), "reqContractDetails"), 210, _n_(601980, "contract", lambda: contract))
    _l_(601982)
    _c_(601985, _a_(601984, _n_(601983, "app", lambda: app), "run"))
    _l_(601986)

    _c_(601989, _a_(601988, _n_(601987, "app", lambda: app), "disconnect")) 
    _l_(601990) 

if _n_(601992, "__name__", lambda: __name__) == "__main__":
    _l_(601996)

    _c_(601994, _n_(601993, "main", lambda: main))
    _l_(601995)