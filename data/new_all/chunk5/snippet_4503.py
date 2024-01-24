# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56572523/navernews-default-nameerror-name-navernews-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(658595)

except ImportError:
    pass
try:
    import sys
    _l_(658597)

except ImportError:
    pass
file_dir = _c_(658602, _a_(658600, _a_(658599, _n_(658598, "os", lambda: os), "path"), "dirname"), _n_(658601, "__file__", lambda: __file__))
_l_(658603)
_c_(658608, _a_(658606, _a_(658605, _n_(658604, "sys", lambda: sys), "path"), "append"), _n_(658607, "file_dir", lambda: file_dir))
_l_(658609)
_c_(658613, _a_(658612, _a_(658611, _n_(658610, "sys", lambda: sys), "path"), "append"), '/NaverNews/Main/News/FirstNews')
_l_(658614)
_c_(658618, _a_(658617, _a_(658616, _n_(658615, "sys", lambda: sys), "path"), "append"), '/NaverNews/Default/Default')
_l_(658619)
try:
    from urllib.request import urlopen
    _l_(658621)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(658623)

except ImportError:
    pass
try:
    import json
    _l_(658625)

except ImportError:
    pass
try:
    from FirstNews import *
    _l_(658627)

except ImportError:
    pass
try:
    from Default import *
    _l_(658629)

except ImportError:
    pass
try:
    import datetime
    _l_(658631)

except ImportError:
    pass
try:
    import random
    _l_(658633)

except ImportError:
    pass

_c_(658640, _a_(658635, _n_(658634, "random", lambda: random), "seed"), _c_(658639, _a_(658638, _a_(658637, _n_(658636, "datetime", lambda: datetime), "datetime"), "now")))
_l_(658641)


class NaverNews:
    _l_(658678)

    def __init__(self, NewsLists):
        _l_(658648)

        _n_(658642, "self", lambda: self).FirstNewsSite = _n_(658643, "NewsLists", lambda: NewsLists)
        _l_(658644)
        # self.SecondNewsSite = NewsLists
        # self.ThirdNewsSite = NewsLists
        # self.FourthNewsSite = NewsLists
        # self.FifthNewsSite = NewsLists
        # self.RealTimeNews = NewsLists
        _n_(658645, "self", lambda: self).Default = _n_(658646, "NewsLists", lambda: NewsLists)
        _l_(658647)

    # @property
    # def NewsLists(self):
    #     return self.NewsLists

    # def SelectNums(self, new_NewsLists):
    def __call__(self):
        _l_(658677)

        _c_(658650, _n_(658649, "print", lambda: print), "Please Select the News Site")
        _l_(658651)
        MenuInput = _c_(658653, _n_(658652, "input", lambda: input), "Select The Menu")
        _l_(658654)
        MenuList = []
        _l_(658655)
        while 1:
            _l_(658676)

            if _n_(658656, "MenuInput", lambda: MenuInput) is 1:
                _l_(658675)

                _c_(658659, _a_(658658, _n_(658657, "self", lambda: self), "FirstNewsSite"))
                _l_(658660)
                _c_(658664, _a_(658662, _n_(658661, "MenuList", lambda: MenuList), "append"), _n_(658663, "FirstNews", lambda: FirstNews))
                _l_(658665)

            else:
                _c_(658668, _a_(658667, _n_(658666, "self", lambda: self), "Default"))
                _l_(658669)
                _c_(658673, _a_(658671, _n_(658670, "MenuList", lambda: MenuList), "append"), _n_(658672, "DefaultNews", lambda: DefaultNews))
                _l_(658674)