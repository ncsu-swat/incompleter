# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46673298/python-attributeerror-stock-analysis-object-has-no-attribute-stock-data
#! /usr/bin/python3
# -*- coding: utf-8 -*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pandas_datareader import data as pdr
    _l_(568719)

except ImportError:
    pass
try:
    import quandl
    _l_(568721)

except ImportError:
    pass

class Stock_Analysis:
    _l_(568763)

    def __init__(self, Stock_Ticker,Start_Date):
        _l_(568756)

        _n_(568722, "self", lambda: self).ticker = _n_(568723, "Stock_Ticker", lambda: Stock_Ticker)
        _l_(568724)
        _n_(568725, "self", lambda: self).start_date = _n_(568726, "Start_Date", lambda: Start_Date)
        _l_(568727)
        try:
            _l_(568755)

            _n_(568728, "self", lambda: self).stock_data = _c_(568735, _a_(568730, _n_(568729, "pdr", lambda: pdr), "get_data_yahoo"), _a_(568732, _n_(568731, "self", lambda: self), "ticker"),_a_(568734, _n_(568733, "self", lambda: self), "start_date"))
            _l_(568736)
        except:
            _l_(568754)

            _c_(568738, _n_(568737, "print", lambda: print), "Error with Yahoo - please enter Quandl Tickers")
            _l_(568739)
            try:
                _l_(568753)

                _n_(568740, "self", lambda: self).quandl_ticker = _c_(568742, _n_(568741, "input", lambda: input))
                _l_(568743)
                _n_(568744, "self", lambda: self).stock_data = _c_(568749, _a_(568746, _n_(568745, "quandl", lambda: quandl), "get"), _a_(568748, _n_(568747, "self", lambda: self), "quandl_ticker"))
                _l_(568750)
            except:
                _l_(568752)

                "Failled"
                _l_(568751)
    def Print_Data(self):
        _l_(568762)

        _c_(568760, _n_(568757, "print", lambda: print), _a_(568759, _n_(568758, "self", lambda: self), "stock_data"))
        _l_(568761)

apple = _c_(568765, _n_(568764, "Stock_Analysis", lambda: Stock_Analysis), "AAPL","2015-01-01")
_l_(568766)
_c_(568769, _a_(568768, _n_(568767, "apple", lambda: apple), "Print_Data"))
_l_(568770)