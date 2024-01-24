# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70636568/when-executing-the-program-it-gives-an-error-typeerror-list-indices-must-be-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(366927)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(366929)

except ImportError:
    pass

def get_from_binance():
    _l_(366949)


    req = _c_(366932, _a_(366931, _n_(366930, "requests", lambda: requests), "get"), "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    _l_(366933)
    response = _c_(366936, _a_(366935, _n_(366934, "req", lambda: req), "json"))
    _l_(366937)
    sell_price = _n_(366938, "response", lambda: response)["price"]
    _l_(366939)
    _c_(366947, _n_(366940, "print", lambda: print), f"{_c_(366945, _a_(366944, _c_(366943, _a_(366942, _n_(366941, 'datetime', lambda: datetime), 'now')), 'strftime'), '%Y-%m-%d %H:%M:%S')}\nBTC Binance: {_n_(366946, 'sell_price', lambda: sell_price)}")
    _l_(366948)


def get_from_bittrex():
    _l_(366964)


    req2 = _c_(366952, _a_(366951, _n_(366950, "requests", lambda: requests), "get"), "https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC")
    _l_(366953)
    response2 = _c_(366956, _a_(366955, _n_(366954, "req2", lambda: req2), "json"))
    _l_(366957)
    sell_price2 = _n_(366958, "response2", lambda: response2)["result"]['Last']
    _l_(366959)
    _c_(366962, _n_(366960, "print", lambda: print), f"BTC Bittrex: {_n_(366961, 'sell_price2', lambda: sell_price2)}")
    _l_(366963)


def get_from_bitfinex():
    _l_(366979)


    req3 = _c_(366967, _a_(366966, _n_(366965, "requests", lambda: requests), "get"), "https://api-pub.bitfinex.com/v2/tickers?symbols=tBTCUSD")
    _l_(366968)
    response3 = _c_(366971, _a_(366970, _n_(366969, "req3", lambda: req3), "json"))
    _l_(366972)
    sell_price3 = _n_(366973, "response3", lambda: response3)["0"]["1"]
    _l_(366974)
    _c_(366977, _n_(366975, "print", lambda: print), f"BTC bitfinex: {_n_(366976, 'sell_price3', lambda: sell_price3)}")
    _l_(366978)


if _n_(366980, "__name__", lambda: __name__) == '__main__':
    _l_(366990)


    _c_(366982, _n_(366981, "get_from_binance", lambda: get_from_binance))
    _l_(366983)
    _c_(366985, _n_(366984, "get_from_bittrex", lambda: get_from_bittrex))
    _l_(366986)
    _c_(366988, _n_(366987, "get_from_bitfinex", lambda: get_from_bitfinex))
    _l_(366989)