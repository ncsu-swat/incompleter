# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59437405/why-when-i-run-my-script-the-downloaded-image-files-have-zero-bytes-and-i-recei
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import praw, requests, os, bs4
    _l_(648476)

except ImportError:
    pass

reddit = _c_(648479, _a_(648478, _n_(648477, "praw", lambda: praw), "Reddit"), client_id='xxxx', 
                      client_secret='xxxx',
                      user_agent='picture downloader',
                      username='xxxx',
                      password='xxxx'
                      ) 
_l_(648480) 
_c_(648484, _n_(648481, "print", lambda: print), _a_(648483, _n_(648482, "reddit", lambda: reddit), "read_only"))
_l_(648485)

_c_(648488, _a_(648487, _n_(648486, "os", lambda: os), "makedirs"), 'redditpics', exist_ok=True) 
_l_(648489) 
for submission in _c_(648494, _a_(648493, _c_(648492, _a_(648491, _n_(648490, "reddit", lambda: reddit), "subreddit"), 'earthporn'), "hot"), limit=50):
    _l_(648514)

    url = _a_(648496, _n_(648495, "submission", lambda: submission), "url")
    _l_(648497)
    _c_(648500, _n_(648498, "print", lambda: print), _n_(648499, "url", lambda: url))
    _l_(648501)
    imageFile = _c_(648512, _n_(648502, "open", lambda: open), _c_(648511, _a_(648505, _a_(648504, _n_(648503, "os", lambda: os), "path"), "join"), 'redditpics', _c_(648510, _a_(648508, _a_(648507, _n_(648506, "os", lambda: os), "path"), "basename"), _n_(648509, "url", lambda: url))), 'wb')
    _l_(648513)
_c_(648516, _n_(648515, "print", lambda: print), 'Done')
_l_(648517)