# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54514394/typeerror-normalize-argument-2-must-be-str-not-series-with-a-dataframe-of-st
# get date out of the index to column    
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df_news = _c_(369279, _a_(369278, _n_(369277, "df_news", lambda: df_news), "reset_index"))
_l_(369280)
# optional
_n_(369281, "df_news", lambda: df_news)['Date'] = _c_(369285, _a_(369283, _n_(369282, "pd", lambda: pd), "to_datetime"), _n_(369284, "df_news", lambda: df_news)['Date'])
_l_(369286)
# groupby and output group rows as list
df_news = _c_(369292, _a_(369290, _c_(369289, _a_(369288, _n_(369287, "df_news", lambda: df_news), "groupby"), 'Date')['name'], "apply"), _n_(369291, "list", lambda: list))
_l_(369293)
_c_(369296, _a_(369295, _n_(369294, "df_news", lambda: df_news), "head"))
_l_(369297)