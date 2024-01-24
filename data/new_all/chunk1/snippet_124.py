# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48387878/attributeerror-dataframe-object-has-no-attribute-to-datetime
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(418567, "tweets_df", lambda: tweets_df)['Time'] = _c_(418571, _a_(418569, _n_(418568, "pd", lambda: pd), "to_datetime"), _n_(418570, "tweets_df", lambda: tweets_df)['Time'])
_l_(418572)
_c_(418575, _a_(418574, _n_(418573, "tweets_df", lambda: tweets_df), "set_index"), 'Time', drop=False, inplace=True)
_l_(418576)
_n_(418577, "tweets_df", lambda: tweets_df).index = _c_(418583, _a_(418582, _c_(418581, _a_(418580, _a_(418579, _n_(418578, "tweets_df", lambda: tweets_df), "index"), "tz_localize"), 'UTC'), "tz_convert"), 'US/Eastern') 
_l_(418584) 