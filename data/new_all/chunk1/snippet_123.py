# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48387878/attributeerror-dataframe-object-has-no-attribute-to-datetime
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
tweets_df = _c_(377237, _a_(377236, _n_(377235, "pd", lambda: pd), "read_csv"), 'valid_tweets.csv')
_l_(377238)

_n_(377239, "tweets_df", lambda: tweets_df)['Time'] = _c_(377243, _a_(377241, _n_(377240, "tweets_df", lambda: tweets_df), "to_datetime"), _n_(377242, "tweets_df", lambda: tweets_df)['Time'])
_l_(377244)
_c_(377247, _a_(377246, _n_(377245, "tweets_df", lambda: tweets_df), "set_index"), 'Time', drop=False, inplace=True)
_l_(377248)