# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74188784/attributeerror-nonetype-object-has-no-attribute-get-text-in-the-line-9
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
soup = _c_(526155, _n_(526153, "BeautifulSoup", lambda: BeautifulSoup), _n_(526154, "page", lambda: page), "html.parser")
_l_(526156)
soup_title = _c_(526159, _a_(526158, _n_(526157, "soup", lambda: soup), "find"), name="a", class_="spacer")
_l_(526160)
_c_(526165, _n_(526161, "print", lambda: print), _c_(526164, _a_(526163, _n_(526162, "soup_title", lambda: soup_title), "get_text")))
_l_(526166)