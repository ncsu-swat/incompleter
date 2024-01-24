# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54514394/typeerror-normalize-argument-2-must-be-str-not-series-with-a-dataframe-of-st
# get date out of the index to column    
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df_news = _c_(350315, _a_(350314, _n_(350313, "df_news", lambda: df_news), "reset_index"))
_l_(350316)
# optional
_n_(350317, "df_news", lambda: df_news)['Date'] = _c_(350321, _a_(350319, _n_(350318, "pd", lambda: pd), "to_datetime"), _n_(350320, "df_news", lambda: df_news)['Date'])
_l_(350322)
# groupby and output group rows as list
df_news = _c_(350328, _a_(350326, _c_(350325, _a_(350324, _n_(350323, "df_news", lambda: df_news), "groupby"), 'Date')['name'], "apply"), _n_(350327, "list", lambda: list))
_l_(350329)
_c_(350332, _a_(350331, _n_(350330, "df_news", lambda: df_news), "head"))
_l_(350333)