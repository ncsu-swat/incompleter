# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75026826/attributeerror-tuple-object-has-no-attribute-symbol-when-downloading-stock
# Define chunk of symbols to download with every server call.
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
symbols=['AMD', 'MSFT', 'NVDA', 'TOVX']
_l_(342572)
chunk_size = 2
_l_(342573)
for i in _c_(342581, _n_(342574, "tqdm", lambda: tqdm), _c_(342580, _n_(342575, "range", lambda: range), 0, _c_(342578, _n_(342576, "len", lambda: len), _n_(342577, "symbols", lambda: symbols)), _n_(342579, "chunk_size", lambda: chunk_size)), desc='Downloading daily Data'):
    _l_(342626)

    symbol_chunk = _n_(342582, "symbols", lambda: symbols)[_n_(342583, "i", lambda: i):_n_(342584, "i", lambda: i) + _n_(342585, "chunk_size", lambda: chunk_size)]
    _l_(342586)
    # Downloading 1D time-frame data...
    request_parameters = _c_(342594, _n_(342587, "StockBarsRequest", lambda: StockBarsRequest), symbol_or_symbols=_n_(342588, "symbol_chunk", lambda: symbol_chunk),
                    timeframe=_a_(342590, _n_(342589, "TimeFrame", lambda: TimeFrame), "Day"),
                    start=_c_(342593, _a_(342592, _n_(342591, "datetime", lambda: datetime), "strptime"), "2022-01-01", '%Y-%m-%d'),
                    end=None,
                    adjustment='raw'
             )
    _l_(342595)
    daily_bars = _c_(342599, _a_(342597, _n_(342596, "client", lambda: client), "get_stock_bars"), _n_(342598, "request_parameters", lambda: request_parameters))
    _l_(342600)
    for bar in _n_(342601, "daily_bars", lambda: daily_bars):
        _l_(342625)

        stock_id = _n_(342602, "symbol_dic", lambda: symbol_dic)[_a_(342604, _n_(342603, "bar", lambda: bar), "symbol")]
        _l_(342605)
        _c_(342623, _a_(342607, _n_(342606, "cursor", lambda: cursor), "execute"), """INSERT INTO alpaca_stock_prices_1D (stock_id, date, open, high, low, close, volume)
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
                       (_n_(342608, "stock_id", lambda: stock_id), _c_(342612, _a_(342611, _a_(342610, _n_(342609, "bar", lambda: bar), "timestamp"), "date")), _a_(342614, _n_(342613, "bar", lambda: bar), "open"), _a_(342616, _n_(342615, "bar", lambda: bar), "high"), _a_(342618, _n_(342617, "bar", lambda: bar), "low"), _a_(342620, _n_(342619, "bar", lambda: bar), "close"), _a_(342622, _n_(342621, "bar", lambda: bar), "volume")))
        _l_(342624)