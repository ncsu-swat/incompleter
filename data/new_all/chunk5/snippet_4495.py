# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56574188/python-3-how-to-fix-filenotfounderror-errno-2-no-such-file-or-directory
##Working Code:
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class backtest:
    _l_(675375)


    def __init__(self, ticker):
        _l_(675374)


        start = '1/3/2000'
        _l_(675329)
        end = '1/3/2019'
        _l_(675330)
        sdate = _c_(675334, _a_(675332, _n_(675331, "pd", lambda: pd), "to_datetime"), _n_(675333, "start", lambda: start))
        _l_(675335)
        edate = _c_(675339, _a_(675337, _n_(675336, "pd", lambda: pd), "to_datetime"), _n_(675338, "end", lambda: end))
        _l_(675340)


        if _c_(675349, _a_(675343, _a_(675342, _n_(675341, "os", lambda: os), "path"), "islink"), _c_(675348, _a_(675344, '{}_{}_to_{}.csv', "format"), _n_(675345, "ticker", lambda: ticker), _n_(675346, "start", lambda: start), _n_(675347, "end", lambda: end))) == True:
            _l_(675373)

            _n_(675350, "self", lambda: self).df = _c_(675358, _a_(675352, _n_(675351, "pd", lambda: pd), "read_csv"), _c_(675357, _a_(675353, '{}_{}_to_{}.csv', "format"), _n_(675354, "ticker", lambda: ticker), _n_(675355, "start", lambda: start), _n_(675356, "end", lambda: end)), parse_dates=True)
            _l_(675359)

        else:
            ##Failed attempt 1
            ##self.filename = '{}_{}_to_{}.csv'.format(ticker, start, end)
            ##self.df.to_csv(self.filename)

            ##Failed attempt 2
            ##self.filename = str(ticker) + '_' + start + '_to_' + end + '.csv'            
            ##self.df.to_csv(self.filename)

            _n_(675360, "self", lambda: self).df = _c_(675366, _a_(675362, _n_(675361, "web", lambda: web), "DataReader"), _n_(675363, "ticker", lambda: ticker), 'yahoo', _n_(675364, "sdate", lambda: sdate), _n_(675365, "edate", lambda: edate))
            _l_(675367)
            _c_(675371, _a_(675370, _a_(675369, _n_(675368, "self", lambda: self), "df"), "to_csv"), 'amzn_1/3/2000_to_1/3/19.csv')
            _l_(675372)



amzn = _c_(675377, _n_(675376, "backtest", lambda: backtest), 'amzn')
_l_(675378)
_c_(675384, _n_(675379, "print", lambda: print), _c_(675383, _a_(675382, _a_(675381, _n_(675380, "amzn", lambda: amzn), "df"), "head"), 1))
_l_(675385)