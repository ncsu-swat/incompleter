# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73271581/module-api-has-no-attribute-error-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import api
    _l_(374238)

except ImportError:
    pass
try:
    import tweepy
    _l_(374240)

except ImportError:
    pass

users = {}
_l_(374241)

keys = _c_(374243, _n_(374242, "open", lambda: open), "keystwitter.txt", 'r')
_l_(374244)

CONSUMER_KEY = _c_(374249, _a_(374248, _c_(374247, _a_(374246, _n_(374245, "keys", lambda: keys), "readline")), "strip"))
_l_(374250)
CONSUMER_SECRET = _c_(374255, _a_(374254, _c_(374253, _a_(374252, _n_(374251, "keys", lambda: keys), "readline")), "strip"))
_l_(374256)
ACCESS_TOKEN = _c_(374261, _a_(374260, _c_(374259, _a_(374258, _n_(374257, "keys", lambda: keys), "readline")), "strip"))
_l_(374262)
ACCESS_TOKEN_SECRET = _c_(374267, _a_(374266, _c_(374265, _a_(374264, _n_(374263, "keys", lambda: keys), "readline")), "strip"))
_l_(374268)

TwitterAuth = _c_(374273, _a_(374270, _n_(374269, "tweepy", lambda: tweepy), "OAuthHandler"), _n_(374271, "CONSUMER_KEY", lambda: CONSUMER_KEY), _n_(374272, "CONSUMER_SECRET", lambda: CONSUMER_SECRET))
_l_(374274)
_c_(374279, _a_(374276, _n_(374275, "TwitterAuth", lambda: TwitterAuth), "set_access_token"), _n_(374277, "ACCESS_TOKEN", lambda: ACCESS_TOKEN), _n_(374278, "ACCESS_TOKEN_SECRET", lambda: ACCESS_TOKEN_SECRET))
_l_(374280)

tweeter = _c_(374284, _a_(374282, _n_(374281, "tweepy", lambda: tweepy), "API"), _n_(374283, "TwitterAuth", lambda: TwitterAuth))
_l_(374285)

StinkyChesse = ['mandzio', 'ewroon', 'klaudiacroft']
_l_(374286)


def initialize():
    _l_(374318)

    file = _c_(374288, _n_(374287, "open", lambda: open), "users.txt", "r")
    _l_(374289)
    for data in _n_(374290, "file", lambda: file):
        _l_(374314)

        user_name = _c_(374293, _a_(374292, _n_(374291, "data", lambda: data), "strip"))
        _l_(374294)
        _c_(374297, _n_(374295, "print", lambda: print), _n_(374296, "user_name", lambda: user_name))
        _l_(374298)
        user_id = _c_(374302, _a_(374300, _n_(374299, "api", lambda: api), "get_user_id"), _n_(374301, "user_name", lambda: user_name))
        _l_(374303)
        follows = _c_(374307, _a_(374305, _n_(374304, "api", lambda: api), "get_all_follows"), _n_(374306, "user_id", lambda: user_id))
        _l_(374308)
        _n_(374309, "users", lambda: users)[_n_(374310, "user_name", lambda: user_name)] = [_n_(374311, "user_id", lambda: user_id), _n_(374312, "follows", lambda: follows)]
        _l_(374313)
    _c_(374316, _n_(374315, "print", lambda: print), "Bot Launched")
    _l_(374317)