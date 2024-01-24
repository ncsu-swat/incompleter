# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74035325/attributeerror-module-tweepy-has-no-attribute-oauthhandler-when-creating-tw
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tweepy
    _l_(386529)

except ImportError:
    pass

auth = _c_(386534, _a_(386531, _n_(386530, "tweepy", lambda: tweepy), "OAuthHandler"), _n_(386532, "consumer_key", lambda: consumer_key), _n_(386533, "consumer_secret", lambda: consumer_secret))
_l_(386535)
_c_(386540, _a_(386537, _n_(386536, "auth", lambda: auth), "set_access_token"), _n_(386538, "access_token", lambda: access_token), _n_(386539, "access_token_secret", lambda: access_token_secret))
_l_(386541)
api = _c_(386545, _a_(386543, _n_(386542, "tweepy", lambda: tweepy), "API"), _n_(386544, "auth", lambda: auth))
_l_(386546)

_c_(386552, _n_(386547, "print", lambda: print), _a_(386551, _c_(386550, _a_(386549, _n_(386548, "api", lambda: api), "verify_credentials")), "screen_name"))
_l_(386553)