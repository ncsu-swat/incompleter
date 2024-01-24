# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56574188/python-3-how-to-fix-filenotfounderror-errno-2-no-such-file-or-directory
##Working Code:
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class backtest:
    _l_(705288)


    def __init__(self, ticker):
        _l_(705287)


        start = '1/3/2000'
        _l_(705242)
        end = '1/3/2019'
        _l_(705243)
        sdate = _c_(705247, _a_(705245, _n_(705244, "pd", lambda: pd), "to_datetime"), _n_(705246, "start", lambda: start))
        _l_(705248)
        edate = _c_(705252, _a_(705250, _n_(705249, "pd", lambda: pd), "to_datetime"), _n_(705251, "end", lambda: end))
        _l_(705253)


        if _c_(705262, _a_(705256, _a_(705255, _n_(705254, "os", lambda: os), "path"), "islink"), _c_(705261, _a_(705257, '{}_{}_to_{}.csv', "format"), _n_(705258, "ticker", lambda: ticker), _n_(705259, "start", lambda: start), _n_(705260, "end", lambda: end))) == True:
            _l_(705286)

            _n_(705263, "self", lambda: self).df = _c_(705271, _a_(705265, _n_(705264, "pd", lambda: pd), "read_csv"), _c_(705270, _a_(705266, '{}_{}_to_{}.csv', "format"), _n_(705267, "ticker", lambda: ticker), _n_(705268, "start", lambda: start), _n_(705269, "end", lambda: end)), parse_dates=True)
            _l_(705272)

        else:
            ##Failed attempt 1
            ##self.filename = '{}_{}_to_{}.csv'.format(ticker, start, end)
            ##self.df.to_csv(self.filename)

            ##Failed attempt 2
            ##self.filename = str(ticker) + '_' + start + '_to_' + end + '.csv'            
            ##self.df.to_csv(self.filename)

            _n_(705273, "self", lambda: self).df = _c_(705279, _a_(705275, _n_(705274, "web", lambda: web), "DataReader"), _n_(705276, "ticker", lambda: ticker), 'yahoo', _n_(705277, "sdate", lambda: sdate), _n_(705278, "edate", lambda: edate))
            _l_(705280)
            _c_(705284, _a_(705283, _a_(705282, _n_(705281, "self", lambda: self), "df"), "to_csv"), 'amzn_1/3/2000_to_1/3/19.csv')
            _l_(705285)



amzn = _c_(705290, _n_(705289, "backtest", lambda: backtest), 'amzn')
_l_(705291)
_c_(705297, _n_(705292, "print", lambda: print), _c_(705296, _a_(705295, _a_(705294, _n_(705293, "amzn", lambda: amzn), "df"), "head"), 1))
_l_(705298)