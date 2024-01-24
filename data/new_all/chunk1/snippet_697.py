# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54585333/typeerror-bad-operand-type-for-unary-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(402531, "df", lambda: df).REFERENCE_CODE = _c_(402535, _a_(402534, _a_(402533, _n_(402532, "df", lambda: df), "REFERENCE_CODE"), "fillna"), '')
_l_(402536)

_a_(402542, _c_(402541, _a_(402540, _a_(402539, _a_(402538, _n_(402537, "df", lambda: df), "REFERENCE_CODE"), "str"), "isnumeric")), "dtype") # returns object
_l_(402543) # returns object

headers = (_a_(402545, _n_(402544, "df", lambda: df), "REFERENCE_CODE") != '') & ~_c_(402550, _a_(402549, _a_(402548, _a_(402547, _n_(402546, "df", lambda: df), "REFERENCE_CODE"), "str"), "isnumeric"))
_l_(402551)

res = _c_(402562, _a_(402558, _c_(402557, _a_(402553, _n_(402552, "df", lambda: df), "groupby"), _c_(402556, _a_(402555, _n_(402554, "headers", lambda: headers), "cumsum")))['REFERENCE_CODE'], "apply"), lambda x: _a_(402560, _n_(402559, "x", lambda: x), "iloc")[0] + '_' + _n_(402561, "x", lambda: x))
_l_(402563)

_c_(402573, _a_(402566, _a_(402565, _n_(402564, "df", lambda: df), "REFERENCE_CODE"), "update"), _n_(402567, "res", lambda: res)[_c_(402572, _a_(402571, _a_(402570, _a_(402569, _n_(402568, "df", lambda: df), "REFERENCE_CODE"), "str"), "isnumeric"))])
_l_(402574)