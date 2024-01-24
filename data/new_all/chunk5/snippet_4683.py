# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53047366/typeerror-when-calling-resample-in-pandas
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas_datareader.data as web
    _l_(677279)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(677281)

except ImportError:
    pass
# removed imports related to plotting

TRAIN_SIZE = 0.2
_l_(677282)
FORECAST_STEPS = 20
_l_(677283)
STOCKS_PREDICT = ['SPY', 'AAPL']
_l_(677284)


def downloadData(startDate, endDate):
    _l_(677309)


    histPanel = _c_(677290, _a_(677286, _n_(677285, "web", lambda: web), "DataReader"), _n_(677287, "STOCKS_PREDICT", lambda: STOCKS_PREDICT), 'iex' , _n_(677288, "startDate", lambda: startDate), _n_(677289, "endDate", lambda: endDate))
    _l_(677291)
    contains_condition = _c_(677297, _a_(677296, (_c_(677294, _a_(677293, _n_(677292, "histPanel", lambda: histPanel), "isnull")) | (_n_(677295, "histPanel", lambda: histPanel) == 0)), "any"), axis=1)
    _l_(677298)
    to_keep = _a_(677301, _n_(677299, "contains_condition", lambda: contains_condition)[_n_(677300, "contains_condition", lambda: contains_condition) == False], "index")
    _l_(677302)
    histPanel = _a_(677304, _n_(677303, "histPanel", lambda: histPanel), "loc")[_n_(677305, "to_keep", lambda: to_keep)]
    _l_(677306)
    aux = _n_(677307, "histPanel", lambda: histPanel)
    _l_(677308)

    return aux


_c_(677313, _n_(677310, "print", lambda: print), _c_(677312, _n_(677311, "downloadData", lambda: downloadData), "01/01/2017","01/01/2019"))
_l_(677314)


def doForecast(Panel):
    _l_(677329)


    closeDF = _n_(677315, "Panel", lambda: Panel)['close']
    _l_(677316)
    ts = _n_(677317, "closeDF", lambda: closeDF)['SPY']
    _l_(677318)
    tsWeekly = _c_(677323, _a_(677322, _c_(677321, _a_(677320, _n_(677319, "ts", lambda: ts), "resample"), 'W-MON'), "last")) # TypeError here
    _l_(677324) # TypeError here
    values = _c_(677327, _a_(677326, _n_(677325, "tsWeekly", lambda: tsWeekly), "tolist"))
    _l_(677328)


def main():
    _l_(677346)

    startDate = _c_(677331, _n_(677330, "datetime", lambda: datetime), 2017, 1, 1)
    _l_(677332)
    endDate = _c_(677335, _a_(677334, _n_(677333, "datetime", lambda: datetime), "today"))
    _l_(677336)

    panel = _c_(677340, _n_(677337, "downloadData", lambda: downloadData), _n_(677338, "startDate", lambda: startDate), _n_(677339, "endDate", lambda: endDate))
    _l_(677341)

    _c_(677344, _n_(677342, "doForecast", lambda: doForecast), _n_(677343, "panel", lambda: panel))
    _l_(677345)


if _n_(677347, "__name__", lambda: __name__) == '__main__':
    _l_(677351)

    _c_(677349, _n_(677348, "main", lambda: main))
    _l_(677350)