# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74253559/python-3-9-caused-typeerror-int-argument-must-be-a-string-a-bytes-like-objec
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
_l_(542736)
headers = {'User-Agent': _n_(542737, "agent", lambda: agent)}
_l_(542738)
query = _c_(542741, _a_(542740, _n_(542739, "requests", lambda: requests), "get"), 'https://query1.finance.yahoo.com/v7/finance/quote?symbols=AALI.JK')
_l_(542742)
data = _c_(542745, _a_(542744, _n_(542743, "query", lambda: query), "json"))
_l_(542746)
data = _c_(542750, _a_(542748, _n_(542747, "pd", lambda: pd), "DataFrame"), _n_(542749, "data", lambda: data)['quoteResponse']['result'])
_l_(542751)
_n_(542752, "data", lambda: data)['regularMarketTime']= _c_(542759, _a_(542758, _a_(542757, _c_(542756, _a_(542754, _n_(542753, "pd", lambda: pd), "to_datetime"), _n_(542755, "data", lambda: data)['regularMarketTime'],unit='s'), "dt"), "strftime"), "%Y-%m-%d")
_l_(542760)
data = _n_(542761, "data", lambda: data)[['regularMarketTime','symbol','regularMarketOpen','regularMarketDayHigh','regularMarketDayLow','regularMarketPrice','regularMarketVolume']]
_l_(542762)
_c_(542766, _a_(542764, _n_(542763, "data_append", lambda: data_append), "append"), _n_(542765, "data", lambda: data))
_l_(542767)