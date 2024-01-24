# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53047366/typeerror-when-calling-resample-in-pandas
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas_datareader.data as web
    _l_(681452)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(681454)

except ImportError:
    pass
# removed imports related to plotting

TRAIN_SIZE = 0.2
_l_(681455)
FORECAST_STEPS = 20
_l_(681456)
STOCKS_PREDICT = ['SPY', 'AAPL']
_l_(681457)


def downloadData(startDate, endDate):
    _l_(681482)


    histPanel = _c_(681463, _a_(681459, _n_(681458, "web", lambda: web), "DataReader"), _n_(681460, "STOCKS_PREDICT", lambda: STOCKS_PREDICT), 'iex' , _n_(681461, "startDate", lambda: startDate), _n_(681462, "endDate", lambda: endDate))
    _l_(681464)
    contains_condition = _c_(681470, _a_(681469, (_c_(681467, _a_(681466, _n_(681465, "histPanel", lambda: histPanel), "isnull")) | (_n_(681468, "histPanel", lambda: histPanel) == 0)), "any"), axis=1)
    _l_(681471)
    to_keep = _a_(681474, _n_(681472, "contains_condition", lambda: contains_condition)[_n_(681473, "contains_condition", lambda: contains_condition) == False], "index")
    _l_(681475)
    histPanel = _a_(681477, _n_(681476, "histPanel", lambda: histPanel), "loc")[_n_(681478, "to_keep", lambda: to_keep)]
    _l_(681479)
    aux = _n_(681480, "histPanel", lambda: histPanel)
    _l_(681481)

    return aux


_c_(681486, _n_(681483, "print", lambda: print), _c_(681485, _n_(681484, "downloadData", lambda: downloadData), "01/01/2017","01/01/2019"))
_l_(681487)


def doForecast(Panel):
    _l_(681502)


    closeDF = _n_(681488, "Panel", lambda: Panel)['close']
    _l_(681489)
    ts = _n_(681490, "closeDF", lambda: closeDF)['SPY']
    _l_(681491)
    tsWeekly = _c_(681496, _a_(681495, _c_(681494, _a_(681493, _n_(681492, "ts", lambda: ts), "resample"), 'W-MON'), "last")) # TypeError here
    _l_(681497) # TypeError here
    values = _c_(681500, _a_(681499, _n_(681498, "tsWeekly", lambda: tsWeekly), "tolist"))
    _l_(681501)


def main():
    _l_(681519)

    startDate = _c_(681504, _n_(681503, "datetime", lambda: datetime), 2017, 1, 1)
    _l_(681505)
    endDate = _c_(681508, _a_(681507, _n_(681506, "datetime", lambda: datetime), "today"))
    _l_(681509)

    panel = _c_(681513, _n_(681510, "downloadData", lambda: downloadData), _n_(681511, "startDate", lambda: startDate), _n_(681512, "endDate", lambda: endDate))
    _l_(681514)

    _c_(681517, _n_(681515, "doForecast", lambda: doForecast), _n_(681516, "panel", lambda: panel))
    _l_(681518)


if _n_(681520, "__name__", lambda: __name__) == '__main__':
    _l_(681524)

    _c_(681522, _n_(681521, "main", lambda: main))
    _l_(681523)