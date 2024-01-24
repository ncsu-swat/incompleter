# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33146950/typeerror-cant-convert-bytes-object-to-str-implicitly-for-tweepy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tweepy import Stream
    _l_(619309)

except ImportError:
    pass
try:
    from tweepy import OAuthHandler
    _l_(619311)

except ImportError:
    pass
try:
    from tweepy.streaming import StreamListener
    _l_(619313)

except ImportError:
    pass

ckey=''
_l_(619314)
csecret=''
_l_(619315)
atoken=''
_l_(619316)
asecret=''
_l_(619317)

class listener(_n_(619318, "StreamListener", lambda: StreamListener)):
    _l_(619330)


    def on_data(self,data):
        _l_(619324)

        _c_(619321, _n_(619319, "print", lambda: print), _n_(619320, "data", lambda: data))
        _l_(619322)
        aux = True
        _l_(619323)
        return aux

    def on_error(self,status):
        _l_(619329)

        _c_(619327, _n_(619325, "print", lambda: print), _n_(619326, "status", lambda: status))
        _l_(619328)


auth = _c_(619334, _n_(619331, "OAuthHandler", lambda: OAuthHandler), _n_(619332, "ckey", lambda: ckey),_n_(619333, "csecret", lambda: csecret))
_l_(619335)
_c_(619340, _a_(619337, _n_(619336, "auth", lambda: auth), "set_access_token"), _n_(619338, "atoken", lambda: atoken), _n_(619339, "asecret", lambda: asecret))
_l_(619341)
twitterStream = _c_(619346, _n_(619342, "Stream", lambda: Stream), _n_(619343, "auth", lambda: auth), _c_(619345, _n_(619344, "listener", lambda: listener)))
_l_(619347)
_c_(619350, _a_(619349, _n_(619348, "twitterStream", lambda: twitterStream), "filter"), track="cricket")
_l_(619351)