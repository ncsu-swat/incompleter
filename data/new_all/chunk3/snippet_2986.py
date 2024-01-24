# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55887818/dataframe-operation-typeerror-cannot-convert-the-series-to-class-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df  = _c_(557560, _a_(557559, _n_(557558, "pd", lambda: pd), "DataFrame"), [["Gothenburg", "2018-01-05", "jan", 1.5, 2.3, 107],
 ["Gothenburg", "2018-01-15", "jan", 1.3, 3.3, 96],
 ["Hallsberg", "2018-02-14", "feb", 2.2, 2.3, 168],
 ["Gothenburg", "2018-03-05", "mar", 1.5, 2.1, 96],
 ["Hallsberg", "2018-01-25", "jan", 2.5, 2.3, 87],
 ["Malmo", "2018-01-02", "jan", 1.6, 2.3, 104],
 ["Gothenburg", "2018-03-05", "mar", 1.9, 2.8, 102],
 ["Malmo", "2018-03-05", "mar", 0.7, 4.3, 151],
 ["Gothenburg", "2018-01-25", "jan", 1.7, 3.2, 45],
 ["Malmo", "2018-03-25", "mar", 1.0, 3.3, 98],
 ["Hallsberg", "2018-03-06", "mar", 3.7, 2.3, 142],
 ["Malmo", "2018-01-10", "jan", 1.0, 2.9, 112],
 ["Hallsberg", "2018-04-29", "apr", 2.7, 2.3, 100]])
_l_(557561)

_n_(557562, "df", lambda: df).columns = ['City', 'Date', 'Month', 'Mean1', 'Mean2', 'Mean3']
_l_(557563)

_n_(557564, "df", lambda: df)["Val1"] = _c_(557568, _a_(557566, _n_(557565, "math", lambda: math), "exp"), -_n_(557567, "df", lambda: df)["Mean1"])
_l_(557569)

_c_(557572, _n_(557570, "print", lambda: print), _n_(557571, "df", lambda: df))
_l_(557573)