# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71321015/attributeerror-dataframe-object-has-no-attribute-get-data-yahoo-i-am-gett
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import copy
    _l_(587361)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(587363)

except ImportError:
    pass
try:
    import talib
    _l_(587365)

except ImportError:
    pass
try:
    import yfinance as yf
    _l_(587367)

except ImportError:
    pass

_c_(587370, _a_(587369, _n_(587368, "pd", lambda: pd), "set_option"), "display.max_rows", None)
_l_(587371)
_c_(587374, _a_(587373, _n_(587372, "pd", lambda: pd), "set_option"), "display.max_columns", None)
_l_(587375)
_c_(587378, _a_(587377, _n_(587376, "pd", lambda: pd), "set_option"), "display.width", None)
_l_(587379)
try:
    from pandas_datareader import data as pdr
    _l_(587381)

except ImportError:
    pass

_c_(587384, _a_(587383, _n_(587382, "yf", lambda: yf), "pdr_override"))
_l_(587385)


def symbol_back_test(symbol):
    _l_(587501)

    global pdr
    _l_(587386)
    pdr = _c_(587390, _a_(587388, _n_(587387, "pdr", lambda: pdr), "get_data_yahoo"), _n_(587389, "symbol", lambda: symbol), period="2y", interval="1d")
    _l_(587391)

    _n_(587392, "pdr", lambda: pdr)["MA_10"] = _c_(587396, _a_(587394, _n_(587393, "talib", lambda: talib), "MA"), _n_(587395, "pdr", lambda: pdr)["Close"], timeperiod=10)
    _l_(587397)
    _n_(587398, "pdr", lambda: pdr)["MA_50"] = _c_(587402, _a_(587400, _n_(587399, "talib", lambda: talib), "MA"), _n_(587401, "pdr", lambda: pdr)["Close"], timeperiod=50)
    _l_(587403)
    _n_(587404, "pdr", lambda: pdr)["RSI_14"] = _c_(587408, _a_(587406, _n_(587405, "talib", lambda: talib), "RSI"), _n_(587407, "pdr", lambda: pdr)["Close"], timeperiod=14)
    _l_(587409)

    position = None
    _l_(587410)
    symbol_trades = []
    _l_(587411)
    trade = {"Symbol": None, "Buy/Sell": None, "Entry": None, "Entry Date": None, "Exit": None, "Exit Date": None}
    _l_(587412)

    for i in _a_(587414, _n_(587413, "pdr", lambda: pdr), "index")[49:]:
        _l_(587498)


        if _n_(587415, "pdr", lambda: pdr)["MA_10"][_n_(587416, "i", lambda: i)] > _n_(587417, "pdr", lambda: pdr)["MA_50"][_n_(587418, "i", lambda: i)] and _n_(587419, "pdr", lambda: pdr)["RSI_14"][_n_(587420, "i", lambda: i)] > 50 and _n_(587421, "position", lambda: position) != "Buy":
            _l_(587454)

            if _n_(587422, "trade", lambda: trade)["Symbol"] is not None:
                _l_(587438)

                _n_(587423, "trade", lambda: trade)["Exit"] = _n_(587424, "pdr", lambda: pdr)["Close"][_n_(587425, "i", lambda: i)]
                _l_(587426)
                _n_(587427, "trade", lambda: trade)["Exit Date"] = _n_(587428, "i", lambda: i)
                _l_(587429)
                _c_(587436, _a_(587431, _n_(587430, "symbol_trades", lambda: symbol_trades), "append"), _c_(587435, _a_(587433, _n_(587432, "copy", lambda: copy), "deepcopy"), _n_(587434, "trade", lambda: trade)))
                _l_(587437)
            if _n_(587439, "position", lambda: position) is not None:
                _l_(587452)

                _n_(587440, "trade", lambda: trade)["Symbol"] = _n_(587441, "symbol", lambda: symbol)
                _l_(587442)
                _n_(587443, "trade", lambda: trade)["Buy/Sell"] = "Buy"
                _l_(587444)
                _n_(587445, "trade", lambda: trade)["Entry"] = _n_(587446, "pdr", lambda: pdr)["Close"][_n_(587447, "i", lambda: i)]
                _l_(587448)
                _n_(587449, "trade", lambda: trade)["Entry Date"] = _n_(587450, "i", lambda: i)
                _l_(587451)

            position = "Buy"
            _l_(587453)
        if _n_(587455, "pdr", lambda: pdr)["MA_10"][_n_(587456, "i", lambda: i)] < _n_(587457, "pdr", lambda: pdr)["MA_50"][_n_(587458, "i", lambda: i)] and _n_(587459, "pdr", lambda: pdr)["RSI_14"][_n_(587460, "i", lambda: i)] < 50 and _n_(587461, "position", lambda: position) != "Sell":
            _l_(587497)

            if _n_(587462, "trade", lambda: trade)["Symbol"] is not None:
                _l_(587478)

                _n_(587463, "trade", lambda: trade)["Exit"] = _n_(587464, "pdr", lambda: pdr)["Close"][_n_(587465, "i", lambda: i)]
                _l_(587466)
                _n_(587467, "trade", lambda: trade)["Exit Date"] = _n_(587468, "i", lambda: i)
                _l_(587469)
                _c_(587476, _a_(587471, _n_(587470, "symbol_trades", lambda: symbol_trades), "append"), _c_(587475, _a_(587473, _n_(587472, "copy", lambda: copy), "deepcopy"), _n_(587474, "trade", lambda: trade)))
                _l_(587477)
            if _n_(587479, "position", lambda: position) is not None:
                _l_(587492)

                _n_(587480, "trade", lambda: trade)["Symbol"] = _n_(587481, "symbol", lambda: symbol)
                _l_(587482)
                _n_(587483, "trade", lambda: trade)["Buy/Sell"] = "Sell"
                _l_(587484)
                _n_(587485, "trade", lambda: trade)["Entry"] = _n_(587486, "pdr", lambda: pdr)["Close"][_n_(587487, "i", lambda: i)]
                _l_(587488)
                _n_(587489, "trade", lambda: trade)["Entry Date"] = _n_(587490, "i", lambda: i)
                _l_(587491)

            _c_(587494, _n_(587493, "print", lambda: print), "Sell")
            _l_(587495)
            position = "Sell"
            _l_(587496)
    aux = _n_(587499, "symbol_trades", lambda: symbol_trades)
    _l_(587500)
    return aux


symbol_list = ["INFY.NS"]
_l_(587502)
for symbol in _n_(587503, "symbol_list", lambda: symbol_list):
    _l_(587510)

    _c_(587508, _n_(587504, "print", lambda: print), _c_(587507, _n_(587505, "symbol_back_test", lambda: symbol_back_test), _n_(587506, "symbol", lambda: symbol)))
    _l_(587509)