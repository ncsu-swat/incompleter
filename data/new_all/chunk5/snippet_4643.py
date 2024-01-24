# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53047366/typeerror-when-calling-resample-in-pandas
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas_datareader.data as web
    _l_(682286)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(682288)

except ImportError:
    pass
# removed imports related to plotting

TRAIN_SIZE = 0.2
_l_(682289)
FORECAST_STEPS = 20
_l_(682290)
STOCKS_PREDICT = ['SPY', 'AAPL']
_l_(682291)


def downloadData(startDate, endDate):
    _l_(682316)


    histPanel = _c_(682297, _a_(682293, _n_(682292, "web", lambda: web), "DataReader"), _n_(682294, "STOCKS_PREDICT", lambda: STOCKS_PREDICT), 'iex' , _n_(682295, "startDate", lambda: startDate), _n_(682296, "endDate", lambda: endDate))
    _l_(682298)
    contains_condition = _c_(682304, _a_(682303, (_c_(682301, _a_(682300, _n_(682299, "histPanel", lambda: histPanel), "isnull")) | (_n_(682302, "histPanel", lambda: histPanel) == 0)), "any"), axis=1)
    _l_(682305)
    to_keep = _a_(682308, _n_(682306, "contains_condition", lambda: contains_condition)[_n_(682307, "contains_condition", lambda: contains_condition) == False], "index")
    _l_(682309)
    histPanel = _a_(682311, _n_(682310, "histPanel", lambda: histPanel), "loc")[_n_(682312, "to_keep", lambda: to_keep)]
    _l_(682313)
    aux = _n_(682314, "histPanel", lambda: histPanel)
    _l_(682315)

    return aux


_c_(682320, _n_(682317, "print", lambda: print), _c_(682319, _n_(682318, "downloadData", lambda: downloadData), "01/01/2017","01/01/2019"))
_l_(682321)


def doForecast(Panel):
    _l_(682336)


    closeDF = _n_(682322, "Panel", lambda: Panel)['close']
    _l_(682323)
    ts = _n_(682324, "closeDF", lambda: closeDF)['SPY']
    _l_(682325)
    tsWeekly = _c_(682330, _a_(682329, _c_(682328, _a_(682327, _n_(682326, "ts", lambda: ts), "resample"), 'W-MON'), "last")) # TypeError here
    _l_(682331) # TypeError here
    values = _c_(682334, _a_(682333, _n_(682332, "tsWeekly", lambda: tsWeekly), "tolist"))
    _l_(682335)


def main():
    _l_(682353)

    startDate = _c_(682338, _n_(682337, "datetime", lambda: datetime), 2017, 1, 1)
    _l_(682339)
    endDate = _c_(682342, _a_(682341, _n_(682340, "datetime", lambda: datetime), "today"))
    _l_(682343)

    panel = _c_(682347, _n_(682344, "downloadData", lambda: downloadData), _n_(682345, "startDate", lambda: startDate), _n_(682346, "endDate", lambda: endDate))
    _l_(682348)

    _c_(682351, _n_(682349, "doForecast", lambda: doForecast), _n_(682350, "panel", lambda: panel))
    _l_(682352)


if _n_(682354, "__name__", lambda: __name__) == '__main__':
    _l_(682358)

    _c_(682356, _n_(682355, "main", lambda: main))
    _l_(682357)