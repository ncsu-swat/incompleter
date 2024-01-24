# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67284107/python-attributeerror-super-object-has-no-attribute-testnet-however-the-at
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from binance.client import Client
    _l_(449122)

except ImportError:
    pass
try:
    from binance.websockets import BinanceSocketManager
    _l_(449124)

except ImportError:
    pass

class Binance_Data(_n_(449125, "Client", lambda: Client)):
    _l_(449168)

    def __init__(self, api_key, api_secret, requests_params=None, tld='us'):
        _l_(449132)

        _c_(449130, _a_(449127, _n_(449126, "super", lambda: super)(), "__init__"), _n_(449128, "api_key", lambda: api_key), _n_(449129, "api_secret", lambda: api_secret), requests_params=None, tld='us')
        _l_(449131)

    def data_stream_test(self, data):
        _l_(449153)

        _c_(449134, _n_(449133, "print", lambda: print), '------------------')
        _l_(449135)
        _c_(449138, _n_(449136, "print", lambda: print), f"Event Title: {_n_(449137, 'data', lambda: data)['e']}")
        _l_(449139)
        _c_(449142, _n_(449140, "print", lambda: print), f"Closing Price: {_n_(449141, 'data', lambda: data)['c']}")
        _l_(449143)
        _c_(449148, _n_(449144, "print", lambda: print), _c_(449147, _n_(449145, "convert_unix_to_utc", lambda: convert_unix_to_utc), _n_(449146, "data", lambda: data)['E']))
        _l_(449149)
        _c_(449151, _n_(449150, "print", lambda: print), '------------------')
        _l_(449152)

    def data_stream(self):
        _l_(449167)

        ds = _c_(449156, _n_(449154, "BinanceSocketManager", lambda: BinanceSocketManager), _n_(449155, "super", lambda: super)())
        _l_(449157)
        conn_key = _c_(449161, _a_(449159, _n_(449158, "ds", lambda: ds), "start_symbol_ticker_socket"), 'XLMUSDT', _n_(449160, "data_stream_test", lambda: data_stream_test))
        _l_(449162)
        _c_(449165, _a_(449164, _n_(449163, "ds", lambda: ds), "start"))
        _l_(449166)