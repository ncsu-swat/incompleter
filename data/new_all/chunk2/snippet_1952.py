# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75982209/typeerror-tradingapp-error-missing-1-required-positional-argument-advancedo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from ibapi.client import EClient
    _l_(435300)

except ImportError:
    pass
try:
    from ibapi.wrapper import EWrapper
    _l_(435302)

except ImportError:
    pass
try:
    from ibapi.contract import Contract
    _l_(435304)

except ImportError:
    pass
try:
    import threading
    _l_(435306)

except ImportError:
    pass
try:
    import time
    _l_(435308)

except ImportError:
    pass


class TradingApp(_n_(435309, "EWrapper", lambda: EWrapper), _n_(435310, "EClient", lambda: EClient)):
    _l_(435336)

    def __init__(self):
        _l_(435317)

        _c_(435315, _a_(435312, _n_(435311, "EClient", lambda: EClient), "__init__"), _n_(435313, "self", lambda: self),_n_(435314, "self", lambda: self))
        _l_(435316)
    def error(self, reqId, errorCode, errorString, advancedOrderRejectJson):
        _l_(435327)

        _c_(435325, _n_(435318, "print", lambda: print), _c_(435324, _a_(435319, "Error {} {} {} {}", "format"), _n_(435320, "reqId", lambda: reqId),_n_(435321, "errorCode", lambda: errorCode),_n_(435322, "errorString", lambda: errorString),_n_(435323, "advancedOrderRejectJson", lambda: advancedOrderRejectJson)))
        _l_(435326)
    def contractDetails(self, reqId, contractDetails):
        _l_(435335)

        _c_(435333, _n_(435328, "print", lambda: print), _c_(435332, _a_(435329, "redID: {}, contract:{}", "format"), _n_(435330, "reqId", lambda: reqId),_n_(435331, "contractDetails", lambda: contractDetails)))
        _l_(435334)

def websocket_con():
    _l_(435345)

    _c_(435339, _a_(435338, _n_(435337, "app", lambda: app), "run"))
    _l_(435340)
    _c_(435343, _a_(435342, _n_(435341, "event", lambda: event), "wait"))
    _l_(435344)

event = _c_(435348, _a_(435347, _n_(435346, "threading", lambda: threading), "Event"))   
_l_(435349)   
app = _c_(435351, _n_(435350, "TradingApp", lambda: TradingApp))      
_l_(435352)      
_c_(435355, _a_(435354, _n_(435353, "app", lambda: app), "connect"), "127.0.0.1", 4001, clientId=1)
_l_(435356)

# starting a separate daemon thread to execute the websocket connection
con_thread = _c_(435360, _a_(435358, _n_(435357, "threading", lambda: threading), "Thread"), target=_n_(435359, "websocket_con", lambda: websocket_con))
_l_(435361)
_c_(435364, _a_(435363, _n_(435362, "con_thread", lambda: con_thread), "start"))
_l_(435365)
_c_(435368, _a_(435367, _n_(435366, "time", lambda: time), "sleep"), 1) # some latency added to ensure that the connection is established
_l_(435369) # some latency added to ensure that the connection is established

#creating object of the Contract class - will be used as a parameter for other function calls
contract = _c_(435371, _n_(435370, "Contract", lambda: Contract))
_l_(435372)
_n_(435373, "contract", lambda: contract).symbol = "AAPL"
_l_(435374)
_n_(435375, "contract", lambda: contract).secType = "STK"
_l_(435376)
_n_(435377, "contract", lambda: contract).currency = "USD"
_l_(435378)
_n_(435379, "contract", lambda: contract).exchange = "SMART"
_l_(435380)

_c_(435384, _a_(435382, _n_(435381, "app", lambda: app), "reqContractDetails"), 100, _n_(435383, "contract", lambda: contract)) # EClient function to request contract details
_l_(435385) # EClient function to request contract details
_c_(435388, _a_(435387, _n_(435386, "time", lambda: time), "sleep"), 5) # some latency added to ensure that the contract details request has been processed
_l_(435389) # some latency added to ensure that the contract details request has been processed
_c_(435392, _a_(435391, _n_(435390, "event", lambda: event), "set"))
_l_(435393)