# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36129435/type-error-unhashable-type-list-in-praw-bot
#Bot

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import praw
    _l_(694954)

except ImportError:
    pass
try:
    import time
    _l_(694956)

except ImportError:
    pass
try:
    import re
    _l_(694958)

except ImportError:
    pass
try:
    import os
    _l_(694960)

except ImportError:
    pass

r = _c_(694963, _a_(694962, _n_(694961, "praw", lambda: praw), "Reddit"), user_agent = "Bot")
_l_(694964)
_c_(694967, _a_(694966, _n_(694965, "r", lambda: r), "login"))
_l_(694968)
cache = []
_l_(694969)



def run_bot():
    _l_(695024)

    subreddit = _c_(694972, _a_(694971, _n_(694970, "r", lambda: r), "get_subreddit"), "broap")
    _l_(694973)
    comments = _c_(694976, _a_(694975, _n_(694974, "subreddit", lambda: subreddit), "get_comments"), limit=25)
    _l_(694977)
    for comment in _n_(694978, "comments", lambda: comments):
        _l_(695023)

        comment_text = _c_(694982, _a_(694981, _a_(694980, _n_(694979, "comment", lambda: comment), "body"), "lower"))
        _l_(694983)
        author = _a_(694985, _n_(694984, "comment", lambda: comment), "author")
        _l_(694986)
        url = _a_(694988, _n_(694987, "comment", lambda: comment), "link_id")
        _l_(694989)
        msg = _c_(694992, _a_(694990, "User {} has tagged you in a post!", "format"), _n_(694991, "author", lambda: author))
        _l_(694993)
        words = _c_(695001, _n_(694994, "filter", lambda: filter), lambda x:_c_(694997, _a_(694996, _n_(694995, "x", lambda: x), "startswith"), '//'), _c_(695000, _a_(694999, _n_(694998, "comment_text", lambda: comment_text), "split")))
        _l_(695002)
        user = _n_(695003, "words", lambda: words)[2:]  
        _l_(695004)  
        if _a_(695006, _n_(695005, "comment", lambda: comment), "id") not in _n_(695007, "cache", lambda: cache) and _n_(695008, "words", lambda: words):
            _l_(695022)

            _c_(695014, _a_(695011, _a_(695010, _n_(695009, "r", lambda: r), "user"), "send_message"), _n_(695012, "user", lambda: user) ,_n_(695013, "msg", lambda: msg))
            _l_(695015)
            _c_(695020, _a_(695017, _n_(695016, "cache", lambda: cache), "add"), _a_(695019, _n_(695018, "comment", lambda: comment), "id"))
            _l_(695021)




while True:
    _l_(695032)

    _c_(695026, _n_(695025, "run_bot", lambda: run_bot))
    _l_(695027)
    _c_(695030, _a_(695029, _n_(695028, "time", lambda: time), "sleep"), 5)
    _l_(695031)