# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41475703/beautiful-soup-attributeerror-nonetype-object-has-no-attribute-find
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
url = "https://www.smith.edu/diningservices/menu_poc/cbord_menus.php"
_l_(366507)
response = _c_(366511, _a_(366509, _n_(366508, "requests", lambda: requests), "get"), _n_(366510, "url", lambda: url))
_l_(366512)
bsObj = _c_(366516, _n_(366513, "BeautifulSoup", lambda: BeautifulSoup), _a_(366515, _n_(366514, "response", lambda: response), "content"), "html.parser")
_l_(366517)