# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56572523/navernews-default-nameerror-name-navernews-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(686301)

except ImportError:
    pass
try:
    import sys
    _l_(686303)

except ImportError:
    pass
file_dir = _c_(686308, _a_(686306, _a_(686305, _n_(686304, "os", lambda: os), "path"), "dirname"), _n_(686307, "__file__", lambda: __file__))
_l_(686309)
_c_(686314, _a_(686312, _a_(686311, _n_(686310, "sys", lambda: sys), "path"), "append"), _n_(686313, "file_dir", lambda: file_dir))
_l_(686315)
_c_(686319, _a_(686318, _a_(686317, _n_(686316, "sys", lambda: sys), "path"), "append"), '/NaverNews/Main/News/FirstNews')
_l_(686320)
_c_(686324, _a_(686323, _a_(686322, _n_(686321, "sys", lambda: sys), "path"), "append"), '/NaverNews/Default/Default')
_l_(686325)
try:
    from urllib.request import urlopen
    _l_(686327)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(686329)

except ImportError:
    pass
try:
    import json
    _l_(686331)

except ImportError:
    pass
try:
    from FirstNews import *
    _l_(686333)

except ImportError:
    pass
try:
    from Default import *
    _l_(686335)

except ImportError:
    pass
try:
    import datetime
    _l_(686337)

except ImportError:
    pass
try:
    import random
    _l_(686339)

except ImportError:
    pass

_c_(686346, _a_(686341, _n_(686340, "random", lambda: random), "seed"), _c_(686345, _a_(686344, _a_(686343, _n_(686342, "datetime", lambda: datetime), "datetime"), "now")))
_l_(686347)


class NaverNews:
    _l_(686384)

    def __init__(self, NewsLists):
        _l_(686354)

        _n_(686348, "self", lambda: self).FirstNewsSite = _n_(686349, "NewsLists", lambda: NewsLists)
        _l_(686350)
        # self.SecondNewsSite = NewsLists
        # self.ThirdNewsSite = NewsLists
        # self.FourthNewsSite = NewsLists
        # self.FifthNewsSite = NewsLists
        # self.RealTimeNews = NewsLists
        _n_(686351, "self", lambda: self).Default = _n_(686352, "NewsLists", lambda: NewsLists)
        _l_(686353)

    # @property
    # def NewsLists(self):
    #     return self.NewsLists

    # def SelectNums(self, new_NewsLists):
    def __call__(self):
        _l_(686383)

        _c_(686356, _n_(686355, "print", lambda: print), "Please Select the News Site")
        _l_(686357)
        MenuInput = _c_(686359, _n_(686358, "input", lambda: input), "Select The Menu")
        _l_(686360)
        MenuList = []
        _l_(686361)
        while 1:
            _l_(686382)

            if _n_(686362, "MenuInput", lambda: MenuInput) is 1:
                _l_(686381)

                _c_(686365, _a_(686364, _n_(686363, "self", lambda: self), "FirstNewsSite"))
                _l_(686366)
                _c_(686370, _a_(686368, _n_(686367, "MenuList", lambda: MenuList), "append"), _n_(686369, "FirstNews", lambda: FirstNews))
                _l_(686371)

            else:
                _c_(686374, _a_(686373, _n_(686372, "self", lambda: self), "Default"))
                _l_(686375)
                _c_(686379, _a_(686377, _n_(686376, "MenuList", lambda: MenuList), "append"), _n_(686378, "DefaultNews", lambda: DefaultNews))
                _l_(686380)