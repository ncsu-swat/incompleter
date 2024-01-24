# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/29587933/attributeerror-module-object-has-no-attribute-choice
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(450160)

except ImportError:
    pass
try:
    from scipy import *
    _l_(450162)

except ImportError:
    pass
try:
    from numpy import linalg as LA
    _l_(450164)

except ImportError:
    pass
try:
    import pickle
    _l_(450166)

except ImportError:
    pass
try:
    import operator
    _l_(450168)

except ImportError:
    pass


def new_pagerank_step(current_page, N, d, links):
    _l_(450192)

    _c_(450172, _n_(450169, "print", lambda: print), _n_(450170, "links", lambda: links)[_n_(450171, "current_page", lambda: current_page)])
    _l_(450173)
    if _c_(450176, _a_(450175, _n_(450174, "random", lambda: random), "rand")) > 1 - _n_(450177, "d", lambda: d):
        _l_(450189)

        next_page = _c_(450182, _a_(450179, _n_(450178, "random", lambda: random), "choice"), _n_(450180, "links", lambda: links)[_n_(450181, "current_page", lambda: current_page)])
        _l_(450183)
    else:
        next_page = _c_(450187, _a_(450185, _n_(450184, "random", lambda: random), "randint"), 0, _n_(450186, "N", lambda: N))
        _l_(450188)
    aux = _n_(450190, "next_page", lambda: next_page)
    _l_(450191)
    return aux


def pagerank_wikipedia_demo():
    _l_(450252)

    with _c_(450194, _n_(450193, "open", lambda: open), "wikilinks.pickle", "rb") as f:
        _l_(450200)

        titles, links = _c_(450198, _a_(450196, _n_(450195, "pickle", lambda: pickle), "load"), _n_(450197, "f", lambda: f))
        _l_(450199)
    current_page = 0
    _l_(450201)
    T = 1000
    _l_(450202)
    N = _c_(450205, _n_(450203, "len", lambda: len), _n_(450204, "titles", lambda: titles))
    _l_(450206)
    d = 0.4
    _l_(450207)
    Result = {}
    _l_(450208)
    result = []
    _l_(450209)
    for i in _c_(450212, _n_(450210, "range", lambda: range), _n_(450211, "T", lambda: T)):
        _l_(450225)

        _c_(450216, _a_(450214, _n_(450213, "result", lambda: result), "append"), _n_(450215, "current_page", lambda: current_page))
        _l_(450217)
        current_page = _c_(450223, _n_(450218, "new_pagerank_step", lambda: new_pagerank_step), _n_(450219, "current_page", lambda: current_page), _n_(450220, "N", lambda: N), _n_(450221, "d", lambda: d), _n_(450222, "links", lambda: links))
        _l_(450224)
    for i in _c_(450228, _n_(450226, "range", lambda: range), _n_(450227, "N", lambda: N)):
        _l_(450242)

        _c_(450232, _a_(450230, _n_(450229, "result", lambda: result), "count"), _n_(450231, "i", lambda: i))
        _l_(450233)
        _n_(450234, "Result", lambda: Result)[_n_(450235, "i", lambda: i)] = _c_(450239, _a_(450237, _n_(450236, "result", lambda: result), "count"), _n_(450238, "i", lambda: i)) / _n_(450240, "T", lambda: T)
        _l_(450241)
    Sorted_Result = _c_(450250, _n_(450243, "sorted", lambda: sorted), _c_(450246, _a_(450245, _n_(450244, "Result", lambda: Result), "items")), key=_c_(450249, _a_(450248, _n_(450247, "operator", lambda: operator), "itemgetter"), 1))
    _l_(450251)

_c_(450254, _n_(450253, "pagerank_wikipedia_demo", lambda: pagerank_wikipedia_demo))
_l_(450255)