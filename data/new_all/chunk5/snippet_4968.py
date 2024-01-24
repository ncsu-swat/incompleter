# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36129435/type-error-unhashable-type-list-in-praw-bot
#Bot

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import praw
    _l_(646664)

except ImportError:
    pass
try:
    import time
    _l_(646666)

except ImportError:
    pass
try:
    import re
    _l_(646668)

except ImportError:
    pass
try:
    import os
    _l_(646670)

except ImportError:
    pass

r = _c_(646673, _a_(646672, _n_(646671, "praw", lambda: praw), "Reddit"), user_agent = "Bot")
_l_(646674)
_c_(646677, _a_(646676, _n_(646675, "r", lambda: r), "login"))
_l_(646678)
cache = []
_l_(646679)



def run_bot():
    _l_(646734)

    subreddit = _c_(646682, _a_(646681, _n_(646680, "r", lambda: r), "get_subreddit"), "broap")
    _l_(646683)
    comments = _c_(646686, _a_(646685, _n_(646684, "subreddit", lambda: subreddit), "get_comments"), limit=25)
    _l_(646687)
    for comment in _n_(646688, "comments", lambda: comments):
        _l_(646733)

        comment_text = _c_(646692, _a_(646691, _a_(646690, _n_(646689, "comment", lambda: comment), "body"), "lower"))
        _l_(646693)
        author = _a_(646695, _n_(646694, "comment", lambda: comment), "author")
        _l_(646696)
        url = _a_(646698, _n_(646697, "comment", lambda: comment), "link_id")
        _l_(646699)
        msg = _c_(646702, _a_(646700, "User {} has tagged you in a post!", "format"), _n_(646701, "author", lambda: author))
        _l_(646703)
        words = _c_(646711, _n_(646704, "filter", lambda: filter), lambda x:_c_(646707, _a_(646706, _n_(646705, "x", lambda: x), "startswith"), '//'), _c_(646710, _a_(646709, _n_(646708, "comment_text", lambda: comment_text), "split")))
        _l_(646712)
        user = _n_(646713, "words", lambda: words)[2:]  
        _l_(646714)  
        if _a_(646716, _n_(646715, "comment", lambda: comment), "id") not in _n_(646717, "cache", lambda: cache) and _n_(646718, "words", lambda: words):
            _l_(646732)

            _c_(646724, _a_(646721, _a_(646720, _n_(646719, "r", lambda: r), "user"), "send_message"), _n_(646722, "user", lambda: user) ,_n_(646723, "msg", lambda: msg))
            _l_(646725)
            _c_(646730, _a_(646727, _n_(646726, "cache", lambda: cache), "add"), _a_(646729, _n_(646728, "comment", lambda: comment), "id"))
            _l_(646731)




while True:
    _l_(646742)

    _c_(646736, _n_(646735, "run_bot", lambda: run_bot))
    _l_(646737)
    _c_(646740, _a_(646739, _n_(646738, "time", lambda: time), "sleep"), 5)
    _l_(646741)