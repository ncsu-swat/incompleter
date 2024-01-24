# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65008891/typeerror-object-of-type-httpconnection-has-no-len-in-python-3-7
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import bs4 as bs
    _l_(627317)

except ImportError:
    pass
try:
    import streamlit as st
    _l_(627319)

except ImportError:
    pass

source_txt = _c_(627322, _a_(627321, _n_(627320, "st", lambda: st), "text_input"), "") #Input url will be entered, say: https://rgtnt.com/
_l_(627323) #Input url will be entered, say: https://rgtnt.com/
_c_(627327, _a_(627325, _n_(627324, "st", lambda: st), "write"), _n_(627326, "source_txt", lambda: source_txt))
_l_(627328)
try:
    import http
    _l_(627330)

except ImportError:
    pass
source = _c_(627335, _a_(627333, _a_(627332, _n_(627331, "http", lambda: http), "client"), "HTTPConnection"), _n_(627334, "source_txt", lambda: source_txt))
_l_(627336)

page_soup = _c_(627340, _a_(627338, _n_(627337, "bs", lambda: bs), "BeautifulSoup"), _n_(627339, "source", lambda: source), 'html.parser')
_l_(627341)