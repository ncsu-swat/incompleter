# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56574188/python-3-how-to-fix-filenotfounderror-errno-2-no-such-file-or-directory
##Working Code:
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class backtest:
    _l_(673040)


    def __init__(self, ticker):
        _l_(673039)


        start = '1/3/2000'
        _l_(672994)
        end = '1/3/2019'
        _l_(672995)
        sdate = _c_(672999, _a_(672997, _n_(672996, "pd", lambda: pd), "to_datetime"), _n_(672998, "start", lambda: start))
        _l_(673000)
        edate = _c_(673004, _a_(673002, _n_(673001, "pd", lambda: pd), "to_datetime"), _n_(673003, "end", lambda: end))
        _l_(673005)


        if _c_(673014, _a_(673008, _a_(673007, _n_(673006, "os", lambda: os), "path"), "islink"), _c_(673013, _a_(673009, '{}_{}_to_{}.csv', "format"), _n_(673010, "ticker", lambda: ticker), _n_(673011, "start", lambda: start), _n_(673012, "end", lambda: end))) == True:
            _l_(673038)

            _n_(673015, "self", lambda: self).df = _c_(673023, _a_(673017, _n_(673016, "pd", lambda: pd), "read_csv"), _c_(673022, _a_(673018, '{}_{}_to_{}.csv', "format"), _n_(673019, "ticker", lambda: ticker), _n_(673020, "start", lambda: start), _n_(673021, "end", lambda: end)), parse_dates=True)
            _l_(673024)

        else:
            ##Failed attempt 1
            ##self.filename = '{}_{}_to_{}.csv'.format(ticker, start, end)
            ##self.df.to_csv(self.filename)

            ##Failed attempt 2
            ##self.filename = str(ticker) + '_' + start + '_to_' + end + '.csv'            
            ##self.df.to_csv(self.filename)

            _n_(673025, "self", lambda: self).df = _c_(673031, _a_(673027, _n_(673026, "web", lambda: web), "DataReader"), _n_(673028, "ticker", lambda: ticker), 'yahoo', _n_(673029, "sdate", lambda: sdate), _n_(673030, "edate", lambda: edate))
            _l_(673032)
            _c_(673036, _a_(673035, _a_(673034, _n_(673033, "self", lambda: self), "df"), "to_csv"), 'amzn_1/3/2000_to_1/3/19.csv')
            _l_(673037)



amzn = _c_(673042, _n_(673041, "backtest", lambda: backtest), 'amzn')
_l_(673043)
_c_(673049, _n_(673044, "print", lambda: print), _c_(673048, _a_(673047, _a_(673046, _n_(673045, "amzn", lambda: amzn), "df"), "head"), 1))
_l_(673050)