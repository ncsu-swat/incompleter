# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65008891/typeerror-object-of-type-httpconnection-has-no-len-in-python-3-7
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import bs4 as bs
    _l_(591969)

except ImportError:
    pass
try:
    import streamlit as st
    _l_(591971)

except ImportError:
    pass

source_txt = _c_(591974, _a_(591973, _n_(591972, "st", lambda: st), "text_input"), "") #Input url will be entered, say: https://rgtnt.com/
_l_(591975) #Input url will be entered, say: https://rgtnt.com/
_c_(591979, _a_(591977, _n_(591976, "st", lambda: st), "write"), _n_(591978, "source_txt", lambda: source_txt))
_l_(591980)
try:
    import http
    _l_(591982)

except ImportError:
    pass
source = _c_(591987, _a_(591985, _a_(591984, _n_(591983, "http", lambda: http), "client"), "HTTPConnection"), _n_(591986, "source_txt", lambda: source_txt))
_l_(591988)

page_soup = _c_(591992, _a_(591990, _n_(591989, "bs", lambda: bs), "BeautifulSoup"), _n_(591991, "source", lambda: source), 'html.parser')
_l_(591993)