# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54514394/typeerror-normalize-argument-2-must-be-str-not-series-with-a-dataframe-of-st
# get date out of the index to column    
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df_news = _c_(344473, _a_(344472, _n_(344471, "df_news", lambda: df_news), "reset_index"))
_l_(344474)
# optional
_n_(344475, "df_news", lambda: df_news)['Date'] = _c_(344479, _a_(344477, _n_(344476, "pd", lambda: pd), "to_datetime"), _n_(344478, "df_news", lambda: df_news)['Date'])
_l_(344480)
# groupby and output group rows as list
df_news = _c_(344486, _a_(344484, _c_(344483, _a_(344482, _n_(344481, "df_news", lambda: df_news), "groupby"), 'Date')['name'], "apply"), _n_(344485, "list", lambda: list))
_l_(344487)
_c_(344490, _a_(344489, _n_(344488, "df_news", lambda: df_news), "head"))
_l_(344491)