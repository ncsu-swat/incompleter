# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73115690/converting-list-requested-from-api-to-dataframe-attributeerror-list-object-ha
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(597658)

except ImportError:
    pass
dates=[ '01-01-2021','01-04-2021','01-07-2021','01-10-2021',
        '01-01-2022','01-04-2022','01-07-2022']
_l_(597659)

# Convert your strings to datetime, using `datetime` library
dates = [_c_(597663, _a_(597661, _n_(597660, "datetime", lambda: datetime), "strptime"), _n_(597662, "date", lambda: date), "%d-%m-%Y") for date in _n_(597664, "dates", lambda: dates)]
_l_(597665)



def create_df(pair,dates):
    _l_(597726)

    df = []
    _l_(597666)
    for index, elem in _c_(597669, _n_(597667, "enumerate", lambda: enumerate), _n_(597668, "dates", lambda: dates)):
        _l_(597723)

        if _n_(597670, "index", lambda: index)== 0:
            _l_(597722)

            curr_date = _c_(597675, _n_(597671, "str", lambda: str), _c_(597674, _a_(597673, _n_(597672, "elem", lambda: elem), "timestamp")))
            _l_(597676)
            next_date = _c_(597682, _n_(597677, "str", lambda: str), _c_(597681, _a_(597680, _n_(597678, "dates", lambda: dates)[_n_(597679, "index", lambda: index)+1], "timestamp")))
            _l_(597683)
            df = _c_(597689, _a_(597685, _n_(597684, "client", lambda: client), "get_prices_intraday"), _n_(597686, "pair", lambda: pair), interval = '1m', from_ = _n_(597687, "curr_date", lambda: curr_date), to = _n_(597688, "next_date", lambda: next_date))
            _l_(597690)
        elif ((_n_(597691, "index", lambda: index)>0) & (_n_(597692, "index", lambda: index)+1 < _c_(597695, _n_(597693, "len", lambda: len), _n_(597694, "dates", lambda: dates)))):
            _l_(597721)

            curr_date = _c_(597700, _n_(597696, "str", lambda: str), _c_(597699, _a_(597698, _n_(597697, "elem", lambda: elem), "timestamp")))
            _l_(597701)
            next_date = _c_(597707, _n_(597702, "str", lambda: str), _c_(597706, _a_(597705, _n_(597703, "dates", lambda: dates)[_n_(597704, "index", lambda: index)+1], "timestamp")))
            _l_(597708)
            df2 = _c_(597714, _a_(597710, _n_(597709, "client", lambda: client), "get_prices_intraday"), _n_(597711, "pair", lambda: pair), interval = '1m', from_ = _n_(597712, "curr_date", lambda: curr_date), to = _n_(597713, "next_date", lambda: next_date))
            _l_(597715)
            _c_(597719, _a_(597717, _n_(597716, "df", lambda: df), "append"), _n_(597718, "df2", lambda: df2))
            _l_(597720)
    aux = _n_(597724, "df", lambda: df)
    _l_(597725)
    return aux
try:
    from eod import EodHistoricalData
    _l_(597728)

except ImportError:
    pass
# create the instance of the SDK
api_key = 'my_api_key'
_l_(597729)
client = _c_(597732, _n_(597730, "EodHistoricalData", lambda: EodHistoricalData), _n_(597731, "api_key", lambda: api_key))
_l_(597733)




GBPAUD = _c_(597736, _n_(597734, "create_df", lambda: create_df), 'GBPAUD.FOREX',_n_(597735, "dates", lambda: dates))
_l_(597737)