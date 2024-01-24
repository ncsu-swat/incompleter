# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37761063/python-str-typeerror-str-object-is-not-callable-the-stop-code
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
soup = _c_(599920, _n_(599917, "BeautifulSoup", lambda: BeautifulSoup), _a_(599919, _n_(599918, "r", lambda: r), "content"), "lxml")
_l_(599921)

berat = _a_(599925, _c_(599924, _a_(599923, _n_(599922, "soup", lambda: soup), "find_all"), "dd", {"class": "pull-left m-0 border-none"})[0], "text")
_l_(599926)
var1 = _c_(599929, _n_(599927, "str", lambda: str), _n_(599928, "berat", lambda: berat))
_l_(599930)
str = _c_(599933, _a_(599932, _n_(599931, "string", lambda: string), "maketrans"), 'us', '12')
_l_(599934)
result = _c_(599938, _a_(599936, _n_(599935, "var1", lambda: var1), "translate"), _n_(599937, "str", lambda: str))
_l_(599939)
_c_(599942, _n_(599940, "print", lambda: print), _n_(599941, "result", lambda: result))
_l_(599943)