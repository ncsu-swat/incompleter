# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55107435/how-to-load-statuses-from-twitter-api-typeerror-string-indices-must-be-integer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import oauth2 as oauth
    _l_(395295)

except ImportError:
    pass
try:
    import json
    _l_(395297)

except ImportError:
    pass
try:
    import configparser
    _l_(395299)

except ImportError:
    pass

config = _c_(395302, _a_(395301, _n_(395300, "configparser", lambda: configparser), "RawConfigParser"))
_l_(395303)
configpath = r'config.py'
_l_(395304)
_c_(395308, _a_(395306, _n_(395305, "config", lambda: config), "read"), _n_(395307, "configpath", lambda: configpath))
_l_(395309)
consumer_key = _c_(395312, _a_(395311, _n_(395310, "config", lambda: config), "get"), 'logintwitter', 'consumer_key')
_l_(395313)
consumer_secret = _c_(395316, _a_(395315, _n_(395314, "config", lambda: config), "get"), 'logintwitter', 'consumer_secret')
_l_(395317)
access_key = _c_(395320, _a_(395319, _n_(395318, "config", lambda: config), "get"), 'logintwitter', 'access_key')
_l_(395321)
access_secret = _c_(395324, _a_(395323, _n_(395322, "config", lambda: config), "get"), 'logintwitter', 'access_secret')
_l_(395325)


consumer = _c_(395330, _a_(395327, _n_(395326, "oauth", lambda: oauth), "Consumer"), key=_n_(395328, "consumer_key", lambda: consumer_key), secret=_n_(395329, "consumer_secret", lambda: consumer_secret)) #twitter: sign me in
_l_(395331) #twitter: sign me in
access_token = _c_(395336, _a_(395333, _n_(395332, "oauth", lambda: oauth), "Token"), key=_n_(395334, "access_key", lambda: access_key), secret=_n_(395335, "access_secret", lambda: access_secret)) #grant me access
_l_(395337) #grant me access
client = _c_(395342, _a_(395339, _n_(395338, "oauth", lambda: oauth), "Client"), _n_(395340, "consumer", lambda: consumer), _n_(395341, "access_token", lambda: access_token)) #object return
_l_(395343) #object return

timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"
_l_(395344)
response, data = _c_(395348, _a_(395346, _n_(395345, "client", lambda: client), "request"), _n_(395347, "timeline_endpoint", lambda: timeline_endpoint))
_l_(395349)

tweets = _c_(395353, _a_(395351, _n_(395350, "json", lambda: json), "loads"), _n_(395352, "data", lambda: data)) #take a JSON string convert it to dictionary structure:
_l_(395354) #take a JSON string convert it to dictionary structure:
for tweet in _n_(395355, "tweets", lambda: tweets):
    _l_(395360)

    _c_(395358, _n_(395356, "print", lambda: print), _n_(395357, "tweet", lambda: tweet)["text"])
    _l_(395359)