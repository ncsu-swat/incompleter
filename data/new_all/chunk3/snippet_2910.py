# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58681634/python3-error-typeerror-str-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
url = "https://www.reddit.com/r/" + _n_(557453, "subreddit", lambda: subreddit) + "/" + _n_(557454, "feed", lambda: feed) + ".json?sort=" + _n_(557455, "feed", lambda: feed) + "&limit=6"
_l_(557456)

resp = _c_(557460, _a_(557458, _n_(557457, "requests", lambda: requests), "get"), _n_(557459, "url", lambda: url), verify=False)
_l_(557461)
json = _c_(557467, _a_(557463, _n_(557462, "json", lambda: json), "loads"), _c_(557466, _a_(557465, _n_(557464, "resp", lambda: resp), "text")))
_l_(557468)

_c_(557471, _n_(557469, "print", lambda: print), _n_(557470, "json", lambda: json)["data"]["children"][0]["data"]["id"])
_l_(557472)