# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55147231/error-attributeerror-list-object-has-no-attribute-encode
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import constants
    _l_(652567)

except ImportError:
    pass
try:
    import oauth2
    _l_(652569)

except ImportError:
    pass
try:
    import urllib.parse as urlparse
    _l_(652571)

except ImportError:
    pass
try:
    import json
    _l_(652573)

except ImportError:
    pass

#Create a consumer, which uses CONSUMER_KEY and CONSUMER_SECRET to identify our app uniquely
consumer = _c_(652580, _a_(652575, _n_(652574, "oauth2", lambda: oauth2), "Consumer"), _a_(652577, _n_(652576, "constants", lambda: constants), "CONSUMER_KEY"), _a_(652579, _n_(652578, "constants", lambda: constants), "CONSUMER_SECRET"))
_l_(652581)
client = _c_(652585, _a_(652583, _n_(652582, "oauth2", lambda: oauth2), "Client"), _n_(652584, "consumer", lambda: consumer))
_l_(652586)

#Use the client to perform a request for the request token
response, content = _c_(652591, _a_(652588, _n_(652587, "client", lambda: client), "request"), _a_(652590, _n_(652589, "constants", lambda: constants), "REQUEST_TOKEN_URL"), 'POST')
_l_(652592)
if _a_(652594, _n_(652593, "response", lambda: response), "status") != 200:
    _l_(652598)

    _c_(652596, _n_(652595, "print", lambda: print), "An error occurred getting the token from Twitter!")
    _l_(652597)

#Get the request token parsing the query string returned
request_token = _c_(652606, _n_(652599, "dict", lambda: dict), _c_(652605, _a_(652601, _n_(652600, "urlparse", lambda: urlparse), "parse_qsl"), _c_(652604, _a_(652603, _n_(652602, "content", lambda: content), "decode"), 'utf-8')))
_l_(652607)

#Ask the user to authorize our app and give us the pin code
_c_(652609, _n_(652608, "print", lambda: print), "Go to the follwing site in your brower:")
_l_(652610)
_c_(652617, _n_(652611, "print", lambda: print), _c_(652616, _a_(652612, "{}?oauth_token={}", "format"), _a_(652614, _n_(652613, "constants", lambda: constants), "AUTHORIZATION_URL"), _n_(652615, "request_token", lambda: request_token)['oauth_token']))
_l_(652618)

oauth_verifier = _c_(652620, _n_(652619, "input", lambda: input), "What is the PIN? ")
_l_(652621)

#Create a Token object which contains the request toen, and the verifier
token = _c_(652626, _a_(652623, _n_(652622, "oauth2", lambda: oauth2), "Token"), _n_(652624, "request_token", lambda: request_token)['oauth_token'], _n_(652625, "request_token", lambda: request_token)['oauth_token_secret'])
_l_(652627)
_c_(652631, _a_(652629, _n_(652628, "token", lambda: token), "set_verifier"), _n_(652630, "oauth_verifier", lambda: oauth_verifier))
_l_(652632)

#Create a client with our consumer (our app) and the newly created (and verified) token
client = _c_(652637, _a_(652634, _n_(652633, "oauth2", lambda: oauth2), "Client"), _n_(652635, "consumer", lambda: consumer), _n_(652636, "token", lambda: token))
_l_(652638)

#Ask Twitter for an acess token, and Twitter knows ot should give us it because we've verified the request token
response, content = _c_(652643, _a_(652640, _n_(652639, "client", lambda: client), "request"), _a_(652642, _n_(652641, "constants", lambda: constants), "ACCESS_TOKEN_URL"), 'POST')
_l_(652644)
access_token = _c_(652652, _n_(652645, "dict", lambda: dict), _c_(652651, _a_(652647, _n_(652646, "urlparse", lambda: urlparse), "parse_qs"), _c_(652650, _a_(652649, _n_(652648, "content", lambda: content), "decode"), 'utf-8')))
_l_(652653)

_c_(652656, _n_(652654, "print", lambda: print), _n_(652655, "access_token", lambda: access_token))
_l_(652657)

#Create an "authorized_token" Token object and use that to perfom Twitter API calls on behalf of user
authorized_token = _c_(652662, _a_(652659, _n_(652658, "oauth2", lambda: oauth2), "Token"), _n_(652660, "access_token", lambda: access_token)['oauth_token'], _n_(652661, "access_token", lambda: access_token)['oauth_token_secret'])
_l_(652663)
authorized_client = _c_(652668, _a_(652665, _n_(652664, "oauth2", lambda: oauth2), "Client"), _n_(652666, "consumer", lambda: consumer), _n_(652667, "authorized_token", lambda: authorized_token))
_l_(652669)

#Make Twittwe API calls!
response, content = _c_(652672, _a_(652671, _n_(652670, "authorized_client", lambda: authorized_client), "request"), 'https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images', 'GET')
_l_(652673)
if _a_(652675, _n_(652674, "response", lambda: response), "status") != 200:
    _l_(652679)

    _c_(652677, _n_(652676, "print", lambda: print), "An error occurred when searching!")
    _l_(652678)
_c_(652684, _n_(652680, "print", lambda: print), _c_(652683, _a_(652682, _n_(652681, "content", lambda: content), "decode"), 'utf-8'))
_l_(652685)