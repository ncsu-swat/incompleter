# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43849689/py-corenlp-typeerror-string-indices-must-be-integers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pycorenlp import StanfordCoreNLP
    _l_(416988)

except ImportError:
    pass
try:
    from newspaper import Article
    _l_(416990)

except ImportError:
    pass

url = u'newsArticle.example.html'
_l_(416991)
nlp = _c_(416993, _n_(416992, "StanfordCoreNLP", lambda: StanfordCoreNLP), 'http://localhost:9000')
_l_(416994)
article = _c_(416997, _n_(416995, "Article", lambda: Article), _n_(416996, "url", lambda: url))
_l_(416998)
_c_(417001, _a_(417000, _n_(416999, "article", lambda: article), "download"))
_l_(417002)
_c_(417005, _a_(417004, _n_(417003, "article", lambda: article), "parse"))
_l_(417006)


LARGE_TEXT=_a_(417008, _n_(417007, "article", lambda: article), "text")
_l_(417009)


res = _c_(417013, _a_(417011, _n_(417010, "nlp", lambda: nlp), "annotate"), _n_(417012, "LARGE_TEXT", lambda: LARGE_TEXT),
               properties={
                   'annotators': 'sentiment',
                   'outputFormat': 'json',
                   'timeout': 1000,
               })
_l_(417014)
for s in _n_(417015, "res", lambda: res)["sentences"]:
    _l_(417026)

    _c_(417024, _n_(417016, "print", lambda: print), "%d: '%s': %s %s" % (
        _n_(417017, "s", lambda: s)["index"],
        _c_(417021, _a_(417018, " ", "join"), [_n_(417019, "t", lambda: t)["word"] for t in _n_(417020, "s", lambda: s)["tokens"]]),
        _n_(417022, "s", lambda: s)["sentimentValue"], _n_(417023, "s", lambda: s)["sentiment"]))
    _l_(417025)