# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62732790/apply-a-function-to-columns-in-pandas-raises-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def _replace_datetime_with_datetime_pub(news_dataframe):
    _l_(568358)

    _n_(568341, "news_dataframe", lambda: news_dataframe).dateTime = _c_(568350, _a_(568343, _n_(568342, "np", lambda: np), "where"), _a_(568345, _n_(568344, "news_dataframe", lambda: news_dataframe), "dateTimePub"), _a_(568347, _n_(568346, "news_dataframe", lambda: news_dataframe), "dateTimePub"), _a_(568349, _n_(568348, "news_dataframe", lambda: news_dataframe), "dateTime"))
    _l_(568351)
    aux = _c_(568356, _a_(568353, _n_(568352, "pd", lambda: pd), "to_datetime"), _a_(568355, _n_(568354, "news_dataframe", lambda: news_dataframe), "dateTime"))
    _l_(568357)
    return aux

_c_(568362, _a_(568360, _n_(568359, "df", lambda: df), "apply"), _n_(568361, "_replace_datetime_with_datetime_pub", lambda: _replace_datetime_with_datetime_pub)) 
_l_(568363) 