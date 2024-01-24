# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75756305/attributeerror-pandasexprvisitor-error-when-trying-to-optimize-pandas-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(473377, "df", lambda: df)["v1"] = _c_(473383, _a_(473379, _n_(473378, "df", lambda: df), "apply"), lambda row: _c_(473382, _a_(473381, _n_(473380, "row", lambda: row)['col3':'col5'], "tolist")), axis=1)
_l_(473384)
_n_(473385, "df", lambda: df)["v2"] = _c_(473391, _a_(473387, _n_(473386, "df", lambda: df), "apply"), lambda row: _c_(473390, _a_(473389, _n_(473388, "row", lambda: row)['col6':'col8'], "tolist")), axis=1)
_l_(473392)
v1 = _c_(473395, _a_(473394, _n_(473393, "df", lambda: df)['v1'], "to_numpy"))
_l_(473396)
v2 = _c_(473399, _a_(473398, _n_(473397, "df", lambda: df)['v2'], "to_numpy"))
_l_(473400)

m = (_n_(473401, "v1", lambda: v1) == _n_(473402, "v1", lambda: v1)[:, None]) | (_n_(473403, "v2", lambda: v2) == _n_(473404, "v2", lambda: v2)[:, None]) | (_n_(473405, "v1", lambda: v1) == _n_(473406, "v2", lambda: v2)[:, None]) | (
            _n_(473407, "v2", lambda: v2) == _n_(473408, "v1", lambda: v1)[:, None])
_l_(473409)

_c_(473413, _a_(473411, _n_(473410, "np", lambda: np), "fill_diagonal"), _n_(473412, "m", lambda: m), False)
_l_(473414)

_n_(473415, "df", lambda: df)['col9'] = _c_(473420, _a_(473417, _n_(473416, "np", lambda: np), "dot"), _n_(473418, "m", lambda: m), _n_(473419, "df", lambda: df)['col2'] + ',')
_l_(473421)
_n_(473422, "df", lambda: df)['col9'] = _c_(473428, _a_(473425, _a_(473424, _n_(473423, "df", lambda: df)['col9'], "str")[:-1], "replace"), '', _a_(473427, _n_(473426, "np", lambda: np), "nan"), regex=True)
_l_(473429)