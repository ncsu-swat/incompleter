# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46995307/attributeerror-in-python-static-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime as dt
    _l_(408334)

except ImportError:
    pass
try:
    from helpers import str2date
    _l_(408336)

except ImportError:
    pass
try:
    from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, nearest_workday, \
    USMartinLutherKingJr, USPresidentsDay, GoodFriday, USMemorialDay, \
    USLaborDay, USThanksgivingDay
    _l_(408338)

except ImportError:
    pass


class USTradingCalendar(_n_(408339, "AbstractHolidayCalendar", lambda: AbstractHolidayCalendar)):
    _l_(408370)

    rules = [
        _c_(408342, _n_(408340, "Holiday", lambda: Holiday), 'NewYearsDay', month=1, day=1, observance=_n_(408341, "nearest_workday", lambda: nearest_workday)),
        _n_(408343, "USMartinLutherKingJr", lambda: USMartinLutherKingJr),
        _n_(408344, "USPresidentsDay", lambda: USPresidentsDay),
        _n_(408345, "GoodFriday", lambda: GoodFriday),
        _n_(408346, "USMemorialDay", lambda: USMemorialDay),
        _c_(408349, _n_(408347, "Holiday", lambda: Holiday), 'USIndependenceDay', month=7, day=4, observance=_n_(408348, "nearest_workday", lambda: nearest_workday)),
        _n_(408350, "USLaborDay", lambda: USLaborDay),
        _n_(408351, "USThanksgivingDay", lambda: USThanksgivingDay),
        _c_(408354, _n_(408352, "Holiday", lambda: Holiday), 'Christmas', month=12, day=25, observance=_n_(408353, "nearest_workday", lambda: nearest_workday))
    ]
    _l_(408355)


    @_n_(408356, "classmethod", lambda: classmethod)
    def get_trading_close_holidays(cls, year):
        _l_(408369)

        aux = _c_(408367, _a_(408358, _n_(408357, "cls", lambda: cls), "holidays"), _c_(408362, _a_(408360, _n_(408359, "dt", lambda: dt), "datetime"), _n_(408361, "year", lambda: year)-1, 12, 31), _c_(408366, _a_(408364, _n_(408363, "dt", lambda: dt), "datetime"), _n_(408365, "year", lambda: year), 12, 31))
        _l_(408368)
        return aux



if _n_(408371, "__name__", lambda: __name__) == '__main__':
    _l_(408378)

    _c_(408376, _n_(408372, "print", lambda: print), _c_(408375, _a_(408374, _n_(408373, "USTradingCalendar", lambda: USTradingCalendar), "get_trading_close_holidays"), 2016))
    _l_(408377)