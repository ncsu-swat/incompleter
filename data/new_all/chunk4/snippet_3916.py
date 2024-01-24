# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65369185/how-to-ignore-nonetype-error-in-tweet-id-statuses-lookup
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def lookup_tweets(tweet_IDs, api):
    _l_(582020)

    full_tweets = []
    _l_(581991)
    tweet_count = _c_(581994, _n_(581992, "len", lambda: len), _n_(581993, "tweet_IDs", lambda: tweet_IDs))
    _l_(581995)
    try:
        _l_(582019)

        for i in _c_(581998, _n_(581996, "range", lambda: range), (_n_(581997, "tweet_count", lambda: tweet_count) // 100) + 1):
            _l_(582014)

            # Catch the last group if it is less than 100 tweets
            end_loc = _c_(582002, _n_(581999, "min", lambda: min), (_n_(582000, "i", lambda: i) + 1) * 100, _n_(582001, "tweet_count", lambda: tweet_count))
            _l_(582003)
            _c_(582012, _a_(582005, _n_(582004, "full_tweets", lambda: full_tweets), "extend"), _c_(582011, _a_(582007, _n_(582006, "api", lambda: api), "statuses_lookup"), _n_(582008, "tweet_IDs", lambda: tweet_IDs)[_n_(582009, "i", lambda: i) * 100:_n_(582010, "end_loc", lambda: end_loc)], tweet_mode='extended')
            )
            _l_(582013)
        aux = _n_(582015, "full_tweets", lambda: full_tweets)
        _l_(582016)
        return aux
    except:
        _l_(582018)

        pass
        _l_(582017)

results = _c_(582024, _n_(582021, "lookup_tweets", lambda: lookup_tweets), _n_(582022, "good_tweet_ids_test", lambda: good_tweet_ids_test), _n_(582023, "api", lambda: api))
_l_(582025)
temp = _c_(582031, _a_(582027, _n_(582026, "json", lambda: json), "dumps"), [_a_(582029, _n_(582028, "status", lambda: status), "_json") for status in _n_(582030, "results", lambda: results)]) #create JSON
_l_(582032) #create JSON
newdf = _c_(582036, _a_(582034, _n_(582033, "pd", lambda: pd), "read_json"), _n_(582035, "temp", lambda: temp), orient='records')
_l_(582037)
_c_(582040, _a_(582039, _n_(582038, "newdf", lambda: newdf), "to_json"), 'tweepy_tweets.json')
_l_(582041)