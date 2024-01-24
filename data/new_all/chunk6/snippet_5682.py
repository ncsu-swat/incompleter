# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70636568/when-executing-the-program-it-gives-an-error-typeerror-list-indices-must-be-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(340404)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(340406)

except ImportError:
    pass

def get_from_binance():
    _l_(340426)


    req = _c_(340409, _a_(340408, _n_(340407, "requests", lambda: requests), "get"), "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    _l_(340410)
    response = _c_(340413, _a_(340412, _n_(340411, "req", lambda: req), "json"))
    _l_(340414)
    sell_price = _n_(340415, "response", lambda: response)["price"]
    _l_(340416)
    _c_(340424, _n_(340417, "print", lambda: print), f"{_c_(340422, _a_(340421, _c_(340420, _a_(340419, _n_(340418, 'datetime', lambda: datetime), 'now')), 'strftime'), '%Y-%m-%d %H:%M:%S')}\nBTC Binance: {_n_(340423, 'sell_price', lambda: sell_price)}")
    _l_(340425)


def get_from_bittrex():
    _l_(340441)


    req2 = _c_(340429, _a_(340428, _n_(340427, "requests", lambda: requests), "get"), "https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC")
    _l_(340430)
    response2 = _c_(340433, _a_(340432, _n_(340431, "req2", lambda: req2), "json"))
    _l_(340434)
    sell_price2 = _n_(340435, "response2", lambda: response2)["result"]['Last']
    _l_(340436)
    _c_(340439, _n_(340437, "print", lambda: print), f"BTC Bittrex: {_n_(340438, 'sell_price2', lambda: sell_price2)}")
    _l_(340440)


def get_from_bitfinex():
    _l_(340456)


    req3 = _c_(340444, _a_(340443, _n_(340442, "requests", lambda: requests), "get"), "https://api-pub.bitfinex.com/v2/tickers?symbols=tBTCUSD")
    _l_(340445)
    response3 = _c_(340448, _a_(340447, _n_(340446, "req3", lambda: req3), "json"))
    _l_(340449)
    sell_price3 = _n_(340450, "response3", lambda: response3)["0"]["1"]
    _l_(340451)
    _c_(340454, _n_(340452, "print", lambda: print), f"BTC bitfinex: {_n_(340453, 'sell_price3', lambda: sell_price3)}")
    _l_(340455)


if _n_(340457, "__name__", lambda: __name__) == '__main__':
    _l_(340467)


    _c_(340459, _n_(340458, "get_from_binance", lambda: get_from_binance))
    _l_(340460)
    _c_(340462, _n_(340461, "get_from_bittrex", lambda: get_from_bittrex))
    _l_(340463)
    _c_(340465, _n_(340464, "get_from_bitfinex", lambda: get_from_bitfinex))
    _l_(340466)