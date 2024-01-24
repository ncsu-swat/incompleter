# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75756305/attributeerror-pandasexprvisitor-error-when-trying-to-optimize-pandas-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(460205, "df", lambda: df)["v1"] = _c_(460211, _a_(460207, _n_(460206, "df", lambda: df), "apply"), lambda row: _c_(460210, _a_(460209, _n_(460208, "row", lambda: row)['col3':'col5'], "tolist")), axis=1)
_l_(460212)
_n_(460213, "df", lambda: df)["v2"] = _c_(460219, _a_(460215, _n_(460214, "df", lambda: df), "apply"), lambda row: _c_(460218, _a_(460217, _n_(460216, "row", lambda: row)['col6':'col8'], "tolist")), axis=1)
_l_(460220)
v1 = _c_(460223, _a_(460222, _n_(460221, "df", lambda: df)['v1'], "to_numpy"))
_l_(460224)
v2 = _c_(460227, _a_(460226, _n_(460225, "df", lambda: df)['v2'], "to_numpy"))
_l_(460228)

# check if current value in column A is equal to any other values in column A
mask_A_A = _c_(460231, _a_(460230, _n_(460229, "pd", lambda: pd), "eval"), 'v1[:, None] == v1')
_l_(460232)

# check if current value in column A is equal to any other values in column B
mask_A_B = _c_(460235, _a_(460234, _n_(460233, "pd", lambda: pd), "eval"), 'v1[:, None] == v2')
_l_(460236)

# check if current value in column B is equal to any other values in column B
mask_B_B = _c_(460239, _a_(460238, _n_(460237, "pd", lambda: pd), "eval"), 'v2[:, None] == v2')
_l_(460240)

# check if any values in column B is equal to any other values in column A
mask_B_A = _c_(460243, _a_(460242, _n_(460241, "pd", lambda: pd), "eval"), 'v2[:, None] == v1')
_l_(460244)

# combine masks and use numexpr to create col9 column
mask = _c_(460247, _a_(460246, _n_(460245, "ne", lambda: ne), "evaluate"), '(mask_A_A | mask_A_B | mask_B_B | mask_B_A) & (v1[:, None] != v1) & (v2[:, None] != v2)')
_l_(460248)
col9 = _c_(460254, _a_(460250, _n_(460249, "np", lambda: np), "where"), _n_(460251, "mask", lambda: mask), _a_(460253, _n_(460252, "df", lambda: df)['col2'], "values")[:, None], '')
_l_(460255)
_n_(460256, "df", lambda: df)['col9'] = _c_(460266, _a_(460258, _n_(460257, "pd", lambda: pd), "Series"), [_c_(460261, _a_(460259, ', ', "join"), _n_(460260, "names", lambda: names)) if _c_(460264, _n_(460262, "len", lambda: len), _n_(460263, "names", lambda: names)) > 0 else None for names in _n_(460265, "col9", lambda: col9)])
_l_(460267)