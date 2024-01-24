# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71139387/typeerror-get-user-takes-1-positional-argument-but-2-were-given-for-twitter-b
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tweepy
    _l_(600034)

except ImportError:
    pass

api_key='xxx'
_l_(600035)
api_key_secret='xxx'
_l_(600036)
access_token='xxx'
_l_(600037)
access_token_secret='xxx'
_l_(600038)

authenticator=_c_(600043, _a_(600040, _n_(600039, "tweepy", lambda: tweepy), "OAuthHandler"), _n_(600041, "api_key", lambda: api_key),_n_(600042, "api_key_secret", lambda: api_key_secret))
_l_(600044)
_c_(600049, _a_(600046, _n_(600045, "authenticator", lambda: authenticator), "set_access_token"), _n_(600047, "access_token", lambda: access_token), _n_(600048, "access_token_secret", lambda: access_token_secret))
_l_(600050)

api = _c_(600054, _a_(600052, _n_(600051, "tweepy", lambda: tweepy), "API"), _n_(600053, "authenticator", lambda: authenticator), wait_on_rate_limit=True)
_l_(600055)

user = _c_(600058, _a_(600057, _n_(600056, "api", lambda: api), "get_user"), "ammfoundation")
_l_(600059)

tweets_user=_c_(600064, _a_(600061, _n_(600060, "api", lambda: api), "user_timeline"), user_id=_a_(600063, _n_(600062, "user", lambda: user), "id"))
_l_(600065)

for tweet in _n_(600066, "tweets_user", lambda: tweets_user):
    _l_(600076)

    if not _a_(600068, _n_(600067, "tweet", lambda: tweet), "favorited"):
        _l_(600075)

        _c_(600073, _a_(600070, _n_(600069, "api", lambda: api), "create_favorite"), _a_(600072, _n_(600071, "tweet", lambda: tweet), "id"))
        _l_(600074)