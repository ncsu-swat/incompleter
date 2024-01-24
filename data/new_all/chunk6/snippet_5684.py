# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70636568/when-executing-the-program-it-gives-an-error-typeerror-list-indices-must-be-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(370555)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(370557)

except ImportError:
    pass

def get_from_binance():
    _l_(370577)


    req = _c_(370560, _a_(370559, _n_(370558, "requests", lambda: requests), "get"), "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    _l_(370561)
    response = _c_(370564, _a_(370563, _n_(370562, "req", lambda: req), "json"))
    _l_(370565)
    sell_price = _n_(370566, "response", lambda: response)["price"]
    _l_(370567)
    _c_(370575, _n_(370568, "print", lambda: print), f"{_c_(370573, _a_(370572, _c_(370571, _a_(370570, _n_(370569, 'datetime', lambda: datetime), 'now')), 'strftime'), '%Y-%m-%d %H:%M:%S')}\nBTC Binance: {_n_(370574, 'sell_price', lambda: sell_price)}")
    _l_(370576)


def get_from_bittrex():
    _l_(370592)


    req2 = _c_(370580, _a_(370579, _n_(370578, "requests", lambda: requests), "get"), "https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC")
    _l_(370581)
    response2 = _c_(370584, _a_(370583, _n_(370582, "req2", lambda: req2), "json"))
    _l_(370585)
    sell_price2 = _n_(370586, "response2", lambda: response2)["result"]['Last']
    _l_(370587)
    _c_(370590, _n_(370588, "print", lambda: print), f"BTC Bittrex: {_n_(370589, 'sell_price2', lambda: sell_price2)}")
    _l_(370591)


def get_from_bitfinex():
    _l_(370607)


    req3 = _c_(370595, _a_(370594, _n_(370593, "requests", lambda: requests), "get"), "https://api-pub.bitfinex.com/v2/tickers?symbols=tBTCUSD")
    _l_(370596)
    response3 = _c_(370599, _a_(370598, _n_(370597, "req3", lambda: req3), "json"))
    _l_(370600)
    sell_price3 = _n_(370601, "response3", lambda: response3)["0"]["1"]
    _l_(370602)
    _c_(370605, _n_(370603, "print", lambda: print), f"BTC bitfinex: {_n_(370604, 'sell_price3', lambda: sell_price3)}")
    _l_(370606)


if _n_(370608, "__name__", lambda: __name__) == '__main__':
    _l_(370618)


    _c_(370610, _n_(370609, "get_from_binance", lambda: get_from_binance))
    _l_(370611)
    _c_(370613, _n_(370612, "get_from_bittrex", lambda: get_from_bittrex))
    _l_(370614)
    _c_(370616, _n_(370615, "get_from_bitfinex", lambda: get_from_bitfinex))
    _l_(370617)