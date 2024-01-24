# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56572523/navernews-default-nameerror-name-navernews-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(696805)

except ImportError:
    pass
try:
    import sys
    _l_(696807)

except ImportError:
    pass
file_dir = _c_(696812, _a_(696810, _a_(696809, _n_(696808, "os", lambda: os), "path"), "dirname"), _n_(696811, "__file__", lambda: __file__))
_l_(696813)
_c_(696818, _a_(696816, _a_(696815, _n_(696814, "sys", lambda: sys), "path"), "append"), _n_(696817, "file_dir", lambda: file_dir))
_l_(696819)
_c_(696823, _a_(696822, _a_(696821, _n_(696820, "sys", lambda: sys), "path"), "append"), '/NaverNews/Main/News/FirstNews')
_l_(696824)
_c_(696828, _a_(696827, _a_(696826, _n_(696825, "sys", lambda: sys), "path"), "append"), '/NaverNews/Default/Default')
_l_(696829)
try:
    from urllib.request import urlopen
    _l_(696831)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(696833)

except ImportError:
    pass
try:
    import json
    _l_(696835)

except ImportError:
    pass
try:
    from FirstNews import *
    _l_(696837)

except ImportError:
    pass
try:
    from Default import *
    _l_(696839)

except ImportError:
    pass
try:
    import datetime
    _l_(696841)

except ImportError:
    pass
try:
    import random
    _l_(696843)

except ImportError:
    pass

_c_(696850, _a_(696845, _n_(696844, "random", lambda: random), "seed"), _c_(696849, _a_(696848, _a_(696847, _n_(696846, "datetime", lambda: datetime), "datetime"), "now")))
_l_(696851)


class NaverNews:
    _l_(696888)

    def __init__(self, NewsLists):
        _l_(696858)

        _n_(696852, "self", lambda: self).FirstNewsSite = _n_(696853, "NewsLists", lambda: NewsLists)
        _l_(696854)
        # self.SecondNewsSite = NewsLists
        # self.ThirdNewsSite = NewsLists
        # self.FourthNewsSite = NewsLists
        # self.FifthNewsSite = NewsLists
        # self.RealTimeNews = NewsLists
        _n_(696855, "self", lambda: self).Default = _n_(696856, "NewsLists", lambda: NewsLists)
        _l_(696857)

    # @property
    # def NewsLists(self):
    #     return self.NewsLists

    # def SelectNums(self, new_NewsLists):
    def __call__(self):
        _l_(696887)

        _c_(696860, _n_(696859, "print", lambda: print), "Please Select the News Site")
        _l_(696861)
        MenuInput = _c_(696863, _n_(696862, "input", lambda: input), "Select The Menu")
        _l_(696864)
        MenuList = []
        _l_(696865)
        while 1:
            _l_(696886)

            if _n_(696866, "MenuInput", lambda: MenuInput) is 1:
                _l_(696885)

                _c_(696869, _a_(696868, _n_(696867, "self", lambda: self), "FirstNewsSite"))
                _l_(696870)
                _c_(696874, _a_(696872, _n_(696871, "MenuList", lambda: MenuList), "append"), _n_(696873, "FirstNews", lambda: FirstNews))
                _l_(696875)

            else:
                _c_(696878, _a_(696877, _n_(696876, "self", lambda: self), "Default"))
                _l_(696879)
                _c_(696883, _a_(696881, _n_(696880, "MenuList", lambda: MenuList), "append"), _n_(696882, "DefaultNews", lambda: DefaultNews))
                _l_(696884)