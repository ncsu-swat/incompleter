# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66566100/attributeerror-object-has-no-attribute-published-when-parsing-cnn-source
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import feedparser
    _l_(530445)

except ImportError:
    pass

url = "http://rss.cnn.com/rss/edition.rss"
_l_(530446)
feed = _c_(530450, _a_(530448, _n_(530447, "feedparser", lambda: feedparser), "parse"), _n_(530449, "url", lambda: url))
_l_(530451)
for news in _a_(530453, _n_(530452, "feed", lambda: feed), "entries"):
    _l_(530459)

    _c_(530457, _n_(530454, "print", lambda: print), _a_(530456, _n_(530455, "news", lambda: news), "published"))
    _l_(530458)