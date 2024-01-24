# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60715059/python-backtrader-error-filenotfounderror-errno-2-no-such-file-or-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(388561)

except ImportError:
    pass
try:
    import backtrader as bt
    _l_(388563)

except ImportError:
    pass

class SmaSignal(_a_(388565, _n_(388564, "bt", lambda: bt), "Signal")):
    _l_(388580)

    param = (('period', 20), )
    _l_(388566)

    def __init__(self):
        _l_(388579)

        _a_(388568, _n_(388567, "self", lambda: self), "lines").signal = _a_(388570, _n_(388569, "self", lambda: self), "data") - _c_(388577, _a_(388573, _a_(388572, _n_(388571, "bt", lambda: bt), "ind"), "SMA"), period=_a_(388576, _a_(388575, _n_(388574, "self", lambda: self), "p"), "period"))
        _l_(388578)

data = _c_(388588, _a_(388583, _a_(388582, _n_(388581, "bt", lambda: bt), "feeds"), "YahooFinanceData"), dataname='AAPL',
                                fromdate=_c_(388585, _n_(388584, "datetime", lambda: datetime), 2018, 1, 1),
                                todate=_c_(388587, _n_(388586, "datetime", lambda: datetime), 2018, 12, 31))
_l_(388589)
cerebro = _c_(388592, _a_(388591, _n_(388590, "bt", lambda: bt), "Cerebro"), stdstats=False)
_l_(388593)
_c_(388597, _a_(388595, _n_(388594, "cerebro", lambda: cerebro), "adddata"), _n_(388596, "data", lambda: data))
_l_(388598)
_c_(388602, _a_(388601, _a_(388600, _n_(388599, "cerebro", lambda: cerebro), "broker"), "setcash"), 1000.0)
_l_(388603)
_c_(388609, _a_(388605, _n_(388604, "cerebro", lambda: cerebro), "add_signal"), _a_(388607, _n_(388606, "bt", lambda: bt), "SIGNAL_LONG"), _n_(388608, "SmaSignal", lambda: SmaSignal))
_l_(388610)
_c_(388616, _a_(388612, _n_(388611, "cerebro", lambda: cerebro), "addobserver"), _a_(388615, _a_(388614, _n_(388613, "bt", lambda: bt), "observers"), "BuySell"))
_l_(388617)
_c_(388623, _a_(388619, _n_(388618, "cerebro", lambda: cerebro), "addobserver"), _a_(388622, _a_(388621, _n_(388620, "bt", lambda: bt), "observers"), "Value"))
_l_(388624)

_c_(388630, _n_(388625, "print", lambda: print), f'Starting Portfolio Value: {_c_(388629, _a_(388628, _a_(388627, _n_(388626, "cerebro", lambda: cerebro), "broker"), "getvalue")):.2f}')
_l_(388631)
_c_(388634, _a_(388633, _n_(388632, 'cerebro', lambda: cerebro), 'run'))
_l_(388635)
_c_(388641, _n_(388636, 'print', lambda: print), f'Final Portfolio Value: {_c_(388640, _a_(388639, _a_(388638, _n_(388637, "cerebro", lambda: cerebro), "broker"), "getvalue")):.2f}')
_l_(388642)
_c_(388645, _a_(388644, _n_(388643, 'cerebro', lambda: cerebro), 'plot'), iplot=True, volume=False)
_l_(388646)