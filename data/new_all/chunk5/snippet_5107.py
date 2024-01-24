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
_l_(687653)

video_ad_2 = {
    "title": "Get a ride, anytime anywhere", 
    "company": "GoJek", 
    "views": 54323
}
_l_(687654)

video_ad_view1=_n_(687655, "video_ad_1", lambda: video_ad_1)["views"]
_l_(687656)
_c_(687659, _n_(687657, "print", lambda: print), _n_(687658, "video_ad_view1", lambda: video_ad_view1))
_l_(687660)

for i in _c_(687662, _n_(687661, "range", lambda: range), 1,2):
    _l_(687677)

    _c_(687665, _n_(687663, "print", lambda: print), _n_(687664, "i", lambda: i))
    _l_(687666)
    _n_(687667, "video_ad_view", lambda: video_ad_view)[_n_(687668, "i", lambda: i)] = _n_(687669, "video_ad_", lambda: video_ad_)[_n_(687670, "i", lambda: i)]["views"]
    _l_(687671)
    _c_(687675, _n_(687672, "print", lambda: print), _n_(687673, "video_ad_view", lambda: video_ad_view)[_n_(687674, "i", lambda: i)])
    _l_(687676)