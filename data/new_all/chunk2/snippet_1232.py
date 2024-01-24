# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69302989/web-scraping-typeerror-nonetype-object-is-not-subscriptable-how-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
my_url = _n_(444573, "str1", lambda: str1)
_l_(444574)
uClient = _c_(444577, _n_(444575, "uReq", lambda: uReq), _n_(444576, "my_url", lambda: my_url))
_l_(444578)
page_html = _c_(444581, _a_(444580, _n_(444579, "uClient", lambda: uClient), "read"))
_l_(444582)
_c_(444585, _a_(444584, _n_(444583, "uClient", lambda: uClient), "close"))
_l_(444586)
page_soup = _c_(444589, _n_(444587, "soup", lambda: soup), _n_(444588, "page_html", lambda: page_html), "html.parser")
_l_(444590)

data = _c_(444593, _a_(444592, _n_(444591, "page_soup", lambda: page_soup), "findAll"), "div", {"class": "_2kHMtA"})
_l_(444594)