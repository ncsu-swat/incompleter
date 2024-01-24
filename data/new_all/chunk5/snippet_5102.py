# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64666975/nameerror-name-video-ad-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
video_ad_1 = {
    "title": "Healthy Living", 
    "company": "Health Promotion Board", 
    "views": 65423
}
_l_(696955)

video_ad_2 = {
    "title": "Get a ride, anytime anywhere", 
    "company": "GoJek", 
    "views": 54323
}
_l_(696956)

video_ad_view1=_n_(696957, "video_ad_1", lambda: video_ad_1)["views"]
_l_(696958)
_c_(696961, _n_(696959, "print", lambda: print), _n_(696960, "video_ad_view1", lambda: video_ad_view1))
_l_(696962)

for i in _c_(696964, _n_(696963, "range", lambda: range), 1,2):
    _l_(696979)

    _c_(696967, _n_(696965, "print", lambda: print), _n_(696966, "i", lambda: i))
    _l_(696968)
    _n_(696969, "video_ad_view", lambda: video_ad_view)[_n_(696970, "i", lambda: i)] = _n_(696971, "video_ad_", lambda: video_ad_)[_n_(696972, "i", lambda: i)]["views"]
    _l_(696973)
    _c_(696977, _n_(696974, "print", lambda: print), _n_(696975, "video_ad_view", lambda: video_ad_view)[_n_(696976, "i", lambda: i)])
    _l_(696978)