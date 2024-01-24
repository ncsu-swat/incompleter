# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33323911/why-do-i-get-an-attributeerror-str-object-has-no-attribute-write-in-this
#Testing implementation of writing to file
#save the HTML to a beautiful soup object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
soup = _c_(447099, _n_(447096, "BeautifulSoup", lambda: BeautifulSoup), _a_(447098, _n_(447097, "browser", lambda: browser), "page_source"), 'html.parser')
_l_(447100)

#TODO: use breadcrumb of page name for loop later on
breadcrumb = _c_(447103, _a_(447102, _n_(447101, "soup", lambda: soup), "select"), '.breadcrumb span')
_l_(447104)
pagename = _c_(447107, _a_(447106, _n_(447105, "breadcrumb", lambda: breadcrumb)[0], "get_text"))
_l_(447108)

#open a file then write to it
bookPage = _c_(447113, _a_(447111, _a_(447110, _n_(447109, "os", lambda: os), "path"), "join"), 'books/cpp/VST', _n_(447112, "pagename", lambda: pagename)+'.txt')
_l_(447114)
_c_(447117, _n_(447115, "open", lambda: open), _n_(447116, "pagename", lambda: pagename), 'wb')
_l_(447118)
_c_(447124, _a_(447120, _n_(447119, "pagename", lambda: pagename), "write"), _c_(447123, _n_(447121, "str", lambda: str), _n_(447122, "soup", lambda: soup)))
_l_(447125)

#close file
#pagename.close()


#TODO: move on to next file