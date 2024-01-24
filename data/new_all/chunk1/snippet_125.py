# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48387878/attributeerror-dataframe-object-has-no-attribute-to-datetime
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(410648, "tweets_df", lambda: tweets_df)['Time'] = _c_(410652, _a_(410650, _n_(410649, "pd", lambda: pd), "to_datetime"), _n_(410651, "tweets_df", lambda: tweets_df)['Time'])
_l_(410653)
for index, row in _c_(410656, _a_(410655, _n_(410654, "tweets_df", lambda: tweets_df), "iterrows")):
    _l_(410663)

    _c_(410661, _a_(410660, _c_(410659, _a_(410658, _n_(410657, "row", lambda: row)['Time'], "tz_localize"), 'UTC'), "tz_convert"), 'US/Eastern')
    _l_(410662)