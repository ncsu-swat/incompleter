# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74278955/python-typeerror-string-indices-must-be-integers-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
articles_list = []
_l_(608081)
y= _c_(608084, _a_(608083, _n_(608082, "requests", lambda: requests), "get"), "https://hacker-news.firebaseio.com/v0/newstories.json")
_l_(608085)
y = _c_(608088, _a_(608087, _n_(608086, "y", lambda: y), "json"))
_l_(608089)
_c_(608092, _n_(608090, "print", lambda: print), _n_(608091, "y", lambda: y))
_l_(608093)
_c_(608096, _n_(608094, "print", lambda: print), "https://hacker-news.firebaseio.com/v0/item/" + _n_(608095, "number", lambda: number) +".json" +"?print=pretty")
_l_(608097)
for number in _n_(608098, "y", lambda: y):
    _l_(608115)

    req = _c_(608104, _a_(608100, _n_(608099, "requests", lambda: requests), "get"), "https://hacker-news.firebaseio.com/v0/item/" + _c_(608103, _n_(608101, "str", lambda: str), _n_(608102, "number", lambda: number)) +".json" +"?print=pretty")
    _l_(608105)
    req = _c_(608108, _a_(608107, _n_(608106, "req", lambda: req), "json"))
    _l_(608109)
    _c_(608112, _n_(608110, "print", lambda: print), _n_(608111, "req", lambda: req))
    _l_(608113)
    break
    _l_(608114)
for thing in _n_(608116, "req", lambda: req)["url"]:
    _l_(608122)

    _c_(608120, _a_(608118, _n_(608117, "articles_list", lambda: articles_list), "append"), _n_(608119, "thing", lambda: thing)["url"])
    _l_(608121)