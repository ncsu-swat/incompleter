# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65008891/typeerror-object-of-type-httpconnection-has-no-len-in-python-3-7
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import bs4 as bs
    _l_(595239)

except ImportError:
    pass
try:
    import streamlit as st
    _l_(595241)

except ImportError:
    pass

source_txt = _c_(595244, _a_(595243, _n_(595242, "st", lambda: st), "text_input"), "") #Input url will be entered, say: https://rgtnt.com/
_l_(595245) #Input url will be entered, say: https://rgtnt.com/
_c_(595249, _a_(595247, _n_(595246, "st", lambda: st), "write"), _n_(595248, "source_txt", lambda: source_txt))
_l_(595250)
try:
    import http
    _l_(595252)

except ImportError:
    pass
source = _c_(595257, _a_(595255, _a_(595254, _n_(595253, "http", lambda: http), "client"), "HTTPConnection"), _n_(595256, "source_txt", lambda: source_txt))
_l_(595258)

page_soup = _c_(595262, _a_(595260, _n_(595259, "bs", lambda: bs), "BeautifulSoup"), _n_(595261, "source", lambda: source), 'html.parser')
_l_(595263)